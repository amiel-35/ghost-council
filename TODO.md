# TODO / Roadmap

Idées en vrac, non ordonnées. Certaines sont simples, d'autres sont des projets.

---

## Nouveaux esprits

### Penseurs modernes à encoder
- **Nassim Taleb** — distingue fragile / robuste / antifragile, cherche la convexité des situations
- **Charlie Munger** — grille de modèles mentaux, inversion systématique ("inversez, toujours inversez")
- **Daniel Kahneman** — sépare système 1 et système 2, traque les biais cognitifs dans un raisonnement
- **Hannah Arendt** — analyse le pouvoir comme action collective, détecte la banalité du mal dans les processus bureaucratiques
- **Simone de Beauvoir** — lit les structures de domination dans les représentations du "naturel"
- **Chomsky** — sépare grammaire profonde et grammaire de surface, appliqué à l'analyse des discours
- **Ivan Illich** — contre-productivité des institutions passé un certain seuil, monopole radical
- **Marshall McLuhan** — le medium est le message, analyse des effets d'un canal sur son contenu
- **Bourdieu** — capital symbolique, habitus, champ — lit les comportements comme stratégies de distinction

### Penseurs disciplinaires (hors philo pure)
- **Shannon** — information theory appliquée : quel est le signal, quel est le bruit ?
- **Feynman** — first principles thinking, refuse les analogies non fondées
- **Von Neumann / Nash** — théorie des jeux, équilibre, stratégie sous information imparfaite

### Personas (variante assumée)
Contrairement aux skills méthode, les personas encodent le personnage + la méthode + le style.
Plus caricaturaux, plus entertainants, limites documentées plus longues.
Candidats : Churchill, Machiavel (version persona vs méthode existante), Zizek, Socrate version ironique.

---

## Outils à construire

### `/council [question]` — faire débattre les ghosts
Prompt qui soumet une question à plusieurs philosophes simultanément, puis arbitre les divergences.
Inspiré de [llm-council](https://github.com/masatoEmata/llm-council) — plusieurs LLM (ou plusieurs roles) délibèrent et convergent.
- Sélectionner 3-5 philosophes pertinents pour la question
- Chaque philosophe applique sa méthode
- L'arbitre synthétise les convergences et expose les contradictions irréductibles
- Ne tranche pas — expose la carte des désaccords

### `/compare [A] [B] [question]` — confrontation ciblée
Deux philosophes sur le même input, côte à côte. Fait apparaître les hypothèses incompatibles.
Exemple : `compare Popper Marx "La réglementation des plateformes est-elle efficace ?"`

### `/suggest [problème]` — quel ghost invoquer ?
Décrit un problème, le skill recommande 2-3 philosophes pertinents avec une justification courte.
Évite d'ouvrir le mauvais outil.

### `/evaluate [philosophe] [output]` — auto-critique
Meta-skill : donne un output censé appliquer une méthode, le skill évalue si la méthode a bien été suivie.
Utile pour calibrer les skills eux-mêmes.

---

## Installabilité cross-plateforme

Actuellement : markdown portable, mais installation manuelle.
Objectif : one-liner ou procédure minimale par plateforme.

### Claude Code
```bash
# Déjà fonctionnel via skills/
# À documenter clairement dans README
```

### Gemini CLI
- Format GEMINI.md + skill activation — à tester et documenter

### GPT (Custom Instructions / GPTs)
- Les skills sont du markdown pur → copiable dans les instructions système d'un GPT personnalisé
- Créer un GPT "ghost-council" qui charge tous les skills en instructions ?
- Ou prompt-pack à coller dans Custom Instructions

### OpenWebUI / Ollama
- Compatible markdown — créer des "model files" ou system prompts pré-configurés

### Raycast / Alfred
- Snippet ou extension qui copie le contenu d'un skill dans le clipboard

### Script d'installation
```bash
curl -s https://raw.githubusercontent.com/.../install.sh | bash
# → copie les skills dans ~/.claude/skills/ ou équivalent
```

---

## Qualité et rigueur

- **Test cases par skill** : 2-3 inputs avec outputs attendus, pour vérifier que la méthode produit bien ce qu'elle doit
- **Peer review** : invite des gens qui connaissent vraiment les philosophes à critiquer les encodages (les sections "limites connues" sont un bon point de départ)
- **Versioning des skills** : `v1.0` dans le frontmatter, changelog si la méthode évolue
- **Contradiction flag** : documenter quand deux skills sont incompatibles sur un même input (Popper vs Hegel sur la falsifiabilité de la dialectique, par exemple)

---

## Expériences à tenter

- Appliquer le conseil complet (5 philosophes) à une vraie décision produit, documenter le résultat
- Comparer les outputs du même skill sur GPT-4, Claude, Gemini — les divergences sont révélatrices
- Faire évaluer les skills par des étudiants en philo — collecter les erreurs les plus fréquentes

---

## Références

- [llm-council](https://github.com/masatoEmata/llm-council) — délibération multi-agents, base pour `/council`
- [Philosophical Multiagent Debate (Du et al., 2023)](https://arxiv.org/abs/2305.14325) — paper sur les débats LLM comme mécanisme de vérité
- [Constitutional AI (Anthropic)](https://arxiv.org/abs/2212.08073) — utilise des principes encodés pour guider le comportement, analogie avec les skills méthode
