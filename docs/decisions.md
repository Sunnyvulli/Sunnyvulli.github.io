# Engineering decisions

## ADR 001: SQLite for the local reference system
**Status:** accepted. **Context:** recruiters should be able to inspect a working pipeline without cloud credentials. **Decision:** use standard-library SQLite and a local read-only API. **Trade-off:** simple reproducibility and transactions versus limited concurrent writers and no demonstration of distributed database operations. Postgres would be appropriate for a multi-user deployed service, but adds setup that this local artifact does not need.

## ADR 002: Complete historical source with explicit provenance
**Status:** accepted. **Decision:** redistribute the licensed UCI hourly CSV unchanged with its hash, attribution, and source period. **Trade-off:** offline reproducibility versus an older dataset that cannot establish current ridership or live-service behavior. Missing hourly records remain missing.

## ADR 003: Semantic contracts plus domain checks
**Status:** accepted. **Decision:** validate unique IDs/date-hour keys, component totals, calendar fields, and numeric domains. **Trade-off:** interpretable rules and tests versus inability to detect plausible but incorrect observations. Quarantine does not reconstruct the correct underlying value.

## ADR 004: Transactional snapshots with active source hashes
**Status:** accepted. **Decision:** commit observations and batch audit together; return cached metadata only when the requested source matches the active snapshot. **Trade-off:** repeat-safe local runs versus whole-file memory use and no incremental-stream processing. The cache assumes no out-of-band database mutation.

## ADR 005: Temporal holdout and an invalid leakage control
**Status:** accepted. **Decision:** report chronological and shuffled splits separately, compare a mean baseline and fixed forest, and deliberately expose target-component leakage as a negative methodological example. **Trade-off:** clear case-study evidence versus insufficient rolling-origin/multi-dataset validation. Observed weather makes this retrospective estimation, not future demand forecasting.

## ADR 006: Dependency-free smoke path; separate research environment
**Status:** accepted. **Decision:** `make run` exercises ingestion twice and six system tests in an isolated temporary database. Pinned scientific dependencies are needed only for model evaluation. **Trade-off:** quick verification of core behavior versus a longer full study reproduction. Docker validation is tracked in the dedicated container CI job.

## ADR 007: Local container isolation and scanner visibility
**Status:** accepted. **Decision:** run the API as UID 10001 with read-only storage and loopback-only host publishing; open SQLite in read-only mode. Scan all reachable Git history with Gitleaks v8.24.2 using default rules and fully redacted output. **Trade-off:** straightforward reproducibility and inspectable checks, but no scanner can prove that every possible secret is absent. Scanning does not revoke compromised credentials, and a local container is not a cloud deployment.
