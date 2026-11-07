# Motion Design — CapCut Omni Reference Tutorial (9:16)

**Canvas:** 1080×1920 · 30fps · ±75s (total VO 73.4s + napas antar scene)
**Brand lock:** cuma pakai palet CapCut — `#00CAE0` Bright Blue · `#000000` Black · `#FFFFFF` White · Bright Blue Gradient · Laser Gradient. Nggak ada warna lain di grafis (kuning cuma muncul kalau memang ada di footage CapCut asli).

---

## 1. Mapping VO → scene (berdasarkan 12 file)

| VO | Durasi | Scene | Isi |
|---|---|---|---|
| vo01 | 3.2s | S1 Create Project | Open CapCut → Create Project |
| vo02 | 7.2s | S2 Omni Reference | Media › Generate › AI Video › Omni Reference |
| vo03 | 7.2s | S3 Upload assets | Product, model, background, textures, audio |
| vo04 | 6.1s | S4 Prompt | Describe product, mood, style |
| vo05 | 8.7s | S5 Settings | Seedance 2.5 · duration · resolution · ratio |
| vo06 | 4.8s | S6 Generate | Hit Generate → hover → + to timeline |
| vo07 | 5.1s | S7 Result | "And here's the result…" |
| vo08 | 9.0s | S8 Fix a section | Clip as reference + short prompt |
| vo09 | 4.3s | S9 Before / After | Generate 5s, before… after |
| vo10 | 6.8s | S10 Black Friday stickers | Stickers, effects, text templates → "Shop Now" |
| vo11 | 8.0s | S11 Black Friday deal | CapCut PC sale, $3.99 or less |
| vo12 | 2.9s | S12 CTA → Logo | Comment "CapCut" → logo CapCut PC outro |

> Asumsi: recap (vo10 lama) di-drop. Kalau urutannya beda, tinggal tuker file.

---

## 2. Layout 9:16 — biar nggak kosong

```
┌──────────────────────────┐  0
│  STEP 02 ●●○○  (pill)    │  ← step tracker, Bright Blue
│                          │
│  OPEN OMNI               │  ← kinetic headline 2 baris, 120–140px
│  REFERENCE               │     keyword ke-2 di #00CAE0
├──────────────────────────┤  ~520
│ ╭──────────────────────╮ │
│ │                      │ │  ← "CAMERA CARD" 1000×980
│ │   screen recording   │ │     crop + zoom 1.8–2.6× ke area kerja,
│ │   (virtual camera)   │ │     pan ngikutin cursor
│ │                      │ │     3D tilt halus + shadow + border glow
│ ╰──────────────────────╯ │
│   ◯ mini-map (full UI)   │  ← thumbnail UI kecil + kotak posisi kamera
├──────────────────────────┤  ~1560
│  Go to Media, then       │  ← caption word-by-word, 60px bold
│  GENERATE …              │     kata kunci nyala Bright Blue
│  ▬▬▬▬▬▬▬▬▬▬░░░░░░░░░░░  │  ← progress bar gradient
└──────────────────────────┘  1920
```

**Background layer (selalu jalan):**
- CapCut Black + 2 blob Bright Blue Gradient blur besar yang drift pelan (opacity 25–35%).
- Dot grid tipis (#FFFFFF 6%) dengan parallax beda kecepatan dari card.
- **Angka step raksasa** outline ("01", "02"…) 900px di belakang card, stroke putih 4%, geser pelan ke atas tiap ganti step.
- Glyph logo CapCut sebagai pattern sangat samar di sudut, muter pelan.

Jadi tiap frame punya 4 lapis: background → angka besar → camera card → typography/caption. Nggak pernah ada area kosong.

---

## 3. Teknik zoom & panning tutorial (virtual camera)

Sumber 16:9 kalau ditaruh utuh di 9:16 cuma ±560px tinggi — teks UI kebaca kecil banget. Jadi tutorialnya pakai **pola Establish → Dive → Track**:

1. **Establish (0.6s):** card tampilin UI full (zoom 1×) dengan tilt 3D (rotateX 10°, rotateY −14°) biar penonton ngerti "ini CapCut".
2. **Dive (0.8s, `power3.inOut`):** card tegak lagi, kamera zoom 2–2.6× ke panel yang dibahas. Mini-map di bawah nunjukin kotak posisi.
3. **Track:** kamera ngikutin cursor dengan lag kecil (smooth follow), tiap klik ada ripple Bright Blue + spotlight (area lain dim 60%).
4. **Jump cut ke step berikut:** whip-pan blur 0.3s atau zoom-through.

Footage yang "nunggu" (loading, resize stiker) di-speed-ramp 3–4× biar ritme tetap rapat.

| Scene | Footage | Gerak kamera (koordinat sumber 2010×1080) |
|---|---|---|
| S1 | tutorial 0:00–0:02 | Establish full UI → dive ke tombol Create project (±1100,120), zoom 1.8× |
| S2 | tutorial 0:02–0:05 | Pan ke panel kiri (0–640, 0–460), zoom 2.4×, track Media → Generate → AI video → tab Omni reference |
| S3 | tutorial 0:06–0:08 | Zoom ke file picker lalu kotak referensi (150–620, 140–300) |
| S4 | tutorial 0:09–0:12 | Zoom 2.6× ke kotak prompt, pan vertikal pelan ngikutin teks yang ke-paste |
| S5 | tutorial 0:13–0:16 | Zoom ke panel settings (150–620, 330–790), track slider → resolusi → aspect ratio |
| S6 | tutorial 0:17–0:22 | Zoom ke tombol Generate (±580,680) → pan ke panel Generations kanan + tip "+" |
| S7 | tutorial 0:23–0:24 | Zoom ke player (660–1390, 80–630), lalu crop hasil full-bleed |
| S8 | tutorial 0:25–0:28 | Pan dari timeline (klip kepilih) naik ke kotak referensi + prompt |
| S9 | tutorial 0:27 & 0:33–0:36 | Crop player saja (before & after) |
| S10 | BF-stickers 0:06–0:12, 0:26–0:34, 0:43–0:52 | Zoom panel Stickers kiri → pan ke preview saat drag "SHOP NOW" |
| S11 | BF-deal-page 0:00–0:06 | Card browser, zoom ke headline + harga |

---

## 4. Elemen 3D & typography per scene

| Scene | 3D / grafis | Typography |
|---|---|---|
| S1 | Card masuk dari bawah dengan flip rotateX 60°→10°, shadow tebal | "OPEN / CAPCUT" slam per kata, lalu "Create Project" pill |
| S2 | Breadcrumb 4 chip 3D melayang di atas card, nyala satu-satu sinkron sama spotlight | "OMNI / REFERENCE" — "REFERENCE" mask-reveal dari bawah, Bright Blue |
| S3 | **5 kartu aset terbang keluar dari card dalam 3D** (z-depth beda, rotasi acak kecil), orbit pelan lalu nempel di carousel | Counter "30 IMAGES · 10 VIDEOS · 10 AUDIO" angka nge-roll |
| S4 | Prompt text bergulir di panel kaca (glassmorphism putih 8%) | Typewriter + kursor Bright Blue; "PROMPT" huruf raksasa di background |
| S5 | **3 spec card flip 3D** (Duration · Resolution · Ratio) — tiap card flip sinkron sama kata di VO; slider animasi | "SEEDANCE 2.5" stroke → fill |
| S6 | Tombol Generate pulse + ring loading Bright Blue Gradient | "GENERATE" scale-punch, lalu "+ ADD TO TIMELINE" |
| S7 | Hasil pecah keluar dari card → full-bleed 9:16 (blur bg dari frame yang sama), sedikit Ken Burns | "ONE PROMPT. / ONE AD." kinetic |
| S8 | Klip timeline terangkat 3D, panah kurva ke kotak referensi | Prompt revisi typewriter dalam chip |
| S9 | **Card 3D flip 180°**: depan BEFORE, belakang AFTER; atau split wipe diagonal | "BEFORE" putih → "AFTER" Bright Blue |
| S10 | Badge "NEW" Laser Gradient + shine sweep; grid stiker muncul stagger 3D (pop dengan overshoot) | "BLACK FRIDAY / STICKERS" + "Effects · Text Templates" |
| S11 | Kartu browser miring 3D; harga keluar dari halaman jadi angka raksasa | "$3.99" 260px Laser Gradient + "or less", fine print kecil |
| S12 | Bubble komentar 3D muncul, ngetik "CapCut", pesawat kertas terbang → transisi ke logo | "COMMENT 'CAPCUT'" / "and I'll send you the link" |

---

## 5. Outro logo CapCut PC for Marketing (±2.5s, setelah CTA)

1. Layar jadi CapCut Black, partikel Bright Blue nyedot ke tengah.
2. **Glyph CapCut** muncul pakai stroke-draw (garis putih ngegambar bentuknya), lalu fill putih + glow Bright Blue sekali pulse.
3. Wordmark **"CapCut"** mask-reveal dari kiri ke kanan ngikutin glyph.
4. Badge **"PC"** pop scale 0→1.1→1 dengan overshoot, Laser Gradient + shine sweep diagonal.
5. **"for Marketing"** slide-up + fade, tracking melebar → normal.
6. Hold 1.2s, tipis-tipis 3D float (rotateY ±4°) biar nggak mati.

Logo dari `assets/brand/capcut-pc-marketing-logo.png` dipotong per bagian (glyph, wordmark, badge, tagline) jadi layer terpisah supaya bisa dianimasiin satu-satu.

---

## 6. Caption

Caption word-by-word di band bawah (60px, bold, putih). Kata kunci (CapCut, Omni Reference, Seedance, Generate, Black Friday, $3.99) nyala Bright Blue. Timing per kata diambil dari teks naskah dan dibagi proporsional ke durasi MP3 — nanti bisa gue fine-tune per kata kalau ada yang meleset.
