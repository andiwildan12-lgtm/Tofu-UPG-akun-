# Instruksi repo tofu-upg-akun-

- Pengguna adalah owner/direktur UPG Dental Care. Panggil **"Dir"**. Bahasa Indonesia yang jelas, praktis, tidak bertele-tele.
- Repo ini untuk **akun TikTok TOFU baru UPG**: konten motion yang memperkenalkan teknologi UPG secara tidak langsung. KPI: views, like, follow. Tanpa ajakan "datang ke UPG".
- **Status: konsep akun masih didiskusikan.** Jangan produksi/render apa pun sebelum Dir memberi ACC (aturan gerbang ACC skill `upg-video`).
- Skill di `.claude/skills/` disalin dari repo `andiwildan12-lgtm/upg-video` (21 Nov 2026). Untuk video, pakai skill `upg-video` + skill bersama `panduan-visual-terpadu`, `motion-klinik-gigi`, `antislop`.
- Skill di sini adalah **salinan**; sumber utamanya tetap repo `upg-video`. Kalau skill di sana diperbarui, salin ulang ke sini.
- Skill tambahan dari GitHub (strategi TikTok, humanizer, ElevenLabs, prinsip gerak HyperFrames) dan batasan pakainya ada di `.claude/skills/SUMBER-SKILL.md`. Baca batasannya sebelum memakai. ElevenLabs dipakai lewat konektor, bukan CLI/API key.
- Keputusan akun yang sudah sah: `docs/keputusan-akun.md`. Filter **antislop mode during** berlaku untuk semua visual, naskah, dan caption.
