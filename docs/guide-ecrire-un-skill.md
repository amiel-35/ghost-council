# Écrire un skill pour ghost-council

Guide pratique pour ajouter un philosophe à la collection.
[English below](#english)

---

## Le test d'entrée

Avant d'ouvrir un fichier : peux-tu écrire la section "Méthode" en verbes d'action concrets ?

Si la réponse est "il pensait que..." ou "sa philosophie repose sur...", tu n'es pas encore là. Ce n'est pas un reproche — c'est que le travail de formalisation n'a pas encore été fait.

Si la réponse est "il commence par X, puis identifie Y, puis nomme Z", tu es au bon endroit.

---

## Le principe : méthode, pas costume

La différence entre un bon skill et un prompt raté :

**Ce qu'on ne veut pas :**
> Tu es Kant. Tu appliques l'éthique kantienne pour analyser ce problème.

Ce prompt active de la biographie, de la vulgarisation et des associations floues. L'output sera impressionniste.

**Ce qu'on veut :**
> Tu appliques l'impératif catégorique. Règle : une action n'est éthiquement acceptable que si elle peut être universalisée sans contradiction. Méthode : reformuler la maxime de l'action, tester si son universalisation produit une contradiction logique ou pratique, conclure.

Ce prompt encode une opération. L'output est reproductible.

Le skill encode la méthode. Le nom du philosophe est un raccourci, pas le contenu.

---

## Structure section par section

### Frontmatter

```yaml
---
name: [nom en minuscules, sans accents]
description: >
  Une ligne sur l'opération concrète. Pas la biographie.
  Déclenche sur des formulations comme : [2-3 exemples de phrases qui appellent ce skill].
---
```

La description sert à décider *quand* convoquer ce skill. Être précis sur les déclencheurs évite les erreurs de casting.

### Rôle

Ce que le skill fait, formulé à la première personne comme si le philosophe parlait.
Inclure ce qui le distingue des autres skills existants — deux méthodes proches ne sont pas interchangeables.

Éviter : "Tu incarnes la pensée de X."
Préférer : "Tu appliques telle opération spécifique."

### Règles absolues

Ce que la méthode ne négocie *jamais*. En bullet points. 3 à 5 maximum.
Si tu ne peux pas formuler une règle absolue, la méthode n'est probablement pas assez caractérisée.

Exemples solides :
- "Ne jamais chercher à confirmer. Chercher à invalider." (Popper)
- "Ne jamais affirmer. Seulement questionner." (Socrate)
- "'Je n'ai pas le choix' est presque toujours faux." (Sartre)

### Méthode

Étapes numérotées, verbes d'action, ordre logique. C'est le coeur du skill.

Règles :
- Chaque étape commence par un verbe à l'infinitif
- L'ordre des étapes est important — si on peut les shuffler sans conséquence, c'est qu'elles ne forment pas une méthode
- 5 à 8 étapes en général. Moins : trop vague. Plus : probablement deux méthodes mélangées.

### Output attendu

Décrire ce que ça produit, pas comment c'est formaté.

La forme suit la méthode — elle n'est pas imposée par le template.

Exemples :
- Socrate : "Une série de questions qui rendent visible une contradiction. Pas de réponse. Pas de conclusion."
- Sartre : "Une reformulation qui remplace les pseudo-contraintes par des choix explicites avec leurs coûts."
- Popper : 4 éléments nommés, parce que la méthode de Popper est analytique par nature.

Si l'output ressemble à "un rapport structuré avec introduction, analyse et conclusion", c'est le signe que tu as glissé vers le format consultant.

### Limites connues

Section obligatoire. Pas optionnelle.

C'est ici qu'on est honnête sur ce que l'encodage trahit. Chaque philosophe résiste à la formalisation d'une façon qui lui est propre — la documenter est plus utile que de prétendre que ça tient parfaitement.

Les skills "Solides" ont des limites courtes et techniques.
Les skills "Fun" ont des limites plus longues — la résistance à la formalisation est plus forte, et c'est normal.

---

## Solides vs Fun

**Solide** : la méthode se traduit en étapes sans perdre l'essentiel. Le skill est reproductible d'un modèle à l'autre. L'output est prévisible.

**Fun** : la posture est forte et reconnaissable, mais la formalisation est partielle. Le skill peut produire des résultats moins reproductibles. La section "Limites connues" sera plus longue.

En cas de doute, commencer en Fun. Passer en Solide si l'expérience montre que le skill tient.

---

## Checklist avant de soumettre

- [ ] La section Méthode est en verbes d'action, dans un ordre non-arbitraire
- [ ] Le Rôle dit ce qui distingue ce skill des skills existants
- [ ] Les Règles absolues sont non-négociables et formulées comme telles
- [ ] L'Output attendu décrit ce qui est produit, pas comment c'est formaté
- [ ] Les Limites connues sont honnêtes sur ce que l'encodage sacrifie
- [ ] Le frontmatter inclut des déclencheurs concrets
- [ ] Aucune phrase du type "tu incarnes X" ou "dans l'esprit de X"

---

## English

### Writing a skill for ghost-council

#### The entry test

Before opening a file: can you write the "Method" section in concrete action verbs?

If your answer starts with "he believed that..." or "his philosophy rests on...", you're not there yet. The formalization work hasn't been done.

If your answer is "he starts by X, then identifies Y, then names Z", you're in the right place.

#### The principle: method, not costume

**What we don't want:**
> You are Kant. You apply Kantian ethics to analyze this problem.

This activates biography, simplification, and fuzzy associations.

**What we want:**
> You apply the categorical imperative. Rule: an action is ethically acceptable only if it can be universalized without contradiction. Method: reformulate the maxim of the action, test whether its universalization produces a logical or practical contradiction, conclude.

The skill encodes the operation. The philosopher's name is a shortcut, not the content.

#### Section by section

**Frontmatter** : name (lowercase, no accents), one-line description of the concrete operation, trigger phrases.

**Role** : what the skill does, first person. What distinguishes it from existing skills.

**Absolute rules** : what the method never negotiates. Bullet points. 3-5 max.

**Method** : numbered steps, action verbs, logical order. Core of the skill.

**Expected output** : describe what it produces, not how it's formatted. Form follows method.

**Known limits** : mandatory. Document what the encoding sacrifices. Solid skills: short, technical. Fun skills: longer — the resistance to formalization is part of the honest picture.

#### Solid vs Fun

**Solid**: method translates to steps without losing the essential. Reproducible across models.

**Fun**: strong posture, partial formalization. Less predictable output. Longer known limits section.

When in doubt, start as Fun. Upgrade to Solid if experience shows the skill holds.

#### Checklist

- [ ] Method section uses action verbs in non-arbitrary order
- [ ] Role states what distinguishes this skill from existing ones
- [ ] Absolute rules are non-negotiable and formulated as such
- [ ] Expected output describes what is produced, not how it's formatted
- [ ] Known limits are honest about what the encoding sacrifices
- [ ] Frontmatter includes concrete trigger phrases
- [ ] No sentence of the form "you embody X" or "in the spirit of X"
