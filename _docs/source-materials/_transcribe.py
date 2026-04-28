"""Transcribe the three audioclip-*.mp4 files in this folder using faster-whisper.

Writes <basename>.transcript.txt next to each source file.
First run downloads the model (~140 MB for 'base') to the HF cache.
"""
import sys
import time
from pathlib import Path
from faster_whisper import WhisperModel

HERE = Path(__file__).parent
MODEL_SIZE = "base"

def main() -> int:
    clips = sorted(HERE.glob("audioclip-*.mp4"))
    if not clips:
        print("No audioclip-*.mp4 files found.", file=sys.stderr)
        return 1

    print(f"Loading model '{MODEL_SIZE}' (CPU, int8)...", flush=True)
    model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

    for clip in clips:
        out = clip.with_suffix(".transcript.txt")
        print(f"\n=== {clip.name} ===", flush=True)
        start = time.perf_counter()
        segments, info = model.transcribe(
            str(clip),
            language="en",
            vad_filter=True,
            beam_size=5,
        )
        lines = []
        for seg in segments:
            ts = f"[{seg.start:6.1f}s]"
            text = seg.text.strip()
            line = f"{ts} {text}"
            print(line, flush=True)
            lines.append(line)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        elapsed = time.perf_counter() - start
        print(f"-> wrote {out.name} ({len(lines)} segments, {elapsed:.1f}s, audio {info.duration:.1f}s)", flush=True)

    return 0

if __name__ == "__main__":
    sys.exit(main())
