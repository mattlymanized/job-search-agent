#!/usr/bin/env python3
"""Build a designed PDF and an ATS-safe PDF from a content file.

Usage: python3 build_resume_pdfs.py CONTENT.py OUTPUT_FOLDER COMPANY

CONTENT.py is a small Python file that defines the resume text. See
../templates/resume-content.template.py for every field. The script never
overwrites an existing file: a taken name gets -v2, -v3 and so on.
Requires Playwright with Chromium.
"""
import html
import importlib.util
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

if len(sys.argv) != 4:
    sys.exit(__doc__)

content_path, out_dir, label = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
spec = importlib.util.spec_from_file_location("resume_content", content_path)
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

e = html.escape
ACCENT = getattr(C, "ACCENT", "#3b6f8f")
TARGET_PAGES = getattr(C, "TARGET_PAGES", 2)
EXTRA_TITLE = getattr(C, "EXTRA_SECTION_TITLE", "Additional Information")
out_dir.mkdir(parents=True, exist_ok=True)


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")


def free_path(base):
    """Return base, or base-v2, base-v3... so nothing is ever overwritten."""
    p, n = out_dir / f"{base}.pdf", 2
    while p.exists():
        p = out_dir / f"{base}-v{n}.pdf"
        n += 1
    return p


def bullets(items):
    return "<ul>" + "".join(f"<li>{e(b)}</li>" for b in items) + "</ul>"


def designed():
    def role(r):
        h = f'<div class="co">{e(r["company"])}</div>'
        for t, d in r["titles"]:
            h += f'<div class="row it"><span>{e(t)}</span><span>{e(d)}</span></div>'
        return h + f'<p>{e(r["intro"])}</p>' + bullets(r["bullets"])

    roles = "".join(role(r) for r in C.ROLES)
    early = "".join(f'<p class="early"><b>{e(x["name"])}</b>{e(x["rest"])}</p>' for x in C.EARLIER)
    edu = "".join(f'<p class="edu"><b>{e(a)}</b>{e(b)}</p>' for a, b in C.EDUCATION)
    extra = ""
    if C.ADDITIONAL:
        add = "".join(f'<div class="add">{e(a)}</div>' for a in C.ADDITIONAL)
        extra = f'<hr><div class="sec"><h2>{e(EXTRA_TITLE)}</h2>{add}</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{e(C.NAME)} Resume</title><style>
@page {{ size: Letter; margin: 0.55in 0.6in; }}
body {{ font-family: Carlito, Calibri, sans-serif; font-size: 10.2pt; line-height: 1.22; margin:0; }}
h1 {{ text-align:center; font-weight:400; font-size:21pt; margin:0 0 2pt 0; }}
.contact {{ text-align:center; font-size:9.2pt; margin-bottom:8pt; }}
hr {{ border:0; border-top:1.2pt solid {ACCENT}; margin:7pt 0 6pt 0; }}
h2 {{ text-align:center; font-size:12.5pt; margin:4pt 0 6pt 0; }}
p {{ margin:0 0 3pt 0; }} .prof {{ margin-top:5pt; }}
.co {{ font-weight:700; margin-top:6pt; }}
.row {{ display:flex; justify-content:space-between; }} .it {{ font-style:italic; }}
ul {{ margin:2pt 0 0 0; padding-left:18pt; }} li {{ margin:0 0 2.2pt 0; padding-left:2pt; }}
.early {{ margin-top:6pt; }} .edu {{ margin:0 0 2pt 0; }} .add {{ font-size:9.6pt; }}
.sec {{ break-inside: avoid; }}
</style></head><body>
<h1>{e(C.NAME)}</h1><div class="contact">{e(C.CONTACT)}</div><hr>
<p><b>{e(C.SUMMARY_LEAD)}</b>{e(C.SUMMARY_REST)}</p>
<p class="prof"><b>Proficient in:</b></p><p>{e(" · ".join(C.SKILLS))}</p>
<hr><h2>Experience</h2>{roles}{early}
<hr><div class="sec"><h2>Education</h2>{edu}</div>
{extra}
</body></html>"""


def ats():
    def role(r):
        # Every title line carries the company, and "Previous:" is dropped,
        # so a parser reads separate jobs.
        triples = r.get("ats_titles") or [
            (t.replace("Previous: ", ""), r["company"], d) for t, d in r["titles"]
        ]
        lines = "".join(
            f'<div class="{"rl" if i == 0 else "rl2"}">{e(t)} | {e(co)} | {e(d)}</div>'
            for i, (t, co, d) in enumerate(triples)
        )
        return lines + f'<p>{e(r["intro"])}</p>' + bullets(r["bullets"])

    roles = "".join(role(r) for r in C.ROLES)
    early = "".join(f'<p>{e(x["name"] + x["rest"])}</p>' for x in C.EARLIER)
    edu = "".join(f'<p>{e(a + b)}</p>' for a, b in C.EDUCATION)
    extra = ""
    if C.ADDITIONAL:
        add = "".join(f'<p class="tight">{e(a)}</p>' for a in C.ADDITIONAL)
        extra = f"<h2>{e(EXTRA_TITLE)}</h2>{add}"
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{e(C.NAME)} Resume</title><style>
@page {{ size: Letter; margin: 0.6in 0.7in; }}
body {{ font-family: Arial, "Liberation Sans", Helvetica, sans-serif; font-size:10pt; line-height:1.28; margin:0; }}
h1 {{ font-size:18pt; margin:0 0 2pt 0; }} .contact {{ margin-bottom:8pt; }}
h2 {{ font-size:11pt; text-transform:uppercase; margin:10pt 0 4pt 0; border-bottom:0.6pt solid #000; break-after:avoid; }}
p {{ margin:0 0 4pt 0; }} .tight {{ margin:0 0 2pt 0; }}
.rl {{ font-weight:700; margin-top:6pt; break-after:avoid; }} .rl2 {{ font-weight:700; }}
ul {{ margin:2pt 0 0 0; padding-left:16pt; }} li {{ margin:0 0 2.5pt 0; }}
</style></head><body>
<h1>{e(C.NAME)}</h1><div class="contact">{e(C.CONTACT)}</div>
<h2>Summary</h2><p>{e(C.SUMMARY_LEAD + C.SUMMARY_REST)}</p>
<h2>Skills</h2><p>{e(", ".join(C.SKILLS))}</p>
<h2>Experience</h2>{roles}{early}
<h2>Education</h2>{edu}
{extra}
</body></html>"""


base = f"{slug(C.NAME)}-Resume-{slug(label)}"
with sync_playwright() as p:
    browser = p.chromium.launch()
    for suffix, build in (("", designed), ("-ATS", ats)):
        page = browser.new_page()
        page.set_content(build())
        path = free_path(base + suffix)
        page.pdf(path=str(path), format="Letter", print_background=True, prefer_css_page_size=True)
        pages = len(re.findall(rb"/Type\s*/Page[^s]", path.read_bytes()))
        flag = "" if pages == TARGET_PAGES else f"  <-- NOT {TARGET_PAGES} PAGES, tell the user before cutting"
        print(f"{path}: {pages} pages{flag}")
    browser.close()
