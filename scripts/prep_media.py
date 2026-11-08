"""Cut, retime and pad footage per scene; slice logo and asset thumbnails.
Run: /usr/local/bin/python3.13 scripts/prep_media.py
"""
import json, subprocess, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
T = "assets/footage/tutorial-source.mp4"
BF = "assets/footage/black-friday-stickers.mp4"
DEAL = "assets/footage/black-friday-deal-page.mp4"
W, H = 2010, 1080

def vo_dur(i):
    if not os.path.exists(f"assets/vo/vo{i:02d}.mp3"):
        return None
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", f"assets/vo/vo{i:02d}.mp3"])
    return float(out)

# scene -> list of (src, in, out, speed). Scene length = VO + 0.6 (S1 gets +0.15 lead).
# Short cut (~45s): VO trimmed + sped up 1.3x (assets/vo/fast). Scenes:
# 1 create, 2 omni ref, 3 assets, 4 prompt, 5 settings, 6 generate, 7 BF stickers, 8 BF deal
# pieces = (src, in, out, speed tuned for the original long-cut scene length OLD[n])
SCENES = {
    1: [(T, 0.0, 2.3, 0.75)],
    2: [(T, 2.0, 5.6, 0.6)],
    3: [(T, 5.6, 8.9, 0.55)],
    4: [(T, 8.9, 12.7, 0.7)],
    5: [(T, 12.7, 16.8, 0.55)],
    6: [(T, 16.8, 22.8, 1.4)],
    7: [(BF, 6.4, 9.4, 2.0), (BF, 26.4, 29.4, 1.5), (BF, 32.4, 35.6, 1.6), (BF, 46.2, 48.0, 1.0)],
    8: [(DEAL, 0.0, 6.4, 0.8)],
}
OLD = {1: 3.91, 2: 7.84, 3: 7.84, 4: 6.71, 5: 9.27, 6: 5.35, 7: 8.65, 8: 8.65}
VO_FOR = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 11, 8: 13}
GAP = 0.3

def fast_dur(i):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", f"assets/vo/fast/vo{i:02d}.mp3"])
    return float(out)

def scene_len(n):
    return round(fast_dur(VO_FOR[n]) + GAP + (0.1 if n == 1 else 0), 2)

def fit_filter(src):
    if src == DEAL:  # white page: scale to width, pad to 2010x1080 with white
        return f"scale={W}:-2,pad={W}:{H}:0:(oh-ih)/2:white"
    return f"scale={W}:{H}"

def cut(n, pieces, total):
    parts, inputs = [], []
    for k, (src, a, b, sp) in enumerate(pieces):
        inputs += ["-ss", str(a), "-t", str(b - a), "-i", src]
        parts.append(f"[{k}:v]{fit_filter(src)},setpts=(PTS-STARTPTS)/{sp},fps=30,setsar=1[p{k}]")
    cat = "".join(f"[p{k}]" for k in range(len(pieces)))
    fg = ";".join(parts) + f";{cat}concat=n={len(pieces)}:v=1:a=0,tpad=stop_mode=clone:stop_duration=30[v]"
    out = f"assets/cut/s{n:02d}.mp4"
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fg, "-map", "[v]",
                           "-t", str(total), "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-g", "30", "-keyint_min", "30",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", out])
    return out

lens = {}
for n, pieces in SCENES.items():
    lens[n] = scene_len(n)
    k = lens[n] / OLD[n]
    cut(n, [(src, a, b, sp / k) for (src, a, b, sp) in pieces], lens[n])
    print("cut", n, lens[n])

# S9 "before" = freeze frame of the pre-revision clip (tutorial 0:27.2)
subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-ss", "27.2", "-i", T, "-frames:v", "1",
                       "-vf", f"scale={W}:{H}", "assets/img/before.jpg"])

# asset thumbnails from file picker frame (tutorial 0:06.8)
subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-ss", "6.8", "-i", T, "-frames:v", "1", "/tmp/_pick.png"])
pick = Image.open("/tmp/_pick.png").convert("RGB")
crops = {"product": (146, 451, 270, 673), "model": (146, 739, 270, 960), "outfit": (369, 164, 590, 385),
         "scene": (959, 164, 1083, 385), "hero": (1230, 164, 1354, 385)}
for name, box in crops.items():
    pick.crop(box).save(f"assets/img/asset-{name}.jpg", quality=92)

# logo slices
logo = Image.open("assets/brand/capcut-pc-marketing-logo.png")
for name, box in {"glyph": (122, 145, 396, 365), "wordmark": (440, 122, 970, 264),
                  "badge": (975, 130, 1158, 238), "tagline": (440, 272, 1162, 388)}.items():
    logo.crop(box).save(f"assets/img/logo-{name}.png")

json.dump({"scenes": lens, "old": OLD, "vo_for": VO_FOR, "vo": {i: round(fast_dur(i), 3) for i in set(VO_FOR.values()) | {12}}},
          open("assets/cut/timing.json", "w"), indent=1)
print("done")
