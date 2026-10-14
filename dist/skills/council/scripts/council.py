#!/usr/bin/env python3
# Adapted from advisory-council 0.2.1, scripts/council.py
# (https://github.com/nzanepro/tvr-skills-agent-advisory-council).
#
# MIT License
#
# Copyright (c) 2026 nzanepro
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Tient la paperasse d'une séance de conseil : fichiers, état, décompte, contrôles, briefs.

Une séance vit dans un dossier. Son déroulé n'est pas codé ici : il est lu dans un format
(references/formats/*.json) qui liste les étapes, leurs fichiers, leurs dépendances et leurs
champs obligatoires. Le format est recopié dans council.json à l'init, la séance se suffit
donc à elle-même.

Chaque fichier naît en gabarit marqué `<!-- council:todo -->` ; supprimer cette ligne quand
le fichier est écrit. Le script n'appelle aucun modèle : il crée les fichiers, dit où on en
est, compte, contrôle le processus et rédige les briefs à donner aux angles.

Sous-commandes :
    init      crée le dossier, council.json et chaque gabarit (n'écrase jamais rien)
    status    l'état de chaque étape et la prochaine chose à faire
    resolve   le chemin à lire pour une référence d'angle (ghost:, ix:, costume:, arbitre:, file:)
    brief     le brief complet d'un angle, de l'arbitre ou du vérificateur pour une étape
    addendum  crée le prochain ADDENDUM-<lettre>.md (formats qui en ont)
    tally     les positions d'une étape, ou le décompte des votes
    check     contrôle la séance contre les règles du format

Codes de sortie : 0 ok, 1 erreur d'usage ou d'entrée (le message dit quoi faire),
3 le contrôle ou le décompte a trouvé des problèmes.

Exemples :
    python3 council.py init seance --title "Passer en freemium" \\
        --seat ghost:popper --seat ix:dixieme-homme@opus --seat costume:humain
    python3 council.py brief seance avis popper
    python3 council.py status seance
    python3 council.py check seance --final
"""
from __future__ import annotations

import argparse
import datetime as _dt
import glob
import json
import os
import re
import string
import sys
import unicodedata
from pathlib import Path

TODO_MARKER = "<!-- council:todo -->"
SCHEMA_VERSION = 1
SEAT_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_IDS = {"cadrage", "grille", "relecture", "dossier", "verification", "bilan",
                "synthese", "divergence", "addendum", "council", "arbitre"}
MODELS = ("opus", "sonnet", "haiku", "codex", "gemini")
EXTERNAL_MODELS = ("codex", "gemini")
KINDS = ("ghost", "ix", "costume", "partie", "arbitre", "file")
PARTIES_FILE = "PARTIES.md"
SEAT_BARE_ORDER = ("ghost", "costume", "ix")
ARBITER_BARE_ORDER = ("arbitre", "ghost", "ix")
NO_ARBITER = "aucun"
# Un gabarit non rempli ressemble à « <une ligne, tranchée> ».
PLACEHOLDER_RE = re.compile(r"<(?!!--)[a-zà-ÿ][^<>\n]{3,}>")
# Tolère l'espace (normale, insécable ou fine) avant les deux-points : « **Position :** ».
FIELD_RE = r"^\*\*{name}[   ]?:\*\*[ \t]*(?P<value>.*)$"

SKILL_DIR = Path(__file__).resolve().parent.parent
REFERENCES_DIR = SKILL_DIR / "references"
FORMATS_DIR = REFERENCES_DIR / "formats"
TEMPLATE_DIR = REFERENCES_DIR / "templates"
BRIEF_DIR = TEMPLATE_DIR / "briefs"
SECTION_FILES = {"costume": REFERENCES_DIR / "angles" / "costumes.md",
                 "arbitre": REFERENCES_DIR / "angles" / "arbitres.md"}
# ix-skills installé depuis sa propre marketplace (cache/ix-skills/…) ou depuis le
# catalogue amiel-35/plugins (cache/amiel-35/…) : le motif couvre les deux.
DEFAULT_ANGLES_PATH = "~/.claude/plugins/cache/*/ix-skills/*/skills"


class CouncilError(Exception):
    """Erreur d'usage ou d'entrée ; le message dit quoi essayer."""


# ----------------------------------------------------------------------------- outils

def write_lf(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def fold(text: str) -> str:
    """Minuscules, sans accents, apostrophes droites : pour comparer des titres."""
    text = unicodedata.normalize("NFKD", text.replace("’", "'").lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def slugify(text: str, limit: int = 40) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", fold(text)).strip("-")
    return slug[:limit].rstrip("-") or "decision"


def fill(template: str, values: dict) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", str(value))
    return template


def load_text(path: Path, what: str) -> str:
    if not path.is_file():
        raise CouncilError(f"{what} {path} introuvable ; réinstaller le skill council en entier "
                           "(references/ doit être à côté de scripts/)")
    return path.read_text(encoding="utf-8")


def file_state(path: Path) -> str:
    if not path.is_file():
        return "absent"
    return "à faire" if TODO_MARKER in path.read_text(encoding="utf-8") else "fait"


def read_field(text: str, name: str) -> str | None:
    match = re.search(FIELD_RE.format(name=re.escape(name)), text, re.MULTILINE | re.IGNORECASE)
    if not match:
        return None
    value = match.group("value").strip()
    if not value or PLACEHOLDER_RE.search(value):
        return None
    return value


def has_field_line(text: str, name: str) -> bool:
    return re.search(FIELD_RE.format(name=re.escape(name)), text,
                     re.MULTILINE | re.IGNORECASE) is not None


def first_heading(path: Path) -> str | None:
    """Le titre `# ...` du fichier s'il est unique ; sinon (titres de section en #) rien."""
    titles = [line[2:].strip() for line in path.read_text(encoding="utf-8").splitlines()
              if line.startswith("# ")]
    return titles[0] if len(titles) == 1 else None


# ----------------------------------------------------------------------------- angles

def ghosts_dir() -> Path:
    """Les ghosts sont les skills voisins de council (skills/ dans le repo, dans dist/ ou installé)."""
    return Path(os.environ.get("COUNCIL_GHOSTS_DIR") or SKILL_DIR.parent).expanduser()


def version_key(path: Path) -> tuple:
    return tuple(int(n) for n in re.findall(r"\d+", str(path)))


def angle_dirs() -> list:
    """Les dossiers où chercher les angles `ix:`, dans l'ordre ; version la plus haute d'abord."""
    raw = os.environ.get("COUNCIL_ANGLES_PATH") or DEFAULT_ANGLES_PATH
    dirs = []
    for entry in raw.split(os.pathsep):
        entry = os.path.expanduser(entry.strip())
        if not entry:
            continue
        matches = [Path(p) for p in glob.glob(entry)] if glob.has_magic(entry) else [Path(entry)]
        dirs += sorted((p for p in matches if p.is_dir()), key=version_key, reverse=True)
    return dirs


def sections(path: Path) -> dict:
    """slug -> titre, pour chaque `## Titre` du fichier."""
    return {slugify(m.group(1)): m.group(1).strip()
            for m in re.finditer(r"^##\s+(.+)$", path.read_text(encoding="utf-8"), re.MULTILINE)}


def try_resolve(kind: str, name: str) -> tuple:
    """(angle ou None, où on a cherché)."""
    if kind == "ghost":
        if name == "council":
            return None, "council ne peut pas siéger dans son propre conseil"
        path = ghosts_dir() / name / "SKILL.md"
        found = path.is_file() and name in os.listdir(ghosts_dir())
        return ({"path": str(path), "section": None, "label": first_heading(path) or name}
                if found else None), str(path)
    if kind == "ix":
        dirs = angle_dirs()
        for base in dirs:
            path = base / name / "SKILL.md"
            if path.is_file():
                return {"path": str(path), "section": None,
                        "label": first_heading(path) or name}, str(path)
        where = ", ".join(str(d) for d in dirs) or (os.environ.get("COUNCIL_ANGLES_PATH")
                                                    or DEFAULT_ANGLES_PATH) + " (aucun dossier)"
        return None, where
    if kind in SECTION_FILES:
        path = SECTION_FILES[kind]
        if not path.is_file():
            return None, str(path)
        heading = sections(path).get(slugify(name))
        return ({"path": str(path), "section": heading, "label": heading}
                if heading else None), f"{path} (sections ##)"
    if kind == "partie":
        # Une partie prenante n'a pas de bibliothèque : sa fiche s'écrit dans la séance.
        if not SEAT_ID_RE.match(name):
            return None, f"{name!r} n'est pas un id en kebab-case (ex. partie:client)"
        return {"path": PARTIES_FILE, "section": name,
                "label": name.replace("-", " ").capitalize()}, PARTIES_FILE
    if kind == "file":
        path = Path(name).expanduser()
        if path.is_dir():
            path = path / "SKILL.md"
        path = path.resolve()
        return ({"path": str(path), "section": None, "label": first_heading(path) or path.stem}
                if path.is_file() else None), str(path)
    raise CouncilError(f"préfixe {kind!r} inconnu ; utiliser {', '.join(k + ':' for k in KINDS)}")


def resolve(ref: str, bare_order=SEAT_BARE_ORDER) -> dict:
    """Résout une référence d'angle en chemin à lire. Introuvable : CouncilError explicite."""
    ref = ref.strip()
    if not ref:
        raise CouncilError("référence d'angle vide")
    kind, sep, name = ref.partition(":")
    candidates = [(kind, name)] if sep and kind in KINDS else [(k, ref) for k in bare_order]
    if sep and kind not in KINDS and len(kind) > 1:
        raise CouncilError(f"{ref!r} : préfixe {kind!r} inconnu ; utiliser "
                           f"{', '.join(k + ':' for k in KINDS)}")
    searched = []
    for kind, name in candidates:
        angle, where = try_resolve(kind, name.strip())
        if angle:
            seat_id = slugify(Path(angle["path"]).parent.name if kind == "file" else name)
            return {"ref": f"{kind}:{name.strip()}", "kind": kind, "id": seat_id, **angle}
        searched.append(f"{kind}: {where}")
    hint = ("installer ix-skills ou régler COUNCIL_ANGLES_PATH, " if any(
        k == "ix" for k, _ in candidates) else "")
    raise CouncilError(f"angle introuvable : {ref} (cherché : {'; '.join(searched)}) ; {hint}"
                       "vérifier l'orthographe ou passer file:<chemin vers un SKILL.md>")


def split_model(spec: str) -> tuple:
    """`ix:dixieme-homme@opus` -> ("ix:dixieme-homme", "opus")."""
    head, sep, tail = spec.rpartition("@")
    if not sep or "/" in tail or (spec.strip().startswith("file:")
                                  and tail.strip().lower() not in MODELS):
        return spec.strip(), None
    model = tail.strip().lower()
    if model not in MODELS:
        raise CouncilError(f"{spec!r} : modèle {tail!r} inconnu ; choisir parmi "
                           f"{', '.join(MODELS)} (sans @ : le modèle du sous-agent)")
    return head.strip(), model


def parse_seats(specs: list) -> list:
    """Chaque --seat peut porter une ou plusieurs références séparées par des virgules."""
    seats, errors = [], []
    for spec in specs:
        for part in (p for p in spec.split(",") if p.strip()):
            try:
                ref, model = split_model(part)
                seats.append({**resolve(ref), "model": model})
            except CouncilError as exc:
                errors.append(str(exc))
    if errors:
        raise CouncilError("\n".join(errors))
    return seats


def parse_arbiter(spec: str | None, fmt: dict) -> dict | None:
    rules = fmt.get("arbiter", {})
    spec = (spec or rules.get("default") or "neutre").strip()
    if spec.lower() == NO_ARBITER:
        if not rules.get("optional"):
            raise CouncilError(f"le format {fmt['name']} exige un arbitre ; --arbiter neutre, "
                               "adversarial, ghost:zeus, ghost:nash, ghost:aristote...")
        return None
    ref, model = split_model(spec)
    arbiter = resolve(ref, ARBITER_BARE_ORDER)
    if arbiter["kind"] == "partie":
        raise CouncilError(f"{ref} : une partie prenante siège, elle n'arbitre pas ; choisir "
                           "neutre, adversarial ou une méthode (ghost:, ix:, file:)")
    return {**arbiter, "model": model}


# ----------------------------------------------------------------------------- formats

STEP_KEYS = {"id", "label", "file", "template", "role", "per_seat", "repeatable", "optional",
             "requires_arbiter", "brief", "after", "reads", "fields", "expect", "require_text",
             "require_any", "forbid_fields", "justify", "headings", "mentions_all_seats",
             "names_arbiter", "tally_field", "vote", "next", "requires_parties",
             "party_cards", "counts_passes"}
ROLES = {"organisateur", "angle", "arbitre", "verificateur"}


def validate_format(fmt: dict) -> list:
    errors = []
    if not isinstance(fmt, dict) or not fmt.get("name"):
        return ["le format n'a pas de nom"]
    steps = fmt.get("steps")
    if not isinstance(steps, list) or not steps:
        return [f"le format {fmt['name']} n'a pas d'étapes"]
    ids = [s.get("id") for s in steps if isinstance(s, dict)]
    for step in steps:
        if not isinstance(step, dict):
            errors.append("une étape n'est pas un objet")
            continue
        sid = step.get("id") or "?"
        for key in ("id", "label", "file", "template", "role", "next"):
            if not step.get(key):
                errors.append(f"étape {sid} : clé {key!r} manquante")
        unknown = set(step) - STEP_KEYS
        if unknown:
            errors.append(f"étape {sid} : clés inconnues {sorted(unknown)}")
        if step.get("role") and step["role"] not in ROLES:
            errors.append(f"étape {sid} : rôle {step['role']!r} inconnu ({', '.join(sorted(ROLES))})")
        if step.get("per_seat") and "{seat}" not in step.get("file", ""):
            errors.append(f"étape {sid} : per_seat exige {{seat}} dans le nom de fichier")
        if step.get("repeatable") and "{letter}" not in step.get("file", ""):
            errors.append(f"étape {sid} : repeatable exige {{letter}} dans le nom de fichier")
        for key in ("after", "reads"):
            for dep in step.get(key, []):
                if dep not in ids:
                    errors.append(f"étape {sid} : {key} cite l'étape inconnue {dep!r}")
        if step.get("template") and not (TEMPLATE_DIR / step["template"]).is_file():
            errors.append(f"étape {sid} : gabarit {step['template']!r} absent de "
                          f"{TEMPLATE_DIR}")
        if step.get("brief") and not (BRIEF_DIR / step["brief"]).is_file():
            errors.append(f"étape {sid} : brief {step['brief']!r} absent de {BRIEF_DIR}")
    if len(set(ids)) != len(ids):
        errors.append("deux étapes portent le même id")
    return errors


def load_format(spec: str) -> dict:
    path = Path(spec).expanduser()
    if not (spec.endswith(".json") or path.is_file()):
        path = FORMATS_DIR / f"{spec}.json"
    if not path.is_file():
        known = ", ".join(sorted(p.stem for p in FORMATS_DIR.glob("*.json")))
        raise CouncilError(f"format {spec!r} introuvable ; formats livrés : {known}, ou un chemin "
                           "vers un .json")
    try:
        fmt = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CouncilError(f"{path} n'est pas du JSON valide ({exc})") from None
    errors = validate_format(fmt)
    if errors:
        raise CouncilError(f"{path} : " + "; ".join(errors))
    return fmt


# ----------------------------------------------------------------------------- séance

def load_session(folder: Path) -> dict:
    path = folder / "council.json"
    if not path.is_file():
        raise CouncilError(f"{path} introuvable ; lancer d'abord `council.py init {folder} "
                           "--title ... --seat ...`")
    try:
        session = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CouncilError(f"{path} n'est pas du JSON valide ({exc}) ; le corriger ou refaire "
                           "init dans un dossier neuf") from None
    errors = validate_format(session.get("format", {}))
    if not session.get("seats"):
        errors.append("aucun siège")
    if errors:
        raise CouncilError(f"{path} : " + "; ".join(errors))
    return session


def has_parties(session: dict) -> bool:
    return any(s.get("kind") == "partie" for s in session["seats"])


def active_steps(session: dict) -> list:
    has_arbiter = session.get("arbiter") is not None
    return [s for s in session["format"]["steps"]
            if not (s.get("requires_arbiter") and not has_arbiter)
            and not (s.get("requires_parties") and not has_parties(session))]


def get_step(session: dict, step_id: str) -> dict:
    for step in active_steps(session):
        if step["id"] == step_id:
            return step
    known = ", ".join(s["id"] for s in active_steps(session))
    raise CouncilError(f"étape {step_id!r} inconnue dans cette séance ; étapes : {known}")


def repeat_files(folder: Path, step: dict) -> list:
    prefix, _, suffix = step["file"].partition("{letter}")
    return sorted(p for p in folder.glob(prefix + "?" + suffix)
                  if p.name[len(prefix)] in string.ascii_uppercase)


def step_files(folder: Path, session: dict, step: dict) -> list:
    if step.get("per_seat"):
        return [step["file"].format(seat=s["id"]) for s in session["seats"]]
    if step.get("repeatable"):
        return [p.name for p in repeat_files(folder, step)]
    return [step["file"]]


def step_report(folder: Path, session: dict) -> list:
    report = []
    for step in active_steps(session):
        files = step_files(folder, session, step)
        states = {name: file_state(folder / name) for name in files}
        entry = {"step": step["id"], "label": step["label"], "files": files}
        if step.get("repeatable"):
            entry["state"] = ("aucun" if not files else
                              "fait" if all(v == "fait" for v in states.values()) else "à faire")
        elif step.get("per_seat"):
            done = [s["id"] for s in session["seats"]
                    if states[step["file"].format(seat=s["id"])] == "fait"]
            entry["done"] = f"{len(done)}/{len(files)}"
            entry["pending"] = [s["id"] for s in session["seats"] if s["id"] not in done]
            entry["state"] = ("fait" if not entry["pending"] else
                              "à faire" if done or any(v == "à faire" for v in states.values())
                              else "absent")
        else:
            entry["state"] = states[files[0]]
        if step.get("optional"):
            entry["optional"] = True
        report.append(entry)
    return report


def seat_line(seat: dict) -> str:
    where = seat["path"] + (f" (section « ## {seat['section']} »)" if seat.get("section") else "")
    return where


def common_values(folder: Path, session: dict) -> dict:
    arbiter = session.get("arbiter")
    roster = "\n".join(
        f"| {s['id']} | {s['label']} | `{s['ref']}` | {s.get('model') or 'défaut'} |"
        for s in session["seats"])
    return {"title": session["title"], "date": session.get("date", ""),
            "format": session["format"]["name"], "format_description":
                session["format"].get("description", ""),
            "folder": str(folder.resolve()), "seat_count": len(session["seats"]),
            "roster_table": roster,
            "seat_ids": ", ".join(s["id"] for s in session["seats"]),
            "arbiter_label": arbiter["label"] if arbiter else "aucun",
            "arbiter_ref": arbiter["ref"] if arbiter else NO_ARBITER,
            "arbiter_model": (arbiter.get("model") or "défaut") if arbiter else "-",
            "seat_rows": "\n".join(f"| {s['id']} | | | |" for s in session["seats"]),
            "seat_rows_unique": "\n".join(f"| {s['id']} | |" for s in session["seats"]),
            "party_cards": "\n".join(
                fill(load_text(TEMPLATE_DIR / "PARTIE.md", "gabarit"), {"seat_id": s["id"]})
                for s in session["seats"] if s.get("kind") == "partie").rstrip("\n")}


def seat_values(common: dict, seat: dict) -> dict:
    return {**common, "seat_id": seat["id"], "seat_label": seat["label"], "seat_ref": seat["ref"],
            "seat_model": seat.get("model") or "défaut", "seat_source": seat_line(seat)}


# ----------------------------------------------------------------------------- init

def cmd_init(args) -> dict:
    folder = Path(args.folder)
    session_path = folder / "council.json"
    created, kept, warnings = [], [], []

    if session_path.is_file():
        if args.seat or args.title or args.arbiter or args.format or args.date:
            raise CouncilError(f"{session_path} existe déjà ; le modifier à la main, ou relancer "
                               "init avec le seul dossier pour recréer les gabarits manquants")
        session = load_session(folder)
    else:
        if not args.title:
            raise CouncilError("--title est obligatoire pour une nouvelle séance, par exemple "
                               "--title \"Passer en freemium\"")
        if not args.seat:
            raise CouncilError("donner les angles avec --seat REF[@MODELE] (répéter), par exemple "
                               "--seat ghost:popper --seat ix:dixieme-homme@opus "
                               "--seat costume:humain")
        fmt = load_format(args.format or "tour")
        seats = parse_seats(args.seat)
        ids = [s["id"] for s in seats]
        errors = []
        for seat in seats:
            if not SEAT_ID_RE.match(seat["id"]):
                errors.append(f"{seat['ref']} donne l'id {seat['id']!r}, pas en kebab-case")
            elif seat["id"] in RESERVED_IDS:
                errors.append(f"{seat['ref']} donne l'id réservé {seat['id']!r} ; passer par "
                              "file:<chemin> depuis un dossier au nom différent")
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup:
            errors.append(f"angle en double : {', '.join(dup)} (règle 2 : un angle par avis)")
        bounds = fmt.get("seats", {})
        low, high = bounds.get("min", 1), bounds.get("max", 25)
        if not low <= len(seats) <= high:
            errors.append(f"le format {fmt['name']} prend {low} à {high} angles, pas {len(seats)}")
        if errors:
            raise CouncilError("; ".join(errors))
        arbiter = parse_arbiter(args.arbiter, fmt)
        session = {"schema": SCHEMA_VERSION, "title": args.title,
                   "date": args.date or _dt.date.today().isoformat(),
                   "seats": seats, "arbiter": arbiter, "format": fmt}
        folder.mkdir(parents=True, exist_ok=True)
        write_lf(session_path, json.dumps(session, indent=2, ensure_ascii=False) + "\n")
        created.append(session_path.name)

    fmt = session["format"]
    rec = fmt.get("seats", {}).get("recommended")
    if rec and not rec[0] <= len(session["seats"]) <= rec[1]:
        warnings.append(f"{len(session['seats'])} angles ; {rec[0]} à {rec[1]} recommandés pour "
                        f"le format {fmt['name']}")
    arbiter = session.get("arbiter")
    if arbiter and arbiter["ref"] in {s["ref"] for s in session["seats"]}:
        warnings.append(f"l'arbitre {arbiter['ref']} siège aussi comme angle : il jugera son "
                        "propre avis")

    common = common_values(folder, session)
    for step in active_steps(session):
        if step.get("repeatable"):
            continue
        template = load_text(TEMPLATE_DIR / step["template"], "gabarit")
        if step.get("per_seat"):
            plan = [(step["file"].format(seat=s["id"]), seat_values(common, s))
                    for s in session["seats"]]
        else:
            plan = [(step["file"], common)]
        for name, values in plan:
            path = folder / name
            if path.exists():
                kept.append(name)
                continue
            write_lf(path, fill(template, values))
            created.append(name)

    return {"ok": True, "folder": str(folder.resolve()), "created": created, "kept": kept,
            "warnings": warnings, "next": active_steps(session)[0]["next"]}


# ----------------------------------------------------------------------------- status

def cmd_status(args) -> dict:
    folder = Path(args.folder)
    session = load_session(folder)
    report = step_report(folder, session)
    steps = {s["id"]: s for s in active_steps(session)}
    by_id = {e["step"]: e for e in report}
    for entry in report:
        # Un fichier écrit mais refusé par ses contrôles (relecture « à corriger », grille non
        # validée) n'est pas une étape faite : la suite ne doit pas la proposer.
        if entry["state"] == "fait":
            errors = [p["message"] for p in step_problems(folder, session, steps[entry["step"]],
                                                          by_id) if p["severity"] == "error"]
            if errors:
                entry["state"] = "à corriger"
                entry["problems"] = errors
    next_step = "terminé ; lancer `council.py check SEANCE --final` puis restituer"
    for entry in report:
        if entry.get("optional"):
            if entry["state"] == "à faire":
                next_step = steps[entry["step"]]["next"]
                break
            continue
        if entry["state"] == "à corriger":
            next_step = f"corriger avant de continuer : {'; '.join(entry['problems'])}"
            break
        if entry["state"] != "fait":
            next_step = steps[entry["step"]]["next"]
            if entry.get("pending"):
                next_step += " (en attente : " + ", ".join(entry["pending"]) + ")"
            break
    arbiter = session.get("arbiter")
    return {"ok": True, "folder": str(folder.resolve()), "title": session["title"],
            "format": session["format"]["name"],
            "seats": [{"id": s["id"], "ref": s["ref"], "model": s.get("model")}
                      for s in session["seats"]],
            "arbiter": {"ref": arbiter["ref"], "model": arbiter.get("model")} if arbiter else None,
            "steps": report, "next": next_step}


# ----------------------------------------------------------------------------- resolve

def cmd_resolve(args) -> dict:
    order = ARBITER_BARE_ORDER if args.arbiter else SEAT_BARE_ORDER
    angles = []
    for spec in args.refs:
        ref, model = split_model(spec)
        angles.append({**resolve(ref, order), "model": model})
    return {"ok": True, "angles": angles}


# ----------------------------------------------------------------------------- brief

LAUNCH = {
    None: "sous-agent Claude Code (outil Agent), modèle par défaut du sous-agent",
    "opus": "sous-agent Claude Code (outil Agent, model: opus)",
    "sonnet": "sous-agent Claude Code (outil Agent, model: sonnet)",
    "haiku": "sous-agent Claude Code (outil Agent, model: haiku)",
    "codex": "codex exec -s read-only --ephemeral -o {file} \"$(cat BRIEF)\"",
    "gemini": "agy -p \"$(cat BRIEF)\" --sandbox > {file}",
}


def method_line(angle: dict, folder: Path) -> str:
    if angle.get("kind") == "partie":
        return (f"lis {folder / PARTIES_FILE}, uniquement la fiche « ## {angle['section']} » : "
                "tu raisonnes depuis la position de cette partie, son mandat, ce qu'elle gagne "
                "ou perd, ses priorités et ses angles morts, et seulement elle. Tu tiens ce rôle")
    if angle.get("section"):
        return (f"lis {angle['path']}, uniquement la section « ## {angle['section']} », "
                "et applique-la")
    return f"lis {angle['path']} en entier, et applique sa méthode"


def read_list(folder: Path, session: dict, step: dict) -> tuple:
    """(fichiers à lire, motifs interdits) pour le worker d'une étape."""
    steps = {s["id"]: s for s in active_steps(session)}
    reads, allowed = [], set(step.get("reads", []))
    for dep in step.get("reads", []):
        if dep not in steps:
            continue
        other = steps[dep]
        if other.get("repeatable"):
            reads.append(f"{folder / other['file'].replace('{letter}', '*')} s'il en existe "
                         "(corrections, elles priment sur le dossier)")
        elif other.get("per_seat"):
            reads += [str(folder / n) for n in step_files(folder, session, other)]
        else:
            reads.append(str(folder / other["file"]))
    forbidden = [s["file"].replace("{seat}", "*").replace("{letter}", "*")
                 for s in active_steps(session) if s["id"] not in allowed and s is not step]
    if step.get("per_seat"):
        forbidden.insert(0, step["file"].replace("{seat}", "*") + " (sauf le tien)")
    if step.get("role") == "angle":
        forbidden.append("council.json")
    return reads, forbidden


def cmd_brief(args) -> dict:
    folder = Path(args.folder).resolve()
    session = load_session(folder)
    step = get_step(session, args.step)
    if not step.get("brief"):
        raise CouncilError(f"l'étape {step['id']} est tenue par l'organisateur : pas de brief")
    report = {e["step"]: e for e in step_report(folder, session)}
    waiting = [d for d in step.get("after", []) if d in report
               and not report[d].get("optional") and report[d]["state"] != "fait"]
    if waiting:
        raise CouncilError(f"trop tôt pour {step['id']} : d'abord {', '.join(waiting)} "
                           "(voir `council.py status`)")
    steps = {s["id"]: s for s in active_steps(session)}
    # Toute la chaîne en amont, pas seulement l'étape précédente : une grille non validée
    # bloque le tour même si la relecture, entre les deux, est passée.
    upstream, todo = [], list(step.get("after", []))
    while todo:
        dep = todo.pop()
        if dep in steps and dep not in upstream:
            upstream.append(dep)
            todo += steps[dep].get("after", [])
    blocking = [p for dep in upstream
                for p in step_problems(folder, session, steps[dep], report)
                if p["severity"] == "error"]
    if blocking:
        raise CouncilError(f"trop tôt pour {step['id']} : "
                           + "; ".join(f"{p['file']} : {p['message']}" for p in blocking))

    if step.get("per_seat"):
        if not args.seat:
            raise CouncilError(f"l'étape {step['id']} se joue par angle ; préciser lequel : "
                               + ", ".join(s["id"] for s in session["seats"]))
        match = [s for s in session["seats"] if s["id"] == args.seat]
        if not match:
            raise CouncilError(f"angle {args.seat!r} absent de la séance : "
                               + ", ".join(s["id"] for s in session["seats"]))
        angle = match[0]
        target = step["file"].format(seat=angle["id"])
    elif step["role"] == "arbitre":
        angle = session.get("arbiter")
        target = step["file"]
    else:
        angle = None
        target = step["file"]

    if angle and angle.get("kind") != "partie" and not Path(angle["path"]).is_file():
        # Le cache d'un plugin change de dossier à chaque mise à jour : on résout à nouveau.
        try:
            fresh = resolve(angle["ref"], ARBITER_BARE_ORDER if step["role"] == "arbitre"
                            else SEAT_BARE_ORDER)
        except CouncilError as exc:
            raise CouncilError(f"la méthode de {angle['ref']} a disparu ({angle['path']}) : "
                               f"{exc}") from None
        angle["path"] = fresh["path"]
        write_lf(folder / "council.json", json.dumps(session, indent=2, ensure_ascii=False) + "\n")

    if step.get("counts_passes"):
        passes = session.setdefault("passes", {})
        passes[step["id"]] = passes.get(step["id"], 0) + 1
        write_lf(folder / "council.json", json.dumps(session, indent=2, ensure_ascii=False) + "\n")

    model = angle.get("model") if angle else None
    path = folder / target
    reads, forbidden = read_list(folder, session, step)
    if angle and angle.get("kind") == "partie":
        forbidden = [f"{f} (sauf ta fiche)" if f == PARTIES_FILE else f for f in forbidden]
    if model in EXTERNAL_MODELS:
        stub = path.read_text(encoding="utf-8") if path.is_file() else ""
        write = ("Tu ne peux pas écrire de fichier. Rends sur la sortie standard, et rien "
                 f"d'autre, le contenu complet de {path.name} : garde les titres du gabarit "
                 "ci-dessous, supprime la ligne `<!-- council:todo -->`, remplis chaque champ.\n\n"
                 f"Gabarit :\n\n{stub}")
    else:
        write = (f"Écris {path} en remplaçant le gabarit : garde ses titres, supprime la ligne "
                 "`<!-- council:todo -->`, remplis chaque champ. Puis réponds en une ligne : "
                 "ta position principale et le chemin écrit.")
    values = {**common_values(folder, session),
              "step": step["id"], "step_label": step["label"], "target": str(path),
              "reads": "\n".join(f"{i}. {r}" for i, r in enumerate(reads, 1)) or "(rien)",
              "forbidden": ", ".join(forbidden) or "(rien)",
              "write": write,
              "angle_label": angle["label"] if angle else "",
              "angle_ref": angle["ref"] if angle else "",
              "method": method_line(angle, folder) if angle else ""}
    text = fill(load_text(BRIEF_DIR / step["brief"], "brief"), values).rstrip("\n") + "\n"
    leftover = re.findall(r"\{\{[a-z_]+\}\}", text)
    if leftover:
        raise CouncilError(f"brief {step['brief']} : variables inconnues {sorted(set(leftover))}")
    return {"ok": True, "step": step["id"], "seat": angle["id"] if angle and step.get("per_seat")
            else None, "target": str(path), "model": model,
            "launch": LAUNCH[model].format(file=path), "brief": text}


# ----------------------------------------------------------------------------- addendum

def cmd_addendum(args) -> dict:
    folder = Path(args.folder)
    session = load_session(folder)
    steps = [s for s in active_steps(session) if s.get("repeatable")]
    if not steps:
        raise CouncilError(f"le format {session['format']['name']} n'a pas d'addenda ; "
                           "ils existent en format deliberation")
    step = steps[0]
    existing = repeat_files(folder, step)
    last_item = 0
    for path in existing:
        for match in re.finditer(r"^##\s+(\d+)\.", path.read_text(encoding="utf-8"), re.MULTILINE):
            last_item = max(last_item, int(match.group(1)))
    prefix = step["file"].partition("{letter}")[0]
    letters = [p.name[len(prefix)] for p in existing]
    if letters and letters[-1] == "Z":
        raise CouncilError("26 addenda existent déjà ; les fondre dans un nouveau dossier")
    letter = string.ascii_uppercase[string.ascii_uppercase.index(letters[-1]) + 1] \
        if letters else "A"
    path = folder / step["file"].format(letter=letter)
    text = fill(load_text(TEMPLATE_DIR / step["template"], "gabarit"),
                {**common_values(folder, session), "letter": letter,
                 "first_item": last_item + 1})
    write_lf(path, text)
    return {"ok": True, "created": path.name, "next_item": last_item + 1}


# ----------------------------------------------------------------------------- tally

def cmd_tally(args) -> dict:
    folder = Path(args.folder)
    session = load_session(folder)
    candidates = [s for s in active_steps(session) if s.get("per_seat") and s.get("tally_field")]
    if args.step:
        step = get_step(session, args.step)
        if not step.get("tally_field"):
            raise CouncilError(f"l'étape {step['id']} n'a rien à compter")
    elif len(candidates) == 1:
        step = candidates[0]
    else:
        raise CouncilError("préciser l'étape avec --step : "
                           + ", ".join(s["id"] for s in candidates))
    field = step["tally_field"]
    rows, missing = [], []
    for seat in session["seats"]:
        path = folder / step["file"].format(seat=seat["id"])
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        value = read_field(text, field) if file_state(path) == "fait" else None
        if value is None:
            missing.append(seat["id"])
            continue
        row = {"seat": seat["id"], "ref": seat["ref"], "value": value,
               "confidence": read_field(text, "Confiance") or "?"}
        if step.get("vote"):
            match = re.match(r"^(?:[Oo]ption\s+)?\**([A-Z])\b", value)
            row["option"] = match.group(1) if match else "Autre"
            if match and re.search(r"\b(?:ou|or|et)\s+(?:l'option\s+|option\s+)?[A-Z]\b",
                                   value[match.end():]):
                row["option"] = "Ambigu"
            justify = step.get("justify", {})
            row["changed"] = read_field(text, justify.get("field", "")) or "?" if justify else "-"
        rows.append(row)

    n = len(session["seats"])
    result = {"ok": not missing, "step": step["id"], "seats": n, "reported": len(rows),
              "missing": missing, "rows": rows}
    lines = [f"| Angle | {field} | Confiance |", "|---|---|---|"]
    lines += [f"| {r['seat']} | {r['value']} | {r['confidence']} |" for r in rows]
    if step.get("vote"):
        totals = {}
        for r in rows:
            entry = totals.setdefault(r["option"], {"option": r["option"], "seats": []})
            entry["seats"].append(r["seat"])
        ordered = sorted(totals.values(), key=lambda t: (-len(t["seats"]), t["option"]))
        result["totals"] = ordered
        result["changed"] = [r["seat"] for r in rows if fold(r["changed"]).startswith("oui")]
        lines += ["", "| Option | Angles | Voix |", "|---|---|---:|"]
        lines += [f"| {t['option']} | {', '.join(t['seats'])} | {len(t['seats'])} sur {n} |"
                  for t in ordered]
        if result["changed"]:
            lines.append(f"\nOnt changé de position : {', '.join(result['changed'])}.")
    lines += ["", f"Rendus : {len(rows)} sur {n} angles."]
    if missing:
        lines.append(f"INCOMPLET : pas de ligne **{field} :** remplie chez {', '.join(missing)}. "
                     "Ne pas faire le bilan avant que chaque angle ait rendu.")
    result["markdown"] = "\n".join(lines)
    return result


# ----------------------------------------------------------------------------- check

def waived(folder: Path, session: dict, rule: dict | None) -> bool:
    """Vrai si le décideur a levé ce contrôle par une ligne d'un autre fichier de la séance."""
    if not rule:
        return False
    steps = {s["id"]: s for s in active_steps(session)}
    other = steps.get(rule["step"])
    path = folder / other["file"] if other else None
    if not path or file_state(path) != "fait":
        return False
    value = read_field(path.read_text(encoding="utf-8"), rule["field"])
    if not value or fold(value).startswith("non"):
        return False
    passes = session.get("passes", {}).get(rule.get("passes_of", ""), 0)
    return passes >= rule.get("min_passes", 0)


def step_problems(folder: Path, session: dict, step: dict, report: dict) -> list:
    """Les problèmes d'une étape : ordre des étapes et contenu de ses fichiers écrits."""
    problems = []
    seat_ids = [s["id"] for s in session["seats"]]
    arbiter = session.get("arbiter")

    def problem(severity, where, message):
        problems.append({"severity": severity, "file": where, "message": message})

    entry = report[step["id"]]
    done_files = [n for n in entry["files"] if file_state(folder / n) == "fait"]

    if done_files:
        for dep in step.get("after", []):
            dep_entry = report.get(dep)
            if dep_entry and not dep_entry.get("optional") and dep_entry["state"] != "fait":
                pending = dep_entry.get("pending")
                problem("error", done_files[0],
                        f"écrit avant que l'étape {dep} soit complète"
                        + (f" (en attente : {', '.join(pending)})" if pending else ""))

    for name in done_files:
        text = (folder / name).read_text(encoding="utf-8")
        for field in step.get("fields", []):
            if read_field(text, field) is None:
                problem("error", name, f"ligne **{field} :** absente ou non remplie")
        for rule in step.get("expect", []):
            value = read_field(text, rule["field"])
            if value is not None and not fold(value).startswith(fold(rule["starts_with"])) \
                    and not waived(folder, session, rule.get("waived_by")):
                problem(rule.get("severity", "error"), name, rule["message"])
        for rule in step.get("require_text", []):
            if not re.search(rule["pattern"], text, re.MULTILINE | re.IGNORECASE):
                problem(rule.get("severity", "warning"), name, rule["message"])
        rule = step.get("require_any")
        if rule and not any(v in text for v in rule["values"]):
            problem("error", name, rule["message"])
        for field in step.get("forbid_fields", []):
            if has_field_line(text, field):
                problem("error", name, f"porte une ligne **{field} :** ; ce fichier ne "
                                       "contient que des corrections, jamais un avis ou un vote")
        rule = step.get("justify")
        if rule:
            value = read_field(text, rule["field"]) or ""
            reason = value.strip()[len(rule["if_starts"]):].strip(" :,;-.")
            if fold(value).startswith(fold(rule["if_starts"])) and \
                    len(reason.split()) < rule.get("min_words", 3):
                problem("error", name, rule["message"])
        if step.get("headings"):
            found = [fold(h) for h in re.findall(r"^##\s+(?:\d+\.\s*)?(.+)$", text,
                                                 re.MULTILINE)]
            for wanted in step["headings"]:
                if not any(fold(wanted) in h for h in found):
                    problem("error", name, f"pas de section « {wanted} »")
        if step.get("mentions_all_seats"):
            absent = [i for i in seat_ids
                      if not re.search(rf"^\|\s*{re.escape(i)}\s*\|", text, re.MULTILINE)]
            if absent:
                problem("error", name, f"angles sans ligne de tableau : {', '.join(absent)}")
        if step.get("party_cards"):
            cards = re.split(r"^##\s+", text, flags=re.MULTILINE)
            by_id = {c.split("\n", 1)[0].strip(): c for c in cards[1:]}
            for seat in session["seats"]:
                if seat.get("kind") != "partie":
                    continue
                card = by_id.get(seat["id"])
                if card is None:
                    problem("error", name, f"pas de fiche « ## {seat['id']} »")
                elif PLACEHOLDER_RE.search(card):
                    problem("error", name, f"la fiche « ## {seat['id']} » n'est pas remplie")
        if step.get("names_arbiter") and arbiter:
            named = read_field(text, "Arbitre") or ""
            tokens = {fold(arbiter["label"]), fold(arbiter["ref"].split(":", 1)[1])}
            if named and not any(t in fold(named) for t in tokens):
                problem("warning", name, f"la ligne **Arbitre :** ne nomme pas l'arbitre de "
                                         f"la séance ({arbiter['ref']})")
    return problems


def cmd_check(args) -> dict:
    folder = Path(args.folder)
    session = load_session(folder)
    problems = []
    report = {e["step"]: e for e in step_report(folder, session)}

    for path in sorted(folder.glob("*.md")):
        if file_state(path) == "fait":
            leftover = PLACEHOLDER_RE.findall(path.read_text(encoding="utf-8"))
            if leftover:
                problems.append({"severity": "warning", "file": path.name,
                                 "message": f"{len(leftover)} champ(s) de gabarit non rempli(s), "
                                            f"le premier : {leftover[0]}"})

    for step in active_steps(session):
        problems += step_problems(folder, session, step, report)

    incomplete = [sid for sid, e in report.items()
                  if not e.get("optional") and e["state"] != "fait"]
    if args.final:
        for sid in incomplete:
            problems.append({"severity": "error", "file": sid, "message": "étape incomplète"})

    errors = [p for p in problems if p["severity"] == "error"]
    return {"ok": not errors, "folder": str(folder.resolve()), "incomplete": incomplete,
            "problems": problems}


# ----------------------------------------------------------------------------- main

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="council.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="crée la séance et ses gabarits",
                       description="Crée SEANCE avec council.json et un gabarit par fichier du "
                                   "format. N'écrase jamais : relancé sur une séance existante, "
                                   "init ne fait qu'ajouter les gabarits manquants.")
    p.add_argument("folder", metavar="SEANCE", help="dossier de la séance")
    p.add_argument("--title", help="la décision en quelques mots (nouvelle séance)")
    p.add_argument("--format", help="tour (défaut), compare, deliberation, ou un chemin .json")
    p.add_argument("--seat", action="append", metavar="REF[@MODELE]",
                   help="un angle : ghost:popper, ix:dixieme-homme, costume:humain, "
                        "file:<chemin> ; @opus|sonnet|haiku|codex|gemini en option. Répéter, ou "
                        "séparer par des virgules")
    p.add_argument("--arbiter", metavar="REF[@MODELE]",
                   help="neutre (défaut), adversarial, ghost:zeus, ghost:nash, ghost:aristote, "
                        "toute autre référence ; « aucun » si le format le permet")
    p.add_argument("--date", help="date de la séance, AAAA-MM-JJ (défaut : aujourd'hui)")

    p = sub.add_parser("status", help="l'état de chaque étape et la suite")
    p.add_argument("folder", metavar="SEANCE")

    p = sub.add_parser("resolve", help="le chemin à lire pour des références d'angles",
                       description="Résout chaque référence en chemin. Sans préfixe, cherche "
                                   "ghost:, puis costume:, puis ix: (avec --arbiter : arbitre:, "
                                   "ghost:, ix:). Les angles ix: sont cherchés dans "
                                   "COUNCIL_ANGLES_PATH (défaut " + DEFAULT_ANGLES_PATH + ").")
    p.add_argument("refs", nargs="+", metavar="REF")
    p.add_argument("--arbiter", action="store_true", help="ordre de recherche d'un arbitre")

    p = sub.add_parser("brief", help="le brief d'un angle, de l'arbitre ou du vérificateur",
                       description="Écrit le brief à donner tel quel au worker d'une étape : le "
                                   "chemin de sa méthode, les fichiers à lire et ceux à ne pas "
                                   "ouvrir, le fichier à écrire. Refuse si l'étape précédente "
                                   "n'est pas finie.")
    p.add_argument("folder", metavar="SEANCE")
    p.add_argument("step", metavar="ETAPE")
    p.add_argument("seat", metavar="ANGLE", nargs="?", help="l'angle, pour une étape par angle")

    p = sub.add_parser("addendum", help="crée le prochain ADDENDUM-<lettre>.md")
    p.add_argument("folder", metavar="SEANCE")

    p = sub.add_parser("tally", help="les positions d'une étape ou le décompte des votes",
                       description="Tableau des positions d'une étape par angle, ou décompte des "
                                   "votes par option. Sort 3 si un angle n'a pas rendu : un "
                                   "décompte partiel n'est pas un décompte.")
    p.add_argument("folder", metavar="SEANCE")
    p.add_argument("--step", metavar="ETAPE")

    p = sub.add_parser("check", help="contrôle la séance contre les règles du format",
                       description="Contrôle ce qui est écrit : champs obligatoires, ordre des "
                                   "étapes, arbitre nommé, aucun vote dans un addendum, vote "
                                   "changé justifié, sections de la synthèse. --final exige en "
                                   "plus que toutes les étapes soient faites. Sort 3 sur erreur.")
    p.add_argument("folder", metavar="SEANCE")
    p.add_argument("--final", action="store_true", help="exiger que toutes les étapes soient faites")

    for sp in sub.choices.values():
        sp.add_argument("--json", action="store_true", help="une ligne JSON au lieu du texte")
    return parser


def render_text(command: str, result: dict) -> str:
    if command == "init":
        lines = [f"créé  {n}" for n in result["created"]] + [f"gardé {n}" for n in result["kept"]]
        lines += [f"attention : {w}" for w in result["warnings"]]
        lines.append(f"suite : {result['next']}")
    elif command == "status":
        arb = result["arbiter"]
        lines = [f"{result['title']} — format {result['format']} ({result['folder']})",
                 "angles : " + ", ".join(f"{s['ref']}@{s['model'] or 'défaut'}"
                                         for s in result["seats"]),
                 f"arbitre : {arb['ref'] + '@' + (arb['model'] or 'défaut') if arb else 'aucun'}"]
        for s in result["steps"]:
            extra = f" {s['done']}" if "done" in s else ""
            files = ", ".join(s["files"]) if s["files"] else "-"
            lines.append(f"  {s['step']:<14}{s['state']:<9}{extra:<6} {files}")
        lines.append(f"suite : {result['next']}")
    elif command == "resolve":
        lines = [f"{a['ref']}\t{a['path']}" + (f"\t## {a['section']}" if a["section"] else "")
                 for a in result["angles"]]
    elif command == "brief":
        lines = [result["brief"].rstrip("\n")]
    elif command == "addendum":
        lines = [f"créé {result['created']}", f"numéroter le premier point {result['next_item']}"]
    elif command == "tally":
        lines = [result["markdown"]]
    else:
        lines = [f"{p['severity']}: {p['file']}: {p['message']}" for p in result["problems"]]
        if result["incomplete"]:
            lines.append("étapes incomplètes : " + ", ".join(result["incomplete"]))
        lines.append("ok" if result["ok"] else "problèmes trouvés")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {"init": cmd_init, "status": cmd_status, "resolve": cmd_resolve,
                "brief": cmd_brief, "addendum": cmd_addendum, "tally": cmd_tally,
                "check": cmd_check}
    try:
        result = handlers[args.command](args)
    except CouncilError as exc:
        if getattr(args, "json", False):
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        else:
            print(f"erreur : {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(render_text(args.command, result))
    return 0 if result.get("ok", True) else 3


if __name__ == "__main__":
    sys.exit(main())
