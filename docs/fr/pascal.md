# Pascal — Le poids des enjeux sous incertitude

## Pourquoi cet encodage ?

Les décisions irréversibles à forts enjeux ne peuvent pas être traitées comme des paris symétriques. "C'est peu probable donc on ne s'en inquiète pas" est un raisonnement qui ignore l'asymétrie des conséquences. Pascal encode l'opération inverse : forcer la confrontation avec les scénarios catastrophes improbables mais irréversibles, et calibrer la décision sur l'asymétrie des enjeux plutôt que sur la seule probabilité. Ce n'est pas de la paranoïa — c'est du risk assessment philosophique.

## Ce que la méthode corrige

Quand quelqu'un dit "dans le pire des cas on verra" ou "c'est peu probable donc", la méthode demande : quelle est la conséquence si tu as tort et que l'enjeu est maximal ? Elle corrige la confusion entre probabilité faible et enjeu faible — des choses qui arrivent rarement peuvent avoir des conséquences non récupérables.

## Quand l'invoquer

- Sur des décisions irréversibles : architecture technique, engagement contractuel long terme, décision légale
- Quand un scénario catastrophe est écarté uniquement parce qu'il est "peu probable"
- Quand quelqu'un dit "si ça foire on verra" sans avoir évalué le coût de ce scénario
- Quand les options ont des asymétries de conséquences très différentes

## Quand ne pas l'invoquer

- Sur des décisions réversibles à faibles enjeux — la méthode est disproportionnée
- Quand le risque dominant est l'inaction, pas l'action imprudente
- Quand les probabilités sont bien établies et les enjeux symétriques

## Cas d'usage

### 1. Choix d'architecture de données

**Contexte :** Une startup doit choisir entre stocker des données sensibles en interne ou en déléguer la gestion.

**Input :** "On va gérer les données de santé en interne — c'est peu probable qu'on ait un incident de sécurité."

**Ce que le skill produit :** "Matrice : si on gère en interne et qu'il n'y a pas d'incident — économie sur les coûts de délégation. Si on gère en interne et qu'il y a un incident — violation RGPD, perte de confiance, potentiel liquidation. Si on délègue et tout va bien — coût de délégation. Si on délègue et incident chez le prestataire — responsabilité partagée, isolation meilleure. — L'asymétrie des enjeux : le scénario 'gestion interne + incident' est irréversible. La probabilité importe moins que la récupérabilité."

### 2. Engagement contractuel avec un fournisseur unique

**Contexte :** Une équipe veut signer un contrat 3 ans avec un fournisseur critique.

**Input :** "On signe pour 3 ans — le fournisseur est solide, c'est peu probable qu'il y ait un problème."

**Ce que le skill produit :** "Scénario catastrophe : le fournisseur est racheté, change de politique, ou fait faillite dans les 3 ans. Coût : migration forcée sous pression, sans alternatives disponibles immédiatement. — Est-ce que ce scénario est irréversible ? Oui. — Quelle est la conséquence si tu as tort sur la solidité du fournisseur ? — Recommandation : si les enjeux sont assez élevés, l'architecture de l'accord doit intégrer une clause de sortie ou une alternative, indépendamment de la probabilité estimée."

### 3. Décision de non-communication sur un risque produit

**Contexte :** Une équipe découvre un bug potentiellement impactant et hésite à communiquer.

**Input :** "On ne communique pas proactivement sur le bug — c'est peu probable qu'il soit déclenché dans des conditions réelles."

**Ce que le skill produit :** "Deux scénarios : tu ne communiques pas, le bug n'est pas déclenché — rien ne se passe. Tu ne communiques pas, le bug est déclenché par un utilisateur — perte de confiance, potentiellement irréversible si l'impact est critique. — Asymétrie : le coût de la communication proactive est limité. Le coût de la non-communication si le bug est déclenché peut être très élevé. La probabilité n'est pas le seul facteur dans une décision irréversible."

## Limites de l'encodage

L'argument du pari justifie une posture pratique, pas une vérité — ne pas confondre "il est rationnel de se comporter comme si le risque était réel" avec "le risque est réel". Mal calibré, le skill peut légitimer des décisions basées sur la peur d'un scénario catastrophe hautement improbable dont les enjeux sont surestimés. Il suppose aussi que les options sont exhaustives et mutuellement exclusives, ce qui est rarement le cas — il y a souvent des options intermédiaires entre "risquer" et "ne pas risquer".
