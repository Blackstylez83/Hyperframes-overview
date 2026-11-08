#!/usr/bin/env bash
# Render index.html -> PNG sequence -> MP4 composited on black with the VO mix.
# (png-sequence output is RGBA, so frames must be flattened onto black.)
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=${1:-renders/capcut-omni-reference-9x16.mp4}
rm -rf renders/frames
npx --yes hyperframes@0.5.5 render --format png-sequence -o renders/frames -q standard > renders/render.log 2>&1
/usr/local/bin/python3.13 - <<'PY'
import re, subprocess
html = open('index.html').read()
au = re.findall(r'<audio id="a(\d+)" data-start="([\d.]+)"[^>]*src="([^"]+)"', html)
total = float(re.search(r'data-composition-id="main" data-start="0" data-duration="([\d.]+)"', html).group(1))
inp, fl = [], []
for i, (_, st, src) in enumerate(au):
    inp += ['-i', src]; ms = int(round(float(st) * 1000))
    fl.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{i}]')
fg = ';'.join(fl) + ';' + ''.join(f'[a{i}]' for i in range(len(au))) + f'amix=inputs={len(au)}:normalize=0,apad,atrim=0:{total}[out]'
subprocess.check_call(['ffmpeg', '-v', 'error', '-y', *inp, '-filter_complex', fg, '-map', '[out]', '-c:a', 'aac', '-b:a', '192k', 'renders/vo-mix.m4a'])
PY
ffmpeg -v error -y -f lavfi -i color=c=black:s=1080x1920:r=30 -framerate 30 -start_number 1 -i renders/frames/frame_%06d.png \
  -i renders/vo-mix.m4a -filter_complex "[0:v][1:v]overlay=shortest=1:format=auto,format=yuv420p[v]" \
  -map "[v]" -map 2:a -c:v libx264 -preset slow -crf 18 -c:a copy -shortest -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
ls -lh "$OUT"
