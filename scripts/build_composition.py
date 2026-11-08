"""Generate index.html (1080x1920) for the CapCut Omni Reference tutorial.
Run after scripts/prep_media.py:  /usr/local/bin/python3.13 scripts/build_composition.py
"""
import json, os
from string import Template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
timing = json.load(open("assets/cut/timing.json"))
vo = {int(k): v for k, v in timing["vo"].items()}
dur = {int(k): v for k, v in timing["scenes"].items()}
# scenes: 1-9 tutorial, 10 recap, 11 BF stickers, 12 BF deal, 13 CTA, 14 logo
VO_FOR = {n: n for n in range(1, 12)}
VO_FOR[12] = 13   # Black Friday deal line (optional until supplied)
VO_FOR[13] = 12   # "Comment 'CapCut'..."
dur[13] = round(vo[12] + 0.6, 2)
dur[14] = 3.6
LAST = 14

starts, t = {}, 0.0
for n in range(1, LAST + 1):
    starts[n] = round(t, 2)
    t += dur[n]
TOTAL = round(t, 2)
cd = {n: round((starts[n + 1] if n < LAST else TOTAL) - starts[n] - 0.01, 3) for n in range(1, LAST + 1)}
vo_start = {n: round(starts[n] + (0.3 if n == 1 else 0.15), 2) for n in range(1, 14)}

STEP = {1: ("01", "SETUP"), 2: ("01", "SETUP"), 3: ("02", "ASSETS"), 4: ("03", "PROMPT"),
        5: ("04", "SETTINGS"), 6: ("05", "GENERATE"), 7: ("05", "RESULT"), 8: ("06", "REFINE"),
        9: ("06", "REFINE"), 10: ("OK", "RECAP"), 11: ("BF", "BLACK FRIDAY"), 12: ("BF", "BLACK FRIDAY")}
HEAD = {1: ("OPEN", "CAPCUT"), 2: ("OMNI", "REFERENCE"), 3: ("DROP IN", "YOUR ASSETS"),
        4: ("WRITE", "THE PROMPT"), 5: ("DIAL IN", "SETTINGS"), 6: ("HIT", "GENERATE"),
        7: ("ONE PROMPT.", "ONE AD."), 8: ("FIX ANY", "SECTION"), 9: ("BEFORE", "AFTER"),
        10: ("THAT'S", "IT."), 11: ("BLACK FRIDAY", "STICKERS"), 12: ("BLACK FRIDAY", "SALE")}
# bottom key phrases: (scene-local time, html)
PHRASES = {
    1: [(0.7, 'Click <b>Create Project</b>')],
    2: [(0.8, 'Media &rsaquo; Generate &rsaquo; <b>AI Video</b>'), (4.5, 'Open the <b>Omni Reference</b> tab')],
    3: [(1.0, 'Product &middot; Model &middot; Outfit &middot; <b>Audio</b>'), (4.6, 'Up to <b>30</b> images &middot; <b>10</b> videos &middot; <b>10</b> audio')],
    4: [(0.8, 'Describe the <b>product</b>, <b>mood</b> &amp; <b>style</b>')],
    5: [(0.6, '<b>Dreamina Seedance 2.5</b>'), (3.4, 'Duration &middot; Resolution &middot; <b>Ratio</b>')],
    6: [(0.4, 'Hit <b>Generate</b>'), (2.6, 'Hover &rarr; click <b>+</b> to add it')],
    7: [(0.7, 'One prompt. A <b>30-second</b> ad.')],
    8: [(0.6, 'Use the clip as a <b>reference</b>'), (4.0, 'Add a <b>short prompt</b>')],
    9: [(0.5, 'A <b>5-second</b> fix')],
    10: [(4.8, 'A <b>30-second</b> ad. Done.')],
    11: [(0.8, 'Stickers &middot; Effects &middot; <b>Text Templates</b>'), (4.3, 'Drag. Drop. <b>Sale-ready.</b>')],
    12: [(0.6, 'CapCut PC <b>Black Friday Sale</b>'), (4.6, 'Get started for <b>$3.99</b> or less')],
}
VIDEO_N = list(range(1, 13))


def scene_overlay(n):
    num, label = STEP[n]
    l1, l2 = HEAD[n]
    pill = (f'<div class="pill" id="s{n}-pill"><span class="dot"></span>'
            f'{"STEP " + num if num not in ("BF", "OK") else ("BONUS" if num == "BF" else "DONE")} &middot; {label}</div>')
    head = (f'<div class="head" id="s{n}-head"><div class="hl"><span class="w" id="s{n}-l1">{l1}</span></div>'
            f'<div class="hl"><span class="w c" id="s{n}-l2">{l2}</span></div></div>')
    phr = "".join(f'<div class="phrase" id="s{n}-p{k}">{h}</div>' for k, (_, h) in enumerate(PHRASES.get(n, [])))
    extra = EXTRA.get(n, "")
    return (f'<div id="sc{n}" class="clip scene" data-start="{starts[n]}" data-duration="{cd[n]}" '
            f'data-track-index="2">{pill}{head}<div class="band">{phr}</div>{extra}</div>')


EXTRA = {
    2: '<div class="crumbs">' + "".join(
        f'<div class="crumb" id="s2-c{i}">{t}</div>' for i, t in enumerate(["Media", "Generate", "AI Video", "Omni Reference"])) + '</div>',
    3: '<div class="assets" id="s3-assets" data-layout-allow-overflow>' + "".join(
        f'<div class="acard" id="s3-a{i}"><img src="assets/img/asset-{k}.jpg" alt=""><span>{lab}</span></div>'
        for i, (k, lab) in enumerate([("product", "PRODUCT"), ("model", "MODEL"), ("outfit", "OUTFIT"), ("scene", "SCENE")]))
       + '<div class="acard audio" id="s3-a4"><div class="wave">' + "".join(f'<i style="height:{h}px"></i>' for h in [30, 62, 44, 88, 56, 96, 40, 70, 34, 58]) + '</div><span>AUDIO</span></div></div>'
       + '<div class="limits" id="s3-lim"><div><b>30</b>images</div><div><b>10</b>videos</div><div><b>10</b>audio</div></div>',
    5: '<div class="model" id="s5-model">SEEDANCE 2.5</div><div class="specs">'
       + "".join(f'<div class="spec" id="s5-k{i}"><small>{a}</small><b>{b}</b></div>'
                 for i, (a, b) in enumerate([("DURATION", "30s"), ("RESOLUTION", "720p"), ("RATIO", "4:3")])) + '</div>',
    6: '<div class="credits" id="s6-cred"><small>CREDITS</small><b id="s6-num">630</b></div>'
       '<div class="loader" id="s6-load"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="50" /></svg><span>GENERATING</span></div>',
    7: '<div class="chips" id="s7-chips"><span>30s</span><span>720p</span><span>SEEDANCE 2.5</span></div>',
    8: '<div class="glass revise" id="s8-rev"><div class="glab">NEW PROMPT</div>'
       '<div class="tw big" id="s8-t0">add more petal flowers around</div>'
       '<div class="tags"><span id="s8-g0">5s</span><span id="s8-g1">4:3</span><span id="s8-g2">REFERENCE: CLIP</span></div></div>',
    9: '<div class="ba-tag before" id="s9-b">BEFORE</div><div class="ba-tag after" id="s9-a">AFTER</div>',
    10: '<div class="checks">' + "".join(
        f'<div class="chk" id="s10-k{i}"><i>&#10003;</i>{t}</div>' for i, t in enumerate(["Assets", "Omni Ref", "Settings", "Generate"])) + '</div>',
    11: '<div class="newb" id="s11-new">NEW</div><div class="specs bf">'
        + "".join(f'<div class="spec" id="s11-k{i}"><b>{t}</b></div>' for i, t in enumerate(["Stickers", "Effects", "Text Templates"])) + '</div>',
    12: '<div class="price" id="s12-price"><div class="amt" id="s12-amt">$3.99</div><div class="or" id="s12-or">or less &middot; CapCut PC</div>'
        '<div class="fine" id="s12-fine">CapCut PC only. Eligible new, expiring &amp; lapsed users. Prices vary by region.</div></div>',
}


def scene13():
    return (f'<div id="sc13" class="clip scene" data-start="{starts[13]}" data-duration="{cd[13]}" data-track-index="2">'
            '<div class="cta-head"><div class="hl"><span class="w" id="s13-l1">COMMENT</span></div>'
            '<div class="hl"><span class="w laser" id="s13-l2">&lsquo;CAPCUT&rsquo;</span></div></div>'
            '<div class="bubble" id="s13-bub"><div class="av"></div><div class="btxt"><small>Add a comment&hellip;</small>'
            '<div class="typed"><span class="tw" id="s13-type">CapCut</span><i class="caret" id="s13-caret"></i></div></div>'
            '<div class="send" id="s13-send"><svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2z"/></svg></div></div>'
            '<div class="cta-sub" id="s13-sub">and I&rsquo;ll send you the link</div>'
            '<div class="plane" id="s13-plane"><svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2z"/></svg></div></div>')


def scene14():
    # slices placed with the original logo geometry, scaled 0.78 and centred
    k, ox, oy = 0.78, (1080 - (1162 - 122) * 0.78) / 2, 820
    def pos(x, y, w, h):
        return f"left:{ox + (x - 122) * k:.0f}px;top:{oy + (y - 122) * k:.0f}px;width:{w * k:.0f}px;height:{h * k:.0f}px"
    return (f'<div id="sc14" class="clip scene" data-start="{starts[14]}" data-duration="{cd[14]}" data-track-index="2">'
            '<div class="burst" id="s14-burst"></div>'
            f'<div class="logo" id="s14-logo">'
            f'<img class="lg" id="s14-glow" src="assets/img/logo-glyph-glow.png" style="{pos(122,145,274,220)}" alt="">'
            f'<img class="lg" id="s14-glyph" src="assets/img/logo-glyph.png" style="{pos(122,145,274,220)}" alt="">'
            f'<img class="lg" id="s14-word" src="assets/img/logo-wordmark.png" style="{pos(440,122,530,142)}" alt="">'
            f'<div class="lg badge" id="s14-badge" style="{pos(975,130,183,108)}"><img src="assets/img/logo-badge.png" alt=""><i class="shine" id="s14-shine"></i></div>'
            f'<img class="lg" id="s14-tag" src="assets/img/logo-tagline.png" style="{pos(440,272,722,116)}" alt="">'
            '</div></div>')


videos = []
for n in VIDEO_N:
    if n == 9:
        continue
    videos.append(f'<video id="v{n:02d}" data-start="{starts[n]}" data-duration="{cd[n]}" data-track-index="1" '
                  f'src="assets/cut/s{n:02d}.mp4" muted playsinline></video>')
after = (f'<div id="afterwrap"><video id="v09" data-start="{starts[9]}" data-duration="{cd[9]}" data-track-index="1" '
         f'src="assets/cut/s09.mp4" muted playsinline></video></div>')
audios = "".join(f'<audio id="a{VO_FOR[n]:02d}" data-start="{vo_start[n]}" data-duration="{vo[VO_FOR[n]]}" data-track-index="10" '
                 f'src="assets/vo/vo{VO_FOR[n]:02d}.mp3" data-volume="1"></audio>' for n in range(1, 14) if VO_FOR[n] in vo)
nums = "".join(f'<div class="bignum" id="num-{x}">{x}</div>' for x in ["01", "02", "03", "04", "05", "06", "OK", "BF"])

html = Template(open("scripts/template.html").read()).substitute(
    TOTAL=TOTAL, NUMS=nums, VIDEOS="".join(videos), AFTER=after,
    SCENES="".join(scene_overlay(n) for n in range(1, 13)) + scene13() + scene14(),
    AUDIOS=audios, HUD_DUR=starts[13], STARTS=json.dumps([0] + [starts[n] for n in range(1, LAST + 1)]),
    DURS=json.dumps([0] + [dur[n] for n in range(1, LAST + 1)]),
    PHRASES=json.dumps({n: [p[0] for p in v] for n, v in PHRASES.items()}),
)
open("index.html", "w").write(html)
print("index.html written, total", TOTAL, "starts", starts)
