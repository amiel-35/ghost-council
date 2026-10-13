"""Tests de council.py : résolution d'angles, formats, init, status, brief, tally, check.

Les angles ix: viennent d'un faux cache (fixture ix_cache) ; les ghosts sont ceux du repo.
Adapté de tests/test_council.py d'advisory-council 0.2.1 (nzanepro, MIT).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from conftest import (
    SEAT_IDS,
    SEATS,
    SKILL_DIR,
    build_deliberation,
    build_tour,
    fill,
    fill_avis,
    fill_cadrage,
    fill_vote,
    init_session,
    make_ix,
    run_json,
)

FORMATS = sorted(p.stem for p in (SKILL_DIR / "references" / "formats").glob("*.json"))


# --------------------------------------------------------------------------- outils

def test_slugify_strips_accents(council):
    assert council.slugify("Dixième homme !") == "dixieme-homme"


def test_fold_normalises_apostrophes_and_accents(council):
    assert council.fold("Ce qu’aucun angle n’a regardé") == "ce qu'aucun angle n'a regarde"


@pytest.mark.parametrize("line", ["**Position :** oui", "**Position:** oui",
                                  "**Position :** oui", "**position :** oui"])
def test_read_field_tolerates_space_before_colon(council, line):
    assert council.read_field(line + "\n", "Position") == "oui"


def test_read_field_ignores_unfilled_placeholder(council):
    assert council.read_field("**Position :** <une ligne, tranchée>\n", "Position") is None


class TestSplitModel:
    def test_no_model(self, council):
        assert council.split_model("ghost:popper") == ("ghost:popper", None)

    @pytest.mark.parametrize("model", ["opus", "sonnet", "haiku", "codex", "gemini"])
    def test_known_models(self, council, model):
        assert council.split_model(f"ix:red-team@{model}") == ("ix:red-team", model)

    def test_fable_is_not_a_seat_model(self, council):
        with pytest.raises(council.CouncilError, match="modèle 'fable' inconnu"):
            council.split_model("ghost:popper@fable")

    def test_unknown_model(self, council):
        with pytest.raises(council.CouncilError, match="inconnu"):
            council.split_model("ghost:popper@gpt9")

    def test_at_sign_inside_a_path_is_not_a_model(self, council):
        assert council.split_model("file:/tmp/a@b/c") == ("file:/tmp/a@b/c", None)


# --------------------------------------------------------------------------- résolution

class TestResolve:
    def test_ghost(self, council):
        angle = council.resolve("ghost:popper")
        assert angle["kind"] == "ghost" and angle["id"] == "popper"
        assert Path(angle["path"]) == SKILL_DIR.parent / "popper" / "SKILL.md"
        assert angle["section"] is None

    def test_ghost_missing(self, council):
        with pytest.raises(council.CouncilError, match="angle introuvable : ghost:nobody"):
            council.resolve("ghost:nobody")

    def test_council_cannot_sit_in_its_own_council(self, council):
        with pytest.raises(council.CouncilError, match="introuvable"):
            council.resolve("ghost:council")

    def test_ghosts_dir_override(self, council, tmp_path, monkeypatch):
        (tmp_path / "g" / "x").mkdir(parents=True)
        (tmp_path / "g" / "x" / "SKILL.md").write_text("# X\n", encoding="utf-8")
        monkeypatch.setenv("COUNCIL_GHOSTS_DIR", str(tmp_path / "g"))
        assert council.resolve("ghost:x")["label"] == "X"

    def test_ix_takes_highest_version(self, council, ix_cache):
        angle = council.resolve("ix:dixieme-homme")
        assert "/3.10.0/" in angle["path"]
        assert angle["kind"] == "ix" and angle["id"] == "dixieme-homme"

    def test_ix_falls_back_to_older_version(self, council):
        assert "/3.9.0/" in council.resolve("ix:seulement-ancienne")["path"]

    def test_ix_path_entries_keep_their_order(self, council, tmp_path, monkeypatch):
        first = make_ix(tmp_path / "a", "1.0.0", "contrarian")
        second = make_ix(tmp_path / "b", "9.0.0", "contrarian")
        monkeypatch.setenv("COUNCIL_ANGLES_PATH", f"{first}:{second}")
        assert council.resolve("ix:contrarian")["path"].startswith(str(first))

    def test_ix_missing_says_where_and_what_to_do(self, council):
        with pytest.raises(council.CouncilError) as exc:
            council.resolve("ix:nexiste-pas")
        assert "COUNCIL_ANGLES_PATH" in str(exc.value)
        assert "3.10.0" in str(exc.value)

    def test_ix_with_no_cache_at_all(self, council, monkeypatch, tmp_path):
        monkeypatch.setenv("COUNCIL_ANGLES_PATH", str(tmp_path / "rien" / "*"))
        with pytest.raises(council.CouncilError, match="aucun dossier"):
            council.resolve("ix:contrarian")

    def test_costume_section(self, council):
        angle = council.resolve("costume:humain")
        assert angle["section"] == "Humain"
        assert angle["path"].endswith("references/angles/costumes.md")

    def test_costume_missing(self, council):
        with pytest.raises(council.CouncilError, match="costume:astrologue"):
            council.resolve("costume:astrologue")

    def test_every_costume_resolves(self, council):
        for name in ("financier", "commercial", "produit", "marque", "technique", "humain",
                     "juridique"):
            assert council.resolve(f"costume:{name}")["kind"] == "costume"

    def test_file_dir_or_skill(self, council):
        by_dir = council.resolve(f"file:{SKILL_DIR.parent / 'kant'}")
        by_file = council.resolve(f"file:{SKILL_DIR.parent / 'kant' / 'SKILL.md'}")
        assert by_dir["path"] == by_file["path"]
        assert by_dir["id"] == "kant"

    def test_file_missing(self, council, tmp_path):
        with pytest.raises(council.CouncilError, match="introuvable"):
            council.resolve(f"file:{tmp_path / 'absent.md'}")

    def test_unknown_prefix(self, council):
        with pytest.raises(council.CouncilError, match="préfixe 'zz' inconnu"):
            council.resolve("zz:popper")

    @pytest.mark.parametrize("bare,kind", [("popper", "ghost"), ("humain", "costume"),
                                           ("contrarian", "ix")])
    def test_bare_names_search_ghost_costume_ix(self, council, bare, kind):
        assert council.resolve(bare)["kind"] == kind

    def test_bare_arbiter_prefers_builtin_arbiters(self, council):
        assert council.resolve("neutre", council.ARBITER_BARE_ORDER)["kind"] == "arbitre"
        assert council.resolve("zeus", council.ARBITER_BARE_ORDER)["kind"] == "ghost"

    def test_resolve_command(self, run):
        code, data = run_json(run, ["resolve", "ghost:popper", "ix:contrarian@haiku",
                                    "costume:humain"])
        assert code == 0
        assert [a["kind"] for a in data["angles"]] == ["ghost", "ix", "costume"]
        assert data["angles"][1]["model"] == "haiku"

    def test_resolve_command_missing_exits_1(self, run):
        code, data = run_json(run, ["resolve", "ix:nexiste-pas"])
        assert code == 1 and "introuvable" in data["error"]


# --------------------------------------------------------------------------- formats

@pytest.mark.parametrize("name", FORMATS)
def test_shipped_formats_are_valid(council, name):
    fmt = council.load_format(name)
    assert council.validate_format(fmt) == []
    for step in fmt["steps"]:
        assert (council.TEMPLATE_DIR / step["template"]).is_file(), step["template"]
        if step.get("brief"):
            assert (council.BRIEF_DIR / step["brief"]).is_file(), step["brief"]


def test_formats_shipped(council):
    assert FORMATS == ["compare", "deliberation", "tour"]


def test_validate_format_catches_unknown_dependency(council):
    fmt = council.load_format("tour")
    fmt["steps"][1]["after"] = ["nulle-part"]
    assert any("nulle-part" in e for e in council.validate_format(fmt))


def test_custom_format_by_path(run, tmp_path, council):
    fmt = json.loads((SKILL_DIR / "references" / "formats" / "tour.json").read_text("utf-8"))
    fmt["name"] = "maison"
    fmt["steps"] = fmt["steps"][:2]
    path = tmp_path / "maison.json"
    path.write_text(json.dumps(fmt), encoding="utf-8")
    folder = init_session(run, tmp_path, fmt=str(path))
    assert not (folder / "SYNTHESE.md").exists()
    assert json.loads((folder / "council.json").read_text("utf-8"))["format"]["name"] == "maison"


def test_unknown_format(run, tmp_path):
    code, data = run_json(run, ["init", tmp_path / "s", "--title", "x", "--seat", "popper",
                                "--seat", "kant", "--format", "conclave"])
    assert code == 1 and "compare, deliberation, tour" in data["error"]


# --------------------------------------------------------------------------- init

class TestInit:
    def test_tour_creates_stubs(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        names = {p.name for p in folder.iterdir()}
        assert names == {"council.json", "CADRAGE.md", "SYNTHESE.md",
                         *(f"AVIS-{i}.md" for i in SEAT_IDS)}
        for name in names - {"council.json"}:
            assert "<!-- council:todo -->" in (folder / name).read_text("utf-8")

    def test_session_records_paths_models_and_format(self, run, tmp_path):
        folder = init_session(run, tmp_path, seats=["ghost:popper@codex", "ix:dixieme-homme@opus",
                                                    "costume:humain"])
        session = json.loads((folder / "council.json").read_text("utf-8"))
        assert [s["model"] for s in session["seats"]] == ["codex", "opus", None]
        assert session["seats"][2]["section"] == "Humain"
        assert session["arbiter"]["ref"] == "arbitre:neutre"
        assert session["format"]["name"] == "tour"

    def test_cadrage_lists_the_grid_and_the_arbiter(self, run, tmp_path):
        folder = init_session(run, tmp_path, arbiter="ghost:zeus@sonnet")
        text = (folder / "CADRAGE.md").read_text("utf-8")
        for ref in SEATS:
            assert f"`{ref}`" in text
        assert "`ghost:zeus`, modèle sonnet" in text

    def test_comma_separated_seats(self, run, tmp_path):
        folder = init_session(run, tmp_path, seats=[",".join(SEATS)])
        assert all((folder / f"AVIS-{i}.md").exists() for i in SEAT_IDS)

    def test_missing_angle_fails_before_creating_anything(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x",
                                    "--seat", "ghost:popper", "--seat", "ix:inconnu",
                                    "--seat", "ghost:inconnu"])
        assert code == 1
        assert "ix:inconnu" in data["error"] and "ghost:inconnu" in data["error"]
        assert not (tmp_path / "s").exists()

    def test_duplicate_angle(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x", "--seat", "popper",
                                    "--seat", "ghost:popper@opus", "--seat", "kant"])
        assert code == 1 and "en double" in data["error"]

    def test_seat_bounds(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x", "--seat", "popper",
                                    "--format", "deliberation"])
        assert code == 1 and "3 à 9" in data["error"]

    def test_compare_takes_exactly_two(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x",
                                    "--seat", "popper", "--seat", "hegel", "--seat", "kant",
                                    "--format", "compare"])
        assert code == 1 and "2 à 2" in data["error"]

    def test_compare_without_arbiter_drops_divergence(self, run, tmp_path):
        folder = init_session(run, tmp_path, seats=["popper", "hegel"], fmt="compare",
                              arbiter="aucun")
        assert not (folder / "DIVERGENCE.md").exists()
        assert (folder / "AVIS-hegel.md").exists()

    def test_compare_with_default_arbiter_has_divergence(self, run, tmp_path):
        folder = init_session(run, tmp_path, seats=["popper", "hegel"], fmt="compare")
        assert (folder / "DIVERGENCE.md").exists()

    def test_tour_requires_an_arbiter(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x", "--seat", "popper",
                                    "--seat", "kant", "--arbiter", "aucun"])
        assert code == 1 and "exige un arbitre" in data["error"]

    def test_never_overwrites_and_recreates_missing(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        (folder / "CADRAGE.md").write_text("mon cadrage\n", encoding="utf-8")
        (folder / "SYNTHESE.md").unlink()
        code, data = run_json(run, ["init", folder])
        assert code == 0
        assert data["created"] == ["SYNTHESE.md"]
        assert (folder / "CADRAGE.md").read_text("utf-8") == "mon cadrage\n"

    def test_existing_session_refuses_new_seats(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        code, data = run_json(run, ["init", folder, "--seat", "kant"])
        assert code == 1 and "existe déjà" in data["error"]

    def test_warns_when_arbiter_also_sits(self, run, tmp_path):
        code, data = run_json(run, ["init", tmp_path / "s", "--title", "x", "--seat", "zeus",
                                    "--seat", "kant", "--seat", "popper", "--arbiter", "zeus"])
        assert code == 0 and any("siège aussi" in w for w in data["warnings"])

    def test_deliberation_stubs(self, run, tmp_path):
        folder = init_session(run, tmp_path, fmt="deliberation")
        names = {p.name for p in folder.iterdir()}
        assert {"DOSSIER.md", "VERIFICATION.md", "BILAN-TOUR1.md", "SYNTHESE.md"} <= names
        assert {f"TOUR1-{i}.md" for i in SEAT_IDS} <= names
        assert {f"TOUR2-{i}.md" for i in SEAT_IDS} <= names
        assert not any(n.startswith("ADDENDUM") for n in names)


# --------------------------------------------------------------------------- status

def test_status_walks_the_format(run, tmp_path):
    folder = init_session(run, tmp_path)
    _, data = run_json(run, ["status", folder])
    assert data["next"].startswith("remplir CADRAGE.md")
    fill_cadrage(folder)
    fill_avis(folder, "popper")
    _, data = run_json(run, ["status", folder])
    assert "en attente : dixieme-homme, humain" in data["next"]
    avis = next(s for s in data["steps"] if s["step"] == "avis")
    assert avis["done"] == "1/3" and avis["state"] == "à faire"


def test_status_on_missing_session(run, tmp_path):
    code, data = run_json(run, ["status", tmp_path / "rien"])
    assert code == 1 and "init" in data["error"]


# --------------------------------------------------------------------------- brief

class TestBrief:
    def test_too_early(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        code, data = run_json(run, ["brief", folder, "avis", "popper"])
        assert code == 1 and "d'abord cadrage" in data["error"]

    def test_angle_brief_gives_path_reads_and_forbidden(self, run, tmp_path, ix_cache):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        code, data = run_json(run, ["brief", folder, "avis", "dixieme-homme"])
        assert code == 0
        brief = data["brief"]
        assert str(ix_cache / "3.10.0" / "skills" / "dixieme-homme" / "SKILL.md") in brief
        assert str(folder.resolve() / "CADRAGE.md") in brief
        assert "AVIS-*.md (sauf le tien)" in brief
        assert str(folder.resolve() / "AVIS-dixieme-homme.md") in brief
        assert "{{" not in brief
        assert "Sources à consulter" in brief
        assert data["model"] is None and "sous-agent" in data["launch"]

    def test_relative_session_path_gives_absolute_paths(self, run, tmp_path, monkeypatch):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        monkeypatch.chdir(tmp_path)
        _, data = run_json(run, ["brief", "seance", "avis", "popper"])
        assert str(folder.resolve() / "CADRAGE.md") in data["brief"]
        assert data["target"] == str(folder.resolve() / "AVIS-popper.md")

    def test_costume_brief_names_its_section(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        _, data = run_json(run, ["brief", folder, "avis", "humain"])
        assert "uniquement la section « ## Humain »" in data["brief"]

    def test_external_model_returns_stdout_brief(self, run, tmp_path):
        folder = init_session(run, tmp_path, seats=["ghost:popper@codex", "kant", "humain"])
        fill_cadrage(folder)
        _, data = run_json(run, ["brief", folder, "avis", "popper"])
        assert "sortie standard" in data["brief"] and "Gabarit" in data["brief"]
        assert data["launch"].startswith("codex exec -s read-only --ephemeral -o ")

    def test_per_seat_step_needs_a_seat(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        code, data = run_json(run, ["brief", folder, "avis"])
        assert code == 1 and "popper" in data["error"]

    def test_unknown_seat(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        code, data = run_json(run, ["brief", folder, "avis", "kant"])
        assert code == 1 and "absent" in data["error"]

    def test_organizer_step_has_no_brief(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        code, data = run_json(run, ["brief", folder, "cadrage"])
        assert code == 1 and "organisateur" in data["error"]

    def test_arbiter_brief_reads_every_avis(self, run, tmp_path):
        folder = init_session(run, tmp_path, arbiter="ghost:zeus@opus")
        fill_cadrage(folder)
        code, _ = run_json(run, ["brief", folder, "synthese"])
        assert code == 1
        for seat_id in SEAT_IDS:
            fill_avis(folder, seat_id)
        code, data = run_json(run, ["brief", folder, "synthese"])
        assert code == 0 and data["model"] == "opus"
        for seat_id in SEAT_IDS:
            assert f"AVIS-{seat_id}.md" in data["brief"]
        assert "zeus/SKILL.md" in data["brief"] and "à l'arbitrage" in data["brief"]

    def test_every_brief_of_a_deliberation_fills(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        for argv in (["tour1", "popper"], ["verification"], ["tour2", "humain"], ["synthese"]):
            code, data = run_json(run, ["brief", folder, *argv])
            assert code == 0, data
            assert "{{" not in data["brief"]

    def test_tour2_brief_reads_the_round_1_reports(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        _, data = run_json(run, ["brief", folder, "tour2", "popper"])
        for seat_id in SEAT_IDS:
            assert f"TOUR1-{seat_id}.md" in data["brief"]
        assert "BILAN-TOUR1.md" in data["brief"]


# --------------------------------------------------------------------------- tally

def test_tally_refuses_partial(run, tmp_path):
    folder = init_session(run, tmp_path)
    fill_cadrage(folder)
    fill_avis(folder, "popper", position="Non")
    code, data = run_json(run, ["tally", folder])
    assert code == 3 and data["missing"] == ["dixieme-homme", "humain"]


def test_tally_positions(run, tmp_path):
    folder = build_tour(run, tmp_path)
    code, data = run_json(run, ["tally", folder])
    assert code == 0 and [r["value"] for r in data["rows"]] == ["Pas maintenant"] * 3


def test_tally_votes_and_changes(run, tmp_path):
    folder = build_deliberation(run, tmp_path)
    fill_vote(folder, "humain", vote="Option A", changed="oui : TOUR1-popper §2 m'a convaincu")
    code, data = run_json(run, ["tally", folder, "--step", "tour2"])
    assert code == 0
    assert [(t["option"], len(t["seats"])) for t in data["totals"]] == [("B", 2), ("A", 1)]
    assert data["changed"] == ["humain"]


def test_tally_needs_step_when_ambiguous(run, tmp_path):
    folder = init_session(run, tmp_path, fmt="deliberation")
    code, data = run_json(run, ["tally", folder])
    assert code == 1 and "tour1" in data["error"] and "tour2" in data["error"]


# --------------------------------------------------------------------------- addendum

def test_addendum_letters_and_continuous_numbering(run, tmp_path):
    folder = init_session(run, tmp_path, fmt="deliberation")
    _, first = run_json(run, ["addendum", folder])
    assert first["created"] == "ADDENDUM-A.md" and first["next_item"] == 1
    text = (folder / "ADDENDUM-A.md").read_text("utf-8")
    (folder / "ADDENDUM-A.md").write_text(text + "\n## 2. Autre point\n", encoding="utf-8")
    _, second = run_json(run, ["addendum", folder])
    assert second["created"] == "ADDENDUM-B.md" and second["next_item"] == 3
    assert "## 3. " in (folder / "ADDENDUM-B.md").read_text("utf-8")


def test_addendum_needs_a_format_that_has_them(run, tmp_path):
    folder = init_session(run, tmp_path)
    code, data = run_json(run, ["addendum", folder])
    assert code == 1 and "deliberation" in data["error"]


# --------------------------------------------------------------------------- check

class TestCheck:
    def test_full_tour_passes_final(self, run, tmp_path):
        folder = build_tour(run, tmp_path)
        code, data = run_json(run, ["check", folder, "--final"])
        assert code == 0, data["problems"]
        assert data["incomplete"] == []

    def test_full_deliberation_passes_final(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        code, data = run_json(run, ["check", folder, "--final"])
        assert code == 0, data["problems"]

    def test_final_on_unfinished_session(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        code, data = run_json(run, ["check", folder, "--final"])
        assert code == 3 and set(data["incomplete"]) == {"cadrage", "avis", "synthese"}

    def test_not_final_on_fresh_session_is_ok(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        code, _ = run_json(run, ["check", folder])
        assert code == 0

    def test_synthesis_before_every_avis(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder)
        fill_avis(folder, "popper")
        fill(folder / "SYNTHESE.md")
        code, data = run_json(run, ["check", folder])
        assert code == 3
        assert any(p["file"] == "SYNTHESE.md" and "avant que l'étape avis" in p["message"]
                   for p in data["problems"])

    def test_grid_not_validated(self, run, tmp_path):
        folder = init_session(run, tmp_path)
        fill_cadrage(folder, validated="non, en attente")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("règle 4" in p["message"] for p in data["problems"])

    def test_missing_position(self, run, tmp_path):
        folder = build_tour(run, tmp_path)
        path = folder / "AVIS-popper.md"
        path.write_text(path.read_text("utf-8").replace("**Position :** Pas maintenant",
                                                        "Position oubliée"), encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("**Position :**" in p["message"] for p in data["problems"])

    def test_synthesis_needs_its_sections(self, run, tmp_path):
        folder = build_tour(run, tmp_path)
        path = folder / "SYNTHESE.md"
        path.write_text(path.read_text("utf-8").replace("## 2. Désaccords", "## 2. Divers"),
                        encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("desaccords" in p["message"] for p in data["problems"])

    def test_arbiter_must_be_named(self, run, tmp_path):
        folder = build_tour(run, tmp_path, arbiter="ghost:nash")
        path = folder / "SYNTHESE.md"
        text = path.read_text("utf-8").replace("**Arbitre :** Nash (`ghost:nash`)", "**Arbitre :**")
        path.write_text(text, encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("**Arbitre :**" in p["message"] for p in data["problems"])

    def test_arbiter_named_wrong_is_a_warning(self, run, tmp_path):
        folder = build_tour(run, tmp_path, arbiter="ghost:nash")
        path = folder / "SYNTHESE.md"
        text = path.read_text("utf-8").replace("**Arbitre :** Nash (`ghost:nash`)",
                                               "**Arbitre :** quelqu'un")
        path.write_text(text, encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 0
        assert any(p["severity"] == "warning" and "ghost:nash" in p["message"]
                   for p in data["problems"])

    def test_leftover_placeholder_is_a_warning(self, run, tmp_path):
        folder = build_tour(run, tmp_path)
        _, data = run_json(run, ["check", folder])
        assert any(p["severity"] == "warning" and "gabarit" in p["message"]
                   for p in data["problems"])

    def test_addendum_with_a_vote(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        run_json(run, ["addendum", folder])
        path = folder / "ADDENDUM-A.md"
        fill(path)
        path.write_text(path.read_text("utf-8") + "\n**Vote :** B\n", encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any(p["file"] == "ADDENDUM-A.md" and "**Vote :**" in p["message"]
                                 for p in data["problems"])

    def test_unfinished_addendum_blocks_nothing_but_shows_in_status(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        run_json(run, ["addendum", folder])
        _, status = run_json(run, ["status", folder])
        assert "addendum" in status["next"]
        code, _ = run_json(run, ["check", folder, "--final"])
        assert code == 0

    def test_vote_changed_without_reason(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        fill_vote(folder, "popper", changed="oui")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("sans nommer" in p["message"] for p in data["problems"])

    def test_verification_needs_verdicts(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        path = folder / "VERIFICATION.md"
        path.write_text(path.read_text("utf-8").replace("CONFIRMÉ", "ok"), encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("verdict" in p["message"] for p in data["problems"])

    def test_bilan_must_name_every_seat(self, run, tmp_path):
        folder = build_deliberation(run, tmp_path)
        path = folder / "BILAN-TOUR1.md"
        path.write_text(path.read_text("utf-8").replace("| humain |", "| ? |"), encoding="utf-8")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("humain" in p["message"] for p in data["problems"])

    def test_tour2_before_bilan(self, run, tmp_path):
        folder = init_session(run, tmp_path, fmt="deliberation")
        fill_cadrage(folder)
        fill(folder / "DOSSIER.md")
        fill_vote(folder, "popper")
        code, data = run_json(run, ["check", folder])
        assert code == 3 and any("TOUR2-popper.md" == p["file"] and "bilan" in p["message"]
                                 for p in data["problems"])


def test_text_output_and_exit_codes(run, tmp_path):
    folder = build_tour(run, tmp_path)
    code, out = run(["check", folder, "--final"])
    assert code == 0 and out.strip().endswith("ok")
    code, out = run(["status", folder])
    assert "format tour" in out and "terminé" in out
