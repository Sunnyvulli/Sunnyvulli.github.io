"""Build the text-based, single-column resume. Requires reportlab."""

from pathlib import Path
from document_links import linked_text
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/Hanumantha-Rao-Resume.txt"
TARGET = ROOT / "assets/Hanumantha-Rao-Resume.pdf"
pdfmetrics.registerFont(
    TTFont("ResumeSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
)
pdfmetrics.registerFont(
    TTFont("ResumeSansBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
)
SECTIONS = {
    "PROFESSIONAL SUMMARY",
    "TECHNICAL SKILLS",
    "PROFESSIONAL EXPERIENCE",
    "SELECTED PROJECTS",
    "EDUCATION",
    "CERTIFICATIONS",
}
styles = {
    "name": ParagraphStyle(
        "name", fontName="ResumeSansBold", fontSize=19, leading=22, spaceAfter=3
    ),
    "headline": ParagraphStyle(
        "headline", fontName="ResumeSansBold", fontSize=10.3, leading=13, spaceAfter=3
    ),
    "contact": ParagraphStyle(
        "contact", fontName="ResumeSans", fontSize=9.1, leading=11.5, spaceAfter=2
    ),
    "section": ParagraphStyle(
        "section",
        fontName="ResumeSansBold",
        fontSize=10.5,
        leading=12,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True,
    ),
    "body": ParagraphStyle(
        "body", fontName="ResumeSans", fontSize=9.5, leading=11.5, spaceAfter=2
    ),
    "job": ParagraphStyle(
        "job",
        fontName="ResumeSansBold",
        fontSize=9.5,
        leading=11.5,
        spaceBefore=2,
        spaceAfter=2,
        keepWithNext=True,
    ),
    "bullet": ParagraphStyle(
        "bullet",
        fontName="ResumeSans",
        fontSize=9.5,
        leading=11.5,
        leftIndent=8,
        firstLineIndent=-8,
        spaceAfter=2,
    ),
    "url": ParagraphStyle(
        "url", fontName="ResumeSans", fontSize=8.4, leading=10, spaceAfter=2
    ),
}


def main():
    lines = SOURCE.read_text().splitlines()
    flow = []
    section = ""
    for i, line in enumerate(lines):
        if not line:
            continue
        if line in SECTIONS:
            section = line
            style = "section"
        elif i == 0:
            style = "name"
        elif i == 1:
            style = "headline"
        elif i in [2, 3]:
            style = "contact"
        elif line.startswith("- "):
            style = "bullet"
        elif line.startswith("https://"):
            style = "url"
        elif section == "PROFESSIONAL EXPERIENCE" or (
            section == "SELECTED PROJECTS" and "|" in line
        ):
            style = "job"
        else:
            style = "body"
        flow.append(Paragraph(linked_text(line), styles[style]))
    doc = SimpleDocTemplate(
        str(TARGET),
        pagesize=(612, 792),
        leftMargin=39,
        rightMargin=39,
        topMargin=31,
        bottomMargin=30,
        title="Hanumantha Rao Vulli - Data Engineer Resume",
        author="Hanumantha Rao Vulli",
    )
    doc.build(flow)


if __name__ == "__main__":
    main()
