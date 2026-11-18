#!/usr/bin/env python3
"""news-image-20261117 entry: copy the front-page image to /output/entry.png.

The image (entry.png beside this file) sums up Tuesday 17 November 2026
world news: Kerch Bridge strike, Trump in Manila, Iran drone/tanker
attacks, JPMorgan outage, Nvidia earnings, Japan scrambles jets, and the
EU Rwanda returns hub. Deterministic, standard library only, no network.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


os.makedirs(OUT_DIR, exist_ok=True)
# Clear the output dir's contents only; never remove /output itself
# (the grader user cannot recreate it).
for name in os.listdir(OUT_DIR):
    path = os.path.join(OUT_DIR, name)
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
shutil.copyfile(SRC, DST)
assert sha256(DST) == sha256(SRC), "copied image differs from source"
print("wrote", DST, sha256(DST))
