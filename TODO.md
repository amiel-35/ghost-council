# TODO / Feuille de route

La feuille de route résumée est dans le README ([FR](README.fr.md#feuille-de-route), [EN](README.md#roadmap)). Ce fichier en donne le détail, dans le même ordre, puis les idées en vrac.

---

## État au 2026-10-13

- **Plugin 0.2.2**, 26 skills : 23 ghosts, Zeus (arbitre), `council`, `doc-skill`.
- **`/council` livré** : formats `tour`, `compare` (qui remplace l'ancien `/compare`) et `deliberation` ; cinq familles d'angles (`ghost:`, `ix:`, `costume:`, `partie:`, `file:`) ; arbitre neutre par défaut ; un modèle par siège en option ; cadrage préparé (`CADRAGE.md` lu par les angles, `GRILLE.md` jamais) ; relecture isolée avant le tour, deux passes au plus ; 124 tests.
- **Documentation** : [guide complet du conseil](docs/council/README.md) en FR et EN, fiches FR et EN de chaque skill, README au format standard (un fichier par langue).
- **Mis à l'épreuve** sur des décisions réelles, puis comparé à advisory-council (nzanepro) sur un même brief, à froid : mêmes conclusions de fond ; `council` attrape les fuites de cadrage avant le tour, pour environ un tiers de coût en moins ; advisory-council rend une conclusion plus nette grâce à son vote en deux tours.

---

## À faire, dans l'ordre

### 1. Conseil : ce qui compte pour le décideur

Les séances réelles l'ont montré : les angles pèsent des faits, pas les valeurs de celui qui décide. Un conseil peut déconseiller unanimement ce que le décideur fera quand même, pour une raison qu'aucun angle n'avait.

- Une section « ce qui compte pour le décideur » dans `GRILLE.md`, remplie avec lui au cadrage.
- Lue par l'arbitre (pas par les angles, pour ne pas souffler de réponse), qui dit dans sa synthèse où la carte des désaccords croise ces valeurs.

### 2. Conseil : le format `revue`

Évaluation croisée anonymisée des avis, sur le modèle du conseil d'ix-memory : chaque avis reçoit une lettre (A à E) tirée au hasard, chaque angle classe les autres sans savoir qui les a écrits, la clé reste dans un fichier que les angles ne lisent pas.

### 3. Conseil : améliorations repérées en séance

- **Une conclusion plus nette en `tour`** : un vote léger sur des options lettrées, sans second tour complet (la force d'advisory-council relevée par la comparaison).
- **Le contradicteur au bon moment** : au tour 1, `ix:dixieme-homme` plaide contre la thèse qu'il devine ; il servirait mieux au second tour d'une `deliberation`, une fois le consensus formé. À documenter, ou à proposer par défaut.
- **Séance de suivi** : `init --suite <séance>` qui reprend les faits ayant survécu et interdit les avis de la séance précédente.
- **L'indépendance déclarée** : la ligne « Indépendance » d'un avis est pré-remplie par le gabarit, donc invérifiable par `check`. Chercher un contrôle réel, ou l'assumer comme limite.
- **« Ne rien faire » en option lettrée** : le décompte le compte aujourd'hui comme « Autre ».

### 4. `/suggest` et `/evaluate`

En `draft` dans `drafts/`, bloqués par les questions ouvertes en bas de chaque fichier.

- **`/suggest [problème]`** : recommande 2 ou 3 ghosts pertinents, avec une justification courte. Pourrait devenir l'étape de choix de la grille de `/council`.
- **`/evaluate [philosophe] [output]`** : évalue si un output a bien suivi la méthode annoncée. Utile pour calibrer les skills eux-mêmes.

### 5. Nouveaux esprits

**Penseurs modernes**
- **Nassim Taleb** : distingue fragile, robuste, antifragile ; cherche la convexité des situations.
- **Charlie Munger** : grille de modèles mentaux, inversion systématique.
- **Daniel Kahneman** : sépare système 1 et système 2, traque les biais cognitifs dans un raisonnement.
- **Hannah Arendt** : le pouvoir comme action collective ; la banalité du mal dans les processus bureaucratiques.
- **Simone de Beauvoir** : les structures de domination dans les représentations du « naturel ».
- **Chomsky** : grammaire profonde et grammaire de surface, appliquées à l'analyse des discours.
- **Ivan Illich** : contre-productivité des institutions passé un seuil, monopole radical.
- **Marshall McLuhan** : le medium est le message.
- **Bourdieu** : capital symbolique, habitus, champ ; les comportements comme stratégies de distinction.

**Penseurs disciplinaires**
- **Shannon** : la théorie de l'information appliquée ; quel est le signal, quel est le bruit ?
- **Feynman** : premiers principes, refus des analogies non fondées.
- ~~Von Neumann / Nash~~ : fait, voir `skills/nash/`.

**Personas (variante assumée)** : contrairement aux skills méthode, une persona encode le personnage, la méthode et le style. Plus caricatural, limites plus longues. Candidats : Churchill, Machiavel (version persona), Zizek, Socrate ironique.

### 6. Installer hors de Claude Code

Les skills sont du markdown pur ; l'objectif est une procédure minimale par plateforme.

- **Gemini CLI** : format GEMINI.md et activation des skills, à tester et documenter.
- **GPT personnalisés** : un GPT « ghost-council » qui charge les skills en instructions, ou un pack à coller dans les instructions personnalisées.
- **OpenWebUI / Ollama** : des model files ou des prompts système préconfigurés.
- **Raycast / Alfred** : un raccourci qui copie le contenu d'un skill.
- **Script d'installation** : `curl … install.sh | bash`, qui copie les skills dans `~/.claude/skills/` ou l'équivalent.

---

## Qualité et rigueur

- **Cas de test par skill** : 2 ou 3 entrées avec la sortie attendue, pour vérifier que la méthode produit ce qu'elle doit.
- **Relecture par des connaisseurs** : faire critiquer les encodages par des gens qui connaissent vraiment les philosophes (les sections « limites connues » sont un bon point de départ).
- **Versions des skills** : un numéro dans le frontmatter, un journal si la méthode évolue.
- **Incompatibilités** : documenter quand deux skills se contredisent sur un même input (Popper contre Hegel sur la falsifiabilité de la dialectique, par exemple).
- ~~Doc EN de Nash~~ : faite le 2026-10-13.

## Expériences à tenter

- Comparer les outputs d'un même skill sur Claude, GPT et Gemini : les divergences sont révélatrices.
- Faire évaluer les skills par des étudiants en philosophie, et collecter les erreurs les plus fréquentes.
- ~~Appliquer le conseil à une vraie décision~~ : fait le 2026-10-13, voir l'état ci-dessus.

---

## Pour les mainteneurs : le build

`skills/` est la source de vérité ; `dist/` est le plugin, généré.

- `python3 build.py` valide chaque `skills/<nom>/SKILL.md` (frontmatter `name` et `description` présents, `name` égal au nom du dossier), vide `dist/skills/` puis recopie tout depuis `skills/`, pour qu'un skill supprimé ne traîne pas dans `dist/`. Il copie aussi `LICENSE` et `THIRD_PARTY.md` dans `dist/`.
- `python3 build.py --check` valide sans rien écrire.
- Ne jamais éditer `dist/` à la main. Monter la version dans `dist/.claude-plugin/plugin.json` à chaque publication qui change le plugin, sinon `claude plugin update` ne voit rien.
- Tests du conseil, depuis la racine du dépôt : `uvx pytest tests/`.
- **Dépôt public** : aucun exemple tiré d'un cas réel (noms, dates, contexte), même pour illustrer une règle. Relire le diff comme un texte public avant chaque push.

---

## Références

- [llm-council (Karpathy)](https://github.com/karpathy/llm-council) : délibération entre plusieurs modèles, à l'origine de l'idée de `/council`.
- [advisory-council (nzanepro)](https://github.com/nzanepro/tvr-skills-agent-advisory-council) : MIT, base du script de `/council`, de son dossier commun et de son vérificateur (voir `THIRD_PARTY.md`).
- [Improving Factuality and Reasoning in Language Models through Multiagent Debate (Du et al., 2023)](https://arxiv.org/abs/2305.14325) : le débat entre modèles comme mécanisme de vérité.
- [Constitutional AI (Anthropic)](https://arxiv.org/abs/2212.08073) : des principes encodés pour guider le comportement, analogie avec les skills méthode.
