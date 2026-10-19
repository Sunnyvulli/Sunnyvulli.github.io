"""Check local links, career document extraction, and reviewed project evidence."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError(f'Duplicate HTML id: {attrs["id"]}')
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            if name in attrs:
                self.links.append(attrs[name])


def normalized(text):
    return re.sub(r"\s+", "", text)


def main():
    parser = Links()
    parser.feed((ROOT / "index.html").read_text())
    for link in parser.links:
        parsed = urlparse(link)
        if parsed.scheme or parsed.netloc:
            continue
        if parsed.path:
            path = ROOT / unquote(parsed.path.lstrip("/"))
            if not path.exists():
                raise ValueError(f"Missing local link: {link}")
        elif parsed.fragment and parsed.fragment not in parser.ids:
            raise ValueError(f"Missing section: {link}")
    results = []
    for name in ("Resume", "Cover-Letter", "Academic-CV"):
        stem = f"Hanumantha-Rao-{name}"
        source = (ROOT / "assets" / f"{stem}.txt").read_text()
        reader = PdfReader(ROOT / "assets" / f"{stem}.pdf")
        extracted = "".join(page.extract_text() or "" for page in reader.pages)
        if normalized(source) != normalized(extracted):
            raise ValueError(f"Text/PDF drift: {stem}")
        if len(reader.pages) != 1:
            raise ValueError(f"Unexpected page count: {stem}")
        if any(len(page.images) for page in reader.pages):
            raise ValueError(f"Unexpected image in text-based document: {stem}")
        if "Applied ML Research Suite" not in extracted:
            raise ValueError(f"Research evidence missing: {stem}")
        results.append(
            {
                "document": stem,
                "pages": len(reader.pages),
                "source_text_matches": True,
                "image_count": 0,
            }
        )
    evidence = json.loads((ROOT / "career-evidence.json").read_text())
    assert len(evidence["projects"]) == 3
    print(
        json.dumps(
            {"local_links_checked": len(parser.links), "documents": results}, indent=2
        )
    )


if __name__ == "__main__":
    main()
