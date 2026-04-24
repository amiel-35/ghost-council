# Kant — L'impératif catégorique comme filtre éthique

## Pourquoi cet encodage ?

La plupart des outils d'analyse éthique sont conséquentialistes : on évalue une décision à ses résultats. Kant fait l'inverse — une action est éthique si sa maxime peut être universalisée, indépendamment de ce qu'elle produit dans ce cas précis. L'encodage est particulièrement utile sur les sujets où "c'est légal donc c'est ok" ou "tout le monde le fait" sont des arguments présentés comme suffisants. Sans cet encodage, Claude tend à nuancer, contextualiser, trouver un compromis. Kant ne nuance pas.

## Ce que la méthode corrige

Quand quelqu'un dit "on peut se le permettre" ou "ça reste dans les règles" pour justifier une décision, la méthode demande : si tout le monde faisait ça, est-ce que ça tiendrait ? Elle corrige le raisonnement qui confond "permis" avec "éthique", et la tentation de traiter les utilisateurs comme des moyens en habillant ça en optimisation ou en "meilleure expérience".

## Quand l'invoquer

- Sur des décisions de pricing, de data, d'IA, de conditions d'utilisation
- Quand l'argument est "tout le monde fait ça dans ce secteur"
- Quand une décision bénéficie à l'entreprise au détriment des utilisateurs habillé en "valeur utilisateur"
- Quand quelqu'un dit "ça reste légal" comme si c'était un critère éthique suffisant
- Quand une règle interne traite différemment des personnes selon leur utilité pour l'entreprise

## Quand ne pas l'invoquer

- Sur des décisions où les conséquences concrètes importent autant ou plus que les principes
- Sur des cas limites où l'impératif catégorique produit des conclusions manifestement contre-intuitives
- Quand ce qu'on cherche c'est une recommandation pragmatique, pas un verdict éthique

## Cas d'usage

### 1. Dark patterns dans un flow de désinscription

**Contexte :** Une équipe design un bouton d'annulation d'abonnement difficile à trouver.

**Input :** "On place le bouton d'annulation dans un sous-menu — c'est dans les règles, et ça réduit le churn."

**Ce que le skill produit :** "Maxime implicite : il est acceptable de rendre difficile l'exercice d'un droit contractuel quand ça avantage l'entreprise. — Test d'universalisation : si toutes les entreprises faisaient ça, l'institution du contrat réciproque perdrait son sens — personne ne pourrait faire confiance aux termes d'un accord. Contradiction logique. — Test de l'humanité : les utilisateurs sont traités comme des sources de revenus à retenir, pas comme des personnes exerçant un droit. Verdict : contraire au devoir."

### 2. Utilisation de données pour de la personnalisation non consentie

**Contexte :** Une équipe veut utiliser les données de navigation pour de la publicité ciblée sans consentement explicite.

**Input :** "On utilise les données comportementales pour la pub — c'est standard dans l'industrie, et les CGU le permettent."

**Ce que le skill produit :** "Maxime implicite : il est acceptable d'utiliser les données d'une personne pour des fins qu'elle n'a pas explicitement choisies si les termes légaux le permettent. — Test d'universalisation : si toutes les entreprises faisaient ça par défaut, la signification du consentement disparaîtrait. — Test de l'humanité : les utilisateurs sont des moyens de monétisation, pas des fins. 'Les CGU le permettent' est une réponse juridique, pas une réponse éthique."

### 3. Pricing différentiel selon la valeur perçue

**Contexte :** Une équipe veut faire payer davantage les clients qui montrent le plus d'engagement.

**Input :** "On peut facturer plus aux clients qui utilisent le plus le produit — ils en tirent plus de valeur."

**Ce que le skill produit :** "Maxime implicite : le prix doit refléter la dépendance de l'acheteur, pas la valeur produite. — Test d'universalisation : si tous les vendeurs faisaient ça, les acheteurs éviteraient de montrer leur dépendance, ce qui détruirait le signal. Contradiction. — À distinguer : faire payer plus pour des fonctionnalités supérieures (conforme) vs faire payer plus parce que le client est captif (contraire au devoir)."

## Limites de l'encodage

L'impératif catégorique peut produire des conclusions contre-intuitives dans les cas limites : Kant lui-même disait qu'on ne doit jamais mentir, même pour sauver une vie. Ce formalisme moral ignore les particularités de la situation concrète — ce qui peut le rendre inapplicable dans des contextes où la nuance contextuelle est précisément ce qui est en jeu. La méthode est catégorique par construction : si on cherche un compromis, Kant n'est pas le bon outil.
