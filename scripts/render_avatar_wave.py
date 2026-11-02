#!/usr/bin/env python3
"""Make a subtle hand-wave GIF from assets/about-avatar-transparent.png.

The source PNG stays visually unchanged: the upper-left hand area is locally
rotated around the wrist, with motion feathered to zero around the sleeve.
Requires Pillow, numpy and opencv-python. Animation regenerated as a GIF.
"""
from pathlib import Path
from PIL import Image
import numpy as np
import cv2
import math

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/about-avatar-transparent.png"
DEST = ROOT / "assets/about-avatar-wave.gif"

original = Image.open(SOURCE).convert("RGBA").resize((562,701), Image.Resampling.LANCZOS)
rgba = np.asarray(original, dtype=np.uint8)
h, w = rgba.shape[:2]
x, y = np.meshgrid(np.arange(w,dtype=np.float32),np.arange(h,dtype=np.float32))

def smoothstep(t):
    t = np.clip(t, 0, 1)
    return t*t*(3-2*t)

# Isolate movement to the waving hand, not the face or the laptop.
weight_x = smoothstep((x-18)/20)*(1-smoothstep((x-151)/36))
weight_y = smoothstep((y-216)/35)*(1-smoothstep((y-346)/75))
weight = weight_x*weight_y
wrist_x, wrist_y = 93, 407
frames = []
for index in range(32):
    angle = math.radians(10.8*math.sin(2*math.pi*index/32))*weight
    ca, sa = np.cos(angle), np.sin(angle)
    src_x = wrist_x+ca*(x-wrist_x)+sa*(y-wrist_y)
    src_y = wrist_y-sa*(x-wrist_x)+ca*(y-wrist_y)
    mapped = cv2.remap(
        rgba, src_x.astype(np.float32), src_y.astype(np.float32),
        cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,0,0,0),
    )
    frames.append(Image.fromarray(mapped, 'RGBA'))

# Fixed palette prevents frame-to-frame color flickering. Transparent GIF index.
matte=(13,26,43)
base=Image.new('RGB',(w,h),matte)
base.paste(frames[0],mask=frames[0].getchannel('A'))
master=base.quantize(colors=224,method=Image.Quantize.MEDIANCUT)
palette=master.getpalette()[:768]
palette += [0]*max(0,768-len(palette))
processed=[]
for frame in frames:
    comp=Image.new('RGB',(w,h),matte)
    comp.paste(frame,mask=frame.getchannel('A'))
    data=np.array(comp.quantize(palette=master,dither=Image.Dither.NONE),dtype=np.uint8)
    data[np.asarray(frame.getchannel('A'))<96]=255
    img=Image.fromarray(data,'P')
    img.putpalette(palette)
    processed.append(img)
processed[0].save(DEST,save_all=True,append_images=processed[1:],
                  loop=0,duration=95,transparency=255,disposal=2,optimize=True)
print(f"Rendered {len(processed)} frames: {DEST}")
