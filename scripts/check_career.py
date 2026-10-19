"""Check local links, career document extraction, and reviewed project evidence."""

import json
import re
import unittest
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
    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "projects" / "mobility-quality")
    )
    if unittest.defaultTestLoader.errors:
        raise ValueError("Cannot discover flagship tests")
    test_count = suite.countTestCases()
    page = (ROOT / "index.html").read_text()
    declared_counts = re.findall(r"(\d+) passing tests", page)
    plain_page = re.sub(r"<[^>]*>", "", page)
    declared_counts += re.findall(r'"tests"\s*:\s*(\d+)', plain_page)
    declared_counts += re.findall(r"(\d+)\s*PASSING TESTS", plain_page)
    declared_counts += re.findall(r"number:'(\d+) tests", page)
    if not declared_counts or any(int(n) != test_count for n in declared_counts):
        raise ValueError("Portfolio test count differs from discovered suite")
    parser = Links()
    parser.feed(page)
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
        if f"{test_count} passing tests" not in source:
            raise ValueError(f"Flagship test count drift: {stem}")
        if "UCI Bike Sharing" not in source:
            raise ValueError(f"Dataset attribution missing: {stem}")
        if re.search(
            r"(?:\+1[\s.-]*)?\(?\d{3}\)?[\s.-]+\d{3}[\s.-]+\d{4}", source + extracted
        ):
            raise ValueError(f"Public phone number reintroduced: {stem}")
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
            {
                "flagship_tests": test_count,
                "local_links_checked": len(parser.links),
                "documents": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
