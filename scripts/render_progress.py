#!/usr/bin/env python3
"""Render animated, static-hostable SVG bars from manually maintained milestones.

Usage: python scripts/render_progress.py
Requires only Python 3.9+ (standard library). No network access.
"""
from pathlib import Path
from html import escape
import json, re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'data' / 'projects.json'
outfile = ROOT / 'assets' / 'project-progress.svg'
data = json.loads(source.read_text(encoding='utf-8'))
projects = data['projects']
if not (1 <= len(projects) <= 10):
    raise SystemExit('Expected between 1 and 10 projects')

def esc(text):
    return escape(str(text), quote=True)

def accent(text):
    return text if isinstance(text, str) and re.fullmatch(r'#[0-9a-fA-F]{6}', text) else '#32d8c6'

W = 1100
H = 104 + len(projects)*110 + 46
lines = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">Project progress tracker</title>
<desc id="desc">Self-reported completion of documented project milestones. These are checklist counts, not objective estimates of software completion.</desc>
<defs>
  <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0b192a"/><stop offset="1" stop-color="#0e2937"/></linearGradient>
  <style>
  text {{ font-family: Arial, Helvetica, sans-serif; }}
  .name {{ font-size: 25px; font-weight: 700; fill: #f1fafc; }}
  .sub {{ font-size: 15px; fill: #a2bfca; }}
  .count {{ font-size: 18px; font-weight: 700; fill: #e7f8f9; }}
  </style>
</defs>
<rect width="{W}" height="{H}" rx="22" fill="url(#bg)" stroke="#244b59" />
<circle cx="52" cy="48" r="7" fill="#34d8c4"/>
<text x="74" y="57" font-size="28" font-weight="700" fill="#f0fbfc">Project milestones</text>
<text x="1040" y="55" font-size="16" text-anchor="end" fill="#9ebbc8">Updated from the checklist</text>"""]

for idx,p in enumerate(projects):
    items = p['milestones']
    if not isinstance(items,list) or not items:
        raise SystemExit(f'Project {p["name"]!r} needs at least one milestone')
    if not all(type(m.get('done')) is bool for m in items):
        raise SystemExit('Milestone done fields must be true or false')
    done = sum(m['done'] for m in items)
    total = len(items)
    width = round(460 * done / total)
    color = accent(p.get('accent','#32d8c6'))
    y = 94 + idx*110
    lines += [
      f'<rect x="29" y="{y}" width="1042" height="94" rx="13" fill="#162e40" stroke="#234657"/>',
      f'<rect x="44" y="{y+21}" width="5" height="52" rx="2" fill="{color}"/>',
      f'<text x="65" y="{y+40}" class="name">{esc(p["name"])}</text>',
      f'<text x="65" y="{y+67}" class="sub">{esc(p["phase"])}</text>',
      f'<rect x="527" y="{y+29}" width="460" height="18" rx="9" fill="#2b4659"/>',
      f'<rect x="527" y="{y+29}" width="{width}" height="18" rx="9" fill="{color}"><animate attributeName="width" from="0" to="{width}" dur="1.3s" begin="{idx*0.13}s" fill="freeze"/></rect>',
      f'<text x="1042" y="{y+43}" class="count" text-anchor="end">{done}/{total}</text>',
      f'<text x="527" y="{y+72}" class="sub">{done} of {total} listed milestones marked complete</text>'
    ]
lines += [f'<text x="43" y="{H-20}" font-size="14" fill="#83a4b3">Manual checklist · not GitHub activity · not a skill score</text>', '</svg>']
outfile.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Updated {outfile.relative_to(ROOT)}')
