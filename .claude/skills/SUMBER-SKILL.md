# Sumber skill di repo ini

Setiap skill dari luar disalin utuh dan menyertakan `LICENSE-UPSTREAM` dari repo asalnya. Diambil 21 Nov 2026.

| Skill | Asal (commit) | Lisensi | Dipakai untuk |
|---|---|---|---|
| `upg-video`, `upg-antang-video`, `upg-hertasning-video`, `produksi-video-klinik`, `motion-klinik-gigi`, `panduan-visual-terpadu`, `antislop`, `antislop-ui`, `antislop-copywriting` | `andiwildan12-lgtm/upg-video` | milik Dir (antislop: lihat folder) | Alur ACC, pipeline MOTION, brand UPG, filter anti-AI-slop |
| `tiktok-growth`, `tiktok-script`, `hook-writer`, `caption-writer`, `social-seo`, `hashtag-strategy`, `thumbnail-design`, `profile-optimization`, `content-pillars`, `viral-reverse-engineering`, `analytics-and-reporting`, `ai-voiceover`, `ai-music-and-sound`, `short-form-video-script`, `storytelling-and-narrative`, `educational-content-and-how-to` | [social-media-skills/skills](https://github.com/social-media-skills/skills) (`f28cef2`) | MIT | Strategi TikTok, hook, naskah, caption, cover, pencarian, analisa |
| `humanizer` | [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) (`ae6ce56`) | MIT | Membersihkan ciri tulisan AI. **Polanya berbasis bahasa Inggris**; untuk bahasa Indonesia dipakai prinsipnya, bersama `antislop-copywriting` |
| `elevenlabs-text-to-speech`, `elevenlabs-music`, `elevenlabs-sound-effects` | [elevenlabs/skills](https://github.com/elevenlabs/skills) (`97478d1`) | MIT | Panduan prompt narasi, backsound, SFX. **Nama diberi awalan `elevenlabs-`** (satu-satunya perubahan) agar tidak tertukar |
| `motion-doctrine`, `cut-the-curve`, `captions-overlay` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) (`4145572`) | Apache-2.0 | Prinsip gerak (perpindahan adegan terasa satu alur kamera, transisi bertempo cocok, caption sebagai overlay) |

## Batasan pakai
- **ElevenLabs:** di proyek ini dipakai lewat **konektor ElevenLabs (MCP)**. Bagian skill yang menyuruh memasang CLI, `npx … onboard init`, atau menyimpan `ELEVENLABS_API_KEY` **tidak dijalankan** (aturan repo: kunci API tidak disimpan di file).
- **HyperFrames:** skill ini ditulis untuk framework HyperFrames. Yang dipakai hanya **prinsip geraknya**; skrip `motion-doctrine/scripts/*.mjs` tidak dijalankan karena pipeline kita Playwright + ffmpeg.
- **social-media-skills:** skill ini juga ada sebagai plugin di akun Dir. Salinan di repo menjamin isinya tetap sama walau plugin berubah. Bagian tentang WoopSocial (alat unggah) tidak dipakai; unggah dilakukan manual oleh tim.
- Kalau bertentangan: identitas dan aturan UPG (`upg-video`, `panduan-visual-terpadu`) serta keputusan di `docs/keputusan-akun.md` yang menang.
