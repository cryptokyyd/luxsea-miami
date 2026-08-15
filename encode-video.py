"""Cut and compress a source clip into a web hero loop, plus its poster.

Autoplay video is the heaviest thing on a page, so the rules here are strict:
no audio track at all, faststart so playback begins before the file is done
downloading, and a bitrate ceiling rather than trusting CRF alone.

The sources are drone clips that arrive over WhatsApp already re-encoded and
already rotated by metadata, so we bake the rotation in and never upscale --
enlarging a 576px source only makes a bigger file, not a sharper one.

    python encode-video.py <source.mp4> <out-name> <start> <duration>
"""
import json
import pathlib
import subprocess
import sys

MEDIA = pathlib.Path(__file__).parent / "assets" / "media"
MAX_KBPS = 1100          # ceiling; the pull-back shots sit well under it
CRF = 27                 # visually clean at this size, roughly half the source


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_streams",
         "-of", "json", str(path)], capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)["streams"][0]
    rot = 0
    for side in s.get("side_data_list", []):
        rot = abs(int(side.get("rotation", 0))) or rot
    w, h = int(s["width"]), int(s["height"])
    return (h, w) if rot in (90, 270) else (w, h)   # what a browser shows


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def encode(src, name, start, dur):
    w, h = probe(src)
    mp4 = MEDIA / f"{name}.mp4"
    jpg = MEDIA / f"{name}-poster.jpg"

    run(["ffmpeg", "-v", "error", "-ss", str(start), "-t", str(dur), "-i", str(src),
         "-an",                                   # autoplay is muted; the track is dead weight
         "-c:v", "libx264", "-profile:v", "high", "-preset", "slow",
         "-crf", str(CRF), "-maxrate", f"{MAX_KBPS}k", "-bufsize", f"{MAX_KBPS * 2}k",
         "-pix_fmt", "yuv420p",                   # Safari will not decode yuv444
         "-movflags", "+faststart",
         "-metadata:s:v", "rotate=0",             # rotation is baked in by the filter chain
         str(mp4), "-y"])

    # Poster: the first frame, so there is no jump when playback starts.
    run(["ffmpeg", "-v", "error", "-ss", str(start), "-i", str(src),
         "-frames:v", "1", "-q:v", "4", str(jpg), "-y"])

    kb = mp4.stat().st_size / 1024
    print(f"{mp4.name}: {w}x{h}  {dur}s  {kb:.0f} KB  ({kb * 8 / dur:.0f} kbps)")
    print(f"{jpg.name}: {jpg.stat().st_size / 1024:.0f} KB")
    return mp4


if __name__ == "__main__":
    src, name, start, dur = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    encode(pathlib.Path(src), name, start, dur)
