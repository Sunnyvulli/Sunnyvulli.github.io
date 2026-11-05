"""Render plain-language research summaries from the reviewed evidence manifest."""

import argparse
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- RESEARCH_CARDS_START -->"
END = "<!-- RESEARCH_CARDS_END -->"


def render():
    evidence = json.loads((ROOT / "career-evidence.json").read_text())
    entries = []
    for project in evidence["projects"]:
        entries.append(
            '<article class="research-entry"><div>'
            f'<h3>{escape(project["title"])}</h3>'
            '<span class="project-type">Independent study</span></div><div>'
            f'<p>{escape(project["description"])}</p>'
            "<details><summary>Methods and limitations</summary>"
            f'<p>{escape(project["detail"])}</p></details>'
            f'<a class="text-link" href="{escape(project["url"], quote=True)}">Read the study and evidence</a>'
            "</div></article>"
        )
    return "\n" + "\n".join(entries) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = ROOT / "index.html"
    text = path.read_text()
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("Exactly one pair of research markers is required")
    before, rest = text.split(START)
    _, after = rest.split(END)
    updated = before + START + render() + END + after
    if args.check:
        if text != updated:
            raise SystemExit("Research summaries have drifted; run sync_evidence.py")
    else:
        path.write_text(updated)


if __name__ == "__main__":
    main()
