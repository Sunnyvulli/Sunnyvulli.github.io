"""Build a readable single-column resume with ordered, selectable text."""

from pathlib import Path
from xml.sax.saxutils import escape
from document_links import linked_text
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/Hanumantha-Rao-Resume.txt"
TARGET = ROOT / "assets/Hanumantha-Rao-Resume.pdf"
pdfmetrics.registerFont(
    TTFont("ResumeSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
)
pdfmetrics.registerFont(
    TTFont("ResumeSansBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
)
pdfmetrics.registerFontFamily("ResumeSans", normal="ResumeSans", bold="ResumeSansBold")
INK = colors.HexColor("#172C40")
ACCENT = colors.HexColor("#27596C")
MUTED = colors.HexColor("#46535F")
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
        "name",
        fontName="ResumeSansBold",
        fontSize=22,
        leading=25,
        textColor=INK,
        spaceAfter=4,
    ),
    "headline": ParagraphStyle(
        "headline",
        fontName="ResumeSansBold",
        fontSize=10.5,
        leading=13,
        textColor=ACCENT,
        spaceAfter=4,
    ),
    "contact": ParagraphStyle(
        "contact",
        fontName="ResumeSans",
        fontSize=9.2,
        leading=11.5,
        textColor=MUTED,
        spaceAfter=2,
    ),
    "section": ParagraphStyle(
        "section",
        fontName="ResumeSansBold",
        fontSize=10,
        leading=12,
        textColor=ACCENT,
        spaceBefore=4,
        spaceAfter=2,
        keepWithNext=True,
    ),
    "body": ParagraphStyle(
        "body",
        fontName="ResumeSans",
        fontSize=9.5,
        leading=11.2,
        textColor=INK,
        spaceAfter=2,
    ),
    "job": ParagraphStyle(
        "job",
        fontName="ResumeSans",
        fontSize=9.5,
        leading=11.2,
        textColor=INK,
        spaceBefore=2,
        spaceAfter=1,
        keepWithNext=True,
    ),
    "bullet": ParagraphStyle(
        "bullet",
        fontName="ResumeSans",
        fontSize=9.5,
        leading=11.2,
        textColor=INK,
        leftIndent=9,
        firstLineIndent=-9,
        spaceAfter=2,
    ),
    "url": ParagraphStyle(
        "url",
        fontName="ResumeSans",
        fontSize=8.6,
        leading=10.5,
        textColor=MUTED,
        spaceAfter=2,
        keepWithNext=True,
    ),
}


def heading_text(line, section):
    """Emphasize identities without splitting dates into a separate column."""
    parts = line.split(" | ")
    if section == "PROFESSIONAL EXPERIENCE":
        return " | ".join(
            f"<b>{escape(part)}</b>" if i < 2 else escape(part)
            for i, part in enumerate(parts)
        )
    return " | ".join(
        f"<b>{escape(part)}</b>" if i == 0 else escape(part)
        for i, part in enumerate(parts)
    )


def main():
    flow = []
    section = ""
    for i, line in enumerate(SOURCE.read_text().splitlines()):
        if not line:
            continue
        if line in SECTIONS:
            section = line
            flow.append(Paragraph(line, styles["section"]))
            rule = HRFlowable(
                width="100%",
                thickness=0.45,
                color=colors.HexColor("#C9D3DA"),
                spaceAfter=2,
            )
            rule.keepWithNext = True
            flow.append(rule)
            continue
        if i == 0:
            style = "name"
        elif i == 1:
            style = "headline"
        elif i in (2, 3, 4):
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
        text = heading_text(line, section) if style == "job" else linked_text(line)
        flow.append(Paragraph(text, styles[style]))
        if i == 4:
            flow.append(Spacer(1, 3))
    SimpleDocTemplate(
        str(TARGET),
        pagesize=(612, 792),
        leftMargin=38,
        rightMargin=38,
        topMargin=25,
        bottomMargin=25,
        title="Hanumantha Rao Vulli - Data Engineer Resume",
        author="Hanumantha Rao Vulli",
    ).build(flow)


if __name__ == "__main__":
    main()
