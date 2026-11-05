"""Build the academic CV from its plain-text source."""

from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from document_links import linked_text

ROOT = Path(__file__).resolve().parents[1]


def main():
    pdfmetrics.registerFont(
        TTFont("CVSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("CVBold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
    )
    styles = {
        "name": ParagraphStyle(
            "name", fontName="CVBold", fontSize=18, leading=22, spaceAfter=5
        ),
        "heading": ParagraphStyle(
            "heading",
            fontName="CVBold",
            fontSize=10,
            leading=13,
            spaceBefore=7,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body", fontName="CVSerif", fontSize=10, leading=11.5, spaceAfter=2
        ),
        "url": ParagraphStyle(
            "url", fontName="CVSerif", fontSize=9.5, leading=11, spaceAfter=4
        ),
    }
    flow = []
    for i, line in enumerate(
        (ROOT / "assets/Hanumantha-Rao-Academic-CV.txt").read_text().splitlines()
    ):
        if not line:
            continue
        if line == "SELECTED PROJECTS CONTINUED":
            flow.append(PageBreak())
        kind = (
            "name"
            if i == 0
            else (
                "heading"
                if line.isupper() and len(line) < 60
                else "url" if line.startswith("https://") else "body"
            )
        )
        flow.append(Paragraph(linked_text(line), styles[kind]))
    SimpleDocTemplate(
        str(ROOT / "assets/Hanumantha-Rao-Academic-CV.pdf"),
        pagesize=(595.2756, 841.8898),
        leftMargin=54,
        rightMargin=54,
        topMargin=44,
        bottomMargin=44,
        title="Hanumantha Rao Vulli - Academic CV",
        author="Hanumantha Rao Vulli",
    ).build(flow)


if __name__ == "__main__":
    main()
