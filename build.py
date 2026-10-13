#!/usr/bin/env python3
"""
build.py — Sync skills/ into the dist/ plugin layout for ghost-council.

skills/<name>/SKILL.md is already in the format Claude Code expects (frontmatter
with `name` + `description`, no transformation needed) — unlike ix-skills, which
compiles a richer multi-target source format. This script only keeps dist/skills/
in sync: wipe, then copy fresh, so a skill deleted from skills/ doesn't linger
in dist/ (a plain `cp -r` or `rsync` without `--delete` would leave it behind).

Usage:
    python3 build.py              # wipe dist/skills/, copy skills/, validate
    python3 build.py --check      # validate only, no write (dry-run)
"""

import re
import shutil
import sys
from pathlib import Path

SKILLS_DIR = Path("skills")
DIST_SKILLS_DIR = Path("dist/skills")
PLUGIN_JSON = Path("dist/.claude-plugin/plugin.json")
# Embarqués dans le plugin installé : la licence du projet et celle du code repris (MIT).
LEGAL_FILES = (Path("LICENSE"), Path("THIRD_PARTY.md"))

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(\S+)", re.MULTILINE)
DESC_RE = re.compile(r"^description:", re.MULTILINE)


def validate_skill(path: Path) -> str | None:
    """Return an error string, or None if the SKILL.md frontmatter looks sane."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "no YAML frontmatter (missing leading --- block)"
    fm = m.group(1)
    name_m = NAME_RE.search(fm)
    if not name_m:
        return "frontmatter missing 'name'"
    if name_m.group(1) != path.parent.name:
        return f"frontmatter name '{name_m.group(1)}' != directory '{path.parent.name}'"
    if not DESC_RE.search(fm):
        return "frontmatter missing 'description'"
    return None


def main() -> int:
    check_only = "--check" in sys.argv
    errors = 0

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())
    if not skill_dirs:
        print(f"✗ no skills found under {SKILLS_DIR}/")
        return 1

    print(f"Validating {len(skill_dirs)} skill(s) in {SKILLS_DIR}/")
    for skill_dir in skill_dirs:
        err = validate_skill(skill_dir / "SKILL.md")
        if err:
            print(f"  ✗ {skill_dir.name}: {err}")
            errors += 1
        else:
            print(f"  ✓ {skill_dir.name}")

    if errors:
        print(f"\n{errors} error(s) — fix before syncing dist/")
        return 1

    if check_only:
        print("\n--check: no files written")
        return 0

    if DIST_SKILLS_DIR.exists():
        shutil.rmtree(DIST_SKILLS_DIR)
    DIST_SKILLS_DIR.mkdir(parents=True)
    for skill_dir in skill_dirs:
        shutil.copytree(skill_dir, DIST_SKILLS_DIR / skill_dir.name)
    print(f"\n✓ synced {len(skill_dirs)} skill(s) → {DIST_SKILLS_DIR}/")
    for legal in LEGAL_FILES:
        shutil.copy2(legal, DIST_SKILLS_DIR.parent / legal.name)
    print(f"✓ copied {', '.join(p.name for p in LEGAL_FILES)} → {DIST_SKILLS_DIR.parent}/")

    if not PLUGIN_JSON.exists():
        print(f"✗ {PLUGIN_JSON} not found — plugin manifest missing")
        return 1
    print(f"✓ {PLUGIN_JSON} present")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
