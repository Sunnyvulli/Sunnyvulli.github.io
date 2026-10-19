import csv
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from pipeline import run

class PipelineTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = Path(__file__).with_name('orders.csv')
        self.db, self.report = self.root / 'data.sqlite', self.root / 'report.json'
    def test_fixture_reconciliation_and_quarantine(self):
        r = run(self.source, self.db, self.report)
        self.assertEqual((r['input_rows'], r['accepted_rows'], r['rejected_rows']), (10, 4, 6))
        self.assertEqual(r['reason_counts'], {'duplicate_order_id':1,'missing_customer_id':1,'invalid_date':1,'invalid_amount':2,'missing_order_id':1})
        self.assertEqual(sum(d['amount_cents'] for d in r['daily_totals']),24025)
        self.assertEqual(r, json.loads(self.report.read_text()))
    def test_rerun_does_not_duplicate(self):
        first = run(self.source, self.db, self.report)
        self.assertEqual(first, run(self.source, self.db, self.report))
        with sqlite3.connect(self.db) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM orders').fetchone()[0],4)
    def test_edge_values_and_invalid_first_occurrence(self):
        source=self.root/'edge.csv'
        with source.open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['order_id','customer_id','order_date','amount'])
            for row in [('A','C','2026-01-01','bad'),('A','C','2026-01-01','1.01'),('B','C','2026-01-01','Infinity'),('C','C','2026-01-01','0.001'),('D','C','2026-01-01','1e100'),('E','C','2026-01-01','0')]: w.writerow(row)
        r=run(source,self.db,self.report)
        self.assertEqual((r['accepted_rows'],r['rejected_rows']),(2,4))
        self.assertEqual(r['daily_totals'][0]['amount_cents'],101)
    def test_invalid_schema_preserves_existing_snapshot(self):
        run(self.source,self.db,self.report)
        source=self.root/'bad.csv';source.write_text('wrong\nx\n')
        with self.assertRaises(ValueError): run(source,self.db,self.report)
        with sqlite3.connect(self.db) as db:self.assertEqual(db.execute('SELECT COUNT(*) FROM orders').fetchone()[0],4)

if __name__ == '__main__': unittest.main()
