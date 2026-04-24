# /council — Draft

> **Statut : draft**
> Questions ouvertes en bas de fichier avant de finaliser.

---

## Usage

```
/council [question]
/council [question] --arbiter [nom]
/council [question] --ghosts [A, B, C]
```

Exemples :
```
/council "Faut-il lancer en freemium ou paywall ?"
/council "Notre expansion en Allemagne est-elle le bon timing ?" --arbiter nash
/council "Est-ce que notre modèle de données tient à l'échelle ?" --ghosts descartes, popper, darwin
```

---

## Ce que le skill fait

Soumet une question à plusieurs ghosts simultanément. Chaque ghost applique sa méthode.
Zeus (ou l'arbitre spécifié) lit les outputs, identifie les convergences et les contradictions
irréductibles, tranche pour la décision posée, et nomme le prix de ce qui a été écarté.

---

## Paramètres

**`[question]`** — obligatoire. La question à soumettre au conseil.
Formuler comme une décision réelle, pas comme une question abstraite.
"Faut-il X ?" ou "Est-ce que Y est viable ?" plutôt que "Qu'est-ce que la philosophie dit de Z ?"

**`--arbiter [nom]`** — optionnel. Par défaut : Zeus.
Remplaçable par n'importe quel skill de la collection.
- `--arbiter zeus` : tranche sans méthode propre (défaut)
- `--arbiter nash` : arbitre depuis l'équilibre stratégique
- `--arbiter aristote` : arbitre depuis les cas empiriques
- `--arbiter trump` : red team — si le verdict tient avec Trump en arbitre, il est solide

**`--ghosts [liste]`** — optionnel. Par défaut : sélection automatique.
Forcer un sous-ensemble de ghosts. Sinon, le skill sélectionne 3-5 ghosts
pertinents pour la question.

---

## Mécanique de sélection des ghosts (défaut)

Quand `--ghosts` n'est pas spécifié :

1. Lire la question et identifier les dimensions en jeu :
   - Dimension éthique → Kant, Rawls, Sartre
   - Dimension stratégique → Machiavel, Sun Tzu, Darwin
   - Dimension empirique → Aristote, Popper, Descartes
   - Dimension structurelle → Marx, Adam Smith, Tocqueville
   - Dimension rhétorique / narrative → Nietzsche, Freud, Wittgenstein
   - Dimension décisionnelle sous incertitude → Pascal, William James, Épictète

2. Sélectionner 3-5 ghosts qui couvrent des dimensions différentes —
   pas les plus évidents, ceux dont la tension est productive.

3. Inclure au moins un ghost susceptible de contredire la conclusion intuitive.

---

## Structure de l'output

```
## Conseil — [question]

### [Ghost A]
[Output de la méthode appliquée à la question]

### [Ghost B]
[Output de la méthode appliquée à la question]

### [Ghost C]
[Output de la méthode appliquée à la question]

---

## Arbitrage — [arbitre]

**Convergences**
[Ce que plusieurs méthodes différentes ont vu depuis des angles différents]

**Contradictions irréductibles**
[Ce qui ne se résout pas — exposé, pas effacé]

**Décision pour cette question**
[Le verdict, avec ses hypothèses explicitées]

**Prix de la décision**
[Ce qui a été écarté et pourquoi]
```

---

## Questions ouvertes (à résoudre avant de sortir du draft)

- [ ] **Longueur des outputs par ghost** : version courte (3-5 lignes) ou complète ?
  Risque avec la version complète : output trop long pour être lu. Risque avec la version courte : perd la valeur de la méthode.
  Hypothèse : version courte avec lien vers output complet sur demande.

- [ ] **Ordre de présentation** : parallèle (tous les ghosts d'abord, arbitrage ensuite)
  ou interleaved (ghost → réaction des autres → arbitrage) ?
  Parallèle est plus lisible. Interleaved est plus fidèle à un vrai débat.

- [ ] **Seuil de sélection automatique** : 3 ghosts minimum ? 5 maximum ?
  Trop peu : angles manquants. Trop : output illisible.

- [ ] **Interaction avec `/suggest`** : council devrait-il appeler suggest en interne
  pour la sélection, ou dupliquer la logique ?

- [ ] **Cas dégénéré** : que se passe-t-il si tous les ghosts convergent ?
  L'arbitrage est trivial — le noter explicitement plutôt que de simuler un désaccord.
