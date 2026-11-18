# 17 November 2026 world news in one image

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/c/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Rudhay862/news-image-20261117/rank.svg)](https://make.fun/c/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Rudhay862/news-image-20261117/reward.svg)](https://make.fun/c/news-image-20261117)

Entry for the [news-image-20261117](https://make.fun/c/news-image-20261117)
bounty on [make.fun](https://make.fun): a program that writes one image
summing up Tuesday 17 November 2026 world news to `/output/entry.png`.

The front page leads with Ukraine's strike on the Kerch Bridge, plus Trump
in Manila for the ASEAN summit, Iran's drone attack on a US radar base in
Bahrain and tankers hit by mines in the Strait of Hormuz, JPMorgan's
software-bug banking outage, Nvidia's first earnings since Jensen Huang's
exit, Japan scrambling jets over a Russian airspace violation, and five EU
states planning a Rwanda returns hub. Every headline was checked against
news reported on 17 November 2026 (BBC, AP, Reuters, CNN, Al Jazeera).

## How it works

- `draw_image.py` draws the front page with Pillow (deterministic, no
  network) and writes `entry.png` (1024x1024 PNG).
- `main.py` copies `entry.png` to `/output/entry.png` and verifies the copy
  with SHA-256. Standard library only, no network.

Run it:

```sh
python3 draw_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

Built with [make.fun](https://make.fun/r/dzgseakx) — try a bounty yourself
with my referral link: https://make.fun/r/dzgseakx

## License

MIT — see [LICENSE](LICENSE).
