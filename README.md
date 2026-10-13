# ghost-council

> Socrate, Popper, Wittgenstein, Sartre et quelques autres encodés comme skills.
> Sans costume. Juste la méthode.

[English below](#english)

---

## C'est quoi

Une collection de skills markdown. Chaque fichier encode la méthode d'un philosophe comme une opération applicable à un texte, une décision, un brief ou n'importe quel problème qui traîne.

Le principe est simple : ces gens n'avaient pas que des opinions, ils avaient des *méthodes*. Popper cherche systématiquement comment invalider une hypothèse. Wittgenstein refuse d'avancer tant qu'un terme n'est pas proprement défini. Sartre détecte la mauvaise foi dans la façon dont on déguise ses choix en contraintes subies. Socrate pose des questions jusqu'à ce que la contradiction apparaisse.

Ces méthodes sont utiles. Le problème des "agents philosophiques" habituels, c'est qu'ils encodent le personnage, pas la méthode. Un prompt "tu es Kant" active de la biographie, de la vulgarisation et des associations floues. Ce n'est pas ce qu'on veut ici.

Les skills encodent la méthode. Après, tu en fais ce que tu veux.

---

## Les skills

**Solides** (méthode formalisable, résistance à la formalisation faible) :
Socrate, Platon, Aristote, Descartes, Popper, Wittgenstein, Hegel, Kant, Pascal, Épictète, Rawls, William James, Adam Smith, Montesquieu, Tocqueville, Nash

**Fun** (posture forte, formalisation partielle) :
Nietzsche, Machiavel, Freud, Darwin, Sun Tzu, Sartre, Marx

**Arbitre** (pas de méthode propre — tranche entre les autres) :
Zeus

**Conseil** (orchestration — fait délibérer les autres) :
council

**Outil** (pour les contributeurs) :
doc-skill, qui génère la documentation FR + EN d'un skill

Chaque skill a une section "limites connues" dans son propre fichier. Les skills fun ont des sections plus longues — certains philosophes résistent à la formalisation, et c'est documenté honnêtement.

---

## Le conseil : `/council`

Fait délibérer plusieurs angles **indépendants** sur une décision pas encore prise, puis un arbitre rend la carte des désaccords. Le conseil ne tranche pas : l'humain décide. **Expérimental (v1)** : les avis sont simulés, ils éclairent une décision, ils n'engagent personne.

- **Angles au choix**, de plusieurs bibliothèques : les ghosts de ce repo (`ghost:popper`), les postures d'[ix-skills](https://github.com/amiel-35/ix-skills) si elles sont installées (`ix:dixieme-homme`), des costumes métier (`costume:humain`, `costume:financier`...), des parties prenantes propres à la décision (`partie:client`, `partie:equipe`), ou n'importe quel SKILL.md (`file:<chemin>`).
- **Cadrage relu** : ce que lisent les angles (`CADRAGE.md`) est séparé de la grille et du penchant du décideur (`GRILLE.md`), et un relecteur isolé vérifie le cadrage avant le tour.
- **Formats** : `tour` (avis en parallèle puis arbitre), `compare` (deux angles côte à côte, ce que leur divergence révèle), `deliberation` (dossier commun, vérificateur, deux tours, vote).
- **Arbitre** : neutre par défaut ; `adversarial`, Zeus, Nash, Aristote ou tout autre angle, toujours nommé dans la restitution.
- **Un modèle par siège** en option (`@opus`, `@sonnet`, `@haiku`, `@codex`, `@gemini`).

Un script Python sans dépendance (`skills/council/scripts/council.py`) tient la paperasse de séance : il crée les fichiers, rédige le brief de chaque angle, dit où on en est et contrôle le processus. Il n'appelle aucun modèle. Détails dans [skills/council/SKILL.md](skills/council/SKILL.md).

---

## Structure d'un skill

```
skills/[nom]/SKILL.md
```

- **Rôle** : l'opération concrète
- **Règles absolues** : ce que la méthode ne négocie pas
- **Méthode** : les étapes en verbes d'action
- **Output attendu** : ce que ça produit
- **Limites connues** : où ça foire

Markdown pur. Portable Claude, GPT, Gemini.

---

## Installation

**Claude Code (plugin marketplace)** :
```bash
claude plugin marketplace add amiel-35/ghost-council
claude plugin install ghost-council
```

**Claude Code (manuel)** : copier `skills/[nom]/` dans `~/.claude/skills/`.

**Maintainers** : `skills/` est la source de vérité, `dist/` est généré pour le plugin.
Après toute modification dans `skills/`, lancer `python3 build.py` avant de commit
(voir [TODO.md](TODO.md#claude-code) pour le détail). Les tests du script de `council`, depuis la racine du dépôt :
`uvx pytest tests/` (ou `python3 -m pytest tests/`).

---

## ⚠️ Avertissement

Ce projet ne prétend pas être sérieux. Les skills sont **volontairement réducteurs et caricaturaux** — c'est une condition de leur utilisabilité, pas un oubli. Encoder Kant en dix verbes d'action, c'est trahir Kant. On le sait. C'est fait exprès.

Les philosophes, professeurs de philosophie, et penseurs qui passent par là sont **libres de critiquer, conseiller ou contribuer** pour améliorer la rigueur ou corriger les contresens. Les PR et les issues sont ouvertes pour ça.

---

## Statut

Expérimental et clairement étiqueté comme tel. C'est autant un exercice intellectuel qu'un outil — si l'idée t'intéresse, la liste des philosophes est ouverte.

---

## Projet frère : ix-skills

[ix-skills](https://github.com/amiel-35/ix-skills) est l'autre collection du même auteur : des skills de travail (cadrage, critique, décision, revue de contrat, synthèse...) et des postures de raisonnement (dixième homme, contrarian, red team, premiers principes...). Les deux se complètent : ghost-council encode des méthodes de pensée, ix-skills des gestes de travail. `/council` les fait siéger ensemble : `ix:dixieme-homme` à côté de `ghost:popper`, si ix-skills est installé.

## Contribuer

Critère d'entrée : méthode formalisable en verbes d'action concrets. Si tu ne peux pas écrire la section "Méthode", le philosophe n'est probablement pas dans le scope.

---

## English

A collection of markdown skills. Each file encodes a philosopher's reasoning method as a concrete operation you can run on any text, decision, brief, or problem.

The idea is simple: these people didn't just have opinions, they had *methods*. Popper systematically looks for ways to invalidate a hypothesis. Wittgenstein refuses to move forward until every term is properly defined. Sartre detects bad faith — the way we disguise our own choices as constraints. Socrates keeps asking questions until the contradiction surfaces.

These methods are useful. The problem with most "philosophical agents" is that they encode the character, not the method. A "you are Kant" prompt activates biography, simplification, and fuzzy associations. That's not what we want here.

The skills encode the method. Do with them what you want.

### Skills

**Solid** (formalizable, low resistance to encoding) :
Socrates, Plato, Aristotle, Descartes, Popper, Wittgenstein, Hegel, Kant, Pascal, Epictetus, Rawls, William James, Adam Smith, Montesquieu, Tocqueville, Nash

**Fun** (strong posture, partial formalization) :
Nietzsche, Machiavelli, Freud, Darwin, Sun Tzu, Sartre, Marx

**Arbiter** (no method of its own — settles between the others) :
Zeus

**Council** (orchestration — makes the others deliberate) :
council

**Tool** (for contributors) :
doc-skill, which generates a skill's FR + EN documentation

Each skill has a "known limits" section in its own file. Fun skills have longer ones — some philosophers resist formalization, and that's documented honestly.

### The council: `/council`

Makes several **independent** angles deliberate on a decision not yet taken; an arbiter then returns the map of disagreements. The council does not decide: the human does. **Experimental (v1)**: the opinions are simulated; they inform a decision, they commit no one.

- **Pick your angles** from several libraries: this repo's ghosts (`ghost:popper`), [ix-skills](https://github.com/amiel-35/ix-skills) postures when installed (`ix:dixieme-homme`), business "costumes" (`costume:humain`, `costume:financier`...), stakeholders specific to the decision (`partie:client`, `partie:equipe`), or any SKILL.md (`file:<path>`).
- **Reviewed framing**: what the angles read (`CADRAGE.md`) is kept apart from the grid and the decision owner's leaning (`GRILLE.md`), and an isolated reviewer checks the framing before the round.
- **Formats**: `tour` (parallel opinions, then the arbiter), `compare` (two angles side by side, what their divergence reveals), `deliberation` (shared dossier, verifier, two rounds, vote).
- **Arbiter**: neutral by default; `adversarial`, Zeus, Nash, Aristotle or any other angle, always named in the output.
- **One model per seat**, optional (`@opus`, `@sonnet`, `@haiku`, `@codex`, `@gemini`).

A dependency-free Python script (`skills/council/scripts/council.py`) keeps the session paperwork: it creates the files, writes each angle's brief, reports progress and checks the process. It calls no model. The skill itself is written in French; see [skills/council/SKILL.md](skills/council/SKILL.md).

### Skill structure

```
skills/[name]/SKILL.md
```

- **Role** : the concrete operation
- **Absolute rules** : what the method doesn't negotiate
- **Method** : steps as action verbs
- **Expected output** : what it produces
- **Known limits** : where it breaks

Plain markdown. Portable across Claude, GPT, Gemini.

### Installation

**Claude Code (plugin marketplace)**:
```bash
claude plugin marketplace add amiel-35/ghost-council
claude plugin install ghost-council
```

**Claude Code (manual)**: copy `skills/[name]/` into `~/.claude/skills/`.

**Maintainers**: `skills/` is the source of truth, `dist/` is generated for the plugin.
After any change under `skills/`, run `python3 build.py` before committing.
Tests for the `council` script, from the repository root: `uvx pytest tests/` (or `python3 -m pytest tests/`).

### ⚠️ Disclaimer

This project does not take itself seriously. The skills are **deliberately reductive and caricatural** — that's a condition of their usability, not an oversight. Encoding Kant in ten action verbs betrays Kant. We know. It's intentional.

Philosophers, philosophy teachers, and thinkers who stumble upon this are **welcome to criticize, advise, or contribute** to improve rigor or fix misrepresentations. PRs and issues are open for exactly that.

### Status

Experimental, clearly labeled as such. As much an intellectual exercise as a tool — if the idea interests you, the philosopher list is open.

### Sibling project: ix-skills

[ix-skills](https://github.com/amiel-35/ix-skills) is the author's other collection: working skills (scoping, critique, decision, contract review, synthesis...) and reasoning postures (tenth man, contrarian, red team, first principles...). They complement each other: ghost-council encodes ways of thinking, ix-skills ways of working. `/council` seats them together — `ix:dixieme-homme` next to `ghost:popper` — when ix-skills is installed.

### Contribute

Entry criterion: formalizable method in concrete action verbs. If you can't write the "Method" section, the philosopher is probably out of scope.

---

## Documentation

| Skill | Catégorie | Description | Doc FR | Doc EN |
|-------|-----------|-------------|--------|--------|
| Socrate | Solide | Fait émerger les contradictions par questionnement systématique | [FR](docs/fr/socrate.md) | [EN](docs/en/socrate.md) |
| Platon | Solide | Remonte du concret vers la forme idéale avec sa dimension normative | [FR](docs/fr/platon.md) | [EN](docs/en/platon.md) |
| Aristote | Solide | Observe, classe, puis théorise — empirisme bottom-up | [FR](docs/fr/aristote.md) | [EN](docs/en/aristote.md) |
| Descartes | Solide | Rend explicites les hypothèses implicites avant toute décision | [FR](docs/fr/descartes.md) | [EN](docs/en/descartes.md) |
| Kant | Solide | Évalue une décision à l'aune de l'impératif catégorique | [FR](docs/fr/kant.md) | [EN](docs/en/kant.md) |
| Popper | Solide | Cherche à invalider plutôt qu'à confirmer une hypothèse | [FR](docs/fr/popper.md) | [EN](docs/en/popper.md) |
| Wittgenstein | Solide | Dissout les pseudo-problèmes par la clarté du langage | [FR](docs/fr/wittgenstein.md) | [EN](docs/en/wittgenstein.md) |
| Hegel | Solide | Construit une synthèse qui dépasse la tension entre deux positions | [FR](docs/fr/hegel.md) | [EN](docs/en/hegel.md) |
| Pascal | Solide | Risk assessment fondé sur l'asymétrie des enjeux sous incertitude | [FR](docs/fr/pascal.md) | [EN](docs/en/pascal.md) |
| Épictète | Solide | Coupe ce qui est en ton pouvoir de ce qui ne l'est pas | [FR](docs/fr/epictete.md) | [EN](docs/en/epictete.md) |
| Rawls | Solide | Évalue une règle depuis la position la plus défavorisée | [FR](docs/fr/rawls.md) | [EN](docs/en/rawls.md) |
| William James | Solide | Court-circuite les débats abstraits par la différence pratique | [FR](docs/fr/william-james.md) | [EN](docs/en/william-james.md) |
| Adam Smith | Solide | Identifie les mécanismes d'incentives qui produisent les comportements | [FR](docs/fr/adam-smith.md) | [EN](docs/en/adam-smith.md) |
| Montesquieu | Solide | Vérifie si une règle est adaptée à son contexte réel | [FR](docs/fr/montesquieu.md) | [EN](docs/en/montesquieu.md) |
| Tocqueville | Solide | Identifie les tensions structurelles et leurs trajectoires longues | [FR](docs/fr/tocqueville.md) | [EN](docs/en/tocqueville.md) |
| Nietzsche | Fun | Trace la généalogie des valeurs pour révéler les intérêts masqués | [FR](docs/fr/nietzsche.md) | [EN](docs/en/nietzsche.md) |
| Machiavel | Fun | Cartographie les rapports de force réels sans les gants | [FR](docs/fr/machiavel.md) | [EN](docs/en/machiavel.md) |
| Freud | Fun | Lit ce qui est voulu derrière ce qui est dit | [FR](docs/fr/freud.md) | [EN](docs/en/freud.md) |
| Darwin | Fun | Analyse ce qui survit dans un environnement de sélection donné | [FR](docs/fr/darwin.md) | [EN](docs/en/darwin.md) |
| Sun Tzu | Fun | Trouve l'asymétrie plutôt qu'attaquer frontalement | [FR](docs/fr/sun-tzu.md) | [EN](docs/en/sun-tzu.md) |
| Sartre | Fun | Détecte la mauvaise foi et retourne les pseudo-contraintes | [FR](docs/fr/sartre.md) | [EN](docs/en/sartre.md) |
| Marx | Fun | Lit les rapports de domination derrière les discours d'intérêt universel | [FR](docs/fr/marx.md) | [EN](docs/en/marx.md) |
| Nash | Solide | Modélise une situation comme un jeu, cherche l'équilibre de Nash et son écart à l'optimum collectif | [FR](docs/fr/nash.md) | [EN](docs/en/nash.md) |
| Zeus | Arbitre | Arbitre les outputs du conseil : convergences, contradictions irréductibles, tranche | [FR](docs/fr/zeus.md) | [EN](docs/en/zeus.md) |
| council | Conseil | Fait délibérer des angles indépendants, rend la carte des désaccords | [FR](docs/fr/council.md) | [EN](docs/en/council.md) |

---

## Documentation

| Skill | Category | Description | Doc FR | Doc EN |
|-------|----------|-------------|--------|--------|
| Socrates | Solid | Surfaces contradictions through systematic questioning | [FR](docs/fr/socrate.md) | [EN](docs/en/socrate.md) |
| Plato | Solid | Ascends from instances to the ideal form with normative dimension | [FR](docs/fr/platon.md) | [EN](docs/en/platon.md) |
| Aristotle | Solid | Observes, classifies, then theorizes — systematic bottom-up | [FR](docs/fr/aristote.md) | [EN](docs/en/aristote.md) |
| Descartes | Solid | Makes implicit assumptions explicit before any decision | [FR](docs/fr/descartes.md) | [EN](docs/en/descartes.md) |
| Kant | Solid | Evaluates decisions through the categorical imperative | [FR](docs/fr/kant.md) | [EN](docs/en/kant.md) |
| Popper | Solid | Seeks to falsify rather than confirm a hypothesis | [FR](docs/fr/popper.md) | [EN](docs/en/popper.md) |
| Wittgenstein | Solid | Dissolves pseudo-problems through language clarity | [FR](docs/fr/wittgenstein.md) | [EN](docs/en/wittgenstein.md) |
| Hegel | Solid | Builds a synthesis that transcends tension between two positions | [FR](docs/fr/hegel.md) | [EN](docs/en/hegel.md) |
| Pascal | Solid | Risk assessment based on stakes asymmetry under uncertainty | [FR](docs/fr/pascal.md) | [EN](docs/en/pascal.md) |
| Epictetus | Solid | Separates what is in your control from what is not | [FR](docs/fr/epictete.md) | [EN](docs/en/epictete.md) |
| Rawls | Solid | Evaluates a rule from the least advantaged position | [FR](docs/fr/rawls.md) | [EN](docs/en/rawls.md) |
| William James | Solid | Short-circuits abstract debates with the practical difference test | [FR](docs/fr/william-james.md) | [EN](docs/en/william-james.md) |
| Adam Smith | Solid | Identifies incentive mechanisms that produce observed behaviors | [FR](docs/fr/adam-smith.md) | [EN](docs/en/adam-smith.md) |
| Montesquieu | Solid | Checks whether a rule is adapted to its actual context | [FR](docs/fr/montesquieu.md) | [EN](docs/en/montesquieu.md) |
| Tocqueville | Solid | Identifies structural tensions and their long-term trajectories | [FR](docs/fr/tocqueville.md) | [EN](docs/en/tocqueville.md) |
| Nietzsche | Fun | Traces the genealogy of values to reveal masked interests | [FR](docs/fr/nietzsche.md) | [EN](docs/en/nietzsche.md) |
| Machiavelli | Fun | Maps real power dynamics without the gloves | [FR](docs/fr/machiavel.md) | [EN](docs/en/machiavel.md) |
| Freud | Fun | Reads what is wanted behind what is said | [FR](docs/fr/freud.md) | [EN](docs/en/freud.md) |
| Darwin | Fun | Analyzes what survives in a given selection environment | [FR](docs/fr/darwin.md) | [EN](docs/en/darwin.md) |
| Sun Tzu | Fun | Finds the asymmetry rather than attacking head-on | [FR](docs/fr/sun-tzu.md) | [EN](docs/en/sun-tzu.md) |
| Sartre | Fun | Detects bad faith and reverses pseudo-constraints | [FR](docs/fr/sartre.md) | [EN](docs/en/sartre.md) |
| Marx | Fun | Reads domination relations behind universal interest discourses | [FR](docs/fr/marx.md) | [EN](docs/en/marx.md) |
| Nash | Solid | Models a situation as a game, finds the Nash equilibrium and its gap to the collective optimum | [FR](docs/fr/nash.md) | [EN](docs/en/nash.md) |
| Zeus | Arbiter | Arbitrates council outputs: convergences, irreducible contradictions, rules on the question | [FR](docs/fr/zeus.md) | [EN](docs/en/zeus.md) |
| council | Council | Makes independent angles deliberate, returns the map of disagreements | [FR](docs/fr/council.md) | [EN](docs/en/council.md) |
