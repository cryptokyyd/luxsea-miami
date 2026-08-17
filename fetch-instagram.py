"""Pull the thumbnails for the posts listed in instagram-feed.json and square them.

Instagram has no free embed for a whole profile any more, and its CDN urls are
signed and expire within days, so hotlinking would leave a grid of broken images
on the site a week later. The images are downloaded, cropped square and served
from our own assets instead: no third-party script, no token, nothing to expire.

To refresh: re-scrape the profile, replace the posts array in the JSON, re-run.

    python fetch-instagram.py
"""
import concurrent.futures
import json
import pathlib
import urllib.request

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).parent
MEDIA = ROOT / "assets" / "media"
FEED = ROOT / "instagram-feed.json"
EDGE = 620          # tiles render ~300px at most; this covers 2x
TARGET_KB = 85      # nine of these load at once, so they stay small

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def grab(post):
    dest = MEDIA / post["file"]
    req = urllib.request.Request(post["src"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read()
    tmp = dest.with_suffix(".tmp")
    tmp.write_bytes(raw)

    im = ImageOps.exif_transpose(Image.open(tmp)).convert("RGB")
    before = im.size
    # A profile grid is square; the posts are a mix of 4:5, 9:16 and 1:1.
    # Centre-crop rather than letterbox so the tiles line up.
    im = ImageOps.fit(im, (EDGE, EDGE), Image.LANCZOS, centering=(0.5, 0.42))

    for q in range(86, 59, -4):
        im.save(dest, "JPEG", quality=q, optimize=True, progressive=True, subsampling=2)
        if dest.stat().st_size <= TARGET_KB * 1024:
            break
    tmp.unlink()
    return f"{post['file']}  {before[0]}x{before[1]} -> {EDGE}x{EDGE}  {dest.stat().st_size/1024:.0f} KB"


if __name__ == "__main__":
    feed = json.loads(FEED.read_text(encoding="utf-8"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for line in pool.map(grab, feed["posts"]):
            print("  " + line)
    total = sum((MEDIA / p["file"]).stat().st_size for p in feed["posts"])
    print(f"{len(feed['posts'])} tiles, {total/1024:.0f} KB total")
