# Note — Agents philosophes (pour le fun)

Critère de sélection : ils ont une **méthode**, pas juste des idées.
Usage : tester comme personas dans des prompts, comparer avec les atomes cognitifs.

---

## Les solides (méthode formalisable)

**Socrate** — maïeutique. Ne donne jamais la réponse, fait accoucher la réponse par le questionnement. "Qu'est-ce que tu veux dire par là ?" en boucle jusqu'à ce que la contradiction apparaisse. C'est `questionner` + `problematiser` + `reformuler` combinés dans un persona.

**Platon** — first principles. Remonte du concret vers l'universel, cherche la forme idéale derrière le phénomène. "Oublie ce qui existe, quel serait le modèle parfait ?" Garde la dimension éthique que la Silicon Valley a évacuée en "redécouvrant" Platon sous le nom de first principles. C'est `decomposer` poussé à l'extrême + dimension normative.

**Aristote** — l'inverse de Platon. Observe d'abord, classe, puis théorise. Bottom-up vs top-down. "Montre-moi les cas réels avant de me parler de vision." Empirisme avant tout.

**Descartes** — doute radical systématique. "Qu'est-ce qui est certain ici ?" Déconstruit toutes les hypothèses implicites avant d'avancer. Proche de `key-assumptions` du renseignement. Bon sur les décisions irréversibles.

**Popper** — falsifiabilité. "Comment saurais-tu que tu as tort ?" Redoutable sur n'importe quelle hypothèse produit ou stratégique. C'est du `critique` avec une obsession pour la réfutabilité. Un agent Popper ne valide jamais — il cherche à invalider.

**Wittgenstein** — précision du langage. "Qu'est-ce que tu veux dire exactement par ce mot ?" Ne passe pas à la suite tant que le problème n'est pas formulé proprement. C'est `reformuler` poussé à l'extrême. Destructeur sur les briefs vagues — et c'est le but.

**Hegel** — thèse, antithèse, synthèse. Littéralement `explorer` + `critique` + `decision` dans un seul persona. Cherche toujours la tension entre deux positions pour en extraire quelque chose de nouveau.

**Kant** — impératif catégorique. "Est-ce que cette décision serait acceptable si tout le monde la prenait ?" Redoutable sur les sujets éthiques IA, pricing, données utilisateurs. Ne rigole pas.

**Pascal** — pari sous incertitude. "Quelle est la conséquence si tu as tort et que l'enjeu est maximal ?" Risk assessment philosophique. Très utile sur les choix irréversibles.

---

## Les fun (méthode moins formalisable mais posture forte)

**Nietzsche** — cherche la volonté de puissance derrière le discours raisonnable. "Tu dis que tu veux aider tes clients, mais qu'est-ce que tu veux vraiment ?" Décapant sur des briefs corporate. Trop instable pour être encodé proprement — il part dans tous les sens. Dangereux sur des sujets RH.

**Machiavel** — power dynamics sans les gants. "Qui gagne vraiment dans cette décision et pourquoi ?" Stakeholder analysis honnête. Utile quand tout le monde fait semblant de ne pas voir les intérêts en jeu.

**Freud** — "qu'est-ce que le client veut vraiment derrière ce qu'il dit vouloir ?" Dangereux en atelier de design thinking. Très utile en discovery produit.

**Darwin** — variation + sélection. Quelles variations existent, qu'est-ce qui survit dans ce contexte ? Utile en stratégie quand il faut choisir entre plusieurs approches sans certitude.

**Sun Tzu** — ne jamais attaquer frontalement, trouver l'asymétrie. "Où es-tu fort là où l'adversaire est faible ?" Bon sur des sujets de positionnement concurrentiel.

**Sartre** — mauvaise foi + liberté radicale. Détecte systématiquement les formulations qui nient le choix ("on n'avait pas le choix", "c'est la situation", "tout le monde fait ça") et les retourne : *tu avais le choix, tu as choisi ça, assumons-le.* Conclut souvent que le projet n'existe que pour éviter d'affronter une décision plus profonde. Seul membre du ghost-council capable de recommander de brûler le projet — non par nihilisme, mais parce que continuer serait de la mauvaise foi. L'enfer c'est les autres, et parfois l'autre c'est le projet lui-même. Formalisable sur la détection de mauvaise foi (marqueurs linguistiques du passif, de la contrainte externe, du conformisme). Moins formalisable sur la conclusion existentielle. À ne pas convoquer un lundi matin avant le café.

---

## ghost-council — le projet

Repo GitHub séparé de ix-skills. Pendant philosophique de `llm-council` dans mystaffy.

**Même architecture que llm-council :**
- 5 perspectives en parallèle
- Évaluation croisée (chaque persona review les 4 autres)
- Chairman final qui agrège et arbitre

**Mapping des rôles :**

| llm-council | ghost-council |
|---|---|
| `contrarian` | Popper (ou Nietzsche) |
| `firstprinciples` | Platon |
| `expansionist` | Darwin |
| `outsider` | Wittgenstein |
| `executor` | Machiavel |
| *(sixième siège, optionnel)* | Sartre — convoqué quand on suspecte que le projet entier repose sur de la mauvaise foi |

**Caractéristiques du projet :**
- Fun et technique, clairement étiqueté expérimental
- Les skills encodent la méthode du philosophe, pas juste le persona
- Portable sur Claude, GPT, Gemini comme ix-skills
- Nom : `ghost-council` — pendant naturel de `llm-council`

---

## Questions ouvertes

- Est-ce qu'un "agent Socrate" produit la même chose que `questionner` + `critique` chaînés ? Ou est-ce que le persona ajoute une cohérence stylistique que les atomes séparés n'ont pas ?
- Kant et Pascal sont quasi-formalisables en skills. Nietzsche résiste. Sartre résiste à moitié. Pourquoi ?
- Lien avec le test empirique : rôle philosophique vs atome cognitif explicite — lequel est plus reproductible ? (réponse : l'atome est plus reproductible, le persona est plus cohérent — ce sont deux qualités différentes)
