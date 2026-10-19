# Evidence priorities — 2026-10-19

## Completed in the dimensional-mart change

Lakehouse Guardian adds explicit hourly fact grain, calendar/weather dimensions, observed-hour denominators, a SQL window report, reconciliation and four deliberately invalid candidates. Recorded local execution: 17,379 facts / 731 dates / 3,292,679 rentals, 25 dbt data checks, 13 Python test methods. This strengthens SQL/modeling evidence without creating another repository or claiming production scale.

## Next engineering work, in order

1. **Persistent incremental behavior:** source versioning, corrections/deletes, deterministic conflict resolution, transactional upsert and repeat-safe backfill, with independently specified expected outputs. Choose a genuine source/update contract before implementation; do not invent customer history or label snapshot replacement as CDC.
2. **Independent source and larger workload:** introduce a different lawful dataset with source hashes and documented joins. Measure query plans, runtime/memory and failure recovery at justified sizes; clearly separate real records from generated load. Preserve current negative findings.
3. **Cloud execution:** only after account, region, scoped identity and spending limit are authorized. Retain IAM, job logs, costs, monitoring and teardown evidence. Validated Terraform alone stays labeled undeployed.
4. **External validation:** obtain a human technical review of the working artifact and independently authored evaluation cases. Record the original review, commit, reproduced findings and response. Expand research manuscripts only when the resulting evidence supports a defensible contribution; no submission or acceptance is inferred.

## Human review status

[Independent technical review request](https://github.com/Sunnyvulli/lakehouse-guardian/issues/7) is public. Status is **requested, not received**. A reviewer must supply actual feedback; a public issue alone does not recruit or certify a reviewer. CI and author self-review are separate.

A focused working-code review can be sought through [Code Review Stack Exchange](https://codereview.stackexchange.com/help/on-topic), following its self-contained-code rules. There is no connected posting account there in this session and no identified consenting external reviewer; no external submission or direct message has been sent. Formal software/journal review has additional scope requirements and is not replaced by a repository issue.

## Career-document synchronization

Resume and CV reflect the verified dimensional-model scope and Lakehouse Python-test count. The portfolio links raw/model evidence and the pending review request. Both cover-letter variants still describe the same truthful capabilities and limits; no rewrite is needed. The six-line profile links the same flagship and remains consistent. Degrees, employment impact, certifications and referees are not inferred from software tests.
