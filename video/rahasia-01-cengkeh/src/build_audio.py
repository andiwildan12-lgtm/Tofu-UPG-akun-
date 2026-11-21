"""Susun audio Rahasia #01: narasi per baris + SFX + backsound A, lalu normalisasi -14 LUFS.
Waktu baris dan SFX sama dengan timeline di src/index.html."""
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SFX = REPO / ".claude/skills/upg-video/assets/sfx"
DUR = 49.0
LINES = [0.30, 4.60, 10.60, 14.95, 18.95, 23.70, 28.05, 35.30, 41.05, 43.30]  # L01..L10
# (file, waktu, gain dB)
EVENTS = [
    (SFX / "typing.mp3", 0.05, 4), (ROOT / "audio/v1/stempel-a.mp3", 4.38, 0),
    (SFX / "swish.mp3", 10.45, -9), (SFX / "whoosh.mp3", 14.80, -6),
    (SFX / "pop.mp3", 19.85, 0), (SFX / "swish.mp3", 27.90, -9),
    (SFX / "whoosh.mp3", 35.15, -6), (ROOT / "audio/v1/stempel-a.mp3", 37.51, 0),
    (SFX / "pop.mp3", 41.05, -2), (SFX / "ding.mp3", 43.40, -10),
]
MUSIC = REPO / "audio/uji/backsound-A-misteri-jenaka.mp3"

inputs, chains, labels = [], [], []
for i, t in enumerate(LINES):
    inputs += ["-i", str(ROOT / f"audio/v1/L{i+1:02d}.mp3")]
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
