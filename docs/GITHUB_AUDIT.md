# GitHub and career-material audit

Audit date: October 18, 2026. Scope: 14 repositories accessible through the connected account, their available default-branch files, reachable refs of the six nonempty public repositories, executable tests, package advisories, portfolio links, and career-document consistency. This is an engineering audit, not a guarantee of complete security, scientific novelty, or ATS acceptance.

## Repository inventory

| Repository | Observed state | Action / finding |
| --- | --- | --- |
| Sunnyvulli | Profile README | Updated stale test count, added measured research suite and career links; kept six lines. |
| Sunnyvulli.github.io | Portfolio, mobility pipeline, career documents | Ten mobility tests and four fixture-pipeline tests passed; refreshed research cards and all three career PDFs; added synchronization checks. |
| Data-Engineer_AI | Previously a short README | Published three runnable research baselines, 20 integrity tests, actual experiment outputs, sources, and limits. |
| docforge-ai | Document-generation application | Fixed evidenced accounting, session, webhook, dependency, and streaming defects; 16 tests passed. Prototype only. |
| Actvity_6_Datasets | Six coursework CSV files | Added schema/row/missing/duplicate audit and a provenance boundary. Original sources and redistribution terms remain undocumented. |
| DBSGITHUBTRAINING | README and empty sample file | Documented its actual training-sandbox status; no application or deployment claimed. |
| quizforge-ai | Empty repository | No implementation to review; retained unchanged. |
| brandkit-ai | Empty repository | No implementation to review; retained unchanged. |
| reviewresponder-ai | Empty repository | No implementation to review; retained unchanged. |
| scriptforge-ai | Empty repository | No implementation to review; retained unchanged. |
| policyforge-ai | Empty repository | No implementation to review; retained unchanged. |
| jobdesc-ai | Empty repository | No implementation to review; retained unchanged. |
| auto-job-applier | Empty repository | No implementation to review; retained unchanged. |
| One private repository | Empty repository | Identity omitted from this public report. Retained unchanged. |

No repositories were deleted, archived, or populated with invented projects. Empty repositories and the training sandbox are not presented as completed portfolio work. The desired four-to-six strong pinned repositories cannot be established merely by inventing content or counting empty repositories; pin settings were not changed.

## Application fixes

### DocForge

- Client-selected identifiers previously created freely credited sessions. Sessions are now server-issued; unknown tokens are rejected, and creation is rate limited.
- Credit accounting previously used an in-memory Map. SQLite now persists balances, reservations, recorded checkouts, and event deduplication on a private single-host volume.
- Credits previously deducted after generation allowed overlapping requests to overspend. Reservations now occur atomically before provider work; failures refund once.
- Duplicate webhooks could repeatedly grant credits, and completed sessions were not checked for paid status. Only signed, paid, server-recorded test checkouts grant credits, once per checkout.
- Browser SSE parsing previously discarded incomplete network-chunk messages and could display success after errors. Incremental parsing and terminal-event checks now preserve frames and distinguish failure.
- Input types, document types, session mismatch, request size, origin, and route handling are checked.
- A vulnerable nodemon dependency chain was removed in favor of Node's native watch mode. The resolved package audit reported zero advisories at execution time; this can change.
- The obsolete serverless configuration was removed. Persistent SQLite requires a single host; the application refuses Vercel startup.
- Real payment keys are rejected. Generation requires explicit provider/model configuration. No paid provider request, live charge, or production deployment was performed.

Remaining application boundaries include crash reconciliation for pending generation reservations, user-account recovery, distributed rate limiting, prospective monitoring, backups/restoration, and live-payment/refund reconciliation. Documentation exposes these rather than declaring the prototype production-ready.

### Research suite

Executed baselines cover engineered-feature phishing robustness, citation-support review triage, and simulated early-transient ranking. They are not the full advertised UTAS research programmes. Phishing is not described as multimodal without raw modalities; citation support is not described as factual truth; simulated astronomy is not described as a live discovery or telescope trial. Existing literature and datasets are attributed. Codex assistance is disclosed. No plagiarism-screening certification or new scientific contribution is asserted.

## Career-material consistency

The supplied resume was read and compared with the existing public resume. Employment, education, contact details, and certification titles follow that source. No new employer performance metrics, additional degree, PhD enrollment, accepted publication, or active credential verification was inferred.

The resume, general cover letter, and academic CV now include the measured research evidence. Each is a single-page selectable-text PDF, has a matching plain-text source, and contains no image-only content. Rendered pages were inspected. Tests verify extracted reading order against source text and local page links. These checks do not establish acceptance in every ATS or fit to a job description that has not been supplied.

`career-evidence.json` drives the three research cards. GitHub Actions checks generated-card drift and career-document/source drift on pushes and pull requests. This keeps documented changes consistent; it does not infer future changes to the owner's employment or qualifications.

## Security and evidence checks

- Six public nonempty repositories were mirrored with reachable refs. A five-pattern scan covered 156 reachable blobs and found no matches for the credential formats checked. See `history-scan.json`. This is not an exhaustive secret scan or proof that inaccessible history contains no credentials.
- Repository inventory and file counts are recorded in `repository-inventory.json`; private identity is redacted.
- Existing mobility/data-quality tests: 14 passed. Research integrity tests: 20 passed. DocForge tests: 16 passed. The 50 tests exercise different projects, not 50 independent security certifications.
- Document extraction/page checks and 29 local-link/asset references passed.
- Branch-protection inspection returned HTTP 403 (`Resource not accessible by integration`). Protection status is **unverified**, not assumed absent.
- Account profile settings, pins, private organization policies, external provider accounts, and credential validity are outside the verified scope.

## Dependency correction

The first Python requirements audit identified multiple advisories affecting pypdf 6.10.0, which was used only by the career-document verification tooling. The pin was updated to 6.19.0, and document extraction checks were rerun with that version. Before/after advisory reports are retained. Research requirements resolved without known advisories in the audit. These package-index checks are time-specific and do not certify application safety.

## Published changes

- Research suite: `d609ef149611137173ccb9e2bda04d906c3e5910`; remote integrity workflow passed.
- DocForge: `d52edc12dc2637ce4ab613120efb4a7d645aa7af`; remote verification workflow 39176547736 passed.
- Profile README: `3f78fa338dd26e0deb9e558fb5b15dfed4a7c95d`.
- Coursework dataset documentation: `9be3e61c907cec01aa83cf22712d63fb5f134977`.
- Git training documentation: `2cc6305d0c46d07925a7e28a51fd4078593c85a9`.

## Continuing work

See `WORK_CHECKPOINT.md` for publication and remote-check status. Scientific publication gates remain in the research suite's `docs/RESEARCH_PLAN.md`. No external supervisor messages, job applications, invitations, or paper submissions were sent.

## Deployment inspection

Portfolio update commit: `2c03da0c0e50c9dc9ad74c11e99eff9977e514c3`. The live page was opened in a browser and all three new research cards were present. At a 1363-pixel viewport there was no horizontal overflow and the research layout was visually inspected. A dedicated mobile viewport render was not executed; responsive CSS alone is not treated as a completed mobile-browser test. All three live career PDFs returned HTTP 200 and matched the updated local bytes.

Remote workflow results for the portfolio implementation commit: portfolio verification 39176716497, Pages deployment 39176716469, security/container verification 39176716435, and Pages build 39176715480 all completed successfully. DocForge verification 39176547736 also passed. The final checkpoint records this verified engineering-delivery state separately from future research and external-access requirements.

## Follow-up validation release

A subsequent research phase adds seven integrity tests (27 total), source-only ASQA/ELI5 transfer, raw-URL PhiUSIIL representation checks, and frozen-model independent simulation testing. The original astronomy pilot contained zero target events; the separately planned remaining-object test contained only two and missed both at the 5% budget. Sparse-event/bootstrap limitations are explicit. These results do not establish scientific novelty or real-world effectiveness. The research report and checkpoint are authoritative for current follow-up status. Career-document test counts were synchronized to 27.


## October 19 research comparison release

Research commit `127cdbead923e4d88b8664e299ddcdff2d8ce369` adds a hash-pinned, openly licensed CPU entailment comparison on ALCE and a frozen-model OpenPhish snapshot probe. NLI AP was lower than lexical AP in both transfer directions; its source-selected review policy missed the 90% recall goal in one direction. The one-class feed probe has provider labels and no benign controls, so its 297/299 agreement does not establish precision or deployment FPR. No raw feed URLs are published. Thirty-three local research integrity tests passed; optional runtime dependency scanning reported no advisories at scan time. Public IRSA access is verified, but matched specialised astronomy and observed-event evaluation remain unfinished. Current details are in [the measured report](https://github.com/Sunnyvulli/Data-Engineer_AI/blob/main/research-suite/results/followup/OPEN_COMPARISON_REPORT.md). Career files reflect these bounded project changes only; no employment, education or credentials were added.
