#!/usr/bin/env python3
# Example run:
#   python3 piiScan.py ./searchText.txt
#   python3 piiScan.py ./searchText.txt --no-mask
#   python3 piiScan.py ./searchText.txt --max-results 1000
#   python3 piiScan.py ./searchText.txt --encoding latin-1
""" 
FOR EDUCATIONAL USE
"""
from __future__ import annotations
import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Set
# --------------------------- Regex Patterns
EMAIL_RE = re.compile(
    r"""
    (?<![\w.+-])                      # left boundary
    ([a-zA-Z0-9._%+-]+                # local part
    @
    [a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)* # domain labels
    \.[a-zA-Z]{2,63})                 # TLD
    (?![\w.+-])                       # right boundary
    """,
    re.VERBOSE,
)
PHONE_RE = re.compile(
    r"""
    (?<!\d)
    (?:\+?1[\s.-]?)?                  # optional country code
    (?:\(?(\d{3})\)?[\s.-]?)          # area code
    (\d{3})[\s.-]?                    # exchange
    (\d{4})                           # subscriber
    (?:\s*(?:ext\.?|x)\s*(\d{2,5}))?  # optional extension
    (?!\d)
    """,
    re.VERBOSE | re.IGNORECASE,
)
SSN_RE = re.compile(
    r"""
    (?<!\d)
    (\d{3}-\d{2}-\d{4})
    (?!\d)
    """,
    re.VERBOSE,
)
# --------------------------- Data Structures
@dataclass(frozen=True)
class ScanResults:
    emails: List[str]
    phones: List[str]
    ssns: List[str]
# --------------------------- File Handling
def iter_text_lines(path: Path, encoding: str = "utf-8") -> Iterable[str]:
    with path.open("r", encoding=encoding, errors="replace") as f:
        for line in f:
            yield line
# --------------------------- Normalization Helpers
def normalize_phone(area: str, exch: str, subs: str, ext: str | None) -> str:
    base = f"{area}-{exch}-{subs}"
    if ext:
        return f"{base} x{ext}"
    return base
# ---------------------------  Core Scanner
def scan_text(
    lines: Iterable[str],
    *,
    dedupe: bool = True,
    max_results: int | None = 5000,
) -> ScanResults:
    emails: List[str] = []
    phones: List[str] = []
    ssns: List[str] = []
    seen_emails: Set[str] = set()
    seen_phones: Set[str] = set()
    seen_ssns: Set[str] = set()
    def add(item: str, out: List[str], seen: Set[str]) -> None:
        if dedupe:
            if item in seen:
                return
            seen.add(item)
        out.append(item)
    for line in lines:
        for m in EMAIL_RE.finditer(line):
            add(m.group(1), emails, seen_emails)
        for m in PHONE_RE.finditer(line):
            area, exch, subs, ext = m.group(1), m.group(2), m.group(3), m.group(4)
            add(normalize_phone(area, exch, subs, ext), phones, seen_phones)
        for m in SSN_RE.finditer(line):
            add(m.group(1), ssns, seen_ssns)
        if max_results is not None:
            if (len(emails) + len(phones) + len(ssns)) >= max_results:
                break
    return ScanResults(emails=emails, phones=phones, ssns=ssns)
# --------------------------- Masking 
def mask_email(email: str) -> str:
    local, _, domain = email.partition("@")
    if len(local) <= 2:
        masked_local = local[0] + "*"
    else:
        masked_local = local[0] + ("*" * (len(local) - 2)) + local[-1]
    return f"{masked_local}@{domain}"
def mask_phone(phone: str) -> str:
    parts = phone.split(" x", 1)
    main = parts[0]
    ext = (" x" + parts[1]) if len(parts) == 2 else ""
    digits = re.sub(r"\D", "", main)
    if len(digits) >= 10:
        return f"***-***-{digits[-4:]}{ext}"
    return f"***-***-****{ext}"
def mask_ssn(ssn: str) -> str:
    return "***-**-" + ssn[-4:]
# --------------------------- DISPLAY
def display(results: ScanResults, *, mask: bool = True) -> None:
    def show(title: str, items: List[str], masker):
        print("\n" + "-" * 45)
        if items:
            print(title.center(60))
            print(("-" * 30).center(60))
            for i in items:
                out = masker(i) if mask else i
                print(out.center(60))
        else:
            print(f"No {title.lower()}".center(60))
    show("Emails found:", results.emails, mask_email)
    show("Phone numbers found:", results.phones, mask_phone)
    show("SSN-like patterns found:", results.ssns, mask_ssn)
    print("\n" + "-" * 45 + "\n")
# --------------------------- MAIN
def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pii_scan",
        description="Scan a text file for emails, phone numbers, and SSN-like patterns.",
    )
    parser.add_argument("path", help="Path to a text file to scan")
    parser.add_argument("--no-mask", action="store_true", help="Print raw matches (default: masked)")
    parser.add_argument("--no-dedupe", action="store_true", help="Do not deduplicate matches")
    parser.add_argument("--max-results", type=int, default=5000, help="Maximum total matches")
    parser.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")
    args = parser.parse_args()
    path = Path(args.path).expanduser().resolve()
    if not path.exists() or not path.is_file():
        raise SystemExit(f"File not found: {path}")
    lines = iter_text_lines(path, encoding=args.encoding)
    results = scan_text(
        lines,
        dedupe=not args.no_dedupe,
        max_results=args.max_results,
    )
    display(results, mask=not args.no_mask)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
