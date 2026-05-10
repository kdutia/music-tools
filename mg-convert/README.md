# mg-convert

Converts audio files to [MakeNoise Morphagene](https://www.makenoisemusic.com/modules/morphagene) compatible format: 48KHz, 32-bit floating-point, stereo WAV.

## Requirements

Install [sox](https://sox.sourceforge.net/):

```bash
# macOS
brew install sox

# Ubuntu/Debian
sudo apt install sox

# Fedora/RHEL
sudo dnf install sox
```

## Usage

```bash
uv run mg-convert.py [directory]
```

- `directory` — path to folder containing `.wav` files (defaults to current directory)

Output files are written to a `converted/` subdirectory and named `mg1.wav`, `mg2.wav`, etc. The Morphagene supports a maximum of 32 files.
