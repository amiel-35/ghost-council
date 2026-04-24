# Prompt — Créer un nouveau skill ghost-council

## Usage

Colle ce prompt dans Claude, suivi du nom du philosophe et de tes notes sur sa méthode (facultatif).

---

## Prompt

Tu crées un nouveau skill pour le projet ghost-council.

**Lis d'abord** `docs/guide-ecrire-un-skill.md` — il définit les critères d'entrée, la structure attendue et les règles de l'encodage. Respecte-le à la lettre.

**Test d'entrée obligatoire :**
Avant de générer quoi que ce soit, vérifie que tu peux écrire la section "Méthode" en verbes d'action concrets dans un ordre non-arbitraire. Si tu ne peux pas, dis-le clairement et arrête-toi là.

**Structure obligatoire** (dans cet ordre exact) :

```
---
name: [nom en minuscules, sans accents]
description: >
  [opération concrète en une ligne]
  Déclenche sur des formulations comme : [2-3 exemples].
---

# [Nom]

## Rôle
## Règle absolue
## Méthode
## Output attendu
## Limites connues
```

**Règles absolues :**
- Méthode = verbes d'action, étapes ordonnées, 5-8 étapes
- Aucune phrase du type "tu incarnes X" ou "dans l'esprit de X"
- Limites connues : obligatoires et honnêtes
- Catégorie Solide ou Fun selon la résistance à la formalisation (en cas de doute : Fun)
- Ce qui distingue ce skill des skills existants doit apparaître dans le Rôle

**Output :**

```
---FILE: skills/[nom]/SKILL.md---
[contenu complet]
---END---
```

---

**Philosophe à encoder :**

[Nom + notes éventuelles sur sa méthode]
