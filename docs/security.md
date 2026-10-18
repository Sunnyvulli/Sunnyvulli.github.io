# Security and container verification

## Secret scanning
The dedicated workflow fetches the complete repository history (`fetch-depth: 0`) and invokes Gitleaks v8.24.2 with its default rules, `--log-opts=--all`, and `--redact`. No baseline exclusions or custom rule suppression are used. The source repository and download instructions are https://github.com/gitleaks/gitleaks . A local verification used the official Linux binary archive and verified its SHA-256 against the release checksum file.

A successful scan means no findings under that tool version and rule set in reachable history. It does not establish that credentials were never exposed, inspect unreachable/deleted objects, or prove the absence of every unknown credential format. If a real credential is found, revoke/rotate it before any history cleanup. Never paste its value into issues, PR descriptions, or logs.

## Container scope
The image uses the official Python 3.12 slim base, builds a SQLite snapshot from the attributed historical dataset, and executes tests. The running API uses UID 10001. Compose publishes port 8080 only to 127.0.0.1, sets a read-only filesystem, drops Linux capabilities, and enables no-new-privileges. Temporary test files use /tmp. The API opens SQLite with mode=ro.

CI checks actual health and date-query responses, invalid-date HTTP 400 behavior, non-root UID, and system tests inside the image. Missing database behavior is covered by an HTTP 503 test that also asserts no empty database file is created. The API has no authentication and must not be exposed publicly as a service without a separate design and deployment review.

## Reproduce
```sh
docker compose up --build --wait
# Inspect http://127.0.0.1:8080/health
docker compose exec -T mobility python -m unittest -v
docker compose down
```

For a local Gitleaks install, use the official release appropriate to your platform and verify its checksum. Then run:
```sh
gitleaks git . --log-opts=--all --redact --no-banner
```

The base image and scanner image are version-tagged, not pinned to immutable digests. Future dependency/image review should consider digest pinning and automated updates. CI status is the evidence of execution; configuration alone is not.
