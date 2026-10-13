# Drafts

Skills en cours de conception — pas encore prêts pour `skills/`.

Les skills dans ce répertoire sont des **méta-skills** (orchestration, sélection, évaluation)
plutôt que des encodages de méthodes philosophiques. Leur structure diffère des skills
philosophiques : ils opèrent sur le conseil lui-même, pas sur un problème directement.

---

| Skill | Statut | Description |
|---|---|---|
| [`/suggest`](suggest/SKILL.md) | draft | Recommande quels ghosts invoquer pour un problème |
| [`/evaluate`](evaluate/SKILL.md) | draft | Vérifie qu'un output a bien suivi la méthode annoncée |

`/council` et `/compare` sont sortis des drafts le 2026-10-13 : ils vivent dans
[`skills/council/`](../skills/council/SKILL.md), `/compare` comme format (`--format compare`).

---

**Différence avec `skills/`** : les skills philosophiques encodent une méthode.
Ces méta-skills orchestrent l'utilisation des skills philosophiques.
Ils ne passent pas le test d'entrée du guide (pas de méthode en verbes d'action
sur un problème substantiel) — et c'est normal.
