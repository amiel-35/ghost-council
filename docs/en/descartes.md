# Descartes — Making implicit assumptions explicit

## Why this encoding?

Irreversible decisions rarely fail because the visible reasoning was wrong. They fail because an implicit assumption — unstated, therefore never verified — turned out to be false after it was too late to go back. Encoding Descartes doesn't produce "doubt everything," which would be paralyzing. It produces a precise operation: make the list of implicit assumptions explicit, rank them by certainty, and flag conclusions that hold only on unverified assumptions.

## What the method corrects

When someone says "we're assuming that..." or "it's obvious that..." or "everyone knows that...", the method asks: is that actually established, or is it an assumption dressed up as certainty? It corrects the confusion between what withstands doubt and what has simply never been doubted. These are very different things.

## When to invoke it

- Before any irreversible decision — acquisition, technical architecture, revenue model
- When a line of reasoning rests on assumptions presented as self-evident
- When someone uses "we've always done it this way" as an argument
- When a plan chains multiple assumptions without making them explicit

## When not to invoke it

- When acting under uncertainty is unavoidable and prolonged doubt has a real cost
- On low-stakes reversible decisions — the method is disproportionate
- When knowledge necessarily rests on community practice — some certainties aren't reconstructible through individual doubt

## Use cases

### 1. Technical architecture decision

**Context:** A team chooses microservices architecture for an early-stage product.

**Input:** "We'll build in microservices from the start — it's the standard today."

**What the skill produces:** "Implicit assumptions: (1) the team is large enough to operate microservices, (2) the domain is stable enough to correctly split services now, (3) the added operational complexity is worth the scalability gain. — For each: is this established or assumed? Assumption 1: how big is the team? Assumption 2: do you know the domain well enough to split it now? Assumption 3: have you hit the limits of a monolith?"

### 2. Product launch plan

**Context:** A team plans a launch based on an assumption of organic growth.

**Input:** "Our plan rests on organic growth — users will naturally recommend the product."

**What the skill produces:** "Implicit assumptions: (1) the product generates enough value to motivate spontaneous recommendation, (2) a natural recommendation mechanism exists in this market, (3) organic growth alone is sufficient within the target timeline. — Which of these three is most fragile? What does it rest on? What happens if it's false?"

### 3. Strategic hiring decision

**Context:** A startup wants to hire an enterprise VP Sales before having any enterprise customers.

**Input:** "We'll hire a VP Sales enterprise now — it'll open that market for us."

**What the skill produces:** "Implicit assumptions: (1) the product is enterprise-ready, (2) a VP Sales can open this market without a complete offer, (3) we can retain this profile while the market gets ready. — Is each of these established or assumed? If assumption 1 is false, what does that cost?"

## Limits of the encoding

Radical doubt is useful but artificial — in practice, you can't question everything simultaneously without paralyzing yourself. The criterion of "clarity and distinctness" that Descartes uses to validate a certainty is itself subjective: what's clear to one person isn't to another. The method reconstructs poorly the knowledge that depends on context or collective practice — some certainties aren't isolable through individual doubt, they hold within a shared system.
