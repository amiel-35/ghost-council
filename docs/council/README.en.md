# The council: complete guide

[Version française](README.md) · [Short EN doc](../en/council.md) · [The skill itself](../../skills/council/SKILL.md)

`/council` has several **independent angles** deliberate on a decision that has not been made yet, then an **arbiter** returns a map of where they converge and where they clash. The council does not decide: whoever decides is still you.

> **Experimental.** The opinions are simulated by a language model. They shed light on a decision, they commit nobody, and they do not replace a real expert on a legal, medical or regulated subject.

**Contents**

1. [In one minute](#1-in-one-minute)
2. [Installing](#2-installing)
3. [A session step by step](#3-a-session-step-by-step)
4. [Angles: five families](#4-angles-five-families)
5. [Formats](#5-formats)
6. [The arbiter](#6-the-arbiter)
7. [Framing, grid and review](#7-framing-grid-and-review)
8. [One model per seat](#8-one-model-per-seat)
9. [Files in a session](#9-files-in-a-session)
10. [The `council.py` script](#10-the-councilpy-script)
11. [Frequently asked questions](#11-frequently-asked-questions)
12. [Limits](#12-limits)

---

## 1. In one minute

A decision that commits you rarely benefits from being read from a single point of view. The council brings several together, chosen on purpose so that they do not see the same things, and it protects one thing above all: **their independence**. Each angle works alone, in a blank context, without reading the others and without knowing what the decision-maker hopes for. An isolated arbiter then reads all the opinions and returns:

- where the angles converge (and whether the convergence looks suspicious);
- where they genuinely disagree, and what each camp rests on;
- what none of them looked at;
- the question that is still open, and for each next step, the result that would change the decision.

You say what you want to decide. Claude, in the role of **organizer**, frames the question, proposes a grid of angles, gets it validated, then launches the angles and the arbiter in separate sub-agents. A small Python script handles the paperwork: it creates the files, writes the brief for each angle and checks that the process was followed. It never calls a model itself.

---

## 2. Installing

### The ghost-council plugin (required)

In a terminal:

```bash
claude plugin marketplace add amiel-35/ghost-council
claude plugin install ghost-council@ghost-council
```

Restart Claude Code. The `council` skill and all the ghosts (Popper, Kant, Pascal…) are then available. To update later:

```bash
claude plugin marketplace update ghost-council
claude plugin update ghost-council@ghost-council
```

### The ix-skills plugin (optional, recommended)

The angles in the `ix:` family (tenth man, contrarian, red team…) come from the sister project [ix-skills](https://github.com/amiel-35/ix-skills). Without it, the council still works with the ghosts, the costumes, the stakeholders and your own files; an `ix:` reference then gives a clear error when the session is created.

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills@ix-skills
```

The script looks for `ix:` angles in the plugin cache (`~/.claude/plugins/cache/*/ix-skills/*/skills`, so whether ix-skills comes from its own marketplace or from the `amiel-35` catalogue), at the highest version. To point somewhere else, set the `COUNCIL_ANGLES_PATH` variable (folders separated by `:`, `*` patterns accepted).

### The amiel-35 catalogue (another way to install)

The author's three plugins (ix-skills, ix-recipes, ghost-council) are also listed together in the [amiel-35/plugins](https://github.com/amiel-35/plugins) marketplace:

```bash
claude plugin marketplace add amiel-35/plugins
claude plugin install ghost-council@amiel-35
claude plugin install ix-skills@amiel-35   # optional
```

Install a plugin from one marketplace only, not both. The council finds ix-skills by default, whichever marketplace it came from.

### Requirements

- **Claude Code**, with sub-agents (on by default): each angle runs in its own.
- **Python 3.9 or newer**, with no library to install.
- Optional: the `codex` or `agy` CLI if you want a model from another provider to take a seat (see [§8](#8-one-model-per-seat)).

---

## 3. A session step by step

An invented example: a small team wonders whether to launch a paid offer.

1. **You ask.** "Take this to the council: should we launch a paid offer by the end of the quarter?"
2. **Claude frames the question and proposes a grid.** A closed, neutral question, a format (`tour` by default), five angles and an arbiter, with one line per angle saying what it covers. It asks whether you already lean toward an option: that leaning will be recorded, but **never shown to the angles**.
3. **You validate** (or swap an angle).
4. **Claude opens the session**: `council.py init` creates a folder with a template for each file. It writes `CADRAGE.md` (the framing: what the angles will read), `GRILLE.md` (the grid, plus your leaning, which the angles will not read) and, if there are stakeholders, `PARTIES.md`.
5. **Review of the framing.** An isolated sub-agent reads the framing looking for leaks (your leaning showing through, a premise stated as settled, a fact written from memory). The round does not start until it returns "prêt" (ready); at most two reviews, after which you can lift the lock by noting the reservations.
6. **The round.** One sub-agent per angle, all launched at the same time, each with its own brief and nothing else. Each writes its opinion.
7. **The arbiter.** One more sub-agent reads the opinions and writes the synthesis.
8. **Check and delivery.** `council.py check --final` verifies that everything was respected; Claude hands you the grid, the synthesis (naming the arbiter), and the question left to decide.

The raw opinions stay in the session folder: you can read them yourself.

---

## 4. Angles: five families

An angle is given by a **reference** of the form `family:name`. The script resolves it to a file to read; the angle's brief gives it that path.

| Family | Example | What it is | Where it is defined |
|---|---|---|---|
| `ghost:` | `ghost:popper` | a philosophical method from this repository | `skills/<name>/SKILL.md` |
| `ix:` | `ix:dixieme-homme` | a reasoning posture from ix-skills | the ix-skills plugin cache |
| `costume:` | `costume:humain` | a business dimension that is easy to forget | `skills/council/references/angles/costumes.md` |
| `partie:` | `partie:client` | a stakeholder in **this** decision | `PARTIES.md`, written for the session |
| `file:` | `file:~/my-angles/purchasing` | any SKILL.md of your own | the file you give |

Without a prefix, a name is looked up in the order `ghost:`, `costume:`, `ix:`. A stakeholder (`partie:`) is always given with its prefix.

### 4.1 Ghosts: methods

They attack the reasoning itself. Each performs **one operation**, documented in [the skills table](../../README.md#documentation).

| To… | Useful ghosts |
|---|---|
| test a hypothesis, look for what would refute it | Popper, Descartes, Socrates |
| decide under uncertainty, weigh asymmetric stakes | Pascal, William James, Epictetus |
| judge the ethics of a choice | Kant, Rawls, Sartre |
| read power dynamics and the games actors play | Machiavelli, Nash, Sun Tzu, Marx |
| read incentives and mechanisms | Adam Smith, Darwin |
| look at long trajectories and context | Tocqueville, Montesquieu, Hegel |
| start from real cases rather than theory | Aristotle, Plato (the opposite) |

### 4.2 The ix postures: ways of thinking

They come from ix-skills and have no domain: they apply to any question.

| Reference | What the posture does |
|---|---|
| `ix:dixieme-homme` | argues the thesis opposite to the consensus, all the way (the "tenth man") |
| `ix:contrarian` | looks for the single breaking point and the unverified assumptions |
| `ix:red-team` | reasons from an adversary who wants to win |
| `ix:key-assumptions` | lists what the reasoning assumes without saying so |
| `ix:firstprinciples` | goes back to the real problem under the question as asked |
| `ix:outside-in` | describes the outside forces before any solution |
| `ix:executor` | checks that it holds up in reality: dependencies, first move |
| `ix:expansionist` | looks for the ambition or potential dismissed too quickly |
| `ix:outsider` | reads like someone with no context at all |

Any ix-skills skill that carries a way of thinking can take a seat; the list is not closed.

### 4.3 Costumes: business dimensions

A costume is a **dimension that is easy to forget**: reason as a salesperson and you forget the money; reason as a product person and you forget who will live with the decision. It guarantees **coverage**, where the ghosts and postures bring **depth**. Each costume has four lines: the question it carries, what it looks at, what it does not judge (to stay in its lane), and its trap.

| Costume | The question it carries | What it looks at | Does not judge | Its trap |
|---|---|---|---|---|
| `costume:financier` | What does this do to cash, cost, the break-even point? | cash flows and their timing, the full cost (time included), what is committed before it is collected, the worst case in numbers | the opportunity | confusing what can be measured with what matters |
| `costume:commercial` | Is this the right moment, the right counterpart, the right move? | who buys and who decides, what the move says to the customer, the doors it closes, the likely reaction on the other side | the right price | mistaking the wish to sign for a market signal |
| `costume:produit` | Is this consistent with what we are supposed to make and sell? | the user's real problem, what the decision adds to or removes from the offer, the exception that becomes the rule | the timing | defending the roadmap against the reality that invalidates it |
| `costume:marque` | What does this say about us, and what does it damage? | the promise and whether it holds, the precedent set, how it reads to those who are not in the room | profitability | confusing image with reputation; the latter is built by what you do |
| `costume:technique` | What surface, what debt, what maintenance? | what will have to be run, repaired and evolved, who will know how, what breaks when it breaks | business value | preferring the elegant solution to the sufficient one |
| `costume:humain` | What does this cost the people who will live it? | the real workload and how it is shared, what it demands of those who did not decide, fatigue, trust, who leaves if it goes badly | everything else | speaking for people instead of saying what they should be asked |
| `costume:juridique` | What commitment, what risk, what reversibility? | what binds and who it binds, what can be undone and at what price, the obligations created, the evidence you keep | the opportunity | it flags, it does not replace a real lawyer |

The **Human** costume is the most often forgotten and the most often decisive: do not remove it to win an opinion.

**Adding a costume.** For a costume useful to everyone: add one more `## Name` section in `costumes.md`, with the four lines; `costume:name` works immediately. For a costume specific to your trade (and which has no place in a public repository): a file of your own, called with `file:<path>`.

### 4.4 Stakeholders: real interests

A stakeholder (`partie`) is **someone this particular decision affects**, seen from where they stand. Unlike costumes, stakeholders have no library: they change with every decision. `--seat partie:client` creates, when the session opens, a `## client` card in `PARTIES.md`, which the organizer fills in before the review. The fields are in French in the file; here is what each holds:

| Field | What goes in it |
|---|---|
| `Qui` (who) | the role or type of actor, **never a named real person** |
| `Mandat` (mandate) | what this stakeholder is responsible for, what it optimizes |
| `Ce qu'elle gagne ou perd` (what it gains or loses) | under each option, including "do nothing" |
| `Ce qu'elle sait` (what it knows) | what it knows well, the sources it believes |
| `Priorités` (priorities) | what it puts above what |
| `Angles morts` (blind spots) | what it tends not to see |
| `Lignes rouges` (red lines) | what it will not accept |
| `Changerait d'avis si` (would change its mind if) | the precise fact or result |

To find the stakeholders, ask: **who gains**, **who pays**, **who will live with the decision day to day**, **who can block it**, **who is quietly harmed**, and **who is on the other side of the table** (the customer, the buyer, the partner: this is often the most missing angle, because the decision-maker never puts themselves there).

Each stakeholder reads only its own card; the other angles do not open it. A card describes a position, never the conclusion it should draw.

**Costume or stakeholder?** `costume:financier` asks "what does this do to cash?". `partie:client` asks "what do I gain or lose, as the customer, under each option?". The first is a generic dimension; the second, a specific interest.

### 4.5 Your own angles

`file:<path>` seats any SKILL.md (or a folder that contains one). Handy for an in-house method, a trade-specific costume, or a skill from another plugin.

### 4.6 Composing a grid

- **Three angles** for a well-framed question, **five or six** for a heavy trade-off, **seven at most** in a deliberation. Beyond that, the synthesis becomes unreadable.
- **Mix the families.** Scattered consequences: costumes. A bet or a choice of direction: ghosts and postures. A decision that touches specific people: stakeholders. A heavy decision: a mix.
- **Three seats to check** before proposing: an angle with an interest in **doing nothing** (often `costume:financier` or `ix:executor`), an angle for **those with the least voice** (often `costume:humain` or a stakeholder), and an angle that **seriously defends the option** (often `ix:expansionist`). Without the last one, the grid leans one way only.
- **Two angles that would reason the same way** on the same facts count as one.

Example grid (invented) for "should we launch a paid offer?": `ghost:pascal`, `costume:financier`, `costume:humain`, `partie:client`, `ix:expansionist`, arbiter `adversarial`.

---

## 5. Formats

| Format | Flow | When |
|---|---|---|
| `tour` (default) | framing, grid → review → opinions in parallel → arbiter | most decisions |
| `compare` | framing, grid → review → two opinions side by side → what the divergence reveals | understanding why two frames see the same problem differently |
| `deliberation` | framing, grid → common file → review → round 1 + verifier → corrections → summary with lettered options → round 2 and vote → arbiter | a heavy, hard-to-reverse decision that hinges on facts |

**`compare`** takes exactly two angles. An isolated reader then writes, in two or three lines, the hypothesis the two do not share, posed as a question. With `--arbiter aucun` (none), you keep the pure side-by-side. Pairs whose tension is productive: Popper / Hegel, Kant / Machiavelli, Marx / Adam Smith, Aristotle / Plato, Sartre / Epictetus, Darwin / Tocqueville.

**`deliberation`** adds a **common file** (the sourced facts, identical for everyone), a **verifier** with no angle who checks every load-bearing fact against its source and publishes corrections as **addenda**, then a **second round** where each angle reads the others, answers them by name and votes on lettered options. It costs roughly twice as much as a `tour`.

The flow of each format is described in `skills/council/references/formats/<format>.json`; a custom format is passed by its path.

---

## 6. The arbiter

The choice of arbiter changes the result; it is always named in the delivery.

| `--arbiter` | What it produces |
|---|---|
| `neutre` (default) | a faithful map of convergences and disagreements, without ruling |
| `adversarial` | only what holds up against a hostile reader survives |
| `ghost:zeus` | an arbitration from a jurisdiction; its verdict remains one more opinion, placed under the map |
| `ghost:nash` | the arbitration read as an equilibrium between positions |
| `ghost:aristote` | the convergences treated as cases, with minimal generalization |

Any other ghost, posture or file can arbitrate: it then applies **its method to the arbitration**, not to the problem, and imports its biases (the synthesis has a section to say so). A stakeholder cannot arbitrate: it takes a seat.

The arbiter reads `GRILLE.md`, and so the decision-maker's leaning, for one test only: would its synthesis read the same if the decision-maker had leaned the other way?

---

## 7. Framing, grid and review

The framing is the piece that most often skews a council: each angle takes up, without knowing it, everything the framing treats as settled. Hence three pieces.

**Two files, two readers.**

| | `CADRAGE.md` (framing) | `GRILLE.md` (grid) |
|---|---|---|
| Who reads it | the angles, the reviewer, the arbiter | the decision-maker, the reviewer, the arbiter; **never the angles** |
| Contents | the question, the sourced facts, the authorized sources, the options (including "do nothing"), what is not known | the validated grid, what each angle covers, the three seats, the decision-maker's leaning, the discarded angles, the review's reservations |

**The framing rules** (details in [`references/cadrage.md`](../../skills/council/references/cadrage.md)):

- a **neutral** session title and question;
- no urgency: a deadline is a fact, not pressure;
- all the options, including **doing nothing**, with what they commit to, as facts;
- every fact **copied from its source**, which has been re-read, never from memory;
- no opinion already given in the sources; a source that mixes facts and opinions is not authorized for the angles;
- in `GRILLE.md`, write what an angle covers ("decision under uncertainty"), **never what it should find**.

**The review.** A sub-agent with no angle reads the framing, the grid and the stakeholder cards, and returns `RELECTURE.md` (the review): leaks, planted premises, facts checked against their source, what is missing, requested corrections, with a verdict of "prêt" (ready) or "à corriger" (needs fixes). The script refuses to start the round until it says "prêt". **At most two reviews**: if the second still asks for corrections, the organizer applies what can be applied, notes the rest in `GRILLE.md` §6, and the decision-maker lifts the lock with the line `**Relecture levée par :** <who>, réserves en §6` (review waived by, reservations in §6).

The final test before the round: could an angle that read only `CADRAGE.md` guess what the decision-maker hopes for? If so, it is not ready.

---

## 8. One model per seat

Each seat, and the arbiter, can carry its own model with `@`: `--seat ix:dixieme-homme@opus`, `--arbiter neutre@sonnet`.

| Model | How it is launched |
|---|---|
| no `@` | Claude Code sub-agent, default model |
| `opus`, `sonnet`, `haiku` | Claude Code sub-agent with that model |
| `codex` | `codex exec -s read-only --ephemeral -o <file> "<brief>"` |
| `gemini` | `agy -p "<brief>" --sandbox > <file>` |

Varying the models decorrelates the blind spots a little, never completely. Careful: a `codex` or `gemini` seat sends the framing and its sources to another provider. For a confidential decision, stay with Claude seats.

---

## 9. Files in a session

Everything lives in one folder, chosen when the session opens. Each file is born as a template marked `<!-- council:todo -->`, removed once it is written.

| File | Written by | Read by | Contents |
|---|---|---|---|
| `council.json` | the script | the script | the grid, the models, the format, frozen at opening |
| `CADRAGE.md` | the organizer | angles, reviewer, arbiter | the question, the facts, the sources, the options |
| `GRILLE.md` | the organizer | decision-maker, reviewer, arbiter | the grid, the leaning, the reservations |
| `PARTIES.md` | the organizer | each stakeholder (its card), reviewer, arbiter | one card per stakeholder |
| `RELECTURE.md` | the reviewer | the organizer | leaks, verified facts, verdict |
| `AVIS-<angle>.md` | each angle | the arbiter | position, confidence, risks, what is missing, where the framing is wrong |
| `SYNTHESE.md` | the arbiter | the decision-maker | convergences, disagreements, blind spot, question to decide, next steps |
| `DIVERGENCE.md` | the reader (`compare`) | the decision-maker | what the divergence reveals |
| `DOSSIER.md` | the organizer (`deliberation`) | everyone | the common factual statement |
| `VERIFICATION.md` | the verifier | the organizer | one verdict per load-bearing fact |
| `ADDENDUM-<letter>.md` | the organizer | everyone | the corrections, never an opinion |
| `BILAN-TOUR1.md` | the organizer | angles in round 2, arbiter | positions, disagreements, lettered options |
| `TOUR1-` / `TOUR2-<angle>.md` | each angle | (round 2: everyone); arbiter | round-1 opinion, then round-2 vote |

(In French: `AVIS` = opinion, `SYNTHESE` = synthesis, `BILAN` = summary, `TOUR` = round.)

---

## 10. The `council.py` script

It lives in the skill folder: `<skill folder>/scripts/council.py`. Plain Python, no dependencies; it never overwrites a file.

| Command | What it does |
|---|---|
| `init SEANCE --title "…" --seat REF[@MODELE] … [--format …] [--arbiter …]` | creates the session (`SEANCE`, the session folder) and its templates; an unknown reference stops everything before anything is written |
| `status SEANCE` | the state of each step and the next thing to do |
| `resolve REF …` | the file an angle will read |
| `brief SEANCE ETAPE [ANGLE]` | the brief to give as is to the sub-agent (`ETAPE` = step); refuses if an earlier step is not done or not valid |
| `addendum SEANCE` | the next corrections addendum (`deliberation`) |
| `tally SEANCE [--step …]` | the table of positions, or the vote count |
| `check SEANCE [--final]` | checks the process: order of steps, mandatory fields, arbiter named, no vote in an addendum… |

All accept `--json`. Exit codes: 0 ok, 1 usage error (the message says what to do), 2 malformed command, 3 the check found a problem.

In practice, you do not have to run it yourself: Claude, in the organizer role, uses it at every step.

---

## 11. Frequently asked questions

**How much does it cost?** A `tour` session with six angles is eight or nine model runs (review, angles, arbiter); a `deliberation`, about double. Keep it for decisions that commit you; for a closed, low-stakes question, a single contrary opinion is enough.

**Why not just ask for "the pros and the cons"?** Because a single interlocutor returns a smooth synthesis that mostly reflects how the question was asked. The council separates the points of view, keeps them from reading each other, and hands back their disagreements instead of blending them.

**What if all the angles agree?** The arbiter says so plainly, without manufacturing a disagreement, but it checks whether the agreement comes from different paths (a strong signal) or from a single premise (a suspicious signal, often planted by the framing).

**Can the council be wrong about what matters to me?** Yes. The angles weigh facts, not your values. It may unanimously advise against something you will do anyway, for a reason none of them had. That is normal: it informs, you decide.

**Where do my sessions live?** In the folder you choose, inside your project. Nothing goes elsewhere, unless you seat an external model (`codex`, `gemini`).

**Can I pick a question back up?** Yes: a new session, where the facts that survived and the synthesis's open questions come in as sourced facts, never as an angle's opinion.

---

## 12. Limits

- **Independence has a ceiling.** Opinions from the same model share its blind spots.
- **The framing remains fragile.** The review catches many leaks; a perfectly neutral framing does not exist.
- **The voices are simulated.** No real stakeholder has spoken; real checks (customers, a lawyer, data) are still to be done.
- **A method-based arbiter imports its biases**, hence the obligation to name it.

The details: [SKILL.md](../../skills/council/SKILL.md), [framing guide](../../skills/council/references/cadrage.md), [common file](../../skills/council/references/dossier.md), [verification](../../skills/council/references/verification.md).

The script, the common file, the verifier and the second round are adapted from [advisory-council](https://github.com/nzanepro/tvr-skills-agent-advisory-council) by nzanepro (MIT, see [THIRD_PARTY.md](../../THIRD_PARTY.md)).
