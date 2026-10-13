# council — Faire délibérer les méthodes avant de décider

> Fiche courte. Pour l'installation, les définitions détaillées des costumes et des parties, les formats et le script : le [guide complet du conseil](../council/README.md).

## Pourquoi cet encodage ?

Chaque ghost de la collection applique une méthode à un problème. Mais une décision qui engage gagne rarement à n'être lue que par une seule méthode : Popper cherche ce qui réfute, Pascal pèse l'asymétrie des enjeux, Machiavel lit les rapports de force, et aucun ne voit ce que voient les autres. `council` encode l'opération qui les fait travailler ensemble sans les mélanger : chaque angle travaille seul, en contexte vierge, puis un arbitre rend la carte de ce qui converge et de ce qui s'oppose.

Ce n'est pas une méthode philosophique, c'est une procédure. Sa seule variable qui compte est l'indépendance des avis : un avis qui a lu les autres, ou qui a deviné ce que le décideur espère, n'est plus un avis, c'est un écho. Tout le reste (la séparation du cadrage et de la grille, la relecture du cadrage avant le tour, l'interdiction d'ouvrir les avis des autres) sert à protéger cette indépendance.

## Ce que la méthode corrige

Quand on demande à un même interlocuteur « quels sont les pour et les contre », on obtient une synthèse lisse qui reflète surtout la façon dont la question a été posée. `council` corrige ça de trois façons. Les angles ne se lisent pas entre eux, donc le premier à parler n'ancre pas les autres. Le cadrage est relu par un lecteur isolé qui cherche les fuites (le penchant du décideur, une prémisse posée comme acquise, un fait écrit de mémoire) avant que le tour parte. Et l'arbitre ne tranche pas : il rend le désaccord intact, avec ce qui fonde chaque camp et le résultat qui ferait bouger chacun.

Quand quelqu'un dit « on en a parlé, tout le monde était d'accord », `council` demande : d'accord sur la même prémisse, ou d'accord par des chemins différents ? Seul le second est un signal.

## Quand l'invoquer

- Avant une décision qui engage et qu'on ne pourra pas défaire facilement : un prix, un engagement, une orientation, un recrutement, un investissement
- Quand on sent qu'on a déjà sa réponse et qu'on veut savoir ce qu'elle laisse de côté
- Quand plusieurs dimensions s'affrontent (argent, personnes, droit, timing) et qu'on risque d'en oublier une
- Pour comparer deux cadres de pensée sur la même question (`--format compare`), ou pour une délibération complète avec dossier commun et vérificateur (`--format deliberation`)

## Quand ne pas l'invoquer

- Pour une décision réversible à faible coût : le rituel coûte plus que l'erreur qu'il évite
- Quand la décision bute sur une donnée manquante : aller la chercher coûte moins cher que faire délibérer six avis sur du vide
- Sur un sujet réglementé, juridique ou médical, à la place d'un expert réel : le conseil éclaire, il n'engage personne
- Pour critiquer un texte déjà écrit ou choisir entre des options déjà notées sur des critères connus : d'autres outils font ça mieux

## Cas d'usage

### 1. Lancer une offre payante

**Contexte :** Une petite équipe produit hésite à passer son outil gratuit en freemium avant la fin de l'année. Le fondateur penche pour le faire.

**Input :** la demande « Faut-il passer en freemium avant la fin de l'année ? », grille proposée par l'organisateur et validée par le fondateur : `ghost:popper`, `costume:financier`, `costume:humain`, `partie:utilisateur-actuel`, `ix:expansionist`, arbitre `adversarial`. Le penchant du fondateur va dans `GRILLE.md`, que les angles ne lisent pas.

**Ce que le skill produit :** Une relecture du cadrage qui signale d'abord que la question embarque l'échéance (« avant la fin de l'année ») comme si elle était imposée, alors que c'est un choix interne : la question est reformulée. Puis cinq avis indépendants et une synthèse : les angles convergent sur le fait que la conversion n'a jamais été mesurée (Popper et le Financier y arrivent par deux chemins différents, signal fort) ; ils s'opposent sur ce que perd l'utilisateur actuel (la partie prenante) contre ce que gagne l'équipe (l'expansionist). La question à trancher est formulée pour être décidable, avec la première étape : mesurer sur un segment avant de généraliser, et le seuil de conversion qui ferait basculer.

### 2. Comparer deux cadres sur une réorganisation

**Contexte :** Une direction veut fusionner deux équipes. Deux managers voient le même projet de façons opposées, sans arriver à dire pourquoi.

**Input :** la demande « Fusionner les deux équipes au prochain trimestre ? », au format `compare`, avec `ghost:marx` et `ghost:adam-smith`.

**Ce que le skill produit :** Deux avis côte à côte, puis, écrit par un lecteur isolé, ce que la divergence révèle, posé comme une question : « Les deux lectures ne s'opposent pas sur la fusion mais sur ce qui fait tenir une équipe : un rapport de pouvoir à rééquilibrer, ou un mécanisme d'incitation à réaligner. Lequel des deux a cassé, ici ? » Pas de verdict : la tension rendue visible.

### 3. Une décision lourde qui bute sur des faits

**Contexte :** Une association hésite à acheter son local plutôt que de continuer à louer. Les chiffres circulent, mais personne ne sait lesquels sont justes.

**Input :** la demande « Acheter le local ou rester locataire ? », au format `deliberation`, avec sept angles dont `costume:juridique`, `partie:benevoles` et `ghost:pascal`.

**Ce que le skill produit :** Un dossier commun écrit avant le tour, avec ses faits sourcés et ce qu'on ne sait pas ; un vérificateur sans angle qui contrôle chaque chiffre porteur contre sa source et publie ses corrections en addenda (« le loyer cité est celui de l'an dernier ») ; un premier tour indépendant, un bilan à options lettrées, un second tour où chaque angle répond aux autres et vote ; puis une synthèse avec le vote, la dissidence sous sa forme la plus forte, et pour chaque prochaine étape le résultat qui changerait la décision.

## Limites de l'encodage

L'indépendance a un plafond. Si tous les avis viennent du même modèle, ils partagent ses angles morts ; varier le modèle par siège décorrèle un peu, jamais complètement. Un conseil de six angles du même modèle reste une seule intelligence qui change de chapeau, avec des précautions.

Le cadrage reste la pièce la plus fragile. La relecture attrape beaucoup de fuites, mais un cadrage parfaitement neutre n'existe pas, surtout quand les sources du décideur ont été écrites en vue de son option. La méthode borne donc la relecture à deux passes, puis demande au décideur de lever le verrou en notant les réserves. Ces réserves doivent être lues : un conseil dont le cadrage fuyait rend une carte inclinée.

Les angles pèsent les faits, pas les valeurs de celui qui décide. Un conseil peut déconseiller unanimement ce que le décideur fera quand même, pour une raison qu'aucun angle n'avait, parce qu'elle tient à ce qui compte pour lui et qu'on ne la lui a pas demandée. Le conseil éclaire, il ne remplace pas le jugement ; il faut le savoir en lisant une unanimité. Une piste est notée pour la suite : une section « ce qui compte pour le décideur » dans `GRILLE.md`, lue par l'arbitre.

Le coût est réel : une séance `tour` de six angles, c'est une dizaine d'exécutions avec la relecture et l'arbitre ; une `deliberation` complète en fait le double. À réserver aux décisions qui le valent.
