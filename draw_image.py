#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news front page (1024x1024).

Every headline below was verified against news reported on Tuesday
17 November 2026 (BBC, AP, Reuters, CNN, Al Jazeera, Just Security).
Run: python3 draw_image.py  ->  writes entry.png beside this file.
Deterministic: fixed layout, fixed fonts, no network, no timestamps.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
NAVY = (15, 42, 68)
RED = (178, 34, 34)
TEAL = (14, 92, 96)
GOLD = (197, 146, 44)
RULE = (120, 110, 95)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill, spacing=4):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def tag(draw, x, y, label, color):
    f = font(FB, 20)
    w = int(draw.textlength(label, font=f)) + 20
    draw.rounded_rectangle([x, y, x + w, y + 30], radius=4, fill=color)
    draw.text((x + 10, y + 4), label, font=f, fill=(255, 255, 255))
    return w


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((32, 16), "THE WORLD IN ONE DAY", font=font(FB, 30), fill=(255, 255, 255))
d.text((32, 56), "TUESDAY  17  NOVEMBER  2026",
       font=font(FB, 40), fill=(255, 214, 90))
d.text((W - 32, 22), "FRONT PAGE", font=font(FB, 24),
       fill=(255, 255, 255), anchor="ra")
d.rectangle([0, 118, W, 124], fill=RED)

# ---- lead story: Kerch Bridge ---------------------------------------------
ly = 140
tag(d, 32, ly, "LEAD  ·  UKRAINE", RED)
d.text((32, ly + 40), "Ukraine hits Kerch Bridge",
       font=font(FB, 48), fill=INK)
d.text((32, ly + 104), "Road span collapses after hit on the",
       font=font(FR, 30), fill=(60, 60, 60))
d.text((32, ly + 140), "link to occupied Crimea; Kyiv calls it",
       font=font(FR, 30), fill=(60, 60, 60))
d.text((32, ly + 176), "\u201can unprecedented operation\u201d.",
       font=font(FR, 30), fill=(60, 60, 60))
# simple bridge drawing, right of the lead text
bx, by = 714, ly + 60
d.line([(bx, by + 130), (bx + 260, by + 130)], fill=NAVY, width=8)
for tx in (bx + 30, bx + 200):
    d.line([(tx, by + 130), (tx, by + 20)], fill=NAVY, width=8)
    d.line([(tx, by + 20), (tx + 40, by + 130)], fill=NAVY, width=3)
    d.line([(tx, by + 20), (tx - 40, by + 130)], fill=NAVY, width=3)
d.line([(bx + 120, by + 130), (bx + 140, by + 130)], fill=RED, width=10)
for ang in range(0, 360, 45):
    import math
    x2 = bx + 130 + int(26 * math.cos(math.radians(ang)))
    y2 = by + 52 + int(26 * math.sin(math.radians(ang)))
    d.line([(bx + 130, by + 52), (x2, y2)], fill=GOLD, width=4)
d.ellipse([bx + 116, by + 38, bx + 144, by + 66], fill=RED)
d.text((bx, by + 150), "KERCH STRAIT", font=font(FB, 20), fill=(90, 90, 90))
d.line([(32, 396), (W - 32, 396)], fill=RULE, width=2)

# ---- story grid ------------------------------------------------------------
cards = [
    ("ASIA", NAVY, "Trump lands in Manila",
     "Opens ASEAN summit; Asia trip ends in China for talks with Xi and Putin."),
    ("MIDDLE EAST", RED, "Iran fires drones at US radar base",
     "Bahrain intercepts the attack; two tankers hit mines in the Strait of Hormuz."),
    ("MARKETS", TEAL, "JPMorgan blames software bug",
     "Monday outage hit online banking and Zelle; bank says no sign of a cyberattack."),
    ("TECH", TEAL, "Nvidia reports after the bell",
     "First earnings since Jensen Huang's exit as chief executive."),
    ("SECURITY", NAVY, "Japan scrambles jets",
     "Tokyo protests a Russian airspace violation; UK sanctions settlement builders."),
    ("MIGRATION", RED, "Five EU states plan Rwanda hub",
     "Germany, Denmark, Austria, Greece and the Netherlands back a joint returns facility."),
]
gx, gy = 32, 412
cw, ch, gap = 472, 166, 10
for i, (label, color, head, deck) in enumerate(cards):
    x = gx + (i % 2) * (cw + gap)
    y = gy + (i // 2) * (ch + gap)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=8,
                        outline=RULE, width=2, fill=(255, 255, 255))
    tag(d, x + 14, y + 12, label, color)
    y2 = draw_wrapped(d, x + 14, y + 52, head, font(FB, 28), cw - 28, INK)
    draw_wrapped(d, x + 14, y2 + 2, deck, font(FR, 19), cw - 28, (70, 70, 70))

# ---- ticker strip -----------------------------------------------------------
ty = 936
d.rectangle([0, ty, W, ty + 42], fill=NAVY)
d.text((32, ty + 9),
       "ALSO: ULA Vulcan rocket fails \u2014 40 Amazon satellites lost  \u00b7  "
       "Depardieu admits assault charge",
       font=font(FR, 21), fill=(255, 255, 255))
d.text((32, H - 24),
       "17 November 2026  \u00b7  Sources: BBC, AP, Reuters, CNN, Al Jazeera",
       font=font(FR, 19), fill=(110, 100, 85))

img.save("entry.png", "PNG", optimize=True)
print("wrote entry.png", img.size)
