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
Socrate, Platon, Aristote, Descartes, Popper, Wittgenstein, Hegel, Kant, Pascal

**Fun** (posture forte, formalisation partielle) :
Nietzsche, Machiavel, Freud, Darwin, Sun Tzu, Sartre

Chaque skill a une section "limites connues" dans son propre fichier. Les skills fun ont des sections plus longues — certains philosophes résistent à la formalisation, et c'est documenté honnêtement.

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

## Statut

Expérimental et clairement étiqueté comme tel. C'est autant un exercice intellectuel qu'un outil — si l'idée t'intéresse, la liste des philosophes est ouverte.

---

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
Socrates, Plato, Aristotle, Descartes, Popper, Wittgenstein, Hegel, Kant, Pascal

**Fun** (strong posture, partial formalization) :
Nietzsche, Machiavel, Freud, Darwin, Sun Tzu, Sartre

Each skill has a "known limits" section in its own file. Fun skills have longer ones — some philosophers resist formalization, and that's documented honestly.

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

### Status

Experimental, clearly labeled as such. As much an intellectual exercise as a tool — if the idea interests you, the philosopher list is open.

### Contribute

Entry criterion: formalizable method in concrete action verbs. If you can't write the "Method" section, the philosopher is probably out of scope.
