#!/usr/bin/env python3
"""Render an editable, honest milestone dashboard for the GitHub profile.

Edit data/projects.json first. The visual reflects manual checklists, NOT
GitHub commit volume, AI skill level, research output, or automatic project progress.
"""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/projects.json').read_text(encoding='utf-8'))
projects=DATA['projects']
WIDTH=1120
HEIGHT=107+len(projects)*156+55
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Project milestone dashboard with current stages and next actions">',
'<defs><linearGradient id="bg" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#0b1828"/><stop offset="1" stop-color="#11253b"/></linearGradient><style><![CDATA[.title{font:700 26px Arial,sans-serif;fill:#eff6ff}.note{font:15px Arial,sans-serif;fill:#b0c9db}.name{font:700 22px Arial,sans-serif;fill:#f3f8ff}.phase{font:14px Arial,sans-serif;fill:#99b4c8}.next{font:15px Arial,sans-serif;fill:#d3e6f2}.counter{font:700 16px Arial,sans-serif;fill:#dceeff}@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}.bar{transform-box:fill-box;transform-origin:left;animation:grow 1.4s ease both}]]></style></defs>',
f'<rect width="{WIDTH}" height="{HEIGHT}" rx="23" fill="url(#bg)" stroke="#214357" stroke-width="2"/>',
'<circle cx="39" cy="44" r="6" fill="#46dfcb"/><text x="58" y="54" class="title">Selected project milestones</text>',
'<text x="58" y="81" class="note">Checklist-based progress · Current stage · Next objective</text>']
for i,p in enumerate(projects):
    y=105+i*156
    name=html.escape(p['name']);phase=html.escape(p['phase']);nxt=html.escape(p['next'])
    color=p.get('accent','#49dcc7'); ms=p['milestones']; done=sum(bool(m['done']) for m in ms); total=max(len(ms),1)
    x=690; w=314; fill=int(w*done/total)
    s += [f'<rect x="28" y="{y}" width="1064" height="143" rx="15" fill="#152e44" stroke="#26475b"/>',
          f'<rect x="45" y="{y+21}" width="5" height="38" rx="2" fill="{color}"/>',
          f'<text x="65" y="{y+48}" class="name">{name}</text>',
          f'<text x="65" y="{y+75}" class="phase">{phase}</text>',
          f'<text x="65" y="{y+113}" class="next">Next: {nxt}</text>',
          f'<rect x="{x}" y="{y+29}" width="{w}" height="15" rx="7" fill="#2a4359"/>',
          f'<rect x="{x}" y="{y+29}" width="{fill}" height="15" rx="7" fill="{color}" class="bar"/>',
          f'<text x="1029" y="{y+43}" class="counter">{done}/{total}</text>',
          f'<text x="{x}" y="{y+72}" class="phase">{done} of {total} listed milestones completed</text>']
s.append(f'<text x="38" y="{HEIGHT-24}" class="note">Manually maintained in data/projects.json · Not a skill or code-activity score</text>')
s.append('</svg>')
(ROOT/'assets/project-dashboard.svg').write_text('\n'.join(s),encoding='utf-8')
print(f'Rendered {len(projects)} projects to assets/project-dashboard.svg')
