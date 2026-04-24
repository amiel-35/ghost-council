# Popper — Chercher à invalider, pas à confirmer

## Pourquoi cet encodage ?

Le biais de confirmation est le défaut par défaut. On cherche des données qui confirment ce qu'on croit déjà, on interprète l'absence de réfutation comme une preuve, on accumule des "succès" qui n'ont jamais été mis à l'épreuve. Popper encode l'opération inverse : formuler précisément ce qui invaliderait une hypothèse, et aller chercher ce cas en priorité. Sans cet encodage, les hypothèses produit et stratégiques ressemblent à des thèses — elles accumulent des confirmations et ignorent les signaux contraires.

## Ce que la méthode corrige

Quand quelqu'un dit "les données confirment que...", la méthode demande : qu'est-ce qui aurait permis de réfuter ? Si personne ne peut répondre, l'hypothèse n'est pas une hypothèse — c'est une croyance. Elle corrige aussi les "amendements ad hoc" : quand une théorie est modifiée à chaque contre-exemple pour la sauver plutôt que pour la tester.

## Quand l'invoquer

- Quand une hypothèse produit ou stratégique est présentée comme "confirmée" par des données
- Quand une équipe cite des succès sans mentionner les cas où ça n'a pas marché
- Quand une thèse est formulée de façon si vague qu'elle ne pourrait pas être réfutée
- Quand quelqu'un amende une théorie à chaque contre-exemple pour la sauver

## Quand ne pas l'invoquer

- Quand l'hypothèse est trop early stage pour être formulée de façon testable sans la vider de sens
- Quand ce qu'on cherche est de la génération d'idées, pas de la validation
- Sur des jugements de valeur qui ne sont pas falsifiables par nature

## Cas d'usage

### 1. Hypothèse de rétention produit

**Contexte :** Une équipe affirme que sa fonctionnalité améliore la rétention.

**Input :** "Les données confirment que les utilisateurs qui utilisent la feature X ont un meilleur taux de rétention."

**Ce que le skill produit :** "Comment saurait-on que cette hypothèse est fausse ? — Si c'est corrélation sans causalité, on observerait quoi ? — Qu'est-ce que ça prédit pour les utilisateurs qui n'utilisent pas la feature ? — Y a-t-il des segments où ce n'est pas vrai ? — Le test le plus sévère : chercher les utilisateurs qui utilisent la feature X et churent quand même. Si tu n'as pas cherché ce cas, tu n'as pas testé l'hypothèse."

### 2. Stratégie de go-to-market

**Contexte :** Une équipe est "convaincue" que son marché cible est les PME.

**Input :** "On est convaincus que les PME sont notre marché — tous les clients qu'on a signés sont des PME."

**Ce que le skill produit :** "Qu'est-ce qui te ferait changer d'avis sur ce segment ? — Est-ce que 'toutes les signatures sont des PME' est un test ou une description de l'effort de vente actuel ? — Quelle est la prédiction falsifiable ? Si les PME sont le bon marché, tu devrais observer quoi dans 6 mois ? — As-tu cherché des contre-exemples : des PME similaires qui n'ont pas signé, des entreprises plus grandes qui auraient voulu signer ?"

### 3. Hypothèse de pricing

**Contexte :** Une équipe veut augmenter ses prix et "pense" que l'élasticité est faible.

**Input :** "On pense que nos clients ne sont pas très price-sensitive — ils n'ont pas réagi aux hausses passées."

**Ce que le skill produit :** "L'hypothèse reformulée de façon falsifiable : 'une hausse de 20% n'affecte pas le taux de conversion ni le taux de churn dans les 3 mois suivants.' — Qu'est-ce qui invaliderait cette hypothèse ? — Les hausses passées étaient de quelle ampleur ? — Y a-t-il des segments où l'élasticité pourrait être différente ? — Verdict provisoire : résistance à la réfutation pour les hausses < X% dans ce segment. Pas de certitude."

## Limites de l'encodage

La falsifiabilité requiert que l'hypothèse soit formulée avec assez de précision pour être testable — dans les sciences sociales et le produit early stage, cette précision est souvent impossible sans vider l'hypothèse de sens. La méthode dit ce qui n'a pas encore été réfuté, jamais ce qui est vrai — ce qui peut être frustrant quand on cherche une recommandation positive. Et l'asymétrie confirmation/réfutation, si elle est logiquement solide, est psychologiquement contre-intuitive : les équipes résistent naturellement à chercher ce qui invaliderait leur thèse.
