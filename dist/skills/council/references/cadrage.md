# Préparer le cadrage

À lire avant d'écrire `CADRAGE.md` et `GRILLE.md`. Le cadrage est la pièce la plus
susceptible de fausser un conseil : chaque angle part de lui, en contexte vierge, et
reprend sans le savoir tout ce qu'il pose comme acquis.

> Règles de cadrage en partie adaptées de `references/dossier-guide.md` et
> `references/facilitation.md` d'advisory-council 0.2.1 (nzanepro, MIT), complétées par
> ce que les premières séances réelles de `council` ont montré.

## Ce que lisent les angles, et ce qu'ils ne lisent pas

| Fichier | Qui le lit | Ce qu'il contient |
|---|---|---|
| `CADRAGE.md` | les angles, le relecteur, l'arbitre | la question, les faits sourcés, les sources autorisées, les options |
| `GRILLE.md` | le décideur, le relecteur, l'arbitre ; **jamais les angles** | la grille validée, ce que couvre chaque angle, les angles écartés, le penchant du décideur |

Tout ce qui dit pourquoi un angle siège, ce qu'on attend de lui ou ce que le décideur
espère va dans `GRILLE.md`. Les briefs des angles l'interdisent.

## Les fuites à éviter

1. **Le penchant du décideur visible des angles.** Un angle contradicteur (le dixième
   homme) attaque alors la position annoncée, pas le consensus qui se forme vraiment. Le
   penchant va dans `GRILLE.md` §4 : le relecteur vérifie qu'il ne fuit pas, l'arbitre
   s'en sert pour tester la synthèse (« se lirait-elle pareil si le décideur avait voulu
   l'inverse ? »).
2. **La raison d'être d'un angle écrite comme une thèse.** « Pascal : un essai coûte
   peu, une généralisation engage beaucoup » est une conclusion soufflée ; on la
   retrouve ensuite dans plusieurs avis, qui ne l'ont pas trouvée eux-mêmes. Dans
   `GRILLE.md` §2, écrire ce que l'angle **couvre** (« la décision sous incertitude »)
   et jamais ce qu'il devrait **trouver**.
3. **Désigner d'avance le rôle d'un angle.** « L'angle qui a intérêt à ne rien faire,
   c'est l'Humain » oriente l'Humain. Ce choix se fait dans la grille, il ne s'annonce
   pas aux angles.
4. **Un fait écrit de mémoire.** Un fait faux dans le cadrage, et c'est chaque angle
   qui le relève au lieu de travailler. Un fait du cadrage se recopie depuis sa source,
   relue au moment d'écrire, et porte cette source.

## Règles du cadrage

1. **Un titre de séance neutre** (`--title`) : il apparaît en tête de chaque fichier que
   lisent les angles. « Offre payante », pas « Lancer l'offre payante ».
2. **Une question fermée et neutre.** « Faut-il X, et pour qui ? », pas « Comment
   déployer X ? ». Pas de verdict, pas de « c'est réglé », pas de « la seule question
   qui reste ».
3. **Pas d'urgence.** Une échéance est un fait (« décision au plus tard fin novembre ») ;
   l'impatience ou la fatigue du décideur n'en sont pas.
4. **Toutes les options vivantes, dont « ne rien faire »**, chacune avec ce qu'elle
   engage ou transmet, en faits. Juger si c'est réversible est le travail des angles.
   Une option absente parce qu'on ne l'aime pas est une fuite.
5. **Des faits, avec leur source et leur date.** Un chiffre dit ce qu'il est : un point
   ou une moyenne, une mesure ou une estimation, une source unique ou recoupée. Ce qui
   vient d'une seule source orale le dit.
6. **Ce qu'on ne sait pas, dit comme tel**, avec l'endroit où on l'a cherché.
7. **Des sources autorisées précises**, et seulement celles-là. Les avis déjà rendus sur
   la même question (séance précédente, notes d'avis) n'y figurent jamais : ce serait
   donner aux angles ce que d'autres ont pensé.
8. **Une source qui mêle faits et avis déjà rendus** (un journal de suivi, des notes de
   préparation) ne s'autorise pas aux angles, même par passages : recopier les faits
   utiles dans le cadrage, avec leur source, et réserver le fichier au relecteur et à
   l'arbitre.
9. **Aucune position d'angle**, même d'une séance précédente : un résultat antérieur
   entre comme un fait sourcé, pas comme un avis.

## La grille

- **Couvrir, pas empiler.** Chaque angle doit pouvoir arriver à une conclusion différente
  des autres, ou regarder d'autres faits. Deux angles qui raisonneraient pareil sur les
  mêmes faits n'en font qu'un.
- **Trois sièges à vérifier** avant de proposer la grille :
  - un angle qui a intérêt à **ne rien faire** (ou à faire moins, ou plus tard) ;
  - un angle pour **la partie qui a le moins de voix** (ceux qui vivront la décision sans
    l'avoir prise) ;
  - un angle qui **défend l'option** sérieusement, faute de quoi la grille penche d'un
    seul côté.
- **Le contradicteur du tour 1** ne connaît pas le consensus, puisque personne n'a encore
  parlé. Un `ix:dixieme-homme` au tour 1 plaide contre la thèse qu'il devine ; c'est utile
  si la grille le sait. Pour un vrai contre-consensus, il sert mieux au tour 2 d'une
  `deliberation`.
- **Chaque question du cadrage a au moins un angle capable d'y répondre** : une question
  de droit sans angle juridique reviendra par une autre porte, plus tard et plus cher.

## Les parties prenantes

Une partie (`partie:<id>`) est quelqu'un que la décision touche, vu de sa place : ce
qu'elle gagne ou perd, ce qu'elle sait, ce qu'elle ne voit pas. Pour les trouver :

- **qui gagne** si l'option passe, et **qui paie** ;
- **qui opère** ou vivra la décision au quotidien ;
- **qui peut la bloquer** ;
- **qui est lésé sans bruit**, la partie qui a le moins de voix ;
- **qui est de l'autre côté de la table** (le client, l'acheteur, le partenaire) : c'est
  souvent l'angle qui manque le plus, parce que le décideur ne s'y met jamais.

Chaque fiche se remplit avant la relecture. Elle décrit un mandat et des intérêts,
jamais une conclusion (« le client pense qu'il faut… » est une fuite). Un rôle, pas
une personne réelle : « l'acheteur du groupe client », pas son nom. Une partie dont le
poids est plus lourd que les autres (ceux qui vivront la décision au quotidien, par
exemple) se dit dans
`GRILLE.md` §2, pas dans sa fiche.

## La relecture

Une fois `CADRAGE.md` et `GRILLE.md` écrits, et la grille validée, un relecteur isolé,
sans angle et sans position, lit les deux et écrit `RELECTURE.md` :
fuites, prémisses semées, faits vérifiés contre leur source, ce qui manque, corrections
demandées. Le tour ne part que sur `**Verdict de relecture :** prêt`. Sur « à corriger »,
l'organisateur corrige le cadrage et relance la relecture (`council.py brief SEANCE
relecture`) : elle réécrit `RELECTURE.md`.

**Deux relectures au plus.** Un cadrage parfaitement neutre n'existe pas, surtout quand
les sources du décideur sont écrites en vue de son option, et chaque relecture a un
coût. Si la seconde rend encore « à corriger », l'organisateur applique ce qui peut
l'être, écrit dans `GRILLE.md` §6 les corrections non faites et pourquoi, et le décideur
lève le verrou : `**Relecture levée par :** <qui>, réserves en §6`. L'arbitre lit ces
réserves et en tient compte.

Le test final avant de lancer le tour : un angle qui lirait `CADRAGE.md` pourrait-il
deviner ce que le décideur espère ? Si oui, ce n'est pas prêt.
