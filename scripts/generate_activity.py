#!/usr/bin/env python3
# Visualize public GitHub events; these are not contribution counts.
import datetime as dt
import json
import os
import urllib.request
from pathlib import Path

user='abubakar-maqsood'
today=dt.datetime.now(dt.timezone.utc).date()
start=today-dt.timedelta(days=29)
url=f'https://api.github.com/users/{user}/events/public?per_page=100'
headers={'User-Agent':'github-profile-readme','Accept':'application/vnd.github+json'}
if os.environ.get('GH_TOKEN'):
    headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
try:
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=20) as resp:
        events=json.load(resp)
    if not isinstance(events,list): raise ValueError('Unexpected API response')
except Exception as exc:
    print('Keeping existing chart because API is unavailable:',exc)
    raise SystemExit(0)
counts=[0]*30
for event in events:
    try:
        day=dt.date.fromisoformat(event['created_at'][:10])
        i=(day-start).days
        if 0<=i<30: counts[i]+=1
    except (KeyError,TypeError,ValueError): pass
maximum=max(1,max(counts))
bar=[]
for i,count in enumerate(counts):
    x=25+i*30
    height=8 if not count else 12+int(72*count/maximum)
    y=146-height
    col='#264a53' if not count else '#42cabb'
    bar.append(f'<rect x="{x}" y="{y}" width="18" height="{height}" rx="4" fill="{col}"/>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="940" height="184" viewBox="0 0 940 184">
<text x="15" y="25" fill="#d4e6ec" font-size="16" font-weight="700" font-family="Arial,Helvetica,sans-serif" letter-spacing="1.5">GITHUB ACTIVITY</text>
<text x="15" y="45" fill="#8398a3" font-size="12" font-family="Arial,Helvetica,sans-serif">Last 30 days of public events · Updated {today} UTC</text>
<path d="M18 76H925 M18 106H925 M18 146H925" stroke="#30414d" stroke-opacity=".35" stroke-dasharray="3 9" />
{''.join(bar)}
<text x="15" y="170" fill="#8398a3" font-size="11" font-family="Arial,Helvetica,sans-serif">{sum(counts)} recent public events returned · Private contributions not included · API may omit older events</text>
</svg>'''
path=Path('assets/2026-refresh/activity-events.svg')
path.write_text(svg,encoding='utf-8')
