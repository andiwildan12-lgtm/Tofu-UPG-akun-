# Laporan cek · Rahasia #01 "Bau Cengkeh" (V1)

File: `rahasia-01-cengkeh.mp4` · 48,98 dtk · 1080×1920 · 30 fps · H.264 + AAC

## Cek teknis (`verify_video.py`): LULUS
- Resolusi, fps, codec: OK
- Decode utuh: OK
- Loudness −14,04 LUFS (target −14 ±1,5): OK
- True peak −2,3 dBTP (batas ≤ −1): OK

## Cek brand dan aturan akun
| Poin | Hasil | Bukti |
|---|---|---|
| Logo asli UPG, pojok kiri atas, tidak menimpa konten | LULUS | `logo-upg-transparan.png`, x 80 y 250, konten mulai y ≥ 420 |
| Palet UPG (krem, oranye, teks gelap; amber dan cokelat-oranye tua sebagai turunan brand) | LULUS | Tidak ada warna di luar palet |
| Kontras: teks di atas oranye = #2A2A2A | LULUS | Semua pill kata kunci |
| Area aman (atas 250, bawah 400, kanan 120 px) | LULUS | Teks di y 420–1520; cover: stempel berakhir di x 919 |
| Tokoh tanpa mata | LULUS | Hanya tangan bersarung tangan |
| Tanpa harga, promo, WA, ajakan ke klinik | LULUS | |
| CTA follow + komen (keputusan Dir) | LULUS | Detik 41–49 |
| Audio: backsound tanpa vokal + SFX, tanpa musik bernyanyi | LULUS | Backsound A dicek transkripsi (kosong) |
| Subtitle selalu ada, maks. 2 baris | LULUS | |

## Cek antislop (mode during)
| Poin | Hasil | Catatan |
|---|---|---|
| Tanda pisah panjang (—) di teks tayang | LULUS | 0 di video, cover, caption |
| Angka/statistik tanpa sumber | LULUS | Tidak ada angka; "abad ke-16" dari bank topik (lihat catatan F4) |
| Kalimat klise AI ("Tahukah kamu", "Yuk simak", dll.) | LULUS | |
| Ikon generik AI (✨, kilat, robot) | LULUS | Semua ilustrasi dibuat khusus: cengkeh, tetes, gigi, stempel, tangan |
| Animasi template (semua fade-up/memantul) | LULUS | Gerak beragam dan punya fungsi: ketik, stempel jatuh + guncangan, garis tergambar, tetes jatuh, kertas masuk; potong langsung saat map sama |
| Ciri khas berulang | LULUS | Stempel "dug", nomor berkas, pill oranye |
| Satu titik fokus per layar | LULUS | |

## Catatan jujur
- **F4 "sejak abad ke-16"**: sumber primernya belum saya baca langsung (dari ringkasan hasil pencarian). Dir sudah menerima saat ACC naskah.
- **Detik 0,0–0,75**: judul hook masih diketik, jadi frame paling awal belum memuat seluruh pertanyaan. Cover terpisah sudah disediakan untuk tampilan di profil.
- File `rancangan-V1.md` memuat satu tanda pisah panjang di catatan internal; tidak tayang, dan tidak diubah agar catatan ACC tetap sah.
