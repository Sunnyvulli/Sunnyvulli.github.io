# Teaching sample: validate before you aggregate

Instructional sample using synthetic data; not evidence of prior teaching employment.

**Goal:** Explain how duplicate records distort SQL summaries and how an explicit quality gate changes the result.

After running pipeline.py, open orders.sqlite with SQLite or Python's sqlite3 module.

```sql
SELECT order_date,
       COUNT(*) AS accepted_orders,
       SUM(amount_cents) AS total_cents
FROM orders
GROUP BY order_date
ORDER BY order_date;
```

Expected rows:

| order_date | accepted_orders | total_cents |
|---|---:|---:|
| 2026-01-01 | 2 | 20000 |
| 2026-01-02 | 2 | 4025 |

**Walkthrough:** GROUP BY creates one group per date. COUNT(*) counts accepted records, including the valid zero-value order. SUM adds integer cents. Convert cents to dollars for display rather than storing approximate floating-point currency.

**Reasoning exercise:** If the duplicate O002 were accepted, how much would the grand total increase?

**Answer:** 7,950 cents ($79.50). The incorrect grand total would be 31,975 cents ($319.75).

**Discussion:** Is a duplicate always an error? A repeated ID might represent a correction. This demo selects the first valid row, but a real system needs an explicit version or update policy. Ask students to propose a timestamp-based policy and explain how ties should be resolved.

**Practice:** Add a valid order on a third date and predict the result before running the pipeline. Then remove its customer ID and explain why the report changes while that date disappears from the SQL result.
