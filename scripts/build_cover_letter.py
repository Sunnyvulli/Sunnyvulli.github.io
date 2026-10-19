"""Build the matching, selectable-text cover letter. Requires reportlab."""

from pathlib import Path
from document_links import linked_text
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(
    TTFont("LetterSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
)
pdfmetrics.registerFont(
    TTFont("LetterSansBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
)


def main():
    blocks = (
        (ROOT / "assets/Hanumantha-Rao-Cover-Letter.txt")
        .read_text()
        .strip()
        .split("\n\n")
    )
    flow = []
    name = ParagraphStyle(
        "name", fontName="LetterSansBold", fontSize=18, leading=23, spaceAfter=5
    )
    contact = ParagraphStyle(
        "contact", fontName="LetterSans", fontSize=9, leading=13, spaceAfter=3
    )
    body = ParagraphStyle(
        "body", fontName="LetterSans", fontSize=10.5, leading=16, spaceAfter=13
    )
    header = blocks.pop(0).splitlines()
    flow.append(Paragraph(linked_text(header[0]), name))
    for line in header[1:]:
        flow.append(Paragraph(linked_text(line), contact))
    flow.append(Spacer(1, 23))
    for block in blocks:
        flow.append(Paragraph(linked_text(block).replace("\n", "<br/>"), body))
    SimpleDocTemplate(
        str(ROOT / "assets/Hanumantha-Rao-Cover-Letter.pdf"),
        pagesize=(612, 792),
        leftMargin=47,
        rightMargin=47,
        topMargin=42,
        bottomMargin=40,
        title="Hanumantha Rao Vulli - Data Engineering Cover Letter",
        author="Hanumantha Rao Vulli",
    ).build(flow)


if __name__ == "__main__":
    main()
