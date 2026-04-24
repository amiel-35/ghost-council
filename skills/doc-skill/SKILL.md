---
name: doc-skill
description: >
  Génère la documentation complète d'un skill ghost-council (FR + EN) et met à jour
  le tableau README. Usage : /doc-skill [nom-du-philosophe]
---

# doc-skill

## Rôle

Tu génères la documentation d'un skill ghost-council à partir de son SKILL.md.
Tu crées deux fichiers de doc (FR + EN) conformes au template, et tu ajoutes la ligne
correspondante dans les deux tableaux du README.

## Règles absolues

- Respecter la structure de `docs/TEMPLATE.md` sans exception ni réordonnancement
- La version EN est une reformulation pour public anglophone — pas une traduction mot à mot
- Vérifier que la ligne README n'existe pas déjà avant de l'ajouter
- Les cas d'usage sont au format strict : contexte → input → output du skill
- Ne jamais copier les Limites connues du SKILL.md — les développer

## Méthode

1. Lire l'argument passé — c'est le nom du philosophe en minuscules (ex: `socrate`)
2. Lire `skills/[nom]/SKILL.md`
3. Lire `docs/TEMPLATE.md` pour respecter la structure exacte
4. Générer `docs/fr/[nom].md` en français, sections dans l'ordre du template
5. Générer `docs/en/[nom].md` en anglais, reformulé pour public anglophone
6. Lire `README.md`, localiser les deux tableaux Documentation (FR et EN)
7. Vérifier que le skill n'a pas déjà une ligne dans ces tableaux
8. Ajouter la ligne dans chaque tableau :
   `| [Nom] | [Solide/Fun] | [description ≤ 12 mots] | [lien fr] | [lien en] |`
9. Confirmer les 3 fichiers créés ou modifiés

## Output attendu

3 fichiers modifiés :
- `docs/fr/[nom].md` — documentation en français
- `docs/en/[nom].md` — documentation en anglais
- `README.md` — ligne ajoutée dans les deux tableaux Documentation
