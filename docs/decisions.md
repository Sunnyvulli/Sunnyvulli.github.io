# Engineering decisions

## ADR 001: SQLite for the local reference system
**Status:** accepted. **Context:** recruiters should be able to inspect a working pipeline without cloud credentials. **Decision:** use standard-library SQLite and a local read-only API. **Trade-off:** simple reproducibility and transactions versus limited concurrent writers and no demonstration of distributed database operations. Postgres would be appropriate for a multi-user deployed service, but adds setup that this local artifact does not need.

## ADR 002: Complete historical source with explicit provenance
**Status:** accepted. **Decision:** redistribute the licensed UCI hourly CSV unchanged with its hash, attribution, and source period. **Trade-off:** offline reproducibility versus an older dataset that cannot establish current ridership or live-service behavior. Missing hourly records remain missing.

## ADR 003: Semantic contracts plus domain checks
**Status:** accepted. **Decision:** validate unique IDs/date-hour keys, component totals, calendar fields, and numeric domains. **Trade-off:** interpretable rules and tests versus inability to detect plausible but incorrect observations. Quarantine does not reconstruct the correct underlying value.

## ADR 004: Transactional snapshots with active source hashes
**Status:** accepted. **Decision:** commit observations and batch audit together; return cached metadata only when the requested source matches the active snapshot. **Trade-off:** repeat-safe local runs versus whole-file memory use and no incremental-stream processing. The initial cache assumed no out-of-band database mutation; ADR 008 supersedes that assumption for observation rows.

## ADR 005: Temporal holdout and an invalid leakage control
**Status:** accepted. **Decision:** report chronological and shuffled splits separately, compare a mean baseline and fixed forest, and deliberately expose target-component leakage as a negative methodological example. **Trade-off:** clear case-study evidence versus insufficient rolling-origin/multi-dataset validation. Observed weather makes this retrospective estimation, not future demand forecasting.

## ADR 006: Dependency-free smoke path; separate research environment
**Status:** accepted. **Decision:** `make run` exercises ingestion twice and six system tests in an isolated temporary database. Pinned scientific dependencies are needed only for model evaluation. **Trade-off:** quick verification of core behavior versus a longer full study reproduction. Docker validation is tracked in the dedicated container CI job.

## ADR 007: Local container isolation and scanner visibility
**Status:** accepted. **Decision:** run the API as UID 10001 with read-only storage and loopback-only host publishing; open SQLite in read-only mode. Scan all reachable Git history with Gitleaks v8.24.2 using default rules and fully redacted output. **Trade-off:** straightforward reproducibility and inspectable checks, but no scanner can prove that every possible secret is absent. Scanning does not revoke compromised credentials, and a local container is not a cloud deployment.


## ADR 008: Verify snapshot contents before cached replay
**Status:** accepted, 2026-10-19. **Context:** matching input and active hashes alone did not detect edited/deleted/extra observation rows. Separate hashing and parsing reads could also describe different source contents. **Decision:** hash and parse one captured byte sequence; compare every typed observation field, ordered by record ID, with the validated input before returning a cached report. Acquire `BEGIN IMMEDIATE` before inspecting or replacing the active snapshot, so cooperating SQLite writers cannot change it between verification and commit. Drift takes the normal atomic replacement path. **Trade-off:** replay reads the full snapshot and sorts accepted source rows; it also reserves the SQLite writer lock even on a cache hit. This is appropriate for the bounded local dataset, not a claim of streaming efficiency or multi-writer throughput. Schema and audit metadata are trusted; arbitrary hostile database edits are outside this repair guarantee. A trigger-injected insert failure confirms that rows, active hash, and manifest roll back together, followed by successful retry. Source replacement after capture uses the captured bytes; it does not establish filesystem-level immutability during the original read.

Primary reference for ADR 008: [SQLite transaction control](https://www.sqlite.org/lang_transaction.html), consulted 2026-10-19.


## ADR 009: Career claims follow executed project evidence
**Status:** accepted, 2026-10-19. **Decision:** add the independently inspectable Lakehouse Guardian and Catalog Sentinel repositories to the portfolio and application documents only after their implementation and main checks pass. Preserve exact controlled-evaluation denominators and distinguish local Spark/Iceberg execution, real Airflow CI execution, validated Terraform, and unapplied AWS resources. The bounded MCP server demonstrates typed capability enforcement, not remote identity or learned-model security. Store reviewed source commits and document phrases in the career evidence manifest. Correct its stale Mobility count to the discovered 13 and enforce that relationship in CI. **Trade-off:** concise resume evidence necessarily omits experimental detail, so source/result/threat-model links carry the full limitations. Retain a one-page resume and a readable two-page academic CV; do not invent bachelor's grades, research components or publications to fill admissions gaps.


## ADR 010: Standalone source links and bounded retrieval evidence
**Status:** accepted, 2026-10-19. Move career links to the independently verified Mobility repository while retaining existing portfolio source paths as compatibility copies; the import records exact source blobs and original history instead of resetting it. Add the executed lexical/extractive retrieval reference only after CI passes. Keep authored development-query metrics distinct from independent answer faithfulness and keep the guard's semantic misses visible. Two before-failing extraction regressions record a real review iteration. The six-line profile and three application documents should identify this same verified scope; no research, degree, employment or deployment fact is inferred.

## ADR 011: Resume hierarchy with ordered text
**Status:** accepted, 2026-10-19. Use a single column, embedded DejaVu fonts, restrained navy/teal headings and thin section rules. Keep dates inline with roles and URLs visible and clickable. Avoid graphics, tables and text boxes in the reading path. The one-page PDF retains exact source text and verified claims. Visual inspection and extraction checks demonstrate this artifact's readability; they do not guarantee compatibility with every ATS. The portfolio, academic CV and cover letter remain factually consistent; no career fact changed, so they do not need rewriting.

## ADR 012: Strengthen analytical depth before adding project breadth
**Status:** accepted, 2026-10-19. Prioritize an explicit dimensional mart and executed reconciliation/failure checks inside Lakehouse Guardian. The dataset supports date/hour facts and date/weather reference dimensions, not invented customer/station entities or SCD2 history. Keep the temporary full-refresh mart distinct from CDC, distributed scale and cloud operation. External human review is invited through a public issue and remains pending until an actual reviewer supplies feedback; automated checks and self-review do not constitute peer review. Career materials should reflect the verified test count/model scope only after the implementation CI passes.
