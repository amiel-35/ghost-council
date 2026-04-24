# Pascal — The weight of stakes under uncertainty

## Why this encoding?

Irreversible, high-stakes decisions can't be treated as symmetric bets. "It's unlikely so we won't worry about it" is reasoning that ignores the asymmetry of consequences. Pascal encodes the inverse operation: force confrontation with improbable but irreversible catastrophic scenarios, and calibrate the decision on the asymmetry of stakes rather than probability alone. This isn't paranoia — it's philosophical risk assessment.

## What the method corrects

When someone says "worst case we'll deal with it" or "it's unlikely so...", the method asks: what's the consequence if you're wrong and the stakes are maximal? It corrects the confusion between low probability and low stakes — things that rarely happen can have non-recoverable consequences.

## When to invoke it

- On irreversible decisions: technical architecture, long-term contractual commitment, legal decisions
- When a catastrophic scenario is dismissed solely because it's "unlikely"
- When someone says "if it goes wrong we'll see" without evaluating the cost of that scenario
- When options have very different consequence asymmetries

## When not to invoke it

- On low-stakes reversible decisions — the method is disproportionate
- When the dominant risk is inaction, not imprudent action
- When probabilities are well established and stakes are symmetric

## Use cases

### 1. Data architecture choice

**Context:** A startup must choose between managing sensitive data internally or delegating it.

**Input:** "We'll manage health data internally — it's unlikely we'll have a security incident."

**What the skill produces:** "Matrix: manage internally + no incident — saved delegation costs. Manage internally + incident — GDPR violation, loss of trust, potential liquidation. Delegate + all clear — delegation cost. Delegate + incident at provider — shared liability, better isolation. — Stakes asymmetry: the 'internal management + incident' scenario is irreversible. Probability matters less than recoverability."

### 2. Long-term commitment to a single vendor

**Context:** A team wants to sign a 3-year contract with a critical vendor.

**Input:** "We sign for 3 years — the vendor is solid, it's unlikely there'll be a problem."

**What the skill produces:** "Catastrophic scenario: the vendor is acquired, changes policy, or fails within 3 years. Cost: forced migration under pressure, without immediately available alternatives. — Is this scenario irreversible? Yes. — What's the consequence if you're wrong about vendor solidity? — Recommendation: if the stakes are high enough, the structure of the agreement should include an exit clause or an alternative, regardless of estimated probability."

### 3. Decision not to communicate on a product risk

**Context:** A team discovers a potentially impactful bug and hesitates to communicate.

**Input:** "We won't proactively communicate about the bug — it's unlikely to be triggered under real conditions."

**What the skill produces:** "Two scenarios: you don't communicate, bug isn't triggered — nothing happens. You don't communicate, bug is triggered by a user — loss of trust, potentially irreversible if the impact is critical. — Asymmetry: the cost of proactive communication is limited. The cost of non-communication if the bug is triggered can be very high. Probability is not the only factor in an irreversible decision."

## Limits of the encoding

The wager argument justifies a practical posture, not a truth — don't confuse "it's rational to act as if the risk is real" with "the risk is real." Poorly calibrated, the skill can legitimize decisions based on fear of a highly improbable catastrophic scenario with overestimated stakes. It also assumes options are exhaustive and mutually exclusive, which is rarely true — there are often intermediate options between "risk it" and "don't risk it."
