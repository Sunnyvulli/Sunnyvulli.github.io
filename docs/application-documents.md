# Application documents

## Files
- assets/Hanumantha-Rao-Resume.pdf: general data-engineering resume.
- assets/Hanumantha-Rao-Resume.txt: complete plain-text resume source.
- assets/Hanumantha-Rao-Cover-Letter.pdf: reusable general data-engineering cover letter.
- assets/Hanumantha-Rao-Cover-Letter.txt: editable plain-text cover-letter source.

The portfolio links these files directly. The resume keeps its existing URL, so existing profile links remain valid. The academic CV remains a separate document.

## Formatting choices
Both PDFs use a single text column, embedded DejaVu Sans fonts, ordinary headings, and no graphics, tables, text boxes, or contact information in page headers/footers. Name, phone, email, location, and links are ordinary document text. Employer dates and job titles follow a consistent format. The resume includes verified portfolio measurements separately from employment responsibilities; no employer performance figures are invented.

## Executed checks
Each PDF has one page, no image objects, and a size below 50 KB. Both pypdf and Poppler pdftotext recovered the complete text in the same order as the corresponding source file after whitespace normalization. Final pages were rendered and visually inspected. These are document/text-extraction checks, not tests inside Greenhouse, Workday, Lever, or a particular employer's ATS. No universal ATS score or interview outcome is guaranteed.

## Use and tailoring
Choose the employer's requested file format. This is a general resume, not a match score against a specific vacancy. Tailor the summary, skill emphasis, and selected evidence to a supplied job description without adding unsupported skills or outcomes. The cover letter is intentionally general because no employer or vacancy was supplied; customize the opening and fit paragraph for a real application. Do not submit research drafts as published work or claim current PhD enrollment.

## Rebuild
The builders use reportlab and DejaVu Sans regular/bold fonts at /usr/share/fonts/truetype/dejavu on Linux. These dependencies are needed only to author PDFs, not to run the project's normal smoke test. Run python scripts/build_resume.py and python scripts/build_cover_letter.py after editing the text sources. Recheck page count, text reading order, and rendered pages before replacing downloads.

## Vendor guidance consulted
Greenhouse. Unsuccessful resume parse. https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse (accessed October 18, 2026). The vendor documents parsing difficulties with images, columns, complex layouts, and contact information in headers/footers. Its guidance informed formatting; this does not mean the documents were tested in its ATS.
