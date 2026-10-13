# Le conseil : guide complet

[English version](README.en.md) · [Fiche courte FR](../fr/council.md) · [Le skill lui-même](../../skills/council/SKILL.md)

`/council` fait délibérer plusieurs **angles indépendants** sur une décision pas encore prise, puis un **arbitre** rend la carte de ce qui converge et de ce qui s'oppose. Le conseil ne tranche pas : celui qui décide décide.

> **Expérimental.** Les avis sont simulés par un modèle de langage. Ils éclairent une décision, ils n'engagent personne et ne remplacent pas un expert réel sur un sujet juridique, médical ou réglementé.

**Sommaire**

1. [En une minute](#1-en-une-minute)
2. [Installer](#2-installer)
3. [Une séance pas à pas](#3-une-séance-pas-à-pas)
4. [Les angles : cinq familles](#4-les-angles--cinq-familles)
5. [Les formats](#5-les-formats)
6. [L'arbitre](#6-larbitre)
7. [Le cadrage, la grille et la relecture](#7-le-cadrage-la-grille-et-la-relecture)
8. [Un modèle par siège](#8-un-modèle-par-siège)
9. [Les fichiers d'une séance](#9-les-fichiers-dune-séance)
10. [Le script `council.py`](#10-le-script-councilpy)
11. [Questions fréquentes](#11-questions-fréquentes)
12. [Limites](#12-limites)

---

## 1. En une minute

Une décision qui engage gagne rarement à n'être lue que d'un seul point de vue. Le conseil en réunit plusieurs, choisis exprès pour ne pas voir la même chose, et protège une seule chose : **leur indépendance**. Chaque angle travaille seul, dans un contexte vierge, sans lire les autres et sans savoir ce que le décideur espère. Un arbitre isolé lit ensuite tous les avis et rend :

- ce sur quoi les angles convergent (et si la convergence est suspecte) ;
- où ils s'opposent vraiment, avec ce qui fonde chaque camp ;
- ce qu'aucun n'a regardé ;
- la question qui reste à trancher, et pour chaque prochaine étape le résultat qui changerait la décision.

Tu dis ce que tu veux décider. Claude, dans le rôle d'**organisateur**, cadre la question, te propose une grille d'angles, la fait valider, puis lance les angles et l'arbitre dans des sous-agents séparés. Un petit script Python tient la paperasse : il crée les fichiers, rédige le brief de chaque angle et contrôle que le processus a été respecté. Il n'appelle aucun modèle lui-même.

---

## 2. Installer

### Le plugin ghost-council (obligatoire)

Dans un terminal :

```bash
claude plugin marketplace add amiel-35/ghost-council
claude plugin install ghost-council
```

Redémarre Claude Code. Le skill `council` et tous les ghosts (Popper, Kant, Pascal…) sont alors disponibles. Mettre à jour plus tard :

```bash
claude plugin marketplace update ghost-council
claude plugin update ghost-council
```

### Le plugin ix-skills (facultatif, recommandé)

Les angles de la famille `ix:` (dixième homme, contrarian, red team…) viennent du projet frère [ix-skills](https://github.com/amiel-35/ix-skills). Sans lui, le conseil fonctionne avec les ghosts, les costumes, les parties et tes propres fichiers ; une référence `ix:` donne alors une erreur claire au moment de créer la séance.

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills
```

Le script cherche les angles `ix:` dans le cache du plugin, à la version la plus haute. Pour pointer ailleurs, régler la variable `COUNCIL_ANGLES_PATH` (des dossiers séparés par `:`, motifs `*` acceptés).

### Prérequis

- **Claude Code**, avec des sous-agents (c'est le cas par défaut) : chaque angle tourne dans le sien.
- **Python 3.9 ou plus récent**, sans aucune bibliothèque à installer.
- Facultatif : la CLI `codex` ou `agy` si tu veux faire siéger un modèle d'un autre fournisseur (voir [§8](#8-un-modèle-par-siège)).

---

## 3. Une séance pas à pas

Exemple inventé : une petite équipe se demande si elle doit lancer une offre payante.

1. **Tu demandes.** « Passe au conseil : faut-il lancer une offre payante d'ici la fin du trimestre ? »
2. **Claude cadre et propose une grille.** Une question fermée et neutre, un format (`tour` par défaut), cinq angles et un arbitre, avec une ligne par angle pour dire ce qu'il couvre. Il te demande si tu penches déjà pour une option : ce penchant sera noté, mais **jamais montré aux angles**.
3. **Tu valides** (ou tu changes un angle).
4. **Claude ouvre la séance** : `council.py init` crée un dossier avec un gabarit par fichier. Il écrit `CADRAGE.md` (ce que liront les angles), `GRILLE.md` (la grille et ton penchant, que les angles ne liront pas) et, s'il y a des parties prenantes, `PARTIES.md`.
5. **Relecture du cadrage.** Un sous-agent isolé relit le cadrage pour y chercher les fuites (ton penchant qui transparaît, une prémisse posée comme acquise, un fait écrit de mémoire). Tant qu'il ne rend pas « prêt », le tour ne part pas ; au plus deux relectures, puis tu peux lever le verrou en notant les réserves.
6. **Le tour.** Un sous-agent par angle, tous lancés en même temps, chacun avec son brief et rien d'autre. Chacun écrit son avis.
7. **L'arbitre.** Un sous-agent de plus lit les avis et écrit la synthèse.
8. **Contrôle et restitution.** `council.py check --final` vérifie que tout a été respecté ; Claude te rend la grille, la synthèse en nommant l'arbitre, et la question à trancher.

Les avis bruts restent dans le dossier de séance : tu peux les relire.

---

## 4. Les angles : cinq familles

Un angle se donne par une **référence** `famille:nom`. Le script la résout en un fichier à lire ; le brief de l'angle lui donne ce chemin.

| Famille | Exemple | Ce que c'est | Où c'est défini |
|---|---|---|---|
| `ghost:` | `ghost:popper` | une méthode philosophique de ce dépôt | `skills/<nom>/SKILL.md` |
| `ix:` | `ix:dixieme-homme` | une posture de raisonnement d'ix-skills | le cache du plugin ix-skills |
| `costume:` | `costume:humain` | une dimension métier qu'on risque d'oublier | `skills/council/references/angles/costumes.md` |
| `partie:` | `partie:client` | une partie prenante de **cette** décision | `PARTIES.md`, écrit pour la séance |
| `file:` | `file:~/mes-angles/achats` | n'importe quel SKILL.md à toi | le fichier donné |

Sans préfixe, un nom est cherché dans l'ordre `ghost:`, `costume:`, `ix:`. Une partie se donne toujours avec son préfixe.

### 4.1 Les ghosts : des méthodes

Ils attaquent le raisonnement lui-même. Chacun fait **une opération**, documentée dans [la table des skills](../../README.md#documentation).

| Pour… | Ghosts utiles |
|---|---|
| tester une hypothèse, chercher ce qui la réfuterait | Popper, Descartes, Socrate |
| décider sous incertitude, peser des enjeux asymétriques | Pascal, William James, Épictète |
| juger l'éthique d'un choix | Kant, Rawls, Sartre |
| lire les rapports de force et les jeux d'acteurs | Machiavel, Nash, Sun Tzu, Marx |
| lire les incitations et les mécanismes | Adam Smith, Darwin |
| regarder les trajectoires longues et le contexte | Tocqueville, Montesquieu, Hegel |
| partir des cas réels plutôt que de la théorie | Aristote, Platon (l'inverse) |

### 4.2 Les postures ix : des façons de penser

Elles viennent d'ix-skills et n'ont pas de domaine : elles s'appliquent à n'importe quelle question.

| Référence | Ce que fait la posture |
|---|---|
| `ix:dixieme-homme` | plaide à fond la thèse contraire au consensus |
| `ix:contrarian` | cherche le point de rupture unique et les hypothèses non vérifiées |
| `ix:red-team` | raisonne depuis un adversaire qui veut gagner |
| `ix:key-assumptions` | liste ce que le raisonnement suppose sans le dire |
| `ix:firstprinciples` | remonte au vrai problème sous la question posée |
| `ix:outside-in` | décrit les forces extérieures avant toute solution |
| `ix:executor` | vérifie que ça tient dans la réalité : dépendances, premier geste |
| `ix:expansionist` | cherche l'ambition ou le potentiel écartés trop vite |
| `ix:outsider` | lit comme quelqu'un qui n'a aucun contexte |

Tout skill d'ix-skills qui porte une façon de penser peut siéger ; la liste n'est pas fermée.

### 4.3 Les costumes : des dimensions métier

Un costume est une **dimension qu'on risque d'oublier** : quand on raisonne en commercial, on oublie l'argent ; en produit, on oublie celui qui vivra la décision. Il garantit la **couverture**, là où les ghosts et les postures apportent la **profondeur**. Chaque costume a quatre lignes : la question qu'il porte, ce qu'il regarde, ce qu'il ne juge pas (pour rester dans son couloir), et son piège.

| Costume | La question qu'il porte | Ce qu'il regarde | Ne juge pas | Son piège |
|---|---|---|---|---|
| `costume:financier` | Qu'est-ce que ça fait à la trésorerie, au coût, au seuil de rentabilité ? | les flux et leur calendrier, le coût complet (temps compris), ce qui est engagé avant d'être encaissé, le pire cas chiffré | l'opportunité | confondre ce qui se mesure avec ce qui compte |
| `costume:commercial` | Est-ce le bon moment, le bon interlocuteur, le bon geste ? | qui achète et qui décide, ce que le geste dit au client, les portes qu'il ferme, la réaction probable en face | le prix juste | prendre l'envie de signer pour un signal du marché |
| `costume:produit` | Est-ce cohérent avec ce qu'on est censé faire et vendre ? | le vrai problème de l'utilisateur, ce que la décision ajoute ou retire à l'offre, l'exception qui devient la règle | le timing | défendre la feuille de route contre la réalité qui l'invalide |
| `costume:marque` | Qu'est-ce que ça dit de nous, et qu'est-ce que ça abîme ? | la promesse et sa tenue, le précédent créé, la lecture de ceux qui ne sont pas dans la pièce | la rentabilité | confondre image et réputation ; la seconde se construit par ce qu'on fait |
| `costume:technique` | Quelle surface, quelle dette, quelle maintenance ? | ce qu'il faudra faire tourner, réparer et faire évoluer, qui saura le faire, ce qui casse quand ça casse | la valeur métier | préférer la solution élégante à la solution suffisante |
| `costume:humain` | Qu'est-ce que ça coûte à ceux qui vont le vivre ? | la charge réelle et sa répartition, ce que ça demande à ceux qui n'ont pas décidé, la fatigue, la confiance, qui part si ça tourne mal | tout le reste | parler à la place des gens au lieu de dire ce qu'il faudrait leur demander |
| `costume:juridique` | Quel engagement, quel risque, quelle réversibilité ? | ce qui engage et qui l'engage, ce qui se défait et à quel prix, les obligations créées, la preuve qu'on garde | l'opportunité | il signale, il ne remplace pas un juriste réel |

Le costume **Humain** est le plus souvent oublié et le plus souvent décisif : ne le retire pas pour gagner un avis.

**Ajouter un costume.** Un costume utile à tout le monde : une section `## Nom` de plus dans `costumes.md`, avec les quatre lignes ; `costume:nom` marche aussitôt. Un costume propre à ton métier (et qui n'a rien à faire dans un dépôt public) : un fichier chez toi, appelé avec `file:<chemin>`.

### 4.4 Les parties prenantes : des intérêts réels

Une partie, c'est **quelqu'un que cette décision-là touche**, vu de sa place. Contrairement aux costumes, les parties n'ont pas de bibliothèque : elles changent à chaque décision. `--seat partie:client` crée, à l'ouverture de la séance, une fiche `## client` dans `PARTIES.md`, que l'organisateur remplit avant la relecture :

| Champ | Ce qu'on y met |
|---|---|
| Qui | le rôle ou le type d'acteur, **jamais une personne réelle nommée** |
| Mandat | ce dont cette partie est responsable, ce qu'elle optimise |
| Ce qu'elle gagne ou perd | selon chaque option, dont « ne rien faire » |
| Ce qu'elle sait | ce qu'elle connaît bien, les sources qu'elle croit |
| Priorités | ce qu'elle met au-dessus de quoi |
| Angles morts | ce qu'elle tend à ne pas voir |
| Lignes rouges | ce qu'elle n'acceptera pas |
| Changerait d'avis si | le fait ou le résultat précis |

Pour trouver les parties, se demander : **qui gagne**, **qui paie**, **qui vivra la décision au quotidien**, **qui peut la bloquer**, **qui est lésé sans bruit**, et **qui est de l'autre côté de la table** (le client, l'acheteur, le partenaire : c'est souvent l'angle qui manque le plus, parce que le décideur ne s'y met jamais).

Chaque partie ne lit que sa fiche ; les autres angles ne l'ouvrent pas. Une fiche décrit une position, jamais la conclusion qu'elle devrait tirer.

**Costume ou partie ?** `costume:financier` demande « qu'est-ce que ça fait à la trésorerie ? ». `partie:client` demande « qu'est-ce que je gagne ou perds, moi, le client, avec chaque option ? ». Le premier est une dimension générique ; la seconde, un intérêt précis.

### 4.5 Tes propres angles

`file:<chemin>` fait siéger n'importe quel SKILL.md (ou un dossier qui en contient un). Pratique pour une méthode maison, un costume métier, ou un skill d'un autre plugin.

### 4.6 Composer une grille

- **Trois angles** pour une question cadrée, **cinq ou six** pour un arbitrage lourd, **sept au plus** en délibération. Au-delà, la synthèse devient illisible.
- **Mélanger les familles.** Conséquences éparpillées : des costumes. Pari ou choix de direction : des ghosts et des postures. Décision qui touche des gens précis : des parties. Décision lourde : un mélange.
- **Trois sièges à vérifier** avant de proposer : un angle qui a intérêt à **ne rien faire** (souvent `costume:financier` ou `ix:executor`), un angle pour **ceux qui ont le moins de voix** (souvent `costume:humain` ou une partie), et un angle qui **défend l'option** sérieusement (souvent `ix:expansionist`). Sans ce dernier, la grille penche d'un seul côté.
- **Deux angles qui raisonneraient pareil** sur les mêmes faits n'en font qu'un.

Exemple de grille (inventé) pour « faut-il lancer une offre payante ? » : `ghost:pascal`, `costume:financier`, `costume:humain`, `partie:client`, `ix:expansionist`, arbitre `adversarial`.

---

## 5. Les formats

| Format | Déroulé | Quand |
|---|---|---|
| `tour` (défaut) | cadrage, grille → relecture → avis en parallèle → arbitre | la plupart des décisions |
| `compare` | cadrage, grille → relecture → deux avis côte à côte → ce que la divergence révèle | comprendre pourquoi deux cadres voient le même problème autrement |
| `deliberation` | cadrage, grille → dossier commun → relecture → tour 1 + vérificateur → corrections → bilan à options lettrées → tour 2 et vote → arbitre | décision lourde, peu réversible, qui bute sur des faits |

**`compare`** prend exactement deux angles. Un lecteur isolé écrit ensuite, en deux ou trois lignes, l'hypothèse que les deux ne partagent pas, posée comme une question. Avec `--arbiter aucun`, on garde la pure juxtaposition. Paires dont la tension est productive : Popper / Hegel, Kant / Machiavel, Marx / Adam Smith, Aristote / Platon, Sartre / Épictète, Darwin / Tocqueville.

**`deliberation`** ajoute un **dossier commun** (les faits sourcés, identiques pour tous), un **vérificateur** sans angle qui contrôle chaque fait porteur contre sa source et publie les corrections en **addenda**, puis un **second tour** où chaque angle lit les autres, répond par leur nom et vote sur des options lettrées. Elle coûte environ le double d'un `tour`.

Le déroulé de chaque format est décrit dans `skills/council/references/formats/<format>.json` ; un format maison se passe par son chemin.

---

## 6. L'arbitre

Le choix de l'arbitre change le résultat ; il est toujours nommé dans la restitution.

| `--arbiter` | Ce qu'il produit |
|---|---|
| `neutre` (défaut) | la carte fidèle des convergences et des désaccords, sans trancher |
| `adversarial` | ne survit que ce qui tient face à un lecteur hostile |
| `ghost:zeus` | un arbitrage depuis une juridiction ; son verdict reste un avis de plus, posé sous la carte |
| `ghost:nash` | l'arbitrage lu comme un équilibre entre positions |
| `ghost:aristote` | les convergences traitées comme des cas, généralisation minimale |

Tout autre ghost, posture ou fichier peut arbitrer : il applique alors **sa méthode à l'arbitrage**, pas au problème, et importe ses biais (la synthèse a une section pour le dire). Une partie prenante ne peut pas arbitrer : elle siège.

L'arbitre lit `GRILLE.md`, donc le penchant du décideur, pour un seul test : sa synthèse se lirait-elle pareil si le décideur avait penché pour l'inverse ?

---

## 7. Le cadrage, la grille et la relecture

Le cadrage est la pièce qui fausse le plus souvent un conseil : chaque angle reprend, sans le savoir, tout ce qu'il pose comme acquis. D'où trois pièces.

**Deux fichiers, deux lecteurs.**

| | `CADRAGE.md` | `GRILLE.md` |
|---|---|---|
| Qui le lit | les angles, le relecteur, l'arbitre | le décideur, le relecteur, l'arbitre ; **jamais les angles** |
| Contenu | la question, les faits sourcés, les sources autorisées, les options (dont « ne rien faire »), ce qu'on ne sait pas | la grille validée, ce que couvre chaque angle, les trois sièges, le penchant du décideur, les angles écartés, les réserves de relecture |

**Les règles du cadrage** (détail dans [`references/cadrage.md`](../../skills/council/references/cadrage.md)) :

- un titre de séance et une question **neutres** ;
- pas d'urgence : une échéance est un fait, pas une pression ;
- toutes les options, dont **ne rien faire**, avec ce qu'elles engagent, en faits ;
- chaque fait **recopié depuis sa source** relue, jamais de mémoire ;
- aucun avis déjà rendu dans les sources ; une source qui mêle faits et avis ne s'autorise pas aux angles ;
- dans `GRILLE.md`, écrire ce que couvre un angle (« la décision sous incertitude »), **jamais ce qu'il devrait trouver**.

**La relecture.** Un sous-agent sans angle lit le cadrage, la grille et les fiches de parties, et rend `RELECTURE.md` : fuites, prémisses semées, faits vérifiés contre leur source, ce qui manque, corrections demandées, avec un verdict « prêt » ou « à corriger ». Le script refuse de lancer le tour tant que ce n'est pas « prêt ». **Deux relectures au plus** : si la seconde demande encore des corrections, l'organisateur applique ce qui peut l'être, note le reste dans `GRILLE.md` §6, et le décideur lève le verrou par la ligne `**Relecture levée par :** <qui>, réserves en §6`.

Le test final avant le tour : un angle qui ne lirait que `CADRAGE.md` pourrait-il deviner ce que le décideur espère ? Si oui, ce n'est pas prêt.

---

## 8. Un modèle par siège

Chaque siège, et l'arbitre, peut porter son modèle avec `@` : `--seat ix:dixieme-homme@opus`, `--arbiter neutre@sonnet`.

| Modèle | Comment il est lancé |
|---|---|
| sans `@` | sous-agent Claude Code, modèle par défaut |
| `opus`, `sonnet`, `haiku` | sous-agent Claude Code avec ce modèle |
| `codex` | `codex exec -s read-only --ephemeral -o <fichier> "<brief>"` |
| `gemini` | `agy -p "<brief>" --sandbox > <fichier>` |

Varier les modèles décorrèle un peu les angles morts, jamais complètement. Attention : un siège `codex` ou `gemini` envoie le cadrage et ses sources chez un autre fournisseur. Pour une décision confidentielle, rester sur des sièges Claude.

---

## 9. Les fichiers d'une séance

Tout vit dans un dossier, choisi à l'ouverture. Chaque fichier naît en gabarit marqué `<!-- council:todo -->`, retiré une fois écrit.

| Fichier | Écrit par | Lu par | Contenu |
|---|---|---|---|
| `council.json` | le script | le script | la grille, les modèles, le format figé à l'ouverture |
| `CADRAGE.md` | l'organisateur | angles, relecteur, arbitre | la question, les faits, les sources, les options |
| `GRILLE.md` | l'organisateur | décideur, relecteur, arbitre | la grille, le penchant, les réserves |
| `PARTIES.md` | l'organisateur | chaque partie (sa fiche), relecteur, arbitre | une fiche par partie prenante |
| `RELECTURE.md` | le relecteur | l'organisateur | fuites, faits vérifiés, verdict |
| `AVIS-<angle>.md` | chaque angle | l'arbitre | position, confiance, risques, ce qui manque, où le cadrage est faux |
| `SYNTHESE.md` | l'arbitre | le décideur | convergences, désaccords, angle mort, question à trancher, prochaines étapes |
| `DIVERGENCE.md` | le lecteur (`compare`) | le décideur | ce que la divergence révèle |
| `DOSSIER.md` | l'organisateur (`deliberation`) | tous | le relevé factuel commun |
| `VERIFICATION.md` | le vérificateur | l'organisateur | un verdict par fait porteur |
| `ADDENDUM-<lettre>.md` | l'organisateur | tous | les corrections, jamais un avis |
| `BILAN-TOUR1.md` | l'organisateur | angles au tour 2, arbitre | positions, désaccords, options lettrées |
| `TOUR1-` / `TOUR2-<angle>.md` | chaque angle | (tour 2 : tous) ; arbitre | avis du tour 1, puis vote du tour 2 |

---

## 10. Le script `council.py`

Il se trouve dans le dossier du skill : `<dossier du skill>/scripts/council.py`. Python seul, sans dépendance ; il n'écrase jamais un fichier.

| Commande | Ce qu'elle fait |
|---|---|
| `init SEANCE --title "…" --seat REF[@MODELE] … [--format …] [--arbiter …]` | crée la séance et ses gabarits ; une référence introuvable arrête tout avant d'écrire |
| `status SEANCE` | l'état de chaque étape et la prochaine chose à faire |
| `resolve REF …` | le fichier qu'un angle lira |
| `brief SEANCE ETAPE [ANGLE]` | le brief à donner tel quel au sous-agent ; refuse si une étape en amont n'est pas faite ou pas valide |
| `addendum SEANCE` | le prochain addendum de corrections (`deliberation`) |
| `tally SEANCE [--step …]` | le tableau des positions, ou le décompte des votes |
| `check SEANCE [--final]` | contrôle le processus : ordre des étapes, champs obligatoires, arbitre nommé, aucun vote dans un addendum… |

Toutes acceptent `--json`. Codes de sortie : 0 ok, 1 erreur d'usage (le message dit quoi faire), 2 commande mal formée, 3 le contrôle a trouvé un problème.

En pratique, tu n'as pas à le lancer toi-même : Claude, dans le rôle d'organisateur, s'en sert à chaque étape.

---

## 11. Questions fréquentes

**Combien ça coûte ?** Une séance `tour` à six angles, c'est huit à neuf exécutions de modèle (relecture, angles, arbitre) ; une `deliberation`, environ le double. À réserver aux décisions qui engagent ; pour une question fermée à faible enjeu, un seul avis contradictoire suffit.

**Pourquoi ne pas simplement demander « les pour et les contre » ?** Parce qu'un seul interlocuteur rend une synthèse lisse, qui reflète surtout la façon dont la question a été posée. Le conseil sépare les points de vue, les empêche de se lire, et rend leurs désaccords au lieu de les fondre.

**Que faire si tous les angles sont d'accord ?** L'arbitre le dit tel quel, sans fabriquer de désaccord, mais il vérifie si l'accord vient de chemins différents (signal fort) ou d'une même prémisse (signal suspect, souvent semée par le cadrage).

**Le conseil peut-il se tromper sur ce qui compte pour moi ?** Oui. Les angles pèsent des faits, pas tes valeurs. Il peut te déconseiller unanimement ce que tu feras quand même, pour une raison qu'aucun n'avait. C'est normal : il éclaire, tu décides.

**Où vivent mes séances ?** Dans le dossier que tu choisis, dans ton projet. Rien ne part ailleurs, sauf si tu fais siéger un modèle externe (`codex`, `gemini`).

**Je peux reprendre une question ?** Oui : une nouvelle séance, où les faits qui ont survécu et les questions ouvertes de la synthèse entrent comme des faits sourcés, jamais l'avis d'un angle.

---

## 12. Limites

- **L'indépendance a un plafond.** Des avis du même modèle partagent ses angles morts.
- **Le cadrage reste fragile.** La relecture attrape beaucoup de fuites ; un cadrage parfaitement neutre n'existe pas.
- **Les voix sont simulées.** Aucune vraie partie prenante ne s'est exprimée ; les vérifications réelles (clients, juriste, données) restent à faire.
- **Un arbitre à méthode importe ses biais**, d'où l'obligation de le nommer.

Le détail : [SKILL.md](../../skills/council/SKILL.md), [guide du cadrage](../../skills/council/references/cadrage.md), [dossier commun](../../skills/council/references/dossier.md), [vérification](../../skills/council/references/verification.md).

Le script, le dossier commun, le vérificateur et le second tour sont adaptés d'[advisory-council](https://github.com/nzanepro/tvr-skills-agent-advisory-council) de nzanepro (MIT, voir [THIRD_PARTY.md](../../THIRD_PARTY.md)).
