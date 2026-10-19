# Career evidence review - 2026-10-19

## Corrections completed in this change

| Review point | Action and evidence boundary |
|---|---|
| Test count | Fresh live portfolio/resume/CV downloads contained 13, not 10. CI now discovers flagship tests and checks the page and all three document sources. PDF extraction must match each source. All current counts are 13. Cached/downloaded older copies can differ. |
| Dataset identity | Name UCI Bike Sharing in the portfolio, resume, cover letter, and CV. Data/license/source links remain in the project. |
| Public contact privacy | Remove the phone from the current three document sources and PDFs; retain professional email. CI rejects formatted US phone numbers in these documents. Previous commits and external copies are not erased; no history reset is performed. |
| Skill support | Remove Terraform, TypeScript, MariaDB, Selenium, and skills-only Hibernate/JUnit/Mockito claims from public skill lists. Add visibly exercised SQLite/Python unittest where appropriate. The original supplied resume explicitly names Lambda/API Gateway/RDS under PRC Cloud Tech, so connect those services to that responsibility instead of leaving unexplained keywords. Employment remains owner-supplied and externally unverified. |
| Research direction | Focus academic CV interests on agentic-AI security/governance, evidence-supported decisions, lineage, and reproducible evaluation. Feature citation-support before phishing. Agent-specific evaluation is labeled a future direction; existing experiments are not relabeled as agent benchmarks. |

## Evidence still required

- Bachelor's exact degree, institution, dates, CGPA/percentage, and grading scale. No invented university, grade, or completion date is inserted.
- MS classification as thesis, capstone, research project, or coursework; provide project title, supervisor, credits/duration, assessment and available report. The current degree listing alone cannot establish any program's research-component eligibility.
- Any genuinely published/accepted work: bibliographic citation, author list, DOI or acceptance evidence. No verified publication is presently available in this repository's evidence; retain the unpublished labels. This is not a claim that every PhD program requires prior publications.
- Employment outcomes: dated, comparable job logs/query plans and exact personal contribution. Keep portfolio measurements separate from employer performance; no invented percentages or traffic volumes.
- Reason for each role transition and confirmation of legal employer versus client, contract/permanent status, and dates. Do not assume the moves were contract endings or promotions.
- Issuer verification URLs and current status for both listed certifications.
- Two appropriate academic referees' names, roles, institutions, professional contacts, relationship and permission to act. Keep contact details in a private application CV or application system unless publication is explicitly authorized; do not add placeholder names or imply consent.
- Named supervisors and specific opportunity text for individual outreach tailoring. This theme-focused public CV is not a substitute for checking each supervisor's current work and requirements.

## Engineering gaps not disguised as writing changes

The temporal study currently compares the calendar forest (MAE 49.77 rentals/hour) with an online weekly-lag baseline (64.03) and training mean (184.22), over the stated 84 historical days. No additional stronger baseline was executed in this presentation change, so no new winning result is claimed. A stronger past-only model comparison and independent dataset validation remain research work.

Mobility Quality Lab still resides in the portfolio repository. Dedicated repository creation is not exposed by the current connector. Extraction must carry CI, paths, license, decisions, provenance and standalone setup, then update every document/profile/site link only after a fresh-clone verification. Existing history is preserved.

Actual cloud execution, metadata, pins, releases and owner-evidence collection remain open in issue #1.

## Verification

- `scripts/check_career.py` passes: 13 discovered flagship tests, 32 local links, matching selectable text and one page for each application PDF.
- Negative checks reject a stale page count, stale resume count, missing dataset name, and a synthetic public phone number. Files restored after each check.
- Formatter and research-card synchronization pass; all three edited PDFs rendered for visual inspection before publication.
- Full PR CI, deployment, and published byte verification are required before reporting this change as complete.

## Verified project evidence added, 2026-10-19
Lakehouse Guardian and Catalog Sentinel are now separate public repositories with green implementation/main CI. The resume/CV/cover letter and portfolio reference the actual local Spark/Iceberg/dbt/LangGraph workflow, real Airflow CI execution, Terraform provider validation, and bounded MCP stdio requests. Terraform is now supported by repository evidence, but no AWS deployment is claimed. TypeScript/MariaDB/Selenium remain omitted. Existing owner-dependent education, certification, employer-outcome and referee gaps are unchanged.

The updated resume remains one page. The academic CV uses a deliberate second page for professional experience, skills and certifications. The hybrid retrieval project is not yet added to application documents because its GitHub publication/CI milestone remains pending.

## Standalone and retrieval follow-through, 2026-10-19
Mobility Quality Lab now has its own independently tested/containers-verified repository; current document links point there and historical portfolio paths remain available. Evidence Ledger RAG is now public and CI-verified with 18 tests, 14 authored queries and retained semantic guard misses. The resume/CV/cover letter include this bounded reference implementation; they do not inherit the research suite's external-validation performance for its guard. All four engineering projects have v0.1.0 releases. The same owner-qualification/publication/employer evidence gaps remain; none is filled by assumption.
