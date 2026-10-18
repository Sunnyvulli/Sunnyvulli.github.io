# GitHub Gold Standard audit

Audit date: 2026-10-18. Scope: public repository inventory, available source/documentation, fresh portfolio clone, executed smoke run, known-format history scan, and GitHub Actions. Scores award only demonstrated criteria. Unverified items receive zero; zero does not necessarily mean defective. The special profile README repository is not a software project and is exempt from the runnable-project rubric.

## Flagship score: 8/10 verified

| # | Criterion | Score | Evidence / remaining gap |
|---|---|---:|---|
| 1 | Clear one-line purpose | 1 | README summary explains pipeline, API and evaluation |
| 2 | Demo or screenshot | 1 | Public portfolio and inspectable data/results |
| 3 | Runs with one command | 1 | `make run` passed from a fresh clone with proposed changes on Python 3.12.14 + GNU Make in 1.693 seconds; no dependency installation. This is not an arbitrary clean-OS guarantee. |
| 4 | Tests exist | 1 | Six system tests, including real HTTP and recovery checks |
| 5 | CI passing | 1 | Released main pipeline/evaluation workflow passed; follow-up workflow adds smoke + formatter and must also pass before merge |
| 6 | Architecture / decisions | 1 | README diagram and docs/decisions.md |
| 7 | Measured results | 1 | 17,379 real observations; 18 model runs; 54 fault-policy evaluations |
| 8 | License, topics, description | 0 | MIT code license present; repository description and topics absent |
| 9 | No secrets or junk | 1 | No tracked build/cache junk. Gitleaks v8.24.2 default rules scanned all 15 reachable commits locally with no findings; CI also scans reachable history with fully redacted output. A passing scanner is not proof against unknown credential formats or unreachable history. |
| 10 | Tagged release and roadmap | 0 | Roadmap/changelog present; fresh clone has no version tag |

A dedicated CI job now builds and starts the Compose API, verifies HTTP behavior/non-root UID, and runs system tests inside the image. Check the linked workflow result before treating Docker execution as verified. The under-five-minute claim applies to the dependency-free smoke path in the recorded environment. The full scientific evaluation installs dependencies and takes longer. A score is a rubric result, not a percentile ranking or career guarantee.

## Public repository triage

| Repository | Verified state | Conservative score / action |
|---|---|---|
| Sunnyvulli.github.io | Working portfolio and flagship implementation | 8/10; remaining metadata and release gaps documented |
| Sunnyvulli | Six-line professional profile README | Profile infrastructure; exempt |
| DBSGITHUBTRAINING | Title-only README and sample.txt | 0 verified rubric points; archive candidate |
| Actvity_6_Datasets | Dataset CSVs, title-only README, no runnable project | 0 verified rubric points; archive/retain privately as coursework candidate |
| Data-Engineer_AI | Introductory README only | 0 verified rubric points; archive candidate |
| docforge-ai | Code and substantial README; no visible root test suite or CI, no verified demo URL or metrics | 2 verified points (purpose and architecture narrative); do not pin until execution, tests, and evaluation are verified |
| quizforge-ai | GitHub reports empty repository | 0/10; archive candidate |
| brandkit-ai | GitHub reports empty repository | 0/10; archive candidate |
| reviewresponder-ai | GitHub reports empty repository | 0/10; archive candidate |
| scriptforge-ai | GitHub reports empty repository | 0/10; archive candidate |
| policyforge-ai | GitHub reports empty repository | 0/10; archive candidate |
| jobdesc-ai | GitHub reports empty repository | 0/10; archive candidate |
| auto-job-applier | GitHub reports empty repository | 0/10; archive candidate |

These are conservative evidence scores, not exhaustive code/security reviews. No repository has been archived or deleted by this audit. Private repositories were excluded. Pin state, photo, public name/bio/location, and manual metadata settings were not changed. The current connector supports content/PR operations but does not expose repository archival, topics, description edits, pinning, or release creation.

## Ordered next work

1. Merge the clean-run/formatter/decision-log change only after PR CI passes.
2. Keep the dedicated Gitleaks history scan passing; review findings without posting secret values.
3. Set repository description/topics and create an actual version tag/release using supported authenticated settings.
4. Archive the specifically identified non-portfolio repositories after owner review of this list; prefer recoverable archival over deletion.
5. Develop distinct backend/cloud/tool projects to the same standard before selecting four to six pins. Do not split one project into multiple repositories to inflate the count.
6. Confirm professional photo, LinkedIn, certification URLs, and substantiated employer metrics with the owner.
7. Re-audit after 30 days, then monthly, including a fresh clone and the 60-second visitor test.

## Security/container follow-up
Gitleaks v8.24.2 official Linux archive checksum verified against its release checksums. Local scan: 15 reachable commits, no findings. Seven system tests now include missing-database HTTP 503 with no accidental file creation. Container execution is verified by the dedicated CI job rather than inferred from the Dockerfile.
