# Prompt — Documenter un skill ghost-council

## Usage

```
doc-skill [Nom]
```

Exemples :
```
doc-skill Socrate
doc-skill Kant
doc-skill Nietzsche
```

---

## Prompt

Tu génères la documentation d'un skill du projet ghost-council.
Le skill à documenter est spécifié à la fin de ce message — lis `skills/[nom]/SKILL.md` pour en extraire le contenu.

Le projet encode des méthodes philosophiques comme des opérations applicables à un texte, une décision ou un problème. L'enjeu : encoder la méthode, pas le personnage. "Tu es Kant" active de la biographie. Le skill Kant applique l'impératif catégorique comme une opération précise.

À partir du SKILL.md ci-dessous, génère deux fichiers de documentation.

**Structure obligatoire pour chaque fichier** (dans cet ordre, sans dévier) :

```
# [Nom] — [Titre court de la méthode]

## Pourquoi cet encodage ?
## Ce que la méthode corrige
## Quand l'invoquer
## Quand ne pas l'invoquer
## Cas d'usage
## Limites de l'encodage
```

**Règles par section :**

- **Pourquoi cet encodage** : pas de biographie — uniquement le problème intellectuel que l'encodage résout. Pourquoi encoder cette méthode plutôt que "tu es [nom]" dans un prompt ?
- **Ce que la méthode corrige** : l'anti-pattern précis qu'elle détecte et casse, formulé comme comportement observable ("quand quelqu'un dit X, la méthode fait Y")
- **Quand l'invoquer** : 3-5 déclencheurs concrets, formulés comme situations réelles, pas des concepts abstraits
- **Quand ne pas l'invoquer** : 2-3 contre-indications honnêtes, sans "ça marche toujours si..."
- **Cas d'usage** : 3 exemples complets au format `contexte → input utilisateur → ce que le skill produit`. Pas de métaphore, du concret.
- **Limites de l'encodage** : développe ce qui est dans le SKILL.md, ne le copie pas mot pour mot

**Version EN :** reformulation pour un public anglophone — pas une traduction littérale. Le registre et les exemples doivent résonner pour quelqu'un qui ne connaît pas le contexte FR du projet.

**Output :**

```
---FILE: docs/fr/[nom].md---
[contenu en français]
---END---

---FILE: docs/en/[nom].md---
[contenu en anglais]
---END---

---README-ROW---
| [Nom] | [Solide/Fun] | [description ≤ 12 mots] | [docs/fr/nom.md] | [docs/en/nom.md] |
---END---
```

---

**Skill à documenter :** [NOM]
