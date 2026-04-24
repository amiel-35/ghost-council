# Skill Documentation System — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable documentation system for ghost-council skills: a standalone prompt, a Claude Code skill, a bilingual template, and a README navigation table.

**Architecture:** A `tools/doc-skill.md` standalone prompt reads a `SKILL.md` and outputs delimited FR/EN docs + README row. A `skills/doc-skill/SKILL.md` wraps the same logic as an invocable Claude Code skill. A `docs/TEMPLATE.md` locks in the section structure as the single source of truth. The README gets two navigation tables (FR + EN) populated one row at a time. Batch generation of the 21 existing skills runs only after 2-3 pilot runs validate the prompt.

**Tech Stack:** Markdown only — no build tools, no scripts. All artifacts are plain `.md` files. Git for versioning.

---

## Note on skill count

The spec says 22 skills. The current `skills/` directory has 21 folders:
`adam-smith aristote darwin descartes epictete freud hegel kant machiavel montesquieu nietzsche pascal platon popper rawls sartre socrate sun-tzu tocqueville william-james wittgenstein`

The batch run task (Task 6) lists all 21. If a 22nd skill is added before the batch, include it.

---

## File Map

Files created or modified by this plan:

| Path | Status | Responsibility |
|------|--------|----------------|
| `docs/TEMPLATE.md` | **create** | Canonical section structure for doc pages (commented reference) |
| `tools/doc-skill.md` | **create** | Standalone prompt: reads a SKILL.md, outputs FR + EN doc + README row |
| `tools/new-skill.md` | **create** | Standalone prompt: generates a new `skills/[nom]/SKILL.md` from a philosopher name |
| `skills/doc-skill/SKILL.md` | **create** | Claude Code skill invocable with `/doc-skill [nom]` |
| `docs/fr/[nom].md` (×21) | **create** | French documentation for each existing skill |
| `docs/en/[nom].md` (×21) | **create** | English documentation for each existing skill |
| `README.md` | **modify** | Add two navigation tables at the end (FR + EN) |

---

## Task 1: `docs/TEMPLATE.md` — the canonical doc structure

**Files:**
- Create: `docs/TEMPLATE.md`

The template is the single source of truth for section names and order. It must be self-explanatory without this plan document.

- [ ] **Step 1: Create `docs/TEMPLATE.md`**

```markdown
# [Nom] — [Titre court de la méthode]

<!-- Section 1 -->
## Pourquoi cet encodage ?

<!--
Pas de biographie. Le problème intellectuel que l'encodage résout.
Pourquoi encoder cette méthode plutôt que "tu es [Nom]" dans un prompt ?
1-3 paragraphes courts.
-->

<!-- Section 2 -->
## Ce que la méthode corrige

<!--
L'anti-pattern précis que cette méthode détecte et casse.
Formulé comme comportement observable :
"quand quelqu'un dit X, la méthode fait Y".
-->

<!-- Section 3 -->
## Quand l'invoquer

<!--
3 à 5 déclencheurs concrets, formulés comme situations.
Pas de règles générales — des cas précis.
-->

<!-- Section 4 -->
## Quand ne pas l'invoquer

<!--
2 à 3 contre-indications honnêtes.
-->

<!-- Section 5 -->
## Cas d'usage

<!--
3 exemples complets, chacun avec :
- Contexte : quelle situation ?
- Input utilisateur : ce que l'utilisateur dit ou demande
- Ce que le skill produit : output concret (peut être abrégé mais reconnaissable)
-->

<!-- Section 6 -->
## Limites de l'encodage

<!--
Ce qui résiste à la formalisation.
Développé depuis le SKILL.md, pas copié.
Les skills "Fun" auront cette section plus dense.
-->

---

<!-- VERSION EN (même structure, reformulée pour public anglophone, pas traduite mot à mot) -->

# [Name] — [Short method title]

## Why this encoding?

## What the method corrects

## When to invoke it

## When not to invoke it

## Use cases

## Limits of the encoding
```

- [ ] **Step 2: Commit**

```bash
git add docs/TEMPLATE.md
git commit -m "docs: add TEMPLATE.md — canonical structure for skill doc pages"
```

---

## Task 2: `tools/doc-skill.md` — standalone documentation prompt

**Files:**
- Create: `tools/doc-skill.md`

This prompt is used standalone (paste into any LLM) or referenced by the `doc-skill` Claude Code skill. It must be self-contained: all instructions are inside, no external references needed.

- [ ] **Step 1: Create `tools/doc-skill.md`**

```markdown
# Prompt : documenter un skill ghost-council

## Entrée attendue

Colle le contenu brut d'un fichier `skills/[nom]/SKILL.md`.

Optionnel : indique la catégorie du skill (Solide ou Fun) si tu la connais.

---

## Ta mission

Tu génères la documentation complète d'un skill ghost-council en français et en anglais, plus la ligne de tableau README.

### Règles de fond

- **Pas de biographie.** Les sections parlent de l'opération encodée, pas du philosophe historique.
- **Version EN = reformulation pour public anglophone**, pas traduction mot à mot. Le ton, les exemples et les formulations peuvent différer.
- **Les limites** sont développées depuis le contenu du SKILL.md — pas copiées, pas inventées. Pour les skills Fun, cette section sera naturellement plus dense.
- **Les cas d'usage** : 3 exemples complets avec contexte → input → output. L'output peut être abrégé mais doit être reconnaissable (pas "le skill produit une analyse").
- **La description README** : ≤ 12 mots, en anglais, formulation active.

### Structure des pages (obligatoire, dans cet ordre)

```
# [Nom] — [Titre court de la méthode]
## Pourquoi cet encodage ?
## Ce que la méthode corrige
## Quand l'invoquer
## Quand ne pas l'invoquer
## Cas d'usage
## Limites de l'encodage
```

Ne pas dévier de cet ordre. Ne pas fusionner des sections. Ne pas ajouter de sections.

---

## Format de sortie

Utilise exactement ces délimiteurs (le script de traitement en dépend) :

~~~
---FILE: docs/fr/[nom].md---
[contenu de la page FR]
---END---

---FILE: docs/en/[nom].md---
[contenu de la page EN]
---END---

---README-ROW---
| [Nom] | [Solide/Fun] | [description ≤ 12 mots en anglais] | [docs/fr/[nom].md](docs/fr/[nom].md) | [docs/en/[nom].md](docs/en/[nom].md) |
---END---
~~~

Le nom dans les chemins de fichiers est le même que le dossier `skills/[nom]/` — minuscules, sans accents (ex : `socrate`, `william-james`).

---

## Calibrage

- Toutes les pages suivent la même structure, quelle que soit la catégorie.
- Les pages Fun auront des sections "Limites de l'encodage" plus denses — c'est normal et voulu.
- Longueur cible par page : 400-600 mots. Pas de padding.
- Ton : direct, pas académique. Le projet ne se prend pas trop au sérieux.
```

- [ ] **Step 2: Commit**

```bash
git add tools/doc-skill.md
git commit -m "tools: add doc-skill.md — standalone prompt for generating skill documentation"
```

---

## Task 3: `tools/new-skill.md` — standalone skill creation prompt

**Files:**
- Create: `tools/new-skill.md`

This prompt generates a new `skills/[nom]/SKILL.md` from a philosopher name and optional notes. It encodes the project's editorial rules so the output is immediately valid.

- [ ] **Step 1: Create `tools/new-skill.md`**

```markdown
# Prompt : créer un nouveau skill ghost-council

## Entrée attendue

- **Nom du philosophe** (obligatoire)
- **Notes sur sa méthode** (optionnel) : ce que tu sais déjà de son fonctionnement intellectuel

---

## Test d'entrée (évaluer avant de générer)

Avant de générer quoi que ce soit, évalue si le philosophe passe le critère d'entrée du projet :

> **La méthode est-elle formalisable en verbes d'action concrets ?**

Si tu ne peux pas écrire une section "Méthode" en 5 à 8 étapes avec des verbes à l'infinitif dans un ordre non-arbitraire, le philosophe est hors scope.

Si c'est le cas, dis-le clairement avec une explication — ne génère pas un SKILL.md approximatif.

---

## Règles éditoriales (à encoder dans l'output)

- **Méthode, pas costume.** Pas de phrases comme "tu incarnes X" ou "dans l'esprit de X".
- **Pas de biographie.** Le Rôle dit ce que le skill fait, pas qui était le philosophe.
- **Les Règles absolues** sont non-négociables. 3 à 5 maximum. Formulées comme contraintes dures.
- **La Méthode** : 5 à 8 étapes, verbes à l'infinitif, ordre logique et non-arbitraire.
- **L'Output attendu** : ce que ça produit, pas comment c'est formaté.
- **Les Limites connues** : section obligatoire. Honnête sur ce que l'encodage sacrifie.
- **Catégorie** : Solide si la méthode est reproductible d'un modèle à l'autre. Fun si la posture est forte mais la formalisation partielle. En cas de doute, Fun.
- **Frontmatter** : inclure des déclencheurs concrets (phrases qui appellent ce skill).

---

## Format de sortie

~~~
---FILE: skills/[nom]/SKILL.md---
---
name: [nom en minuscules, sans accents]
description: >
  [une ligne sur l'opération concrète]
  Déclenche sur des formulations comme : [2-3 exemples de phrases déclencheuses].
---

# [Nom avec majuscule]

## Rôle

[Formulé à la première personne. Ce qui distingue ce skill des autres.]

## Règle absolue

- [règle 1]
- [règle 2]
- [règle 3]

## Méthode

1. [verbe à l'infinitif] : [description]
2. [verbe à l'infinitif] : [description]
...

## Output attendu

[Ce que ça produit. Pas le format — l'essence de l'output.]

## Limites connues

- [limite 1]
- [limite 2]
- [limite 3]
---END---
~~~

---

## Checklist auto-vérification (applique avant de sortir l'output)

- [ ] La section Méthode utilise des verbes à l'infinitif dans un ordre non-arbitraire
- [ ] Le Rôle dit ce qui distingue ce skill des autres skills existants
- [ ] Les Règles absolues sont non-négociables et formulées comme telles
- [ ] L'Output attendu décrit ce qui est produit, pas comment c'est formaté
- [ ] Les Limites connues sont honnêtes sur ce que l'encodage sacrifie
- [ ] Le frontmatter inclut des déclencheurs concrets
- [ ] Aucune phrase du type "tu incarnes X" ou "dans l'esprit de X"
```

- [ ] **Step 2: Commit**

```bash
git add tools/new-skill.md
git commit -m "tools: add new-skill.md — standalone prompt for creating new skill SKILL.md files"
```

---

## Task 4: `skills/doc-skill/SKILL.md` — invocable Claude Code skill

**Files:**
- Create: `skills/doc-skill/SKILL.md`

This is the Claude Code skill invoked with `/doc-skill [nom]`. It orchestrates the full documentation workflow: read SKILL.md, read TEMPLATE.md, generate both doc files, update README. It references `tools/doc-skill.md` for the generation logic.

- [ ] **Step 1: Create `skills/doc-skill/` directory and `SKILL.md`**

```bash
mkdir -p /path/to/ghost-council/skills/doc-skill
```

Then create `skills/doc-skill/SKILL.md` with this content:

```markdown
---
name: doc-skill
description: >
  Génère la documentation FR + EN d'un skill ghost-council existant et l'ajoute au tableau README.
  Invocation : /doc-skill [nom-du-philosophe]
---

# doc-skill

## Rôle

Tu génères la documentation complète d'un skill ghost-council : une page FR, une page EN, et une ligne dans les deux tableaux README. Tu lis le SKILL.md du philosophe concerné, tu appliques le template de documentation, et tu écris les fichiers directement. Tu vérifies que la ligne README n'existe pas avant de l'ajouter.

## Règle absolue

- Toujours lire `skills/[nom]/SKILL.md` avant de générer quoi que ce soit.
- Toujours lire `docs/TEMPLATE.md` avant de générer les pages.
- Toujours lire `README.md` avant de modifier les tableaux — vérifier que la ligne n'existe pas déjà.
- Version EN = reformulation pour public anglophone, jamais traduction mot à mot.
- Ne pas dévier de la structure du TEMPLATE.md.

## Méthode

1. Lire `skills/[nom]/SKILL.md` — extraire le rôle, la méthode, les règles, l'output, les limites.
2. Lire `docs/TEMPLATE.md` — mémoriser la structure exacte des sections.
3. Générer `docs/fr/[nom].md` — page FR complète selon la structure du template.
4. Générer `docs/en/[nom].md` — page EN reformulée pour public anglophone (pas traduite).
5. Lire `README.md` — chercher si une ligne `[Nom]` existe déjà dans les tableaux Documentation.
6. Si la ligne n'existe pas : ajouter une ligne dans le tableau FR et une dans le tableau EN.
7. Confirmer les fichiers modifiés : lister `docs/fr/[nom].md`, `docs/en/[nom].md`, `README.md`.

## Output attendu

3 fichiers créés ou modifiés :
- `docs/fr/[nom].md` — page de documentation française
- `docs/en/[nom].md` — page de documentation anglaise
- `README.md` — deux nouvelles lignes dans les tableaux FR et EN

Confirmation explicite à la fin : "Fait. 3 fichiers modifiés : docs/fr/[nom].md, docs/en/[nom].md, README.md"

## Limites connues

- Ne gère pas les skills dont le nom de dossier diffère du nom affiché (ex : `william-james` → "William James") — vérifier le frontmatter du SKILL.md.
- Ne génère pas de SKILL.md pour un nouveau philosophe — utiliser `tools/new-skill.md` pour ça.
- Si les tableaux README n'existent pas encore, s'arrêter et demander à l'utilisateur d'exécuter la tâche README d'abord (Task 5 du plan d'implémentation).
- La qualité des cas d'usage dépend de la richesse du SKILL.md source — les skills avec peu d'exemples produiront des docs moins illustrées.
```

- [ ] **Step 2: Commit**

```bash
git add skills/doc-skill/SKILL.md
git commit -m "feat: add doc-skill — Claude Code skill for generating bilingual skill documentation"
```

---

## Task 5: README navigation tables

**Files:**
- Modify: `README.md` (append at end of file)

The two tables are added at the end of the existing README, one in French, one in English. They start empty (headers only) — the `doc-skill` skill populates them one row at a time during the batch run.

- [ ] **Step 1: Read the current end of README.md**

Read `README.md` to find the last line, so the tables are appended after all existing content without duplication.

- [ ] **Step 2: Append the two navigation tables to `README.md`**

Add this block at the very end of `README.md`:

```markdown

---

## Documentation

| Skill | Catégorie | Description | Doc FR | Doc EN |
|-------|-----------|-------------|--------|--------|

---

## Documentation

| Skill | Category | Description | Doc FR | Doc EN |
|-------|----------|-------------|--------|--------|
```

Note: the two tables are intentionally separated by `---`. The first is the French section, the second is the English section. The `doc-skill` skill adds one row to each per invocation.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add empty Documentation navigation tables to README (FR + EN)"
```

---

## Task 6: Pilot run — validate doc-skill on 2-3 skills

**Files:**
- Create: `docs/fr/socrate.md`, `docs/en/socrate.md`
- Create: `docs/fr/kant.md`, `docs/en/kant.md`
- Create: `docs/fr/nietzsche.md`, `docs/en/nietzsche.md`
- Modify: `README.md` (3 rows added to each table)

Before the full batch, validate the prompt and skill on one Solid skill, one Solid skill with a clear edge case, and one Fun skill. This catches structural or tone problems before generating 21 files.

- [ ] **Step 1: Run `/doc-skill socrate`**

Invoke the `doc-skill` skill for `socrate` (Solid skill, simple structure):

```
/doc-skill socrate
```

Expected output: `docs/fr/socrate.md` and `docs/en/socrate.md` created, README row added.

- [ ] **Step 2: Review `docs/fr/socrate.md`**

Check manually:
- All 6 sections present in the right order
- No biographie, no "il pensait que"
- "Cas d'usage" has 3 examples with contexte → input → output
- "Limites de l'encodage" developed from SKILL.md content, not copied verbatim
- Tone: direct, not academic

If anything is off, fix `tools/doc-skill.md` before continuing.

- [ ] **Step 3: Run `/doc-skill kant`**

```
/doc-skill kant
```

Expected output: `docs/fr/kant.md` and `docs/en/kant.md` created, README row added.

- [ ] **Step 4: Review `docs/fr/kant.md`**

Same checklist as Step 2. Kant is a Solid skill with a more complex method — verify that the "Cas d'usage" captures the categorical imperative test correctly, not just generic ethics commentary.

- [ ] **Step 5: Run `/doc-skill nietzsche`**

```
/doc-skill nietzsche
```

Expected output: `docs/fr/nietzsche.md` and `docs/en/nietzsche.md` created, README row added.

- [ ] **Step 6: Review `docs/fr/nietzsche.md`**

Nietzsche is a Fun skill — verify that "Limites de l'encodage" is denser than Socrate's and Kant's. If it's the same length, something is wrong.

- [ ] **Step 7: Review the EN versions of all 3 pilots**

Open `docs/en/socrate.md`, `docs/en/kant.md`, `docs/en/nietzsche.md`. Check they are reformulations, not word-for-word translations. Section titles should be in English. Examples can differ from the FR version.

- [ ] **Step 8: Review README tables**

Open `README.md`. The two tables should each have 3 rows: Socrate, Kant, Nietzsche. Links should be valid relative paths.

- [ ] **Step 9: Fix `tools/doc-skill.md` if needed, then commit pilots**

If the pilot review found issues, fix `tools/doc-skill.md` first, then re-run affected skills. Once satisfied:

```bash
git add docs/fr/socrate.md docs/en/socrate.md
git add docs/fr/kant.md docs/en/kant.md
git add docs/fr/nietzsche.md docs/en/nietzsche.md
git add README.md
git add tools/doc-skill.md  # only if modified
git commit -m "docs: add pilot documentation for socrate, kant, nietzsche (FR + EN)"
```

---

## Task 7: Batch run — remaining 18 skills

**Files:**
- Create: `docs/fr/[nom].md` and `docs/en/[nom].md` for each of the 18 remaining skills
- Modify: `README.md` (18 rows added to each table)

Only run this after Task 6 pilots are validated. Run one skill at a time, not all at once.

Skills remaining (21 total minus 3 pilots = 18):

```
adam-smith aristote darwin descartes epictete freud
hegel machiavel montesquieu pascal platon popper
rawls sartre sun-tzu tocqueville william-james wittgenstein
```

- [ ] **Step 1: Run doc-skill for each remaining skill**

For each name in the list above, run:

```
/doc-skill adam-smith
/doc-skill aristote
/doc-skill darwin
/doc-skill descartes
/doc-skill epictete
/doc-skill freud
/doc-skill hegel
/doc-skill machiavel
/doc-skill montesquieu
/doc-skill pascal
/doc-skill platon
/doc-skill popper
/doc-skill rawls
/doc-skill sartre
/doc-skill sun-tzu
/doc-skill tocqueville
/doc-skill william-james
/doc-skill wittgenstein
```

Run one at a time. After each run, verify the confirmation message ("Fait. 3 fichiers modifiés").

- [ ] **Step 2: Spot-check 3 random skills**

Pick 3 from the list and open their FR + EN pages. Apply the same review checklist from Task 6 Step 2. If problems are found, fix `tools/doc-skill.md` and re-run affected skills.

- [ ] **Step 3: Verify README tables are complete**

Open `README.md`. Count rows in each table — should be 21.

- [ ] **Step 4: Commit all remaining docs**

```bash
git add docs/fr/ docs/en/ README.md
git commit -m "docs: generate bilingual documentation for all 21 skills"
```

---

## Self-review against spec

**Spec coverage check:**

| Spec requirement | Task |
|-----------------|------|
| `tools/new-skill.md` — standalone prompt for new SKILL.md | Task 3 |
| `tools/doc-skill.md` — standalone prompt for FR + EN + README row | Task 2 |
| `docs/TEMPLATE.md` — reference template | Task 1 |
| `skills/doc-skill/SKILL.md` — invocable Claude Code skill | Task 4 |
| README navigation tables (FR + EN) | Task 5 |
| Batch run after pilot validation | Tasks 6 + 7 |
| Version EN = reformulation, not translation | Encoded in Task 2 prompt and Task 4 skill |
| doc-skill checks README before adding row | Task 4, Méthode step 5-6 |
| Pilot run on 2-3 skills before batch | Task 6 |

**Placeholder scan:** No TBD, no TODO, no "similar to Task N". All code blocks are complete. All file paths are exact.

**Type consistency:** No type system involved — prompt content and markdown section names are consistent across Task 2 (prompt), Task 4 (skill), and Task 1 (template). Section names match verbatim: `## Pourquoi cet encodage ?`, `## Ce que la méthode corrige`, etc.

**One gap identified and resolved:** The spec mentions the doc-skill should "confirm 3 files modified" — this is encoded in the Output attendu section of Task 4.

**Second note:** The spec says "22 skills existants" but the current `skills/` directory has 21. The batch task (Task 7) uses 21. If a 22nd skill is added before execution, add it to the batch list.
