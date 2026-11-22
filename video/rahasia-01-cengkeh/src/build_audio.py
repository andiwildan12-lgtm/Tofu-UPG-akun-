"""Susun audio Rahasia #01: narasi per baris + SFX + backsound A, lalu normalisasi -14 LUFS.
Waktu baris dan SFX sama dengan timeline di src/index.html."""
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SFX = REPO / ".claude/skills/upg-video/assets/sfx"
DUR = 57.0
# (file narasi, waktu mulai) · V2: baris tetap memakai audio v1, baris baru dari audio v2
LINES = [("v1/L01", 0.30), ("v1/L02", 4.60), ("v1/L03", 10.60), ("v1/L04", 14.95),
         ("v2/N05", 18.95), ("v2/N06", 24.65), ("v2/N07", 29.30), ("v2/N08", 34.85),
         ("v2/N09", 42.25), ("v1/L10", 45.75), ("v2/N11", 50.30), ("v1/L09", 53.80)]
ST = ROOT / "audio/v1/stempel-a.mp3"
# (file, waktu, gain dB)
EVENTS = [
    (SFX / "typing.mp3", 0.05, 4), (ST, 4.38, 0),
    (SFX / "swish.mp3", 10.45, -9), (SFX / "whoosh.mp3", 14.80, -6),
    (SFX / "whoosh.mp3", 18.80, -9), (SFX / "pop.mp3", 21.80, -2),      # tetes jatuh ke kapas
    (SFX / "click.mp3", 27.50, 2),                                      # kapas masuk lubang
    (SFX / "pop.mp3", 29.95, -2),                                       # tambalan menutup
    (SFX / "whoosh.mp3", 34.70, -9), (ST, 39.96, 0),                    # TERJAWAB
    (SFX / "whoosh.mp3", 42.00, -6), (ST, 44.06, 0),                    # KAMU YANG TENTUKAN
    (SFX / "pop.mp3", 45.75, -2), (SFX / "ding.mp3", 51.20, -10),
    (SFX / "pop.mp3", 53.80, -2),
]
MUSIC = REPO / "audio/uji/backsound-A-misteri-jenaka.mp3"

inputs, chains, labels = [], [], []
for i, (f, t) in enumerate(LINES):
    inputs += ["-i", str(ROOT / f"audio/{f}.mp3")]
    ms = int(t * 1000)
    chains.append(f"[{i}]aresample=48000,adelay={ms}|{ms}[v{i}]"); labels.append(f"[v{i}]")
n = len(LINES)
for j, (f, t, g) in enumerate(EVENTS):
    inputs += ["-i", str(f)]
    ms = int(t * 1000)
    chains.append(f"[{n+j}]aresample=48000,volume={g}dB,adelay={ms}|{ms}[s{j}]"); labels.append(f"[s{j}]")
m = n + len(EVENTS)
inputs += ["-stream_loop", "1", "-i", str(MUSIC)]
# backsound pelan di bawah suara, masuk halus, keluar halus
chains.append(f"[{m}]aresample=48000,volume=-11dB,afade=t=in:d=0.6,atrim=0:{DUR},afade=t=out:st={DUR-2.2}:d=2.2[mu]")
labels.append("[mu]")
chains.append("".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0,atrim=0:{DUR},"
              "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]")
cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(chains),
       "-map", "[out]", "-ac", "2", "-ar", "48000", str(ROOT / "audio/narasi.wav")]
subprocess.run(cmd, check=True)
# tahap 2: koreksi gain ke tepat -14 LUFS (loudnorm satu tahap meleset ~1-2 dB)
import re, shutil
wav = ROOT / "audio/narasi.wav"; tmp = ROOT / "audio/_tmp.wav"
meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "ebur128", "-f", "null", "-"],
                      capture_output=True, text=True).stderr
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", meas)[-1])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-af",
                f"volume={-14 - I:.2f}dB,alimiter=limit=0.84:level=disabled", "-ar", "48000", str(tmp)], check=True)
shutil.move(tmp, wav)
print(f"audio/narasi.wav selesai (koreksi {-14 - I:+.2f} dB)")
