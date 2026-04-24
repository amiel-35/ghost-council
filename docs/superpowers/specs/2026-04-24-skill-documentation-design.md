# Design — Système de documentation des skills ghost-council

**Date :** 2026-04-24
**Statut :** Approuvé

---

## Contexte

ghost-council est une collection de 22 skills markdown encodant des méthodes philosophiques (Socrate, Kant, Popper…). Chaque `skills/[nom]/SKILL.md` définit le rôle, les règles, la méthode, l'output attendu et les limites connues du philosophe encodé.

Le README actuel présente le projet mais ne fournit pas de documentation détaillée par skill ni de tableau de navigation. L'objectif est d'ajouter une couche de documentation riche et bilingue, générée par un prompt réutilisable.

---

## Ce qu'on construit

1. **Une arborescence de documentation bilingue** (`docs/fr/` et `docs/en/`)
2. **Un template de référence** (`docs/TEMPLATE.md`)
3. **Un prompt standalone** (`tools/doc-skill.md`) utilisable dans n'importe quel Claude
4. **Un skill Claude Code** (`skills/doc-skill/SKILL.md`) invocable avec `/doc-skill [nom]`
5. **Un tableau de navigation** ajouté en fin de README (FR et EN)

---

## Arborescence

```
ghost-council/
├── README.md                        ← tableau ajouté en fin de fichier (FR + EN)
├── skills/
│   ├── [nom]/SKILL.md               ← inchangé
│   └── doc-skill/SKILL.md           ← nouveau : skill de génération
├── tools/
│   └── doc-skill.md                 ← prompt standalone
├── docs/
│   ├── TEMPLATE.md                  ← structure de référence (commentée)
│   ├── fr/
│   │   ├── socrate.md
│   │   ├── kant.md
│   │   └── ...
│   └── en/
│       ├── socrate.md
│       ├── kant.md
│       └── ...
└── docs/superpowers/specs/          ← specs de design (ce fichier)
```

---

## Structure d'une page de documentation

Sections dans cet ordre, sans dévier :

```markdown
# [Nom] — [Titre court de la méthode]

## Pourquoi cet encodage ?
Pas de biographie. Le problème intellectuel que l'encodage résout.
Pourquoi encoder cette méthode plutôt que "tu es Kant" dans un prompt ?

## Ce que la méthode corrige
L'anti-pattern précis qu'elle détecte et casse.
Formulé comme comportement observable : "quand quelqu'un dit X, la méthode fait Y".

## Quand l'invoquer
3-5 déclencheurs concrets, formulés comme situations.

## Quand ne pas l'invoquer
2-3 contre-indications honnêtes.

## Cas d'usage
3 exemples complets : contexte → input utilisateur → ce que le skill produit.

## Limites de l'encodage
Ce qui résiste à la formalisation. Développé depuis le SKILL.md, pas copié.
```

**Calibrage :** toutes les pages suivent la même structure, quelle que soit la catégorie (Solide/Fun). Les pages "Fun" auront naturellement des sections "Limites" plus denses.

**Version EN :** reformulation pour public anglophone, pas traduction mot à mot.

---

## Prompt standalone (`tools/doc-skill.md`)

Le prompt prend le contenu brut d'un SKILL.md en input et génère les deux fichiers + la ligne README avec des délimiteurs :

```
---FILE: docs/fr/[nom].md---
[contenu]
---END---

---FILE: docs/en/[nom].md---
[contenu]
---END---

---README-ROW---
| [Nom] | [Solide/Fun] | [description ≤ 12 mots] | [lien fr] | [lien en] |
---END---
```

---

## Skill Claude Code (`skills/doc-skill/SKILL.md`)

Invocation : `/doc-skill [nom-du-philosophe]`

**Méthode d'exécution :**
1. Lire `skills/[nom]/SKILL.md`
2. Lire `docs/TEMPLATE.md`
3. Générer `docs/fr/[nom].md`
4. Générer `docs/en/[nom].md`
5. Lire README.md, ajouter la ligne dans les deux tableaux (FR et EN)
6. Confirmer les 3 fichiers modifiés

**Règles absolues :**
- Respecter la structure du TEMPLATE.md sans exception
- Version EN = reformulation, pas traduction
- Vérifier que la ligne README n'existe pas avant d'ajouter

---

## Tableau README

Ajouté en fin de README, dans les deux langues :

```markdown
## Documentation

| Skill | Catégorie | Description | Doc FR | Doc EN |
|-------|-----------|-------------|--------|--------|
| Socrate | Solide | ... | [FR](docs/fr/socrate.md) | [EN](docs/en/socrate.md) |

## Documentation

| Skill | Category | Description | Doc FR | Doc EN |
|-------|----------|-------------|--------|--------|
| Socrates | Solid | ... | [FR](docs/fr/socrate.md) | [EN](docs/en/socrate.md) |
```

Le skill `doc-skill` ajoute une ligne dans chaque tableau à chaque invocation.

---

## Ce qui n'est pas dans le scope

- Génération automatique des 22 pages en batch (une invocation par skill)
- Système de versioning des docs
- Validation de la cohérence entre SKILL.md et la doc générée
