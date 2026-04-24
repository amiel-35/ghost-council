# ghost-council

> Socrate, Popper, Wittgenstein, Sartre et quelques autres encodés comme skills.
> Sans costume. Juste la méthode.

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

A collection of markdown skills. Each one encodes a philosopher's reasoning method as a concrete operation you can run on any text, decision, or problem.

The idea: Popper, Wittgenstein, Socrates, Sartre and others had *methods*, not just opinions. These skills encode the method, not the character. A "you are Kant" prompt activates biography and fuzzy associations. That's not useful.

Skills are portable across Claude, GPT, and Gemini. Do with them what you want.

**Solid** (formalizable): Socrates, Plato, Aristotle, Descartes, Popper, Wittgenstein, Hegel, Kant, Pascal

**Fun** (strong posture, looser formalization): Nietzsche, Machiavel, Freud, Darwin, Sun Tzu, Sartre

Each skill has a "known limits" section — fun skills have longer ones.

Experimental, clearly labeled as such. As much an intellectual exercise as a tool — if the idea interests you, the philosopher list is open.

Contribution criterion: formalizable method, concrete action verbs. If you can't write the "Method" section, the philosopher is probably out of scope.
