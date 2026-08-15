#!/usr/bin/env python3
"""Optimise and install owner-supplied photos.

Drop originals into assets/incoming/<boat>/ and run this. Files are
auto-oriented, stripped of metadata, resized and re-encoded to sit inside the
existing weight budget (the library median is ~92 KB, the heaviest 247 KB),
then named into the sequence each boat's gallery already uses.

Phone photos carry GPS in EXIF. These are pictures of a boat at its home
marina, and the site deliberately does not publish where that is, so the
metadata is dropped rather than merely ignored.
"""
import hashlib
import pathlib
import sys

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).parent
MEDIA = ROOT / "assets" / "media"
INCOMING = ROOT / "assets" / "incoming"

PREFIX = {"chriscraft": "cc", "sundancer": "sd", "amberjack": "aj"}
LONG_EDGE = 1400          # galleries render ~620px wide; this covers 2x
TARGET_KB = 190           # ceiling, matching the heaviest file already shipped
MIN_QUALITY = 68


def digest(path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def phash(im, s=16):
    """Difference hash. A photo that has been round-tripped through WhatsApp is
    a different file byte-for-byte but the same photograph, and the site's rule
    is that no photograph appears on two pages — so identity has to be judged on
    the picture, not the bytes."""
    im = im.convert("L").resize((s + 1, s), Image.LANCZOS)
    px = im.load()
    bits = 0
    for y in range(s):
        for x in range(s):
            bits = bits << 1 | (px[x, y] < px[x + 1, y])
    return bits


def nearest(bits, table):
    """Closest known image and its Hamming distance out of 256 bits. Measured on
    this library the split is unambiguous: re-encodes land at 4-24, genuinely
    different photographs at 75 and above."""
    if not table:
        return None, 256
    name = min(table, key=lambda n: bin(bits ^ table[n]).count("1"))
    return name, bin(bits ^ table[name]).count("1")


NEAR_DUPLICATE = 40


def encode(im, dest, src):
    """Walk quality down until the file fits the budget, and keep the result
    only if it actually beats the original.

    These arrived through WhatsApp, which has already compressed them hard and
    stripped their metadata (verified: none of the 33 carried EXIF or GPS).
    Re-encoding a file that is already small and already at display size only
    adds weight and a second generation of artefacts, so the original bytes are
    copied through instead.
    """
    best = None
    for q in range(88, MIN_QUALITY - 1, -4):
        im.save(dest, "JPEG", quality=q, optimize=True, progressive=True,
                subsampling=2)
        best = q
        if dest.stat().st_size <= TARGET_KB * 1024:
            break

    if dest.stat().st_size >= src.stat().st_size:
        dest.write_bytes(src.read_bytes())
        return None
    return best


def next_index(prefix):
    used = [int(p.stem.split("-")[1]) for p in MEDIA.glob(f"{prefix}-*.jpg")
            if p.stem.split("-")[1].isdigit()]
    return max(used, default=0) + 1


def main():
    if not INCOMING.exists():
        sys.exit(f"no incoming folder at {INCOMING}")

    # The site's rule is that no photograph appears on two pages, so a file
    # that is byte-identical to one already in the library is not imported.
    known = {digest(p): p.name for p in MEDIA.iterdir() if p.suffix.lower() == ".jpg"}
    seen = {p.name: phash(Image.open(p)) for p in MEDIA.iterdir()
            if p.suffix.lower() == ".jpg"}
    added, skipped, before, after = [], [], 0, 0

    for folder, prefix in PREFIX.items():
        src_dir = INCOMING / folder
        if not src_dir.exists():
            continue
        idx = next_index(prefix)
        for src in sorted(src_dir.iterdir()):
            if src.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".heic"):
                continue
            d = digest(src)
            if d in known:
                skipped.append(f"{src.name} — identical to {known[d]}")
                continue

            try:
                im = Image.open(src)
            except Exception as e:                      # HEIC without a plugin
                skipped.append(f"{src.name} — cannot read ({e})")
                continue

            im = ImageOps.exif_transpose(im).convert("RGB")   # honour rotation

            match, dist = nearest(phash(im), seen)
            if dist <= NEAR_DUPLICATE:
                skipped.append(f"{src.name} — same photo as {match} (distance {dist})")
                continue

            im.thumbnail((LONG_EDGE, LONG_EDGE), Image.LANCZOS)

            dest = MEDIA / f"{prefix}-{idx:02d}.jpg"
            while dest.exists():
                idx += 1
                dest = MEDIA / f"{prefix}-{idx:02d}.jpg"

            q = encode(im, dest, src)
            known[digest(dest)] = dest.name
            seen[dest.name] = phash(Image.open(dest))
            before += src.stat().st_size
            after += dest.stat().st_size
            note = "as-is" if q is None else f"q{q}"
            added.append(f"{dest.name}  {im.size[0]:>4}x{im.size[1]:<4}  "
                         f"{src.stat().st_size / 1024:6.0f} KB -> "
                         f"{dest.stat().st_size / 1024:5.0f} KB  {note:>5}")
            idx += 1

    for line in added:
        print(line)
    for line in skipped:
        print("skipped:", line)
    if added:
        print(f"\n{len(added)} imported, {before / 1e6:.2f} MB -> {after / 1e6:.2f} MB "
              f"({100 - after / before * 100:.0f}% smaller)")
    else:
        print("nothing to import — drop files into assets/incoming/<boat>/ first")
    return added


if __name__ == "__main__":
    main()
