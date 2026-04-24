# /compare — Draft

> **Statut : draft**
> Questions ouvertes en bas de fichier avant de finaliser.

---

## Usage

```
/compare [ghost A] [ghost B] [question]
```

Exemples :
```
/compare popper hegel "La disruption de marché est-elle prévisible ?"
/compare kant machiavel "Faut-il mentir à un client sur l'état du produit ?"
/compare marx adam-smith "Nos incentives équipe sont-ils bien alignés ?"
```

---

## Ce que le skill fait

Soumet la même question à deux ghosts en parallèle, côte à côte.
Pas d'arbitrage — pas de conclusion. L'output est la juxtaposition.

La valeur : rendre visible les hypothèses incompatibles que chaque méthode
importe sur le problème. Deux méthodes qui divergent sur le même input
révèlent quelle hypothèse implicite est en jeu.

---

## Différence avec `/council`

`/council` sélectionne, analyse, arbitre. L'output est une décision.
`/compare` juxtapose deux méthodes sans trancher. L'output est une tension visible.

`/compare` est utile quand :
- On veut comprendre *pourquoi* deux personnes voient le même problème différemment
- On veut choisir délibérément entre deux cadres avant d'analyser
- On veut montrer à quelqu'un ce que sa position implique en lui confrontant son contraire naturel

---

## Structure de l'output

```
## Comparaison — [Ghost A] vs [Ghost B]
### Question : [question]

---

### [Ghost A] — [titre de la méthode]

[Output de la méthode A appliquée à la question]

---

### [Ghost B] — [titre de la méthode]

[Output de la méthode B appliquée à la question]

---

### Ce que la divergence révèle

[L'hypothèse implicite incompatible entre les deux méthodes — formulée comme
une question que la divergence pose, pas comme une conclusion]
```

La section "Ce que la divergence révèle" est obligatoire et courte (2-3 lignes max).
Elle nomme la faille, elle ne la comble pas.

---

## Paires naturelles (non exhaustif)

Paires dont la tension est structurellement productive :

| A | B | Tension |
|---|---|---|
| Popper | Hegel | Falsifiabilité vs dialectique — ce qui "compte" comme preuve |
| Kant | Machiavel | Principe vs intérêt — la morale comme contrainte ou comme naïveté |
| Marx | Adam Smith | Idéologie vs mécanisme — comment lire une structure économique |
| Aristote | Platon | Bottom-up vs top-down — d'où vient la connaissance valide |
| Sartre | Épictète | Liberté radicale vs dichotomie du contrôle — où commence l'agentivité |
| Freud | Popper | Interprétation vs réfutabilité — ce qui compte comme explication |
| Darwin | Tocqueville | Sélection immédiate vs trajectoire longue — quel horizon de lecture |

---

## Questions ouvertes

- [ ] **La section "divergence révèle"** : qui la produit ? Le skill lui-même (méta-analyse)
  ou c'est laissé à l'utilisateur ? Risque si le skill la produit : glisser vers un arbitrage
  non demandé. Risque si c'est laissé à l'utilisateur : l'output le plus utile est absent.
  Hypothèse : le skill la produit, formulée comme question ouverte, pas comme conclusion.

- [ ] **Ordre des ghosts** : est-ce que l'ordre A/B change quelque chose ?
  Probablement oui (effet d'ancrage). À tester.

- [ ] **Longueur des outputs** : même question que pour `/council`.
  Ici encore plus sensible — le côte-à-côte doit tenir dans une lecture.
