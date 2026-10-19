# Evidence and ownership completion

Status: engineering checks can be reproduced; employment, credentials, personal code ownership, and cloud operations remain unverified. This document is a completion protocol, not a certificate.

## Employment impact

For each employer, collect the exact legal employer name, dates, role, employment type, and a redacted experience letter or other corroborating record. Confirm which organization employed you and which was a client. Do not publish private employment documents or internal code here.

For one representative pipeline per role, record: input source, daily records or bytes, schedule, destination, your exact contribution, production versus staging, and evidence date. Separate team results from work you personally owned.

For performance claims, retain comparable before/after query plans or job logs, hardware, dataset size, observation period, and repetitions. Calculate improvement as (before - after) / before. If evidence is unavailable, retain the current qualitative wording; do not insert estimated percentages.

Use this private worksheet format:

| Claim | Exact contribution | Evidence source and date | Confidentiality review | Verified? |
|---|---|---|---|---|
| Employer/date/title | To be supplied | To be supplied privately | Pending | No |
| Pipeline volume/frequency | To be supplied | To be supplied privately | Pending | No |
| Performance improvement | To be supplied | Comparable measurements required | Pending | No |

## Credentials

Supply issuer verification links for the AWS and Oracle certifications; check the holder name, exact credential, issue date, and expiration/status. A badge image alone does not authenticate the credential. Confirm degree details against an award record or transcript. Keep identity numbers and private transcripts outside the public repository.

## Demonstrate code ownership

Run these tasks yourself and record explanations and a commit. A working implementation alone is not proof of independent ability.

1. Run `make run`. Explain why 165 missing hours must not become zero rentals.
2. Trace `pipeline.py` from CSV hash through validation to the transaction. Explain why a JSON export failure does not roll back SQLite.
3. Explain why cached replay reads and validates the source and compares all stored observation fields. Demonstrate a changed row being repaired and explain the added read/sort and writer-lock cost.
4. Modify validation to reject an additional realistic contract violation. Add a failing regression test first; explain the compatibility consequence.
5. Demonstrate HTTP 400, 404, and 503 and explain parameterized SQL and read-only database access.
6. Explain the temporal backtest and why its weekly-lag baseline is not a fixed 28-day-ahead forecast.

Completion requires correct explanations, a working change, and passing checks; no completion is claimed yet.

## Workload evidence and cloud gap

Run `cd projects/mobility-quality && python workload.py`. The checked-in result records repeated fresh loads, cached replays, and snapshot preservation after invalid input. Replays are the same historical observations, not additional real-world traffic.

A cloud milestone still requires a connected account and an actual run: immutable input storage, scheduled batch execution, durable output, scoped identity, logs, failure/retry evidence, billing observations, and teardown. Record commit, source hash, region, service configuration, timestamps, actual workload, resource limits, outcomes, and cost. A Dockerfile or CI run does not establish AWS operation. Do not expose the unauthenticated local API publicly.

## GitHub presentation

Feature the portfolio and research suite. Empty AI-product repositories and `auto-job-applier` should be archived or made private; coursework repositories should be clearly described and excluded from portfolio highlights. Preserve existing work. Current connector capabilities cannot archive repositories, change visibility, or change pins; these remain pending account-level actions.

Do not add placeholder commits to empty repositories to imply completed projects. The older profile audit is historical: its statement that Data-Engineer_AI contains only an introductory README predates the research suite.
