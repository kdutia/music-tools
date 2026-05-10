#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
"""
mg-convert: Convert audio files to MakeNoise Morphagene compatible format.

Output format: 48KHz, 32-bit floating-point, stereo WAV.
Files longer than 2.9 minutes are split into chunks.
Requires sox to be installed on the system.
"""

import argparse
import math
import subprocess
import sys
from pathlib import Path

MAX_FILES = 32
CHUNK_SECONDS = 2.9 * 60  # 174 seconds
SUFFIXES = "123456789abcdefghijklmnopqrstuvw"


def get_duration(filepath: Path) -> float:
    result = subprocess.run(
        ["soxi", "-D", str(filepath)],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def convert_chunk(filepath: Path, outfile: Path, start: float, duration: float) -> None:
    subprocess.run(
        [
            "sox", "--norm", str(filepath),
            "-c", "2", "-r", "48k", "-e", "float", "-b", "32",
            str(outfile),
            "trim", str(start), str(duration),
        ],
        check=True,
    )


def convert(input_dir: Path) -> None:
    wav_files = sorted(f for f in input_dir.glob("*.wav") if not f.name.startswith("._"))
    if not wav_files:
        print(f"No .wav files found in: {input_dir}")
        sys.exit(0)

    output_dir = input_dir / "converted"
    output_dir.mkdir(exist_ok=True)

    print(f"Processing files in: {input_dir}\n")

    out_index = 0

    for filepath in wav_files:
        duration = get_duration(filepath)
        num_chunks = max(1, math.ceil(duration / CHUNK_SECONDS))

        for chunk in range(num_chunks):
            if out_index >= MAX_FILES:
                print(
                    "WARNING: Too many files. Morphagene's max is 32. "
                    "Exiting without processing the rest."
                )
                sys.exit(0)

            start = chunk * CHUNK_SECONDS
            chunk_duration = min(CHUNK_SECONDS, duration - start)
            outfile = output_dir / f"mg{SUFFIXES[out_index]}.wav"

            if num_chunks > 1:
                print(f"Converting: {filepath.name} (chunk {chunk + 1}/{num_chunks})...")
            else:
                print(f"Converting: {filepath.name}...")

            convert_chunk(filepath, outfile, start, chunk_duration)
            print("Done!\n")
            out_index += 1

    print(f"All converted files are located in: {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert audio files to MakeNoise Morphagene compatible format."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing .wav files (default: current directory)",
    )
    args = parser.parse_args()

    input_dir = Path(args.directory).resolve()
    if not input_dir.is_dir():
        print(f"Error: '{args.directory}' is not a valid directory.")
        sys.exit(1)

    convert(input_dir)


if __name__ == "__main__":
    main()
