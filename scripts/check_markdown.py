#!/usr/bin/env python3
"""Validate local Markdown links and balanced fenced code blocks."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def exact_case(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return False
    current = ROOT
    for part in relative.parts:
        try:
            names = {child.name for child in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current /= part
    return True


def target_path(raw: str, source: Path) -> Path | None:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    target = unquote(target.split("#", 1)[0].strip())
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None
    return (source.parent / target).resolve()


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    open_fence: tuple[str, int] | None = None
    h1_count = 0
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("# "):
            h1_count += 1
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if open_fence is None:
                open_fence = (marker[0], number)
            elif marker[0] == open_fence[0]:
                open_fence = None
        for raw in LINK.findall(line):
            resolved = target_path(raw, path)
            if resolved is None:
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}:{number}: missing local target: {raw}")
            elif not exact_case(resolved):
                errors.append(f"{path.relative_to(ROOT)}:{number}: target case differs on disk: {raw}")
    if open_fence is not None:
        errors.append(f"{path.relative_to(ROOT)}:{open_fence[1]}: unclosed code fence")
    if h1_count != 1:
        errors.append(f"{path.relative_to(ROOT)}: expected exactly one level-one heading, found {h1_count}")
    return errors


def main() -> int:
    files = sorted(ROOT.rglob("*.md"))
    errors = [error for path in files for error in validate_file(path)]
    if errors:
        print("\n".join(errors))
        print(f"\nMarkdown validation failed with {len(errors)} error(s).")
        return 1
    print(f"Markdown validation passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
