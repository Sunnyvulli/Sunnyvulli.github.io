# Public visibility verification — 2026-10-19

Rechecked the deployed HTML/PDF bytes and GitHub API after a review reported missing projects. This records direct observations, not search-engine indexing or pin-state assumptions.

| Review concern | Current verified state |
| --- | --- |
| Three projects missing/publication unclear | [Lakehouse Guardian](https://github.com/Sunnyvulli/lakehouse-guardian), [Catalog Sentinel](https://github.com/Sunnyvulli/catalog-sentinel), [Evidence Ledger RAG](https://github.com/Sunnyvulli/evidence-ledger-rag) each return public repository metadata and substantive README content. Their README metrics match the career evidence manifest. |
| Missing portfolio/resume/CV/profile links | All three names and links are present in current portfolio, resume source/PDF, CV source/PDF and six-line [profile README](https://github.com/Sunnyvulli/Sunnyvulli). Normalize PDF whitespace when searching: a name can wrap across lines. |
| Mobility test mismatch | Current deployed portfolio and all three original PDFs say 13 passing tests; profile says 13 tests. No current 10-passing-tests statement was found in those surfaces. |
| LinkedIn only in letter | Owner-provided LinkedIn is present in deployed portfolio and original three PDFs, plus profile README. |
| Research repository single commit | GitHub API currently returns two commits: `e60cd5c` (verification/history scan) and `3f3797b` (initial snapshot). Deliberate initial history is preserved. |
| Research description | Still `role as data engineer`. Proposed replacement: `Reproducible applied ML studies in citation support, phishing robustness and early-transient ranking; executed baselines, failure analyses and unpublished manuscripts.` Description mutation is not exposed by the current connector. |
| Pins | Pin changes are not exposed by the current connector; this run does not claim to verify or change the selected pins. Recommended five: Lakehouse Guardian, Catalog Sentinel, Evidence Ledger RAG, Mobility Quality Lab, Data-Engineer_AI. |
| Unsupported skills | Current resume omits TypeScript, MariaDB and Selenium. Terraform is now supported by executed provider validation, not AWS deployment. Employment skill claims remain owner-supplied; do not invent employer metrics. |
| Letter audience | Added a separate AI-platform/agentic letter with direct repository URLs, preserving the data-engineering letter. |

## Claim boundaries

- Lakehouse: 21 controlled batches; precision 1.00, recall 0.80; plausible count inflation is missed. Local workflow, actual Airflow CI and validated Terraform, no AWS deployment.
- MCP: 13 expected denials enforced in 16 real stdio requests. Host-assigned permissions are not remote identity or independent prompt-injection resistance.
- Retrieval: hybrid 11/14 versus BM25 10/14 on authored development queries, not evidence of general superiority. Guard misses meaning changes; exact cited spans do not establish answer faithfulness.
- A search result or partial profile grid is not a complete repository inventory. The cause of the review's older/missing observations is unconfirmed; no cache or indexing diagnosis is asserted.

## Document synchronization

The added AI-platform letter uses existing verified results and no new qualification. Existing resume, academic CV and data-engineering letter remain consistent, so no factual rewrite is needed. The new document joins the CI source-text, page-count, URL, phone/privacy and engineering-claim checks. Rendered one page and visually inspected before publication. The portfolio offers both letter variants.

Build: `python scripts/build_cover_letter.py --variant agentic`. Check: `python scripts/check_career.py`.
