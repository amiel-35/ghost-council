# /suggest — Draft

> **Statut : draft**
> Questions ouvertes en bas de fichier avant de finaliser.

---

## Usage

```
/suggest [problème]
```

Exemples :
```
/suggest "Notre taux de churn a doublé en deux mois sans qu'on comprenne pourquoi"
/suggest "On hésite à licencier un manager performant mais toxique"
/suggest "Notre concurrent vient de lever 50M — comment on réagit ?"
```

---

## Ce que le skill fait

Lit le problème, recommande 2-3 ghosts pertinents avec une justification courte
pour chacun. Évite d'ouvrir le mauvais outil — ou d'en ouvrir cinq alors qu'un suffit.

La recommandation n'est pas "voici les philosophes qui ont pensé à ce sujet".
C'est "voici les méthodes dont l'opération est adaptée à ce que ce problème demande".

---

## Logique de recommandation

Pour chaque problème, identifier :

1. **Ce que le problème demande réellement** — pas son sujet, son opération :
   - Expliquer un comportement → Adam Smith, Freud, Marx
   - Tester une hypothèse → Popper, Descartes, Aristote
   - Décider sous incertitude → Pascal, Darwin, William James
   - Évaluer une règle ou une décision → Kant, Rawls, Épictète
   - Analyser un rapport de force → Machiavel, Sun Tzu, Tocqueville
   - Clarifier un concept flou → Wittgenstein, Socrate, Aristote
   - Déconstruire un discours → Nietzsche, Freud, Marx
   - Dépasser une opposition → Hegel

2. **Ce que le problème ne demande pas** — éliminer les ghosts dont la méthode
   est hors-sujet même si le philosophe "semble" lié au thème.

3. **Recommander 2-3 ghosts maximum** avec :
   - Le nom
   - L'opération concrète qu'il appliquera à ce problème (pas la biographie)
   - Pourquoi cette méthode est adaptée à cette question spécifique

---

## Structure de l'output

```
Pour ce problème, je recommande :

**[Ghost A]** — [opération concrète sur ce problème]
Pourquoi : [1-2 lignes, lié au problème spécifique]

**[Ghost B]** — [opération concrète sur ce problème]
Pourquoi : [1-2 lignes, lié au problème spécifique]

[Ghost C optionnel si la tension entre A et B est productive à nommer]

---
Si tu veux les trois simultanément : `/council "[question reformulée]" --ghosts [A, B, C]`
```

---

## Ce que le skill ne fait pas

- Il ne résout pas le problème
- Il ne choisit pas le "meilleur" ghost — il recommande ceux dont la méthode
  est adaptée, pas ceux dont la conclusion sera la plus confortable
- Il ne remplace pas `/council` — il l'alimente

---

## Questions ouvertes

- [ ] **Reformulation de la question** : le skill devrait-il reformuler le problème
  en une question pour `/council` ? Utile mais risque de changer ce que l'utilisateur voulait poser.

- [ ] **Cas "aucun ghost n'est adapté"** : si le problème est technique, opérationnel,
  ou purement factuel — le nommer explicitement plutôt que de recommander des ghosts
  par défaut. "Ce problème n'appelle pas une méthode philosophique" est une réponse valide.

- [ ] **Nombre de recommandations** : 2 ou 3 ? Deux crée une tension naturelle.
  Trois permet un conseil complet sans `/council`. À trancher.

- [ ] **Interaction avec `/council`** : le lien vers `/council` dans l'output
  est une hypothèse — à valider que c'est utile et pas juste du bruit.
