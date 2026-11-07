# Skenario Motion Graphic Tutorial — "Make a 30-Second Perfume Ad with CapCut Omni Reference"

**Format:** 4:3 · 1440×1080 · 30fps · target durasi ±70–75 detik (final ngikut panjang MP3 VO)
**Bahasa:** VO & semua teks di layar **English**
**Footage utama:** `assets/footage/tutorial-source.mp4` (screen record CapCut 2010×1080, 36.7s, **tanpa audio**)
**Gaya:** dark UI tutorial — screen recording ditaruh di "window frame" rounded, lalu di-*zoom & pan* ke area yang lagi dibahas. Overlay: spotlight (area lain di-dim), cursor ring + click ripple, label callout, kinetic typography, step counter.

> **Revisi v2:** Hook & roadmap dihapus — video langsung buka di CapCut (scene Create Project). VO dinomori ulang mulai `vo01`, semua English.

---

## 1. Breakdown video sumber

| Waktu sumber | Apa yang terjadi di layar |
|---|---|
| 0:00–0:01 | CapCut Home → klik **Create project** |
| 0:02–0:03 | Editor kosong → panel kiri **Media → Generate → AI video** |
| 0:04–0:05 | Pilih tab **Omni reference** (s/d 30 gambar, 10 video, 10 audio) |
| 0:06–0:07 | File picker → pilih aset: foto botol parfum, kain pink, background, model, + 2 file audio |
| 0:08 | Aset masuk ke kotak referensi (5 gambar + audio 00:02 & 00:03) |
| 0:09–0:12 | Paste prompt panjang ber-timestamp ("commercial segment from 4s to 23s is ultra-photorealistic…") |
| 0:13–0:16 | Model **Dreamina Seedance 2.5** → Settings: 10s → **30s**, **720p**, **4:3**, 1 generation |
| 0:17–0:18 | Klik **Generate** (kredit 630 → **1890**) |
| 0:19–0:22 | Proses generate → hasil muncul di panel Generations + tip "hover, click + to add to timeline" |
| 0:23–0:24 | Hasil masuk timeline — iklan parfum **LUMÉA** di ladang mawar |
| 0:25–0:26 | Pilih potongan klip di timeline → jadikan referensi |
| 0:27 | Prompt revisi: **"add more petal flowers around"** · 5s · 4:3 (567 kredit) |
| 0:28–0:31 | Generate revisi |
| 0:32–0:36 | Preview hasil revisi — kelopak mawar beterbangan di sekitar botol |

---

## 2. Skenario per scene (4:3)

> Durasi scene final = panjang MP3 + ±0.5s napas. Semua teks on-screen di bawah ditulis persis seperti yang bakal tampil.

| # | Scene | Visual / motion | Teks on-screen | Footage | VO |
|---|---|---|---|---|---|
| S1 | **Create project** | Video langsung buka: window frame CapCut scale 0.92→1 + fade dari gelap. Zoom pelan ke tombol *Create project*, cursor ring + click ripple. Step counter muncul di pojok. | "STEP 01 · New Project" | 0:00–0:02 | vo01 |
| S2 | **Open Omni Reference** | Pan ke panel kiri. Spotlight berurutan: **Media → Generate → AI video → Omni reference**, tiap item dapat callout + garis penunjuk. | "Media › Generate › AI video › Omni reference" | 0:02–0:05 | vo02 |
| S3 | **Upload assets** | Zoom ke file picker. Thumbnail aset "terbang" keluar jadi kartu berlabel. Badge info pop-in. | Cards: "PRODUCT · MODEL · BACKGROUND · TEXTURE · AUDIO" · Badge: "Up to 30 images · 10 videos · 10 audio" | 0:06–0:08 | vo03 |
| S4 | **Write the prompt** | Zoom ke kotak prompt, overlay typewriter potongan prompt. | "STEP 02 · Prompt" | 0:09–0:12 | vo04 |
| S5 | **Timestamp tip** | Grafis timeline bar 0–30s terbelah 3 segmen, tiap segmen nyala bergantian sinkron sama VO. | "PRO TIP · Prompt by timestamp" · Segments: "0–4s INTRO · 4–23s HERO · 23–30s OUTRO" | 0:09–0:12 (blur di belakang) | vo05 |
| S6 | **Model & settings** | Zoom ke Settings. Kartu spek pop-in satu-satu. Slider durasi dianimasikan 10s→30s, opsi 4:3 di-highlight kotak cyan. | "STEP 03 · Settings" · Cards: "Seedance 2.5 · 30s · 720p · 4:3" | 0:13–0:16 | vo06 |
| S7 | **Generate** | Tombol Generate pulse. Counter kredit animasi 630 → 1890. Loading ring, lalu tip kuning di-zoom. | "STEP 04 · Generate" · Tip: "Hover → click + to add to timeline" | 0:17–0:22 | vo07 |
| S8 | **The result** | Zoom ke player preview, lalu hasil di-"pop out" jadi full 4:3 selama 2–3 detik. | "Generated in one shot" | 0:23–0:24 | vo08 |
| S9 | **Fix a section** | Highlight potongan klip di timeline (kotak putih), panah ke kotak referensi. Typewriter prompt revisi + chip setting. | Prompt: "add more petal flowers around" · Chips: "5s · 4:3" | 0:25–0:28 | vo09 |
| S10 | **Before / After** | Split-screen wipe vertikal: kiri sebelum (sumber 0:27), kanan sesudah (sumber 0:35). | "BEFORE" / "AFTER" | 0:27 & 0:33–0:36 | vo10 |
| S11 | **Recap** | 4 chip step slide-in stagger, masing-masing dapet centang ✓. | "✓ Assets · ✓ Omni Reference · ✓ Settings · ✓ Generate" | grafis | vo11 |
| S12 | **CTA** | End card: hasil akhir blur di background + teks CTA + kartu follow (adaptasi block `instagram-follow` ke 4:3). | "Save this for later" · "Follow for more AI video tricks" | 0:35–0:36 + grafis | vo12 |

**Detail motion global**
- Easing zoom/pan: `power3.inOut`, durasi 0.8–1.2s; zoom max 2.2× biar teks UI nggak pecah (sumber cuma 1080p).
- Transisi antar scene: zoom-through (scale up + blur 8px) atau whip pan kecil, max 0.4s.
- Palet: background `#0E0F12`, aksen cyan `#22D3EE` (match tombol CapCut), kuning `#FACC15` untuk tips, putih untuk teks.
- Font: Inter / DM Sans bold untuk judul, medium untuk label.
- Musik (opsional): lo-fi / corporate upbeat ±100–110 BPM, di-duck −12dB pas VO bunyi.

---

## 3. Daftar Voice Over (English)

Simpan di **`assets/vo/`** dengan nama persis seperti di bawah. Gaya: casual, friendly, kayak ngajarin temen; tempo sedang. Kasih jeda ±0.3s di awal & akhir tiap file. Durasi cuma acuan — timeline nanti gue sinkronin ke panjang asli MP3.

| File | Scene | Script | ±Durasi |
|---|---|---|---|
| `vo01.mp3` | S1 | "Open CapCut and click Create Project." | 3s |
| `vo02.mp3` | S2 | "On the left panel, go to Media, then Generate, choose AI Video, and open the Omni Reference tab." | 6s |
| `vo03.mp3` | S3 | "Now drop in all your assets — your product shot, a model, a background, textures, even audio files. You can add up to thirty images, ten videos, and ten audio clips." | 9s |
| `vo04.mp3` | S4 | "Next, write your prompt. Describe the product, the mood, and the visual style you want." | 5s |
| `vo05.mp3` | S5 | "Pro tip: break your prompt down by timestamp. Zero to four seconds for the intro, four to twenty-three for the hero shot, and the rest for the outro. It gives you way more control." | 10s |
| `vo06.mp3` | S6 | "Pick the Dreamina Seedance 2.5 model. In settings, slide the duration up to thirty seconds, set it to 720p, and choose a four-by-three ratio." | 8s |
| `vo07.mp3` | S7 | "Hit Generate and give it a moment. When it's done, hover over the result and click the plus icon to add it to your timeline." | 7s |
| `vo08.mp3` | S8 | "And here's the result. The glass looks real, right down to the light reflections." | 5s |
| `vo09.mp3` | S9 | "Not happy with one part? Easy. Grab that clip, use it as a reference, and add a short prompt — like 'add more petal flowers around.'" | 8s |
| `vo10.mp3` | S10 | "Generate just five seconds, and the difference is huge. Before… and after." | 5s |
| `vo11.mp3` | S11 | "So that's it: assets, Omni Reference, settings, generate. A thirty-second ad, done." | 6s |
| `vo12.mp3` | S12 | "If this helped, save it and follow for more AI video tricks!" | 4s |

**Total VO ±76 detik.**

---

## 4. Aset opsional (biar hasilnya lebih tajam)

| File | Kegunaan |
|---|---|
| `assets/footage/result-final.mp4` | Export asli iklan LUMÉA (30s) + versi revisi kelopak (5s) dari CapCut. Area preview di screen record cuma ±730px, jadi buat S8 & S10 bakal jauh lebih tajam kalau pakai export aslinya. |
| `assets/music/bgm.mp3` | Musik latar. |
| Handle / nama akun | Buat kartu follow di end card (default gue isi placeholder). |
