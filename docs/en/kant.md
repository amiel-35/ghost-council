# Kant — The categorical imperative as ethical filter

## Why this encoding?

Most ethical analysis tools are consequentialist: a decision is evaluated by its results. Kant does the opposite — an action is ethical if its maxim can be universalized, regardless of what it produces in this particular case. The encoding is especially useful when "it's legal so it's fine" or "everyone does it" are presented as sufficient arguments. Without this encoding, Claude tends to nuance, contextualize, find compromise. Kant doesn't compromise.

## What the method corrects

When someone says "we can afford to" or "it's within the rules" to justify a decision, the method asks: if everyone did this, would it hold? It corrects the reasoning that conflates "permitted" with "ethical," and the temptation to treat users as means while dressing it up as optimization or "better experience."

## When to invoke it

- On pricing, data, AI, and terms-of-service decisions
- When the argument is "everyone in this industry does it"
- When a decision benefits the company at users' expense, packaged as "user value"
- When someone says "it's legal" as if that were sufficient ethical grounds
- When an internal rule treats people differently based on their utility to the company

## When not to invoke it

- On decisions where concrete consequences matter as much or more than principles
- On edge cases where the categorical imperative produces manifestly counter-intuitive conclusions
- When what you're looking for is a pragmatic recommendation, not an ethical verdict

## Use cases

### 1. Dark patterns in a cancellation flow

**Context:** A team designs a subscription cancellation button that's hard to find.

**Input:** "We put the cancellation button in a sub-menu — it's within the rules, and it reduces churn."

**What the skill produces:** "Implicit maxim: it's acceptable to make it difficult to exercise a contractual right when it benefits the company. — Universalization test: if all companies did this, the institution of reciprocal contract would lose its meaning — no one could trust the terms of an agreement. Logical contradiction. — Humanity test: users are treated as revenue sources to retain, not as persons exercising a right. Verdict: contrary to duty."

### 2. Using data for non-consented personalization

**Context:** A team wants to use behavioral data for targeted advertising without explicit consent.

**Input:** "We use behavioral data for advertising — it's industry standard, and the ToS permit it."

**What the skill produces:** "Implicit maxim: it's acceptable to use a person's data for purposes they didn't explicitly choose if legal terms permit it. — Universalization test: if all companies did this by default, the meaning of consent would disappear. — Humanity test: users are means of monetization, not ends. 'The ToS permit it' is a legal answer, not an ethical one."

### 3. Differential pricing based on perceived value

**Context:** A team wants to charge more to customers who show the most engagement.

**Input:** "We can charge more to customers who use the product most — they get more value from it."

**What the skill produces:** "Implicit maxim: price should reflect buyer dependency, not value produced. — Universalization test: if all sellers did this, buyers would avoid showing dependency, destroying the signal. Contradiction. — To distinguish: charging more for superior features (conforming to duty) vs charging more because the customer is captive (contrary to duty)."

## Limits of the encoding

The categorical imperative can produce counter-intuitive conclusions in edge cases: Kant himself held that you should never lie, even to save a life. This moral formalism ignores the particularities of concrete situations — which can make it inapplicable in contexts where contextual nuance is precisely what's at stake. The method is categorical by design: if you're looking for compromise, Kant is the wrong tool.
