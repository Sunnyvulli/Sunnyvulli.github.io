"""Render portfolio research cards from the reviewed evidence manifest."""

import argparse
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- RESEARCH_CARDS_START -->"
END = "<!-- RESEARCH_CARDS_END -->"


def render():
    evidence = json.loads((ROOT / "career-evidence.json").read_text())
    cards = []
    for p in evidence["projects"]:
        cards.append(
            '<article class="card"><span class="num">EXECUTED BASELINE</span>'
            f'<h3>{escape(p["title"])}</h3><p>{escape(p["description"])}</p>'
            f'<p>{escape(p["detail"])}</p><a class="btn" href="{escape(p["url"], quote=True)}">Methods and evidence ↗</a></article>'
        )
    return (
        '<div class="grid" style="margin-top:28px">'
        + "".join(cards)
        + '</div><p style="font-size:12px">Developed with Codex assistance. <a href="https://github.com/Sunnyvulli/Data-Engineer_AI/blob/main/research-suite/results/SUMMARY.md">Measured results</a> · <a href="https://github.com/Sunnyvulli/Data-Engineer_AI/blob/main/research-suite/docs/PROVENANCE.md">Sources and provenance</a> · <a href="https://github.com/Sunnyvulli/Data-Engineer_AI/blob/main/research-suite/results/followup/REPORT.md">Follow-up validation report</a></p>'
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = ROOT / "index.html"
    text = path.read_text()
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("Exactly one pair of research-card markers is required")
    before, rest = text.split(START)
    _, after = rest.split(END)
    updated = before + START + render() + END + after
    if args.check:
        if text != updated:
            raise SystemExit(
                "Evidence cards have drifted; run python scripts/sync_evidence.py"
            )
    else:
        path.write_text(updated)


if __name__ == "__main__":
    main()
