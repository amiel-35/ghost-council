# council — Let the methods deliberate before you decide

## Why this encoding?

Each ghost in the collection applies one method to a problem. But a decision that commits you rarely benefits from being read through a single method: Popper looks for what refutes, Pascal weighs asymmetric stakes, Machiavelli reads power dynamics, and none of them sees what the others see. `council` encodes the operation that makes them work together without blending them: each angle works alone, in a fresh context, then an arbiter returns the map of what converges and what clashes.

It isn't a philosophical method, it's a procedure. The one variable that matters is the independence of the opinions: an opinion that has read the others, or guessed what the decision owner hopes for, is no longer an opinion, it's an echo. Everything else (keeping the framing apart from the grid, reviewing the framing before the round, forbidding angles to open each other's work) exists to protect that independence.

## What the method corrects

Ask a single interlocutor for "the pros and cons" and you get a smooth summary that mostly reflects how the question was asked. `council` corrects that three ways. Angles never read each other, so whoever speaks first doesn't anchor the rest. The framing is reviewed by an isolated reader hunting for leaks (the owner's leaning, a premise stated as settled, a fact written from memory) before the round starts. And the arbiter doesn't decide: it returns the disagreement intact, with what grounds each side and the result that would move each one.

When someone says "we talked it through, everyone agreed", `council` asks: agreed from the same premise, or agreed by different routes? Only the second is a signal.

## When to invoke it

- Before a decision that commits you and can't easily be undone: a price, a commitment, a direction, a hire, an investment
- When you suspect you already have your answer and want to know what it leaves out
- When several dimensions pull against each other (money, people, law, timing) and one is likely to be forgotten
- To compare two frames of thought on the same question (`--format compare`), or for a full deliberation with a shared dossier and a verifier (`--format deliberation`)

## When not to invoke it

- For a cheap, reversible decision: the ritual costs more than the mistake it prevents
- When the decision hinges on missing data: fetching it is cheaper than having six opinions deliberate over a void
- On regulated, legal or medical matters, in place of a real expert: the council informs, it commits no one
- To critique an already-written text, or to pick between options already scored on known criteria: other tools do that better

## Use cases

### 1. Launching a paid tier

**Context:** A small product team is considering moving its free tool to freemium before year end. The founder leans toward doing it.

**Input:** the request "Should we move to freemium before year end?", with a grid proposed by the facilitator and validated by the founder: `ghost:popper`, `costume:financier`, `costume:humain`, `partie:utilisateur-actuel`, `ix:expansionist`, arbiter `adversarial`. The founder's leaning goes in `GRILLE.md`, which the angles never read.

**What the skill produces:** A framing review that first flags that the question carries the deadline ("before year end") as if it were imposed, when it's an internal choice: the question gets reworded. Then five independent opinions and a synthesis: the angles converge on the fact that conversion has never been measured (Popper and the finance angle get there by different routes, a strong signal); they clash over what current users lose (the stakeholder seat) versus what the team gains (the expansionist). The question to settle is phrased to be decidable, with the first step: measure on one segment before rolling out, and the conversion threshold that would tip the decision.

### 2. Comparing two frames on a reorganisation

**Context:** Leadership wants to merge two teams. Two managers see the same plan in opposite ways and can't say why.

**Input:** the request "Merge the two teams next quarter?", in `compare` format, with `ghost:marx` and `ghost:adam-smith`.

**What the skill produces:** Two opinions side by side, then, written by an isolated reader, what the divergence reveals, posed as a question: "The two readings don't disagree about the merger, they disagree about what holds a team together: a power balance to restore, or an incentive mechanism to realign. Which of the two actually broke here?" No verdict: the tension made visible.

### 3. A heavy decision that hinges on facts

**Context:** A non-profit is weighing buying its premises instead of renting. Figures are circulating, but nobody knows which ones are right.

**Input:** the request "Buy the premises or keep renting?", in `deliberation` format, with seven angles including `costume:juridique`, `partie:benevoles` and `ghost:pascal`.

**What the skill produces:** A shared dossier written before the round, with sourced facts and stated unknowns; an angle-free verifier who checks every load-bearing figure against its source and publishes corrections as addenda ("the rent quoted is last year's"); an independent first round, a tally with lettered options, a second round where each angle answers the others and votes; then a synthesis with the vote, the dissent in its strongest form, and for each next step the result that would change the decision.

## Limits of this encoding

Independence has a ceiling. If every opinion comes from the same model, they share its blind spots; varying the model per seat decorrelates a little, never fully. A council of six angles from one model is still one intelligence changing hats, with safeguards.

The framing stays the weakest link. The review catches many leaks, but a perfectly neutral framing doesn't exist, especially when the owner's own sources were written with their option in mind. The method therefore caps the review at two passes, then asks the owner to lift the lock and record the reservations. Those reservations must be read: a council whose framing leaked returns a tilted map.

Angles weigh facts, not the owner's values. A council can unanimously advise against what the owner will do anyway, for a reason no angle had, because it rests on what matters to them and nobody asked. The council informs, it doesn't replace judgment; keep that in mind when reading a unanimous result. A follow-up is planned: a "what matters to the decision owner" section in `GRILLE.md`, read by the arbiter.

The cost is real: a six-angle `tour` session is around ten runs with the review and the arbiter; a full `deliberation` doubles that. Keep it for decisions that are worth it.
