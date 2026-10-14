---
name: council
license: MIT (parties reprises d'advisory-council, nzanepro, voir THIRD_PARTY.md)
description: >
  Fait délibérer des angles indépendants sur une décision avant qu'elle soit prise,
  puis un arbitre rend la carte des désaccords : le conseil ne tranche pas, l'humain
  décide. Angles au choix, pris dans plusieurs bibliothèques (ghosts de cette
  collection, postures d'ix-skills, costumes métier, n'importe quel SKILL.md) ;
  format au choix (tour simple, comparaison de deux angles, délibération complète
  avec dossier et vérificateur) ; arbitre au choix (neutre par défaut, adversarial,
  Zeus, Nash, Aristote...). Déclenche sur "/council", "fais délibérer",
  "réunis un conseil", "passe ça au conseil", "pèse cette décision avec plusieurs
  angles", "compare Popper et Hegel sur...", "avant de trancher, je veux les
  désaccords". Ne sert pas à critiquer un texte déjà écrit ni à choisir entre des
  options déjà posées sur des critères connus.
---

# council : peser une décision avant de la prendre

## Rôle

Organiser un tour de table sur une décision **non encore prise**, puis en faire
restituer la carte des désaccords par un arbitre.

Ce qui fait la valeur du geste n'est pas le nombre d'avis, c'est leur
**indépendance**, et le fait de s'arrêter de produire pour peser. Distinct des
voisins : une critique attaque un contenu déjà écrit, une décision tranche entre
des options déjà posées, une exploration ouvre le champ. `council` fait délibérer
plusieurs angles indépendants sur une même question et rend le désaccord visible.

Tu es l'**organisateur** : tu cadres, tu fais valider la grille, tu lances les
angles et l'arbitre, tu tiens la séance. Tu n'écris aucun avis et tu n'arbitres pas.

## Règles absolues

1. **Chaque angle travaille en contexte vierge.** Un avis produit dans le fil qui a
   formulé la question hérite de son biais : c'est l'auteur qui se relit. Sans
   indépendance, un conseil est un écho.
2. **Un angle par avis.** Empiler deux angles sur un avis produit une réponse molle
   qui n'assume ni l'un ni l'autre.
3. **Aucun angle ne reçoit la réponse attendue.** Ni ce qu'on espère, ni ce que les
   autres ont dit. En `deliberation`, les corrections factuelles publiées en addenda
   sont des faits, pas des avis : elles se lisent, sans dire quel angle les a trouvées.
4. **La grille se valide avant le tour.** C'est la décision de celui qui décide,
   donc c'est sa grille.
5. **L'arbitre n'est pas l'organisateur, et il est toujours nommé dans la
   restitution.** Celui qui a rédigé les briefs pondérerait vers ce qu'il attendait.
6. **Le désaccord se restitue intact.** L'information est dans l'écart entre les
   angles. Un conseil lissé ne sert à rien.
7. **Le conseil ne tranche jamais.** Il éclaire, l'humain décide.
8. **Un angle est une méthode, pas une personne.** Pas de fiche, pas de mémoire,
   pas de citation inventée attribuée à une personne réelle. Pour une posture
   inspirée d'un vivant, l'angle porte le nom de la posture (« arbitre brutal »),
   jamais celui de la personne.

## Les angles

Tout skill qui porte une façon de penser fait un angle valide. Un angle se donne
par une **référence**, que le script résout en chemin à lire :

| Référence | Ce que c'est | Résolu vers |
|---|---|---|
| `ghost:popper` | un ghost de cette collection : une méthode philosophique | `skills/popper/SKILL.md`, à côté de ce skill |
| `ix:dixieme-homme` | une posture d'ix-skills (`dixieme-homme`, `contrarian`, `red-team`, `key-assumptions`, `firstprinciples`, `outside-in`, `executor`, `expansionist`, `outsider`...) | le premier dossier qui l'a dans `COUNCIL_ANGLES_PATH` (défaut : le cache du plugin ix-skills, quelle que soit sa marketplace, version la plus haute) |
| `costume:humain` | une dimension métier qu'on risque d'oublier | la section `## Humain` de `references/angles/costumes.md` |
| `partie:client` | une partie prenante : quelqu'un que la décision touche (qui gagne, paie, opère, bloque, subit) | sa fiche `## client` dans `PARTIES.md`, écrite pour la séance |
| `file:<chemin>` | n'importe quel SKILL.md | ce fichier |

Sans préfixe, le script cherche dans l'ordre `ghost:`, `costume:`, `ix:`. Une partie
se donne toujours avec son préfixe. Une
référence introuvable arrête l'`init` avec un message qui dit où il a cherché :
jamais en pleine séance.

Le brief de chaque angle donne **le chemin à lire**, jamais « applique la méthode
X » : ça marche même si le plugin n'est pas installé chez le worker, et avec un
autre modèle.

**Quelle famille.** Conséquences éparpillées : des costumes (la couverture).
Pari ou choix de direction : des postures et des ghosts (la profondeur, ils
attaquent le raisonnement lui-même). Décision qui touche des gens précis : des
parties (les intérêts réels). Décision lourde : un mélange.

**Les parties prenantes.** Une partie n'a pas de bibliothèque : elle change à chaque
décision. `init` crée dans `PARTIES.md` une fiche par `partie:<id>` (qui, mandat, ce
qu'elle gagne ou perd, ce qu'elle sait, priorités, angles morts, lignes rouges, ce qui
la ferait changer d'avis), que l'organisateur remplit avant la relecture. Chaque partie
ne lit que sa fiche ; les autres angles ne l'ouvrent pas. Une partie est un rôle ou un
type d'acteur, jamais une personne réelle nommée, et sa fiche décrit une position, pas
la conclusion qu'elle devrait tirer. Le costume
`humain` est le plus souvent oublié et le plus souvent décisif.

**Trois sièges à vérifier.** Un angle qui a intérêt à ne rien faire (souvent
`costume:financier` ou `ix:executor`), un angle pour la partie qui a le moins de voix
(souvent `costume:humain`), et un angle qui défend l'option sérieusement (souvent
`ix:expansionist`) ; sans lui, la grille penche d'un seul côté. « Ne rien faire »
figure dans les options du cadrage.

**Le contradicteur.** Au tour 1, personne n'a encore parlé : un `ix:dixieme-homme`
plaide contre la thèse qu'il devine. Il devine à partir du cadrage, d'où la règle
de ne jamais y laisser le penchant du décideur.

**Taille.** Trois angles pour une question cadrée, cinq ou six pour un arbitrage
lourd, sept au plus en `deliberation`. Au-delà, la synthèse devient illisible.

## Les formats

| Format | Déroulé | Quand |
|---|---|---|
| `tour` (défaut) | cadrage, grille → relecture → avis en parallèle → arbitre | la plupart des décisions |
| `compare` | cadrage, grille → relecture → deux avis côte à côte → ce que la divergence révèle | comprendre pourquoi deux cadres voient le même problème autrement |
| `deliberation` | cadrage, grille → dossier commun → relecture → tour 1 + vérificateur → corrections → bilan à options lettrées → tour 2 → arbitre | décision lourde, peu réversible, qui bute sur des faits |

Le déroulé n'est pas codé dans le script : il est lu dans
`references/formats/<format>.json` (étapes, fichiers, dépendances, champs
obligatoires). Un format maison se passe par son chemin.

En `compare`, `--arbiter aucun` donne la pure juxtaposition ; sinon un lecteur isolé
écrit, en deux ou trois lignes, l'hypothèse que les deux angles ne partagent pas,
formulée comme une question. Paires dont la tension est productive : Popper / Hegel
(ce qui compte comme preuve), Kant / Machiavel (principe ou intérêt), Marx / Adam
Smith (idéologie ou mécanisme), Aristote / Platon (bas en haut ou haut en bas),
Sartre / Épictète (où commence l'agentivité), Darwin / Tocqueville (quel horizon).

## L'arbitre

Le choix de l'arbitre est un paramètre, pas un détail.

| `--arbiter` | Ce qu'il produit |
|---|---|
| `neutre` (défaut) | la carte fidèle des convergences et des désaccords |
| `adversarial` | ne survit que ce qui tient face à un lecteur hostile : si la conclusion tient avec un arbitre hostile, elle tient |
| `ghost:zeus` | un arbitrage depuis une juridiction ; son verdict reste un avis de plus, posé sous la carte |
| `ghost:nash` | l'arbitrage lu comme un équilibre entre positions |
| `ghost:aristote` | les convergences traitées comme des cas, généralisation minimale |

Un arbitre qui a une méthode l'applique **à l'arbitrage, pas au problème**, et
importe ses biais dans la synthèse : c'est voulu ou c'est un défaut selon ce qu'on
cherche. La synthèse a une section pour le dire, et l'arbitre y est nommé.

## Un modèle par siège

En option, chaque siège (et l'arbitre) porte son modèle : `--seat
ix:dixieme-homme@opus`, `--seat ghost:popper@codex`, `--arbiter neutre@sonnet`.

| Modèle | Comment le lancer |
|---|---|
| sans `@` | sous-agent Claude Code, modèle par défaut du sous-agent |
| `opus`, `sonnet`, `haiku` | sous-agent Claude Code (outil Agent) avec ce modèle |
| `codex` | `codex exec -s read-only --ephemeral -o <fichier> "<brief>"` |
| `gemini` | `agy -p "<brief>" --sandbox > <fichier>` |

Le script ne lance rien : il écrit le modèle dans `council.json`, et `brief --json`
rend la ligne de lancement. Les workers externes ne peuvent pas écrire de fichier :
leur brief leur demande le contenu complet sur la sortie standard, qui va
directement dans le fichier de l'avis. Tu ne retouches pas ce qu'ils rendent.

Varier le modèle décorrèle un peu les angles morts, jamais complètement.

## Méthode

Le script : `<dossier de ce skill>/scripts/council.py` ; dans les exemples ci-dessous,
`council.py` désigne ce chemin complet (un chemin relatif ne marche pas depuis un
plugin installé). Stdlib seule, n'écrase jamais un fichier, `--json` sur chaque
sous-commande. Codes de sortie : 0 si tout va bien, 1 sur erreur d'usage ou d'entrée
(le message dit quoi faire), 2 sur une commande mal formée (argparse), 3 si le
contrôle trouve un problème.

### 1. Cadrer et proposer la grille

Lire `references/cadrage.md` avant d'écrire quoi que ce soit : le cadrage est la
pièce qui fausse le plus souvent un conseil, parce que chaque angle reprend sans le
savoir ce qu'il pose comme acquis.

Reformuler la décision en **une question fermée et neutre** : une question floue
produit six avis flous. Choisir le format, les angles et l'arbitre. Les présenter au
décideur avec une phrase par angle (ce qu'il couvre que les autres ne couvrent pas),
et **attendre sa validation**. S'il conteste un angle, en changer. Lui demander s'il
penche déjà pour une option : ça se note, ça ne se montre pas aux angles.

Si la décision bute sur un chiffre inconnu, le dire : aller le chercher coûte moins
cher que faire délibérer sept avis sur du vide.

### 2. Ouvrir la séance

```bash
python3 council.py init <seance> --title "Passer en freemium" \
    --seat ghost:popper --seat ix:dixieme-homme@opus --seat costume:humain
# --format compare|deliberation, --arbiter adversarial|ghost:zeus@opus|...
```

`<seance>` est un dossier neuf dans le projet de l'utilisateur. `init` crée
`council.json` et un gabarit par fichier, marqué `<!-- council:todo -->`.

Deux fichiers, deux lecteurs :

- **`CADRAGE.md`, que lisent les angles** : la question, les faits sans lesquels on
  raisonne à faux (chacun recopié depuis sa source relue, avec cette source), les
  sources autorisées, les options dont « ne rien faire », ce qu'on ne sait pas.
  Rien sur la grille, rien sur ce que le décideur espère.
- **`GRILLE.md`, que les angles ne lisent jamais** : la grille, ce que couvre chaque
  angle (jamais ce qu'il devrait trouver), les trois sièges, le penchant du décideur,
  les angles écartés. Écrire `**Grille validée :** oui, par <qui>, le <date>`
  seulement quand c'est vrai.

Supprimer la ligne `council:todo` de chacun.

**La relecture.** Un sous-agent isolé, sans angle, lit les deux fichiers
(`brief <seance> relecture`) et écrit `RELECTURE.md` : fuites, prémisses semées,
faits vérifiés contre leur source, ce qui manque. Le tour ne part que sur
`**Verdict de relecture :** prêt` ; `brief` refuse sinon. Sur « à corriger », corriger
le cadrage et relancer la relecture, qui réécrit le fichier. **Deux relectures au
plus** : si la seconde demande encore des corrections, appliquer ce qui peut l'être,
noter le reste dans `GRILLE.md` §6, et faire lever le verrou par le décideur
(`**Relecture levée par :** <qui>, réserves en §6`).

### 3. Faire tourner les étapes

À chaque étape, `status` dit quoi faire :

```bash
python3 council.py status <seance>
python3 council.py brief <seance> avis popper     # le brief, à donner tel quel
python3 council.py brief <seance> synthese        # celui de l'arbitre
```

- **Les angles en parallèle.** Un sous-agent par angle, **tous lancés dans le même
  message**, chacun avec son brief et rien d'autre : pas de résumé de la
  conversation, pas d'indice sur ce que tu attends. Le brief dit au worker quoi lire,
  quoi ne pas ouvrir et quel fichier écrire.
- **Un worker qui échoue** ou rend un fichier vide est relancé une fois avec le même
  brief. S'il échoue encore, il manque : tu n'écris jamais son avis à sa place.
- **L'arbitre** se lance dans un sous-agent isolé, quand `status` le dit. Jamais
  toi : tu as écrit les briefs.
- `brief` refuse une étape dont la précédente n'est pas finie.

Sans sous-agents (un seul agent dans un seul contexte), l'indépendance est plus
faible : écrire tous les avis avant d'en relire aucun, dans un ordre fixé d'avance,
l'angle le plus contrarien d'abord ; ne jamais retoucher un avis déjà écrit ; et
dire dans la restitution que tous les avis viennent d'un seul contexte.

### 4. En format `deliberation`

- **La relecture vient après le dossier** : elle relit le cadrage, la grille et le
  dossier ensemble, avant que le tour 1 parte.
- **Le dossier commun** (`DOSSIER.md`) : le relevé factuel identique pour tous,
  écrit avant le tour 1 et plus jamais retouché ensuite. Question neutre, options
  dont « ne rien faire », faits sourcés, estimations avec leur méthode, ce qu'on ne
  sait pas, ce qui est déjà décidé. Jamais le penchant du décideur, qui reste dans
  `GRILLE.md`. Voir `references/dossier.md`.
- **Le vérificateur** (`brief <seance> verification`) : sans angle, sans position,
  sans vote. Il part en même temps que le tour 1 et vérifie chaque affirmation
  porteuse contre sa source primaire. C'est le siège le moins cher et celui qui
  attrape le plus d'erreurs : ne jamais le supprimer. Voir `references/verification.md`.
- **Les corrections** (`addendum <seance>`) : ce que le vérificateur a trouvé, en
  addenda numérotés qui priment sur le dossier. Corrections seulement, jamais un
  avis ni un vote.
- **Le bilan** (`BILAN-TOUR1.md`), écrit par toi quand tous les tours 1 sont là
  (`tally <seance> --step tour1` donne le tableau) : positions dans leurs mots,
  accords, désaccords consignés sans arbitrage, options lettrées dont la dissidence
  la plus forte. Tu offres des options, tu n'en recommandes aucune.
- **Le tour 2** : chaque angle lit tout, répond aux autres par leur id et vote ; un
  vote qui change nomme ce qui l'a fait changer. `tally <seance> --step tour2`
  compte les voix.

### 5. Contrôler et restituer

```bash
python3 council.py check <seance> --final
```

`check` contrôle l'ordre (pas de synthèse avant tous les avis, pas de bilan avant
la vérification), les champs obligatoires (`**Position :**`, `**Confiance :**`,
`**Vote :**`, `**Arbitre :**`), les sections de la synthèse, l'absence de vote
dans un addendum, la justification d'un vote changé. Il sort 0 quand la séance est
complète et propre. Corriger ce qu'il signale avant de restituer.

## Output attendu

Trois blocs, dans cet ordre :

1. **La grille validée** : les angles retenus et pourquoi, le format, l'arbitre.
2. **La synthèse de l'arbitre, en le nommant** : convergences (et si elles sont
   suspectes), désaccords intacts avec ce qui fonde chaque camp, ce qu'aucun angle
   n'a regardé.
3. **La question à trancher**, formulée pour être décidable, et pour chaque
   prochaine étape **le résultat qui changerait la décision**.

Les avis bruts restent dans le dossier de séance et ne sont pas déversés : ce qui
compte, c'est l'écart entre eux. Si tous les angles convergent, le dire tel quel :
ne pas simuler un désaccord.

## Limites connues

- **L'indépendance a un plafond.** Si tous les avis viennent du même modèle, ils
  partagent ses angles morts. Varier le modèle par siège décorrèle un peu, jamais
  complètement.
- **Le coût est réel.** Six angles, une ou deux relectures et un arbitre, c'est huit
  à neuf exécutions ; une délibération complète en fait le double. Réserver aux décisions qui engagent. Sur
  une question fermée à faible enjeu, un seul avis contradictoire suffit.
- **Un conseil ne remplace pas une donnée manquante.**
- **Il ne convient pas aux décisions réversibles à faible coût** : le rituel coûte
  plus que l'erreur qu'il évite.
- **Il ne remplace pas un expert réel** sur un sujet réglementé, juridique ou
  médical : il éclaire, il n'engage personne. Les angles sont simulés, pas de vraies
  parties prenantes.
- **Un arbitre à méthode importe ses biais**, d'où l'obligation de le nommer.

## Parenté

Lignée revendiquée : [llm-council](https://github.com/karpathy/llm-council) pour la
délibération multi-avis ; les travaux sur le débat multi-agents comme mécanisme de
vérité ([Du et al., 2023](https://arxiv.org/abs/2305.14325)), avec la réserve,
établie dans la littérature ultérieure, qu'un débat entre instances d'un même modèle
ne bat pas de façon fiable des méthodes plus simples à budget égal. D'où la règle
d'indépendance, qui est ici la variable qui compte.

Le script, le dossier commun, le vérificateur et le second tour sont adaptés
d'[advisory-council](https://github.com/nzanepro/tvr-skills-agent-advisory-council)
de nzanepro (MIT, voir `THIRD_PARTY.md` à la racine du dépôt et du plugin), dont on n'a pas repris
les personas parties prenantes.
