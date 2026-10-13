# Vérification et addenda

À lire pour lancer le vérificateur, relire `VERIFICATION.md` ou publier des
corrections en addendum (format `deliberation`).

> Adapté et traduit de `references/verification.md` d'advisory-council 0.2.1
> (nzanepro, MIT).

## Pourquoi un vérificateur

À la première utilisation de la méthode d'origine, il n'y en avait pas : trois
erreurs dans le dossier, un résultat jamais reproduit et une conclusion fondée sur
un fichier vide sont entrés dans le relevé. Un seul agent chargé de vérifier les
aurait attrapés. Le vérificateur n'a ni angle, ni mandat, ni vote : il n'a donc
aucune raison de préférer une réponse. C'est le siège le moins cher, et celui
qu'on ne supprime jamais.

## Ce qui est porteur

Une affirmation est **porteuse** si une option, un vote ou un risque changerait
qu'elle soit fausse. Typiquement : des chiffres (taille de marché, prix, taux,
coûts, dates, effectifs), des règles (réglementation, conditions d'une plateforme,
clauses), des faits de marché (ce qu'un concurrent propose, d'après des sources
publiques), des attributions (« l'étude X a trouvé »), des comparaisons.

Les lister toutes d'abord, avec l'endroit où chacune est faite. Dire le compte :
« 14 vérifiées sur 14 listées ». Une vérification qui ne dit pas combien elle en a
couvert ne peut pas montrer qu'elle les a toutes couvertes.

## Comment vérifier

1. **Aller à la source primaire**, ou à une source indépendante. Jamais au rapport
   ou à l'outil qui a produit le chiffre : ce serait refaire son calcul sans le tester.
2. **Vérifier l'étiquette autant que la valeur** : le bon segment, la bonne année,
   la bonne version. Les lignes mal étiquetées sont l'erreur la plus fréquente.
3. **Vérifier la base** : dans une comparaison, chaque ligne contre la même
   référence. Recalculer chaque pourcentage à partir de ses deux nombres.
4. **Vérifier la sélection** : le chiffre cité est-il toute la série ou le point
   favorable ?
5. **Vérifier ce que « validé » veut dire** : une base dite validée ne l'a peut-être
   jamais été sur la grandeur en litige.
6. **Chercher les compensations** : un total juste peut cacher deux grosses erreurs
   de signe contraire.
7. **Contrôle positif sur les recherches** : avant d'écrire « aucune règle »,
   « aucun concurrent », « aucune donnée », vérifier que la recherche pouvait
   trouver quelque chose de connu au même endroit. Sinon NON VÉRIFIÉ : jamais
   atteint n'est pas vérifié absent.
8. **Noter la méthode** en une ligne, pour qu'un autre puisse refaire la vérification.

Sans accès au web, le vérificateur contrôle la cohérence interne (calculs, unités,
étiquettes, bases) et marque le reste NON VÉRIFIÉ, « pas d'accès au web » comme lieu
de recherche.

## Verdicts

| Verdict | Sens | Va en addendum ? |
|---|---|---|
| CONFIRMÉ | la source soutient l'affirmation telle qu'écrite | non |
| CONTREDIT | la source dit autre chose ; donner la bonne valeur | oui |
| TROMPEUR | vrai, mais cadré pour tromper (mauvaise base, point isolé, condition manquante) | oui, avec l'énoncé complet |
| NON VÉRIFIÉ | source hors d'atteinte ; dire où on a cherché | seulement si porteur, comme point ouvert |
| ESTIMATION | invérifiable ; méthode jugée raisonnable ou non | seulement si la méthode ne tient pas |

## Addenda

Chacun se crée par `council.py addendum <seance>`, qui prend la lettre et le
numéro de point suivants.

- **Corrections et mesures seulement.** Jamais la position, le vote ou le
  raisonnement d'un angle : un addendum qui en porte un casse l'indépendance de
  tous les avis suivants. `check` le refuse.
- **Dire la préséance** en tête : « Prime sur DOSSIER.md et les addenda précédents
  en cas de conflit. »
- **Numéroter en continu** d'un addendum à l'autre (A : points 1 à 9, B : 10 à 14),
  pour que chaque correction ait une référence stable.
- **Chaque point** : ce que disait le dossier, ce qui est juste, la source, qui l'a
  trouvé, quelle question ou option il touche.
- **Publier les corrections dès qu'elles sont confirmées**, avant le bilan et le
  tour 2. On garde les votes sous séquestre, pas les corrections.
- **Retirer ses propres erreurs franchement.** Ne jamais retoucher le dossier une
  fois le tour 1 parti : l'addendum est la retouche.

## Désaccords entre angles sur un fait

Quand deux angles arrivent à des réponses différentes sur la même question de fait,
chacun avec ses preuves, l'addendum consigne les deux **sans trancher**, et dit ce
que chacune impliquerait. Le bilan dit ensuite si l'action dépend de qui a raison ;
souvent non, et le désaccord reste ouvert dans la synthèse avec le test qui le
départagerait.
