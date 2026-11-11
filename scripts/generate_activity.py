#!/usr/bin/env python3
"""Generate a styled public-event SVG; events API is bounded and is not contributions/streak data."""
import datetime as dt, json, os, urllib.request
from pathlib import Path
user=os.getenv('ACTIVITY_USER','abubakar-maqsood')
root=Path(__file__).resolve().parents[1]
out=root/'assets/2026-refresh/activity-events.svg'
today=dt.datetime.now(dt.timezone.utc).date()
start=today-dt.timedelta(days=29)
counts=[0]*30
req=urllib.request.Request(
    f'https://api.github.com/users/{user}/events/public?per_page=100',
    headers={
        'User-Agent':'github-profile-activity-generator',
        'Accept':'application/vnd.github+json',
        'Authorization':'Bearer '+os.environ.get('GH_TOKEN','')
    }
)
try:
    with urllib.request.urlopen(req,timeout=18) as response:
        events=json.load(response)
    if not isinstance(events,list):
        raise ValueError('Events response was not an array')
except Exception as ex:
    print('Could not retrieve real public events; existing SVG remains:',ex)
    raise SystemExit(0)
for event in events:
    try:
        day=dt.date.fromisoformat(event['created_at'][:10])
        idx=(day-start).days
        if 0<=idx<30:
            counts[idx]+=1
    except Exception:
        pass
mx=max(max(counts),1)
bar_gap=29
bars=[]
labels=[]
for i,count in enumerate(counts):
    h=8 if count==0 else round(90*count/mx)+8
    x=42+i*bar_gap
    y=176-h
    fill='#203d4b' if count==0 else '#31d7c4'
    bars.append(f"<rect x='{x}' y='{y}' width='18' height='{h}' rx='5' fill='{fill}'/>")
    if i in (0, 9, 19, 29):
        d=(start+dt.timedelta(days=i)).isoformat()
        labels.append(f"<text x='{x+9}' y='201' text-anchor='middle' fill='#90b8c3' font-size='11' font-family='Arial, Helvetica, sans-serif'>{d[5:]}</text>")
total=sum(counts)
svg = f"""<svg xmlns='http://www.w3.org/2000/svg' width='960' height='230' viewBox='0 0 960 230'>
  <defs><linearGradient id='bg' x1='0' x2='1' y1='0' y2='1'><stop offset='0%' stop-color='#0b1f31'/><stop offset='100%' stop-color='#12273b'/></linearGradient></defs>
  <rect width='960' height='230' rx='24' fill='url(#bg)'/>
  <rect x='1' y='1' width='958' height='228' rx='23' fill='none' stroke='#29506a'/>
  <text x='34' y='44' font-family='Arial, Helvetica, sans-serif' font-size='18' font-weight='700' fill='#ecfbf7'>PUBLIC GITHUB ACTIVITY</text>
  <text x='34' y='70' font-family='Arial, Helvetica, sans-serif' font-size='14' fill='#a8c8d3'>Last 30 days of public events - updated {today.isoformat()} UTC - {total} events found</text>
  <g opacity='0.55'><path d='M34 184 H925' stroke='#2f4e62'/><path d='M34 150 H925' stroke='#213b4b' stroke-dasharray='5 10'/><path d='M34 116 H925' stroke='#213b4b' stroke-dasharray='5 10'/><path d='M34 82 H925' stroke='#213b4b' stroke-dasharray='5 10'/></g>
  {''.join(bars)}
  {''.join(labels)}
  <text x='34' y='215' font-family='Arial, Helvetica, sans-serif' font-size='12' fill='#8bb2bf'>Uses GitHub public events API. This is activity, not the same thing as private contributions or total contribution count.</text>
</svg>"""
out.write_text(svg, encoding='utf-8')
print('Wrote', out, 'based on', len(events), 'public recent events')
