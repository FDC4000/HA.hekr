"""Generate the Hekr/Wisen platform brand icon for Home Assistant.

Motif: a central smart-home hub (house glyph) with connected device nodes —
representing the Hekr/Wisen IoT platform (many device types via one hub), not a
single appliance.

Outputs (home-assistant/brands requirements): transparent PNG, square, trimmed.
  icon.png     256x256
  icon@2x.png  512x512

Run:  python generate_icon.py
Requires: Pillow
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw

S = 4  # supersampling factor
N = 256 * S


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def c(v):  # logical (0..256) -> supersampled px
    return v * S


HUB_TOP = (59, 130, 246, 255)   # #3B82F6
HUB_BOT = (29, 78, 216, 255)    # #1D4ED8
NODE_BLUE = (79, 142, 247, 255)  # #4F8EF7
NODE_GREEN = (34, 197, 94, 255)  # #22C55E (one "active" node)
NODE_RING = (30, 58, 138, 255)   # #1E3A8A
LINE = (96, 165, 250, 200)       # #60A5FA, slightly translucent


def draw_icon() -> Image.Image:
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    center = (c(128), c(128))
    nodes = [
        ((c(58), c(58)), NODE_BLUE),
        ((c(198), c(58)), NODE_GREEN),
        ((c(58), c(198)), NODE_BLUE),
        ((c(198), c(198)), NODE_BLUE),
    ]

    # connection lines (under hub and nodes)
    for (pos, _col) in nodes:
        d.line([center, pos], fill=LINE, width=c(6))

    # hub: vertical-gradient rounded square
    hw, hh, rad = c(92), c(92), c(24)
    grad = Image.new("RGBA", (hw, hh))
    gd = ImageDraw.Draw(grad)
    for y in range(hh):
        gd.line([(0, y), (hw, y)], fill=lerp(HUB_TOP, HUB_BOT, y / (hh - 1)))
    mask = Image.new("L", (hw, hh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, hw - 1, hh - 1], radius=rad, fill=255)
    hub_xy = (c(128) - hw // 2, c(128) - hh // 2)
    img.paste(grad, hub_xy, mask)

    # device nodes (on top of lines)
    for (pos, col) in nodes:
        r = c(17)
        box = [pos[0] - r, pos[1] - r, pos[0] + r, pos[1] + r]
        d.ellipse(box, fill=col, outline=NODE_RING, width=c(2))

    # white house glyph inside the hub (smart-home hub)
    white = (255, 255, 255, 255)
    # roof
    d.polygon([(c(110), c(128)), (c(128), c(110)), (c(146), c(128))], fill=white)
    # body
    d.rounded_rectangle([c(115), c(128), c(141), c(148)], radius=c(3), fill=white)
    # door (punch-out using hub gradient color approx)
    d.rounded_rectangle([c(124), c(136), c(132), c(148)], radius=c(2), fill=HUB_BOT)

    return img


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    master = draw_icon()
    for size, name in ((256, "icon.png"), (512, "icon@2x.png")):
        master.resize((size, size), Image.LANCZOS).save(os.path.join(here, name))
        print(f"wrote {name} ({size}x{size})")


if __name__ == "__main__":
    main()
