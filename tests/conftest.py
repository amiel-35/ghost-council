"""Fixtures partagées des tests de council.py.

council.py est un script autonome (pas un paquet installé) : on le charge par son chemin.
Adapté de tests/conftest.py d'advisory-council 0.2.1 (nzanepro, MIT).
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "council"
SCRIPT_PATH = SKILL_DIR / "scripts" / "council.py"

# Une grille mélangée, comme le critère de fini du brief : un ghost, une posture ix, un costume.
SEATS = ["ghost:popper", "ix:dixieme-homme", "costume:humain"]
SEAT_IDS = ["popper", "dixieme-homme", "humain"]
TITLE = "Passer l'offre en freemium"


def _load_council():
    spec = importlib.util.spec_from_file_location("council", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_ix(base: Path, version: str, *names: str) -> Path:
    """Un faux cache ix-skills : base/<version>/skills/<nom>/SKILL.md."""
    skills = base / version / "skills"
    for name in names:
        (skills / name).mkdir(parents=True, exist_ok=True)
        (skills / name / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: test\n---\n\n# {name} v{version}\n", encoding="utf-8")
    return skills


@pytest.fixture()
def ix_cache(tmp_path, monkeypatch):
    """COUNCIL_ANGLES_PATH pointé sur un faux cache à deux versions (3.9.0 et 3.10.0)."""
    base = tmp_path / "ix-cache"
    make_ix(base, "3.9.0", "dixieme-homme", "contrarian", "seulement-ancienne")
    make_ix(base, "3.10.0", "dixieme-homme", "contrarian")
    monkeypatch.setenv("COUNCIL_ANGLES_PATH", str(base / "*" / "skills"))
    monkeypatch.delenv("COUNCIL_GHOSTS_DIR", raising=False)
    return base


@pytest.fixture()
def council(ix_cache):
    """Un import neuf de council.py par test, avec le faux cache ix."""
    return _load_council()


@pytest.fixture()
def run(council, capsys):
    """Appelle council.main([...]) et rend (code de sortie, stdout)."""

    def _run(argv):
        code = council.main([str(a) for a in argv])
        return code, capsys.readouterr().out

    return _run


def run_json(run, argv):
    code, out = run(list(argv) + ["--json"])
    return code, json.loads(out)


def init_session(run, tmp_path, name="seance", seats=None, fmt=None, arbiter=None, extra=None):
    folder = tmp_path / name
    args = ["init", folder, "--title", TITLE]
    for seat in (seats if seats is not None else SEATS):
        args += ["--seat", seat]
    if fmt:
        args += ["--format", fmt]
    if arbiter:
        args += ["--arbiter", arbiter]
    code, out = run(args + (extra or []))
    assert code == 0, out
    return folder


def strip_todo(text: str) -> str:
    return "\n".join(ln for ln in text.splitlines() if ln.strip() != "<!-- council:todo -->") + "\n"


def set_fields(text: str, **fields: str) -> str:
    """Remplace les lignes `**Nom :** ...` ; les _ du nom de l'argument valent des espaces."""
    for name, value in fields.items():
        label = name.replace("_", " ")
        pattern = re.compile(rf"^\*\*{re.escape(label)} ?:\*\*.*$", re.MULTILINE)
        text, count = pattern.subn(lambda _m: f"**{label} :** {value}", text, count=1)
        assert count == 1, f"champ {label!r} introuvable"
    return text


def fill(path: Path, **fields: str) -> str:
    text = strip_todo(path.read_text(encoding="utf-8"))
    if fields:
        text = set_fields(text, **fields)
    path.write_text(text, encoding="utf-8")
    return text


def fill_cadrage(folder: Path, validated="oui, par le décideur le 2026-10-13") -> None:
    fill(folder / "CADRAGE.md", Question="Faut-il passer en freemium ?",
         **{"Grille_validée": validated})


def fill_avis(folder: Path, seat_id: str, prefix="AVIS", position="Pas maintenant") -> None:
    fill(folder / f"{prefix}-{seat_id}.md", Position=position, Confiance="moyenne")


def fill_vote(folder: Path, seat_id: str, vote="B", changed="non") -> None:
    fill(folder / f"TOUR2-{seat_id}.md", Vote=vote, Confiance="moyenne",
         **{"Changé_depuis_le_tour_1": changed})


def build_tour(run, tmp_path, **kw) -> Path:
    """Une séance `tour` complète qui passe `check --final`."""
    folder = init_session(run, tmp_path, **kw)
    fill_cadrage(folder)
    for seat_id in SEAT_IDS:
        fill_avis(folder, seat_id)
    fill(folder / "SYNTHESE.md")
    return folder


def build_deliberation(run, tmp_path) -> Path:
    """Une séance `deliberation` complète qui passe `check --final`."""
    folder = init_session(run, tmp_path, fmt="deliberation")
    fill_cadrage(folder)
    fill(folder / "DOSSIER.md")
    for seat_id in SEAT_IDS:
        fill_avis(folder, seat_id, prefix="TOUR1")
    path = folder / "VERIFICATION.md"
    fill(path)
    path.write_text(path.read_text(encoding="utf-8").replace(
        "| DOSSIER §4 F1 | ... |", "| DOSSIER §4 F1 | CONFIRMÉ |"), encoding="utf-8")
    fill(folder / "BILAN-TOUR1.md")
    for seat_id in SEAT_IDS:
        fill_vote(folder, seat_id)
    fill(folder / "SYNTHESE.md", **{"Vote_du_conseil": "B : 3 sur 3"})
    return folder
