# Hanumantha Rao Vulli | Data Engineering & Research

**[Open portfolio](https://sunnyvulli.github.io/)** · [Resume](assets/Hanumantha-Rao-Resume.pdf) · [Academic CV](assets/Hanumantha-Rao-Academic-CV.pdf)

## Start here

| Evidence | What to inspect |
|---|---|
| [Mobility Quality Lab](projects/mobility-quality) | Real historical data, deterministic Python/SQLite pipeline, local API, tests, and operator guide |
| [Reproducible study](research/mobility-study.pdf) | Measured evaluation, leakage controls, fault injection, limitations; unpublished draft |
| [Teaching lab](teaching/data-reliability-lab.md) | SQL/Python lesson with exercises, expected answers, and scoring rubric |

The flagship project uses 17,379 real hourly observations with source/license attribution. Thirteen tests (ten system and three temporal-protocol tests) pass locally. CI runs the tests and a pinned-dependency evaluation. The containerized API has a dedicated CI build, non-root runtime, HTTP-contract, and read-only-filesystem check. GitHub Pages serves static content; the Python API runs locally.

## Repository layout

- index.html: responsive portfolio with employer and faculty views
- projects/mobility-quality/: implementation, attributed data, tests, results, design, API, container option
- research/: manuscript source and PDF
- teaching/: practical lesson and rubric
- assets/: downloadable application documents
- evidence/data-quality/: earlier synthetic-data learning exercise
- .github/workflows/: deployment and verification

## One-command smoke run

Prerequisites: Python 3.11+ and GNU Make. No account, API key, or dependency installation is needed for this path. From a fresh clone:

```sh
make run
```

This loads the real dataset twice into an isolated temporary database, checks expected totals, and executes thirteen tests (ten system and three temporal-protocol tests). The full research reproduction below installs scientific dependencies separately. A run under five minutes is only claimed for the recorded test environment, not every clean machine.

## Reproduce

```sh
git clone https://github.com/Sunnyvulli/Sunnyvulli.github.io.git
cd Sunnyvulli.github.io/projects/mobility-quality
python pipeline.py
python -m unittest -v
python -m pip install -r requirements.txt
python evaluate.py
```

## Design decisions
SQLite keeps the complete local data path inspectable without account setup or paid services. SQL parameters protect query inputs. Dataset hashes and batch manifests support repeatable loading. Calendar and count reconciliation supplement domain checks. Missing observations are not fabricated. Evaluation separates temporal assessment from shuffled splits and explicitly identifies an invalid leakage control.

## Limitations and roadmap
This is historical system-wide data, not live station-level availability. No client adoption, distributed cloud deployment, or published research is claimed. Whole-day temporal evaluation and an online weekly-lag baseline are implemented. Next: independent dataset validation and a distinct cloud artifact with actual deployment evidence. Additional separate repositories should be created only when distinct projects are complete enough to inspect. No empty repositories are created to fill a pin quota.

Software licensing: projects/mobility-quality/LICENSE. Dataset attribution: projects/mobility-quality/data/SOURCE.md. Resume credentials follow the supplied resume; external verification links are still needed.

Engineering trade-offs: [docs/decisions.md](docs/decisions.md). Gold Standard audit: [docs/profile-audit.md](docs/profile-audit.md).

## Container and history verification

Run `docker compose up --build --wait` to start the local API, then visit http://127.0.0.1:8080/health . See [security/container workflow](.github/workflows/security-container.yml) and [security notes](docs/security.md).

## Temporal evaluation follow-up

[Whole-day backtest](research/temporal-followup.md): 84 historical test days, calendar-only forest MAE 49.766 versus online weekly-lag MAE 64.031. Protocol, seeds, raw results, exploratory uncertainty, and limitations are included. [Build note](docs/build-notes-temporal.md). After installing evaluation dependencies, run `make backtest`.

## Application documents

[ATS-friendly resume PDF](assets/Hanumantha-Rao-Resume.pdf) · [Resume text](assets/Hanumantha-Rao-Resume.txt) · [General cover letter PDF](assets/Hanumantha-Rao-Cover-Letter.pdf) · [Cover letter text](assets/Hanumantha-Rao-Cover-Letter.txt). Single-column selectable text; parsing checks and tailoring limits are documented in [application documents](docs/application-documents.md). No universal ATS score is claimed.

## Applied ML research suite

The [research repository](https://github.com/Sunnyvulli/Data-Engineer_AI) includes executed phishing robustness, citation-support triage, and simulated-transient ranking baselines, with 27 integrity tests, source-data hashes, and measured results. These are separately identified as baselines rather than accepted publications or production systems.

The resume, cover letter, and academic CV include this evidence. Research cards are generated from `career-evidence.json`; `scripts/check_career.py` and `scripts/sync_evidence.py --check` guard document/text and page-content drift. See [the account audit](docs/GITHUB_AUDIT.md) for scope and unresolved boundaries.

## Additional verified engineering
- [Lakehouse Guardian](https://github.com/Sunnyvulli/lakehouse-guardian): local Spark/Iceberg/dbt workflow, actual Airflow CI and validated Terraform; no AWS apply.
- [Catalog Sentinel](https://github.com/Sunnyvulli/catalog-sentinel): bounded read-only MCP tools and actual stdio misuse probes.
- [Evidence Ledger RAG](https://github.com/Sunnyvulli/evidence-ledger-rag): incremental lexical retrieval, cited extracts and retained guard failures; [recorded explorer](https://sunnyvulli.github.io/evidence-ledger-rag/).
