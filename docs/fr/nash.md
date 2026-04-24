# Nash — L'équilibre derrière les comportements collectifs

## Pourquoi cet encodage ?

La théorie des jeux de Nash résout un problème que ni Adam Smith ni Machiavel ne traitent vraiment : comment se comportent des agents rationnels *qui anticipent le comportement des autres* ? Smith lit les mécanismes d'incitation dans un marché. Machiavel cartographie les rapports de force d'un décideur unique. Nash modélise les situations où l'outcome de chacun dépend des choix de tous — et cherche le point de stabilité, l'équilibre, qui n'est pas forcément le meilleur résultat possible. L'encodage produit une carte des forces, pas une prescription.

## Ce que la méthode corrige

Quand quelqu'un dit "tout le monde a intérêt à coopérer" ou "personne ne comprend pourquoi ça reste bloqué", la méthode demande : quel est l'équilibre de Nash de cette situation ? Un système peut rester dans un état sous-optimal non pas parce que les acteurs sont stupides ou malveillants, mais parce que cet état est stable — aucun d'eux ne peut unilatéralement en sortir sans se retrouver moins bien. Ça corrige la confusion entre ce qui est souhaitable collectivement et ce qui est stable individuellement.

## Quand l'invoquer

- Quand une situation semble bloquée sans qu'on comprenne pourquoi personne ne bouge
- Sur des décisions où l'outcome dépend de ce que font les autres acteurs (concurrence, négociation, standards)
- Pour anticiper les réactions d'adversaires ou de partenaires à une décision stratégique
- Quand on veut concevoir une règle ou un mécanisme qui change les comportements — pas juste les recommander

## Quand ne pas l'invoquer

- Si les acteurs ne sont pas rationnels ou si les motivations sont fortement non-économiques
- Sur des décisions individuelles sans dimension stratégique (pas d'autres joueurs dont les choix influencent le résultat)
- Quand l'information sur les gains des autres acteurs est trop incomplète pour modéliser quoi que ce soit d'utile

## Cas d'usage

### 1. Guerre des prix dans un duopole

**Contexte :** Deux acteurs dominants dans un marché réduisent leurs prix de façon répétée, érodant leurs marges à tous les deux.

**Input :** "On est dans une guerre des prix avec notre concurrent principal — personne ne gagne, mais personne n'arrête."

**Ce que le skill produit :** "Joueurs : vous, le concurrent. Stratégies : maintenir le prix, baisser le prix. Gains : si vous montez seul, vous perdez des parts de marché. Si vous maintenez tous les deux, les marges sont acceptables. Équilibre de Nash : baisser, parce que quelle que soit la stratégie de l'autre, baisser est moins risqué individuellement. Optimum collectif : maintenir les prix — personne ne le fait parce que ce n'est pas l'équilibre. Mécanisme de sortie : un signal public d'intention (annonce de prix), une coordination via un standard industriel, ou une fusion. Sans mécanisme, l'équilibre ne bouge pas."

### 2. Adoption d'un standard technique

**Contexte :** Plusieurs acteurs d'un marché hésitent à adopter un nouveau protocole — tous attendent que les autres bougent en premier.

**Input :** "Tout le monde reconnaît que le standard serait meilleur pour l'écosystème, mais personne n'est le premier à migrer."

**Ce que le skill produit :** "Carte du jeu : adopter ou attendre. Gains : migrer seul coûte cher en développement et en compatibilité. Migrer quand les autres ont migré est moins coûteux. Ne pas migrer quand les autres ont migré : isolation. Équilibre actuel : attendre (stratégie dominante à court terme). Optimum collectif : migrer ensemble. L'écart s'explique par le coût d'être premier adoptant. Mécanisme de sortie : engagement coordonné (consortium), subvention au premier adoptant, ou acteur assez grand pour rendre la migration rentable seul et entraîner les autres."

### 3. Négociation salariale dans une équipe

**Contexte :** Des employés savent qu'ils pourraient négocier collectivement, mais chacun craint d'être le seul à demander.

**Input :** "Tout le monde pense être sous-payé mais personne ne demande d'augmentation — on se retrouve tous dans la même situation."

**Ce que le skill produit :** "Joueurs : chaque employé individuellement. Stratégies : demander, ne pas demander. Gains : demander seul = risque perçu de représailles ou de refus gênant. Ne pas demander = statu quo. Équilibre de Nash : ne pas demander (chacun attend que les autres bougent). Optimum collectif : négociation coordonnée ou transparence salariale. Le mécanisme de sortie est un changement des règles du jeu — transparence salariale entre collègues ou représentation collective — pas une incitation individuelle à la prise de risque."

## Limites de l'encodage

L'hypothèse de rationalité est un modèle, pas une description du monde réel — les gens font des choix sous-optimaux pour des raisons émotionnelles, idéologiques ou par manque d'information, et le skill ne capte pas ça. Modéliser les gains est souvent le travail le plus difficile : ce que les acteurs optimisent vraiment (réputation, évitement du conflit, loyauté) est rarement observable directement. Le skill fonctionne mieux sur des jeux à deux ou trois joueurs avec des stratégies clairement délimitées — les situations réelles sont souvent plus complexes. Combiner avec Adam Smith pour l'analyse des incitations et avec Machiavel pour les rapports de force qui ne se réduisent pas à des équilibres stables.
