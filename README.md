# Hanumantha Rao Vulli | Data Engineering & Research

**[Open portfolio](https://sunnyvulli.github.io/)** · [Resume](assets/Hanumantha-Rao-Resume.pdf) · [Academic CV](assets/Hanumantha-Rao-Academic-CV.pdf)

## Start here

| Evidence | What to inspect |
|---|---|
| [Mobility Quality Lab](projects/mobility-quality) | Real historical data, deterministic Python/SQLite pipeline, local API, tests, and operator guide |
| [Reproducible study](research/mobility-study.pdf) | Measured evaluation, leakage controls, fault injection, limitations; unpublished draft |
| [Teaching lab](teaching/data-reliability-lab.md) | SQL/Python lesson with exercises, expected answers, and scoring rubric |

The flagship project uses 17,379 real hourly observations with source/license attribution. Seven system tests pass locally. CI runs the tests and a pinned-dependency evaluation. The containerized API has a dedicated CI build, non-root runtime, HTTP-contract, and read-only-filesystem check. GitHub Pages serves static content; the Python API runs locally.

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

This loads the real dataset twice into an isolated temporary database, checks expected totals, and executes seven system tests. The full research reproduction below installs scientific dependencies separately. A run under five minutes is only claimed for the recorded test environment, not every clean machine.

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
This is historical system-wide data, not live station-level availability. No client adoption, distributed cloud deployment, or published research is claimed. Next: whole-day rolling-origin evaluation, stronger time-series baselines, and a second dataset. Additional separate repositories should be created only when distinct projects are complete enough to inspect. No empty repositories are created to fill a pin quota.

Software licensing: projects/mobility-quality/LICENSE. Dataset attribution: projects/mobility-quality/data/SOURCE.md. Resume credentials follow the supplied resume; external verification links are still needed.

Engineering trade-offs: [docs/decisions.md](docs/decisions.md). Gold Standard audit: [docs/profile-audit.md](docs/profile-audit.md).

## Container and history verification

Run `docker compose up --build --wait` to start the local API, then visit http://127.0.0.1:8080/health . See [security/container workflow](.github/workflows/security-container.yml) and [security notes](docs/security.md).
