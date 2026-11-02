#!/usr/bin/env python3
"""Generate clean GitHub-compatible animated assets from editable milestone data.

- Header: real typing-name GIF
- Project dashboard: GIF bars rise from zero to the saved milestone fraction
- SVG: accessible alternative, uses SMIL width animation
- PNG poster frames for anyone who prefers static images
No automatic project completion detection: edit data/projects.json yourself.

Requires Pillow; run `python -m pip install pillow`.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, math, html

BASE = Path(__file__).resolve().parents[1]
ASSETS = BASE / 'assets'
ASSETS.mkdir(exist_ok=True)
PROJECTS = json.loads((BASE/'data/projects.json').read_text(encoding='utf-8'))['projects']

NAVY = (24, 25, 29)
NAVY2 = (32, 33, 36)
NAVY3 = (42, 43, 47)
CYAN = (216, 166, 89)
CYAN_BRIGHT = (231, 190, 121)
BLUE = (139, 160, 202)
WHITE = (242, 247, 255)
SUB = (180, 201, 221)
MUTED = (140, 170, 194)
TRACK = (66, 65, 67)
F = {
    'bold': ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf', 'DejaVuSans-Bold.ttf'],
    'regular': ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf','DejaVuSans.ttf'],
    'mono': ['/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 'DejaVuSansMono.ttf'],
}

def font(size, family='regular'):
    for file in F[family]:
        try: return ImageFont.truetype(file,size)
        except OSError: pass
    return ImageFont.load_default()

def tw(draw, text, f):
    return draw.textbbox((0,0),text,font=f)[2]

def lighten(c, factor): return tuple(min(255,int(v+(255-v)*factor)) for v in c)

def color(s, default=CYAN):
    if not isinstance(s,str) or not s.startswith('#') or len(s)!=7:return default
    return tuple(int(s[i:i+2],16) for i in (1,3,5))

def corner(draw,box,rad,fill,outline=None,width=1):
    draw.rounded_rectangle(box,radius=rad,fill=fill,outline=outline,width=width)

def bg(w,h):
    im=Image.new('RGB',(w,h),NAVY)
    p=im.load()
    for y in range(h):
        for x in range(w):
            t=.3*x/w+.28*y/h
            p[x,y]=(int(NAVY[0]*(1-t)+NAVY2[0]*t),int(NAVY[1]*(1-t)+NAVY2[1]*t),int(NAVY[2]*(1-t)+NAVY2[2]*t))
    d=ImageDraw.Draw(im)
    # restrained editorial grid for depth
    for x in range(40,w,48): d.line([(x,0),(x,h)], fill=(35,36,40),width=1)
    for y in range(38,h,48):d.line([(0,y),(w,y)], fill=(35,36,40),width=1)
    return im

def export_gif(images,filename,durations):
    # One shared 256-colour palette, avoids flicker across frames.
    pal=images[-1].convert('P', palette=Image.Palette.ADAPTIVE,colors=96)
    frames=[im.quantize(palette=pal, dither=Image.Dither.NONE) for im in images]
    frames[0].save(ASSETS/filename, save_all=True, append_images=frames[1:], optimize=True, loop=0, duration=durations, disposal=2)

def make_header():
    w,h=1200,278
    static=bg(w,h)
    d=ImageDraw.Draw(static)
    corner(d,(30,24,218,56),15,(13,58,70),outline=(23,156,169),width=2)
    d.ellipse((47,37,55,45),fill=CYAN_BRIGHT)
    d.text((64,33),'HELLO, I\'M ABK',font=font(15,'bold'),fill=(225,248,254))
    d.arc((950,-76,1260,242),60,300,fill=(31,78,100),width=3)
    d.arc((1006,-24,1226,198),58,302,fill=(29,106,122),width=2)
    d.text((1035,111),'</>',font=font(39,'mono'),fill=CYAN)
    d.text((932,242),'BUILD  /  LEARN  /  SHARE',font=font(12,'mono'),fill=(119,159,182))
    d.line((40,244,862,244),fill=(42,80,96),width=2)
    d.text((42,181),'AI Research Interests  /  Applied Machine Learning',font=font(22),fill=SUB)
    d.text((42,213),'Software Developer  /  Frontend, Shopify & SEO',font=font(19,'bold'),fill=CYAN_BRIGHT)
    name='Muhammad Abubakar Maqsood'
    size=51
    f=font(size,'bold')
    while tw(d,name,f)>900 and size>40:
        size-=1;f=font(size,'bold')
    # 42 frames ~6 seconds: type for 27 frames then hold full name
    images=[]; durations=[]
    for idx in range(43):
        im=static.copy();q=ImageDraw.Draw(im)
        chars= min(len(name),max(0,idx+1))
        visible=name[:chars]
        q.text((39,96),visible,font=f,fill=WHITE)
        endx=39+tw(q,visible,f)
        if idx % 6<4 and idx <36:
            corner(q,(endx+7,101,endx+12,144),2,CYAN_BRIGHT)
        # animated underline grows as typing completes
        size_line = int(810*(chars/len(name)))
        if size_line>0:
            corner(q,(41,158,41+size_line,162),2,CYAN)
        # status light quietly pulses; nonessential
        pulse=0.5+0.5*math.sin(idx*0.36)
        q.ellipse((1128,39,1139,50),fill=lighten((14,125,149),.3*pulse))
        images.append(im)
        durations.append(110 if idx<30 else 180)
    # ensure final frame has complete name and underline
    static_frame=static.copy();q=ImageDraw.Draw(static_frame)
    q.text((39,96),name,font=f,fill=WHITE);corner(q,(41,158,851,162),2,CYAN)
    static_frame.save(ASSETS/'name-cover-still.png',optimize=True)
    export_gif(images,'name-cover-typing.gif',durations)

def wrap_to_width(d,text,max_width,f,max_lines=2):
    words=text.split(); lines=[]; cur=''
    for w in words:
        cand=(cur+' '+w).strip()
        if tw(d,cand,f)>max_width and cur:
            lines.append(cur);cur=w
        else:cur=cand
    if cur:lines.append(cur)
    if len(lines)>max_lines:
        lines=lines[:max_lines]
        last=lines[-1]
        while tw(d,last+'...',f)>max_width and last:
            last=last[:-1]
        lines[-1]=last+'...'
    return lines

def draw_card(d,p,i,amount):
    y=104 + i*155
    ms=p.get('milestones',[]); total=max(len(ms),1)
    done=sum(bool(m.get('done')) for m in ms)
    c=color(p.get('accent'),[CYAN,BLUE,(181,150,238),(239,183,103)][i%4])
    # use accent colors kept in JSON; brighter using custom palette if stale
    if c==(69,217,197):c=CYAN
    elif c==(128,183,255):c=BLUE
    elif c==(194,163,255):c=(187,154,241)
    elif c==(241,189,112):c=(247,188,102)
    corner(d,(26,y,1094,y+140),18,NAVY3,outline=(82,77,69),width=1)
    corner(d,(43,y+19,49,y+52),3,c)
    d.text((65,y+16),str(p.get('name','Untitled')),font=font(23,'bold'),fill=WHITE)
    d.text((65,y+53),str(p.get('phase','In progress')),font=font(16),fill=SUB)
    nxt=str(p.get('next','Update next step'))
    next_f=font(15)
    lines=wrap_to_width(d,'Next: '+nxt,580,next_f,2)
    for j,line in enumerate(lines):d.text((65,y+94+j*20),line,font=next_f,fill=(215,229,242))
    x=711; bar_w=272;bar_y=y+29;bar_h=17
    corner(d,(x,bar_y,x+bar_w,bar_y+bar_h),8,TRACK)
    target=bar_w*(done/total)
    fill=max(0,round(target*amount))
    if fill:corner(d,(x,bar_y,x+fill,bar_y+bar_h),min(8,fill//2),c)
    d.text((1008,y+26),f'{done}/{len(ms)}',font=font(18,'bold'),fill=WHITE)
    d.text((711,y+67),'Milestones checked',font=font(15),fill=MUTED)
    # progress as milestone marks rather than % skill estimate
    for j in range(len(ms)):
        cx=x+j*17;cy=y+101
        d.ellipse((cx,cy,cx+7,cy+7),fill=c if ms[j].get('done') else (60,81,101))

def make_dashboard():
    w=1120; h=104+len(PROJECTS)*155+65
    static=bg(w,h);d=ImageDraw.Draw(static)
    corner(d,(0,0,w-1,h-1),21,None,outline=(43,81,106),width=2)
    d.ellipse((38,33,51,46), fill=CYAN)
    d.text((64,24),'PROJECT MILESTONES',font=font(28,'bold'),fill=WHITE)
    d.text((64,65),'Current stage  /  Editable milestone checklist  /  Next step',font=font(16),fill=SUB)
    d.text((34,h-37),'Manual milestone tracking  •  Not GitHub commit volume or a skill score',font=font(14),fill=MUTED)
    imgs=[]
    for k in range(38):
        im=static.copy();q=ImageDraw.Draw(im)
        for i,p in enumerate(PROJECTS):
            t=(k-i*2)/17
            t=max(0,min(1,t))
            amt=t*t*(3-2*t)
            draw_card(q,p,i,amt)
        imgs.append(im)
    imgs[-1].save(ASSETS/'project-dashboard-still.png',optimize=True)
    export_gif(imgs,'project-dashboard-grow.gif',[110]*25+[180]*12+[850])
    # Native SVG alternative: animates bar width 0 -> done fraction using SMIL
    esc=lambda val:html.escape(str(val),quote=True)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Project progress tracker based on manually checked milestones">',
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071322"/><stop offset="1" stop-color="#10243a"/></linearGradient></defs>',
        f'<rect width="{w}" height="{h}" rx="22" fill="url(#bg)" stroke="#2b516a" stroke-width="2"/>',
        '<circle cx="43" cy="40" r="6" fill="#16d6e7"/><text x="64" y="51" font-size="27" font-weight="700" fill="#f2f7ff" font-family="DejaVu Sans,Arial,sans-serif">PROJECT MILESTONES</text>',
        '<text x="64" y="79" font-size="16" fill="#b4c9dd" font-family="Arial,sans-serif">Current stage / Checklist progress / Next step</text>']
    for i,p in enumerate(PROJECTS):
        y=104+i*155;ms=p['milestones'];done=sum(bool(m.get('done')) for m in ms); total=max(1,len(ms)); target=round(272*done/total)
        ac=p.get('accent','#16d6e7')
        svg += [f'<rect x="26" y="{y}" width="1068" height="140" rx="18" fill="#132b41" stroke="#284a5e"/>',
                f'<rect x="43" y="{y+19}" width="6" height="33" rx="3" fill="{ac}"/>',
                f'<text x="65" y="{y+41}" font-family="Arial,sans-serif" font-weight="700" font-size="23" fill="#f2f7ff">{esc(p["name"])}</text>',
                f'<text x="65" y="{y+71}" font-family="Arial,sans-serif" font-size="16" fill="#b4c9dd">{esc(p.get("phase",""))}</text>']
        # no overflow next line in SVG via rough split to max 76 chars
        chunks=[]; cur=''
        for word in ('Next: '+str(p.get('next',''))).split():
            cand=(' '.join((cur,word))).strip()
            if len(cand)>70 and cur:chunks.append(cur);cur=word
            else:cur=cand
        if cur:chunks.append(cur)
        for j,line in enumerate(chunks[:2]):
            svg.append(f'<text x="65" y="{y+105+j*18}" font-family="Arial,sans-serif" font-size="15" fill="#d7e5f2">{esc(line)}</text>')
        svg += [f'<rect x="711" y="{y+29}" width="272" height="17" rx="8" fill="#2d455b"/>',
                f'<rect x="711" y="{y+29}" width="0" height="17" rx="8" fill="{ac}"><animate attributeName="width" from="0" to="{target}" begin="{0.2+i*0.2}s" dur="1.65s" fill="freeze" calcMode="spline" keySplines="0.2 0 0.2 1"/></rect>',
                f'<text x="1009" y="{y+43}" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="#f2f7ff">{done}/{len(ms)}</text>',
                f'<text x="711" y="{y+83}" font-family="Arial,sans-serif" font-size="15" fill="#94aec4">Milestones checked</text>']
    svg.append(f'<text x="34" y="{h-26}" font-family="Arial,sans-serif" font-size="14" fill="#94aec4">Manual milestones / Not an automatic project completion or skill score</text>')
    svg.append('</svg>')
    (ASSETS/'project-dashboard.svg').write_text('\n'.join(svg),encoding='utf-8')

if __name__=='__main__':
    make_dashboard()
    print(f'Rendered animated header and {len(PROJECTS)} project rows')
