#!/usr/bin/env python3
"""Generate a public-event SVG; events API is bounded and is not contributions/streak data."""
import datetime as dt, json, os, urllib.request, xml.sax.saxutils as x
from pathlib import Path
user=os.getenv('ACTIVITY_USER','abubakar-maqsood')
root=Path(__file__).resolve().parents[1]
out=root/'assets/2026-refresh/activity-events.svg'
today=dt.datetime.now(dt.timezone.utc).date()
start=today-dt.timedelta(days=29)
counts=[0]*30
req=urllib.request.Request(f'https://api.github.com/users/{user}/events/public?per_page=100',headers={'User-Agent':'github-profile-activity-generator','Accept':'application/vnd.github+json','Authorization':'Bearer '+os.environ.get('GH_TOKEN','')})
try:
    with urllib.request.urlopen(req,timeout=18) as response: events=json.load(response)
    if not isinstance(events,list):raise ValueError('Events response was not an array')
except Exception as ex:
    print('Could not retrieve real public events; existing SVG remains:',ex)
    raise SystemExit(0)
for event in events:
    try:
        day=dt.date.fromisoformat(event['created_at'][:10]); index=(day-start).days
        if 0<=index<30:counts[index]+=1
    except (KeyError,ValueError,TypeError):pass
mx=max(max(counts),1)
bars=[]
for i,count in enumerate(counts):
    h=round(112*count/mx) if count else 3
    cx=38+i*29
    bars.append(f'<rect x="{cx}" y="{174-h}" width="17" height="{h}" rx="4" fill="{("#47c9b0" if count else "#213948")}"/>')
total=sum(counts)
svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="950" height="220" viewBox="0 0 950 220"><rect width="950" height="220" rx="20" fill="#101d2b"/><rect x="1" y="1" width="948" height="218" rx="19" stroke="#365260" fill="none"/><text x="32" y="37" fill="#edf8f8" font-size="19" font-weight="700" font-family="Arial,sans-serif">PUBLIC GITHUB EVENTS</text><text x="32" y="60" fill="#a1c5c8" font-size="13" font-family="Arial,sans-serif">Last 30 days · updated {today.isoformat()} UTC · {total} recent public events returned</text><path d="M28 177H921" stroke="#35505b"/>{''.join(bars)}<text x="32" y="202" fill="#8eb2bd" font-size="12" font-family="Arial,sans-serif">{start.isoformat()}</text><text x="920" text-anchor="end" y="202" fill="#8eb2bd" font-size="12" font-family="Arial,sans-serif">{today.isoformat()}</text><title>Public event API, maximum 100 recent events; does not equal contribution count. Older events and private contributions may be absent.</title></svg>"""
out.write_text(svg)
print('Wrote',out,'based on',len(events),'public recent events')
