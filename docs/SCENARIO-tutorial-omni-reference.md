# Skenario Motion Graphic Tutorial — "Bikin Iklan Parfum 30 Detik pakai CapCut Omni Reference"

**Format:** 4:3 · 1440×1080 · 30fps · target durasi ±75–85 detik (final ngikut panjang MP3 VO)
**Footage utama:** `assets/footage/tutorial-source.mp4` (screen record CapCut 2010×1080, 36.7s, **tanpa audio**)
**Gaya:** dark UI tutorial — screen recording ditaruh di "window frame" rounded, lalu di-*zoom & pan* ke area yang lagi dibahas. Overlay: spotlight (area lain di-dim), cursor ring + click ripple, label callout, kinetic typography, step counter.

---

## 1. Breakdown video sumber (yang gue pelajari)

| Waktu sumber | Apa yang terjadi di layar |
|---|---|
| 0:00–0:01 | CapCut Home → klik **Create project** |
| 0:02–0:03 | Editor kosong → panel kiri **Media → Generate → AI video** |
| 0:04–0:05 | Pilih tab **Omni reference** (bisa referensi s/d 30 gambar, 10 video, 10 audio) |
| 0:06–0:07 | File picker → pilih aset: foto botol parfum, kain pink, background, model cewek, + 2 file audio |
| 0:08 | Aset masuk ke kotak referensi (5 gambar + audio 00:02 & 00:03) |
| 0:09–0:12 | Paste **prompt panjang ber-timestamp** (mis. "commercial segment from 4s to 23s is ultra-photorealistic… glass refraction, caustics, shallow depth of field") |
| 0:13–0:16 | Model **Dreamina Seedance 2.5** → buka Settings: Duration 10s → **30s**, Resolusi **720p**, Aspect **4:3**, jumlah generate **1** |
| 0:17–0:18 | Klik **Generate** (estimasi kredit naik 630 → **1890**) |
| 0:19–0:22 | Proses generate; muncul hasil di panel Generations → tip "hover lalu klik + untuk masuk timeline" |
| 0:23–0:24 | Hasil masuk timeline — iklan parfum **LUMÉA** di ladang mawar |
| 0:25–0:26 | Klik kanan / pilih potongan klip di timeline → jadikan referensi |
| 0:27 | Prompt revisi singkat: **"add more petal flowers around"** · 5s · 4:3 (567 kredit) |
| 0:28–0:31 | Generate revisi |
| 0:32–0:36 | Preview hasil revisi — kelopak mawar beterbangan di sekitar botol, siap **Use as reference / masuk timeline** |

**Inti pelajaran:** Omni reference = satu prompt + banyak aset (produk, model, background, audio) → Seedance 2.5 bikin klip iklan 30 detik utuh; lalu revisi bagian tertentu pakai potongan klip sebagai referensi + prompt pendek.

---

## 2. Skenario per scene (4:3)

> Kolom **VO** merujuk ke daftar voice over di bagian 3. Durasi scene final = panjang MP3 + ±0.5s napas.

| # | Scene | Visual / motion | Footage sumber | VO |
|---|---|---|---|---|
| S1 | **Hook** | Full-bleed hasil akhir (botol LUMÉA + kelopak beterbangan) di-zoom pelan 110%→100%. Judul kinetic muncul per kata: **"IKLAN PARFUM 30 DETIK"** lalu sub "cuma 1 prompt". Flash putih tipis ke S2. | 0:32–0:36 (crop area preview) | VO01 |
| S2 | **Roadmap** | Background gelap + grid halus. 4 chip step slide-in stagger: ① Siapin aset ② Omni reference ③ Atur setting ④ Generate & revisi. Chip aktif menyala cyan (warna aksen CapCut). | — (grafis) | VO02 |
| S3 | **Create project** | Window frame CapCut muncul dari bawah (scale 0.9→1). Zoom ke tombol *Create project*, cursor ring + click ripple. Step counter "01/04" di pojok. | 0:00–0:02 | VO03 |
| S4 | **Masuk Omni reference** | Pan ke panel kiri. Spotlight berurutan: **Media → Generate → AI video → Omni reference**, tiap item dapat label callout + garis penunjuk. | 0:02–0:05 | VO04 |
| S5 | **Upload aset** | Zoom ke file picker. Thumbnail aset "terbang" keluar dari layar jadi kartu berlabel: **PRODUK · MODEL · BACKGROUND · TEKSTUR · AUDIO**. Badge info: "maks 30 gambar · 10 video · 10 audio". | 0:06–0:08 | VO05 |
| S6 | **Tulis prompt** | Zoom ke kotak prompt. Overlay typewriter potongan prompt. Lalu grafis timeline bar 0–30s terbelah 3 segmen: *0–4s intro · 4–23s commercial · 23–30s closing* — nunjukin konsep prompt per-timestamp. | 0:09–0:12 | VO06, VO07 |
| S7 | **Model & settings** | Zoom ke Settings. Kartu spek pop-in satu-satu: **Seedance 2.5 · 30s · 720p · 4:3**. Slider durasi dianimasikan 10s→30s. Opsi 4:3 di-highlight kotak cyan. | 0:13–0:16 | VO08 |
| S8 | **Generate** | Tombol Generate pulse. Counter kredit animasi **630 → 1890**. Loading ring di tengah, lalu tip kuning "hover → klik +" di-zoom. | 0:17–0:22 | VO09 |
| S9 | **Hasil masuk timeline** | Zoom ke player preview + timeline. Hasil di-"pop out" dari window jadi full 4:3 sebentar (2–3 detik) biar penonton lihat kualitasnya. | 0:23–0:24 | VO10 |
| S10 | **Revisi bagian tertentu** | Highlight potongan klip di timeline (kotak putih), panah ke kotak referensi. Typewriter: *"add more petal flowers around"* + chip **5s · 4:3**. | 0:25–0:28 | VO11 |
| S11 | **Before / After** | Split-screen wipe vertikal: kiri *sebelum* (botol tanpa kelopak, sumber 0:27), kanan *sesudah* (kelopak beterbangan, sumber 0:35). Label BEFORE / AFTER. | 0:27 & 0:33–0:36 | VO12 |
| S12 | **Recap + CTA** | 4 chip roadmap balik lagi dengan centang ✓ semua. Lalu end card: hasil akhir blur di background + teks CTA + kartu follow (adaptasi block `instagram-follow` ke 4:3). | 0:35–0:36 + grafis | VO13, VO14 |

**Detail motion global**
- Easing zoom/pan: `power3.inOut`, durasi 0.8–1.2s; jangan zoom >2.2× biar teks UI nggak pecah (sumber cuma 1080p).
- Transisi antar scene: zoom-through (scale up + blur 8px) atau whip pan kecil, max 0.4s.
- Palet: background `#0E0F12`, aksen cyan `#22D3EE` (match tombol CapCut), highlight kuning `#FACC15` untuk tips, putih untuk teks.
- Font: Inter / DM Sans bold untuk judul, medium untuk label.
- Musik: lo-fi / corporate upbeat ±100–110 BPM, di-duck −12dB pas VO bunyi (opsional, kalau lo supply).

---

## 3. Daftar Voice Over (yang perlu lo rekam / supply MP3)

Simpan di **`assets/vo/`** dengan nama persis seperti di bawah. Gaya: santai, kayak ngobrol ke temen, tempo sedang. Kasih jeda ±0.3s di awal & akhir tiap file. Estimasi durasi = acuan aja — gue nanti sinkronin timeline ke panjang asli tiap MP3.

| File | Scene | Naskah VO | ±Durasi |
|---|---|---|---|
| `vo01.mp3` | S1 | "Iklan parfum kayak gini… bukan syuting. Ini dibikin pakai satu prompt doang di CapCut." | 5s |
| `vo02.mp3` | S2 | "Caranya cuma empat langkah: siapin aset, pakai Omni Reference, atur setting, terus generate dan revisi." | 6s |
| `vo03.mp3` | S3 | "Pertama, buka CapCut, terus klik Create Project." | 3s |
| `vo04.mp3` | S4 | "Di panel kiri, masuk ke Media, Generate, pilih AI Video, lalu klik tab Omni Reference." | 6s |
| `vo05.mp3` | S5 | "Sekarang masukin semua aset lo: foto produk, model, background, tekstur, sampai file audio. Bisa sampai tiga puluh gambar, sepuluh video, dan sepuluh audio sekaligus." | 9s |
| `vo06.mp3` | S6 | "Lanjut tulis prompt-nya. Jelasin produknya, suasananya, dan gaya visual yang lo mau." | 5s |
| `vo07.mp3` | S6 | "Tipsnya: pecah prompt per detik. Misalnya detik nol sampai empat buat intro, empat sampai dua puluh tiga buat bagian iklan utama, sisanya buat penutup. Hasilnya jauh lebih terkontrol." | 10s |
| `vo08.mp3` | S7 | "Pilih model Dreamina Seedance 2.5. Di setting, geser durasinya ke tiga puluh detik, resolusi 720p, dan rasio empat banding tiga." | 8s |
| `vo09.mp3` | S8 | "Klik Generate, tunggu sebentar. Kalau udah jadi, hover hasilnya terus klik tanda plus buat masukin ke timeline." | 7s |
| `vo10.mp3` | S9 | "Dan ini hasilnya. Botol kacanya kelihatan nyata, lengkap sama pantulan cahayanya." | 5s |
| `vo11.mp3` | S10 | "Ada bagian yang kurang pas? Gampang. Ambil potongan klipnya, jadiin referensi, terus kasih prompt pendek. Contohnya: add more petal flowers around." | 9s |
| `vo12.mp3` | S11 | "Generate lima detik aja, dan langsung beda banget. Sebelum… dan sesudah." | 5s |
| `vo13.mp3` | S12 | "Jadi intinya: aset, Omni Reference, setting, generate. Iklan tiga puluh detik, beres." | 6s |
| `vo14.mp3` | S12 | "Kalau tutorial ini ngebantu, save dan follow buat trik AI video lainnya!" | 4s |

**Total VO ±88 detik.**

---

## 4. Aset opsional (biar hasilnya lebih tajam)

| File | Kegunaan |
|---|---|
| `assets/footage/result-final.mp4` | Export asli iklan LUMÉA (30s) + versi revisi kelopak (5s) dari CapCut. Area preview di screen record cuma ±730px, jadi buat S1, S9, S11 bakal jauh lebih tajam kalau pakai export aslinya. |
| `assets/music/bgm.mp3` | Musik latar. |
| Handle / nama akun | Buat kartu follow di end card (default gue isi placeholder). |

Kalau MP3 udah masuk, gue tinggal build komposisinya di `index.html` (1440×1080), sinkron tiap scene ke durasi VO, terus `npm run check` + render.
