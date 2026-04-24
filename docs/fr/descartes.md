# Descartes — Rendre explicites les hypothèses implicites

## Pourquoi cet encodage ?

Les décisions irréversibles échouent rarement parce que le raisonnement visible était faux. Elles échouent parce qu'une hypothèse implicite — non formulée, donc jamais vérifiée — s'est révélée fausse après qu'il était trop tard pour revenir en arrière. L'encodage de Descartes ne produit pas "doute tout", ce qui serait paralysant. Il produit une opération précise : rendre la liste des hypothèses implicites explicite, les classer par niveau de certitude, et marquer les conclusions qui ne tiennent que sur des hypothèses non vérifiées.

## Ce que la méthode corrige

Quand quelqu'un dit "on part du principe que..." ou "c'est évident que..." ou "tout le monde sait que...", la méthode demande : est-ce vraiment établi, ou est-ce une hypothèse habillée en certitude ? Elle corrige la confusion entre ce qui résiste au doute et ce qui n'a simplement jamais été mis en doute. Ce sont deux choses très différentes.

## Quand l'invoquer

- Avant toute décision irréversible — acquisition, architecture technique, modèle de revenus
- Quand un raisonnement repose sur des hypothèses présentées comme des évidences
- Quand quelqu'un dit "on a toujours fait comme ça" comme argument
- Quand un plan enchaîne plusieurs hypothèses sans les rendre explicites

## Quand ne pas l'invoquer

- Quand agir sous incertitude est inévitable et que le doute prolongé a un coût réel
- Sur des décisions réversibles à faibles enjeux — la méthode est disproportionnée
- Quand la connaissance repose nécessairement sur la pratique communautaire — certaines certitudes ne sont pas reconstruibles par le doute individuel

## Cas d'usage

### 1. Décision d'architecture technique

**Contexte :** Une équipe choisit une architecture microservices pour un produit en early stage.

**Input :** "On va construire en microservices dès le début — c'est le standard aujourd'hui."

**Ce que le skill produit :** "Hypothèses implicites : (1) l'équipe est assez grande pour opérer des microservices, (2) le domaine est suffisamment stable pour découper les services correctement maintenant, (3) la complexité opérationnelle ajoutée vaut le gain de scalabilité. — Pour chacune : est-ce établi ou supposé ? Hypothèse 1 : combien êtes-vous ? Hypothèse 2 : connaissez-vous assez bien le domaine pour découper maintenant ? Hypothèse 3 : avez-vous atteint les limites d'un monolithe ?"

### 2. Plan de lancement produit

**Contexte :** Une équipe prévoit un lancement basé sur une hypothèse de croissance organique.

**Input :** "Notre plan repose sur la croissance organique — les utilisateurs vont recommander le produit naturellement."

**Ce que le skill produit :** "Hypothèses implicites : (1) le produit génère suffisamment de valeur pour motiver une recommandation spontanée, (2) il existe un mécanisme de recommandation naturel dans ce marché, (3) la croissance organique seule est suffisante dans le timing visé. — Laquelle de ces trois hypothèses est la plus fragile ? Sur quoi repose-t-elle ? Qu'est-ce qui se passe si elle est fausse ?"

### 3. Décision de recrutement stratégique

**Contexte :** Une startup veut recruter un directeur des ventes "enterprise" avant d'avoir des clients enterprise.

**Input :** "On va recruter un VP Sales enterprise maintenant — ça va nous ouvrir ce marché."

**Ce que le skill produit :** "Hypothèses implicites : (1) le produit est prêt pour l'enterprise, (2) un VP Sales peut ouvrir ce marché sans que l'offre soit complète, (3) on peut conserver ce profil le temps que le marché soit vraiment prêt. — Chacune de ces hypothèses est-elle établie ou supposée ? Si l'hypothèse 1 est fausse, qu'est-ce que ça coûte ?"

## Limites de l'encodage

Le doute radical est utile mais artificiel — en pratique, on ne peut pas tout remettre en question simultanément sans se paralyser. Le critère de "clarté et distinction" que Descartes applique pour valider une certitude est lui-même subjectif : ce qui est clair pour l'un ne l'est pas pour l'autre. La méthode reconstruit mal les connaissances qui dépendent du contexte ou de la pratique collective — certaines certitudes ne sont pas isolables par le doute individuel, elles tiennent dans un système partagé.
