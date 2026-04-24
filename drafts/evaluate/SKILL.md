# /evaluate — Draft

> **Statut : draft**
> Questions ouvertes en bas de fichier avant de finaliser.

---

## Usage

```
/evaluate [ghost] [output]
```

Exemples :
```
/evaluate popper "Notre A/B test confirme que la feature X améliore l'engagement"
/evaluate sartre "On n'avait pas le choix, le marché nous y obligeait"
/evaluate kant "C'est éthique parce que nos concurrents font la même chose"
```

---

## Ce que le skill fait

Lit un output censé appliquer la méthode d'un ghost donné.
Évalue si la méthode a bien été suivie — pas si la conclusion est juste.
Produit un diagnostic : étapes suivies, étapes manquantes, erreurs de méthode.

Usage principal : calibrer les skills eux-mêmes. Quand on n'est pas sûr qu'un
ghost a bien appliqué sa méthode, `/evaluate` sert de contre-expertise.

---

## Différence avec utiliser le ghost directement

Utiliser le ghost → applique la méthode au problème.
`/evaluate` → vérifie qu'un output existant a appliqué la méthode correctement.

C'est une méta-opération : le ghost évalué ne produit pas l'output, il est le
critère d'évaluation de l'output.

---

## Logique d'évaluation

Pour chaque ghost, la méthode est encodée dans son SKILL.md.
`/evaluate` compare l'output soumis aux étapes de la méthode :

1. **Identifier les étapes de la méthode** du ghost concerné
2. **Pour chaque étape** : est-elle présente dans l'output ? Correctement appliquée ?
3. **Identifier les étapes manquantes** : ce que la méthode aurait dû faire et n'a pas fait
4. **Identifier les erreurs de méthode** : ce qui a été fait mais qui viole une règle absolue
5. **Identifier les glissements** : où la méthode a dérivé vers autre chose
   (ex : Popper qui cherche à confirmer au lieu d'invalider)
6. **Verdict** : la méthode a-t-elle été suivie ? Partiellement ? Pas du tout ?

---

## Structure de l'output

```
## Évaluation — [Ghost] appliqué à : "[extrait de l'output]"

**Méthode attendue :** [résumé des étapes clés du ghost]

**Étapes présentes**
- [étape X] : ✓ [comment elle apparaît dans l'output]

**Étapes manquantes**
- [étape Y] : ✗ [ce qui aurait dû être fait]

**Erreurs de méthode**
- [règle absolue Z violée] : [comment et où]

**Glissements détectés**
- [ce vers quoi l'output a dérivé à la place]

**Verdict**
[La méthode a été suivie / partiellement suivie / non suivie]
[Si non : ce qui a été produit à la place et pourquoi c'est différent]
```

---

## Cas d'usage naturels

**Calibration des skills** : un ghost produit un output surprenant — est-ce la méthode
qui s'applique vraiment ici, ou le modèle qui dérive ?

**Formation** : quelqu'un essaie d'appliquer un ghost manuellement dans un prompt.
`/evaluate` vérifie si l'application est correcte.

**Red team** : soumettre un output à `/evaluate popper` pour vérifier qu'il
n'est pas en train de confirmer au lieu d'invalider.

**Débogage du conseil** : après un `/council`, si l'output d'un ghost semble
hors-sujet, `/evaluate` diagnostique le problème.

---

## Questions ouvertes

- [ ] **Granularité de l'évaluation** : évaluer toutes les étapes de la méthode
  ou seulement les règles absolues ? Les règles absolues sont plus discriminantes
  mais moins complètes.

- [ ] **Qui évalue Hegel ?** : certains ghosts (Hegel, Nietzsche) ont des méthodes
  plus difficiles à vérifier mécaniquement. Le verdict sera moins fiable — à noter
  dans les limites de ces skills spécifiquement.

- [ ] **Output partiel** : si l'output soumis est trop court pour que la méthode
  complète soit évaluable, le dire explicitement plutôt que de produire une évaluation
  incomplète habillée en verdict.

- [ ] **Évaluation récursive** : peut-on `/evaluate zeus [output de zeus]` ?
  Zeus n'a pas de méthode propre — l'évaluation se fait sur les règles absolues
  (ne pas fusionner, nommer le prix). C'est faisable mais à documenter comme cas particulier.

- [ ] **Sévérité** : le skill doit-il être sévère (signaler toute dérive)
  ou pragmatique (signaler seulement ce qui change la conclusion) ? Sévère est plus
  utile pour la calibration. Pragmatique est plus utile pour l'utilisation courante.
  Hypothèse : paramètre optionnel `--strict`.
