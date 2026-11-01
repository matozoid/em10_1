#!/usr/bin/env python3
"""Contact sheets (PNG) of decoded block-1 font glyphs and carved block-2 JPEGs.
usage: sheet.py fonts <font_entry.bin> out.png | sheet.py jpegs <dir> out.png
Output is vendor content: keep local (gitignored)."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import glyphs

def fonts(path, out, cols=16, scale=2):
    g = glyphs.glyphs(open(path, 'rb').read())
    cw = max(x[1] for x in g) + 4; ch = 32 + 4
    rows = (len(g) + cols - 1) // cols
    im = Image.new('L', (cols * cw * scale, rows * ch * scale), 40)
    for i, (_, w, h, px) in enumerate(g):
        gl = Image.new('L', (w, h)); gl.putdata([[0, 85, 170, 255][v] for r in px for v in r])
        gl = gl.resize((w * scale, h * scale), Image.NEAREST)
        im.paste(gl, ((i % cols) * cw * scale + 2, (i // cols) * ch * scale + 2))
    im.save(out); print(len(g), 'glyphs ->', out, im.size)

def jpegs(d, out, cell=240, cols=8):
    fs = sorted(glob.glob(d + '/**/*.jpg', recursive=True))
    rows = (len(fs) + cols - 1) // cols
    im = Image.new('RGB', (cols * cell, rows * cell), (60, 60, 120))
    for i, f in enumerate(fs):
        t = Image.open(f).convert('RGB'); t.thumbnail((cell - 8, cell - 8))
        im.paste(t, ((i % cols) * cell + 4, (i // cols) * cell + 4))
    im.save(out); print(len(fs), 'jpegs ->', out, im.size)

if __name__ == '__main__':
    {'fonts': fonts, 'jpegs': jpegs}[sys.argv[1]](sys.argv[2], sys.argv[3])
