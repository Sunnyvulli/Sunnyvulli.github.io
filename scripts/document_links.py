"""Escape document text while preserving clickable, visible HTTPS URLs."""

import re
from xml.sax.saxutils import escape


def linked_text(text):
    parts = re.split(r"(https://[^\s<>]+)", text)
    return "".join(
        (
            f'<link href="{escape(part, {chr(34): "&quot;"})}"><u>{escape(part)}</u></link>'
            if part.startswith("https://")
            else escape(part)
        )
        for part in parts
    )
