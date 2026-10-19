# Reliable replay: inspect the data, not just its label

## Problem reproduced
A cached source hash identifies the input, but does not prove that the database still contains its observations. Before this change, editing a count, deleting a row, or inserting an extra row still returned `cached=True`. A deterministic source-replacement test also showed that separate hash/read operations could hash one file and parse another. The test replaces the path after the bytes are read; it does not simulate every possible concurrent filesystem write.

## Behavior after the change
The pipeline hashes and parses the same captured bytes. Within `BEGIN IMMEDIATE`, replay compares all 17 observation columns, ordered by ID, with the validated source. A complete match returns the existing report unchanged; mismatch follows the normal transactional reload and updates the report. An injected SQLite insert failure after deletion rolls back observations, manifest, and active hash together. Removing the failure permits a successful retry.

This is local consistency repair, not hostile-tamper protection. Database schema and audit metadata are trusted. Comparison reads the full snapshot, sorts the source rows, and takes a writer reservation even for a cache hit. No concurrency throughput, cloud operation, or uptime claim is made. SQLite may report a busy database after its connection timeout if another writer holds the lock; no unbounded retry is added. See [SQLite transaction semantics](https://www.sqlite.org/lang_transaction.html) and ADR 008 in [the decision log](decisions.md).

## Executed verification, 2026-10-19
- Before the fix: the cache regression failed for all three mutations, and the source-replacement regression raised a schema error; the rollback regression already passed.
- After the fix: `make test` passed 13 flagship tests (10 system + 3 temporal) and four earlier data-quality tests. The cache regression compares every restored row, not just totals.
- `make run` passed, preserving 17,379 observations and 3,292,679 rentals. One recorded smoke run took 4.698 seconds on Python 3.12.14 with SQLite 3.53.1; this includes tests and is not a service latency or clean-OS guarantee.
- Input SHA-256: `e03de4ee4ef4dc376ac6e04bf829673c6269e8eba5c60fa121640fa2f829504f`. The input and historical model/evaluation artifacts are unchanged.
- `make format-check`, `scripts/sync_evidence.py --check`, and `scripts/check_career.py` passed. The latter checked 32 local links plus matching selectable text in all three one-page application PDFs.
- Resume, cover letter, academic CV, README, and portfolio use the new verified count of 13 flagship tests. All three PDFs were rendered and visually reviewed after editing; qualifications, employment, research findings, and publication status are unchanged.

## Review and remaining work
Self-review: SQL identifiers come from the fixed `FIELDS` constant; values remain bound parameters. No new dependency, credential, network service, or API surface is introduced. Replay is deliberately more expensive; a large-scale design would need a different integrity strategy. Existing research cards and user wording are preserved apart from the verified test count. PR CI must pass before merge, including the full-history scan, container execution, smoke tests, document checks, and scientific reproductions. This document does not assert that CI has passed before its results exist.

The distinct-project and actual cloud-operation gaps remain. Repository metadata, pins, and release creation still require an available account capability; no tag/release or profile-setting change is implied.
