#!/usr/bin/env python3
"""Check or losslessly optimize repository PNG assets with Pillow."""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required: python -m pip install Pillow", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
IMAGE_ROOT = ROOT / "images"
# PNG encoders can differ by a handful of bytes between Pillow/zlib versions.
# Ignore those non-actionable differences so local and CI checks stay stable.
MIN_SAVING_BYTES = 16


def optimized_bytes(path: Path) -> bytes:
    with Image.open(path) as image:
        output = io.BytesIO()
        image.save(output, format="PNG", optimize=True, compress_level=9)
        return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="replace PNGs when lossless output is smaller")
    parser.add_argument("--check", action="store_true", help="fail when lossless savings remain")
    args = parser.parse_args()
    files = sorted(IMAGE_ROOT.rglob("*.png"))
    before = after = changed = 0
    for path in files:
        original = path.read_bytes()
        candidate = optimized_bytes(path)
        before += len(original)
        after += min(len(original), len(candidate))
        if len(original) - len(candidate) >= MIN_SAVING_BYTES:
            changed += 1
            if args.write:
                path.write_bytes(candidate)
    print(f"Scanned {len(files)} PNGs; potential/actual saving: {before - after:,} bytes across {changed} files.")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
