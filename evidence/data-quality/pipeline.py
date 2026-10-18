"""AI-assisted portfolio demonstration; synthetic orders, no external dependencies."""
import argparse
import csv
import json
import sqlite3
from collections import Counter
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


def run(source, database, report):
    with Path(source).open(newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    required = {'order_id', 'customer_id', 'order_date', 'amount'}
    if not rows or not required.issubset(rows[0]):
        raise ValueError('Input must contain order_id, customer_id, order_date, amount and at least one row')
    seen, accepted, rejected = set(), [], []
    for number, row in enumerate(rows, 2):
        reasons = []
        order_id = row['order_id'].strip()
        customer = row['customer_id'].strip()
        if not order_id:
            reasons.append('missing_order_id')
        if not customer:
            reasons.append('missing_customer_id')
        try:
            day = date.fromisoformat(row['order_date']).isoformat()
        except ValueError:
            day = None
            reasons.append('invalid_date')
        try:
            amount = Decimal(row['amount'])
            if not amount.is_finite() or amount < 0 or amount != amount.quantize(Decimal('.01')):
                raise ValueError()
            cents = int(amount * 100)
            if cents > 9223372036854775807:
                raise ValueError()
        except (InvalidOperation, ValueError, OverflowError):
            cents = None
            reasons.append('invalid_amount')
        # First valid occurrence wins; invalid rows cannot reserve an ID.
        if order_id in seen:
            reasons.append('duplicate_order_id')
        if reasons:
            rejected.append({'line': number, 'order_id': order_id, 'reasons': reasons})
        else:
            seen.add(order_id)
            accepted.append((order_id, customer, day, cents))
    with sqlite3.connect(database) as db:
        # Atomic snapshot replacement makes repeated runs deterministic.
        db.execute('CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, order_date TEXT NOT NULL, amount_cents INTEGER NOT NULL CHECK(amount_cents >= 0))')
        db.execute('DELETE FROM orders')
        db.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', accepted)
        summary = db.execute('SELECT order_date, COUNT(*), SUM(amount_cents) FROM orders GROUP BY order_date ORDER BY order_date').fetchall()
    result = {'input_rows': len(rows), 'accepted_rows': len(accepted), 'rejected_rows': len(rejected),
              'reason_counts': dict(Counter(reason for row in rejected for reason in row['reasons'])),
              'quarantine': rejected,
              'daily_totals': [{'date': day, 'orders': count, 'amount_cents': cents} for day, count, cents in summary]}
    Path(report).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', default='orders.csv')
    p.add_argument('--database', default='orders.sqlite')
    p.add_argument('--report', default='report.json')
    a = p.parse_args()
    print(json.dumps(run(a.input, a.database, a.report), indent=2))
