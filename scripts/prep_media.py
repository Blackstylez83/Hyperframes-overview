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
    if not os.path.exists(f"assets/vo/fast12/vo{i:02d}.mp3"):
        return None
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", f"assets/vo/fast12/vo{i:02d}.mp3"])
    return float(out)

# scene -> list of (src, in, out, speed). Scene length = VO + 0.6 (S1 gets +0.15 lead).
SCENES = {
    1: [(T, 0.0, 2.3, 0.75)],
    2: [(T, 2.0, 5.6, 0.6)],
    3: [(T, 5.6, 8.9, 0.55)],
    4: [(T, 8.9, 12.7, 0.7)],
    5: [(T, 12.7, 16.8, 0.55)],
    6: [(T, 16.8, 22.8, 1.4)],
    7: [(T, 32.3, 35.2, 0.6)],   # result playing in the preview (moving)
    8: [(T, 25.0, 29.0, 0.55)],
    9: [(T, 33.6, 36.6, 0.72)],
    10: [(T, 6.0, 7.2, 1.0), (T, 3.9, 5.1, 1.0), (T, 13.4, 15.2, 1.5), (T, 16.9, 18.7, 1.5), (T, 34.0, 36.6, 0.9)],  # recap montage
    11: [(BF, 6.4, 8.4, 1.33), (BF, 26.4, 29.4, 1.2), (BF, 32.4, 35.6, 1.2), (BF, 46.2, 48.0, 1.0)],
    12: [(DEAL, 0.0, 6.4, 1.0)],
}
# scene -> VO file number (vo13 = Black Friday deal line, may not exist yet)
VO_FOR = {n: n for n in range(1, 12)}
VO_FOR[12] = 13

def scene_len(n):
    d = vo_dur(VO_FOR[n]) or 6.4  # placeholder until vo13 is supplied
    base = d + 0.6 + (0.15 if n == 1 else 0)
    # Black Friday footage plays uncut at gentle speed: scene is at least as long as its footage
    foot = sum((b - a) / sp for _, a, b, sp in SCENES[n]) + 0.1
    return round(max(base, foot) if n in (11, 12) else base, 2)

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
    cut(n, pieces, lens[n])
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

json.dump({"scenes": lens, "vo": {i: round(vo_dur(i), 3) for i in range(1, 14) if vo_dur(i)}},
          open("assets/cut/timing.json", "w"), indent=1)
print("done")
