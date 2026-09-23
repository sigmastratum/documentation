---
title: SRIP Control Precedence Review
description: Non-normative review model for resolving control conflicts across the SRIP architecture.
published: true
date: 2026-09-23T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-07-17T00:00:00.000Z
---

> **Sigma Runtime Standard - Public Integration Notice**
>
> This non-normative integration document is licensed under Creative Commons
> Attribution 4.0 International (`CC BY 4.0`). It does not amend canonical
> SRIPs or grant implementation, certification, or runtime authority.

# SRIP Control Precedence Review

Status: **Non-normative review draft**

This document proposes a common way to inspect control conflicts across SRIPs.
It does not override precedence rules declared in canonical proposals. Any
conflict between this review model and an SRIP is a finding requiring a separate
normative review.

## 1. Why Precedence Is Needed

Several SRIPs can legitimately produce different recommendations for one
runtime state. For example:

- entropy regulation may request perturbation while safety requests containment;
- retrieval may find relevant material while memory-influence governance rejects
  its authority;
- dialectical generation may produce a useful candidate while governance blocks
  canonical promotion;
- a commerce semantic signal may suggest a candidate while deterministic
  commerce state forbids the transition.

The architecture needs a stable distinction between evidence, recommendation,
authorization, execution, and post-effect audit.

## 2. Control Classes

| Class | Meaning | Representative SRIPs |
| --- | --- | --- |
| Evidence | Observes or measures state without granting authority | 03, 07, 08, 16, 21, 27 |
| Assembly | Selects, compresses, or structures context | 11, 14, 18, 25 |
| Recommendation | Proposes regulation, perturbation, or candidate state | 10, 15, 16, 23 |
| Boundary | Allows, limits, quarantines, or rejects influence | 06, 13, 20, 26 |
| Domain authority | Owns deterministic state within a declared domain | 12 |
| Governance authority | Evaluates legitimacy, capture, contestability, and promotion | 22 |
| Effect execution | Represents authorized contact with an external target | 05, 17, 24, 25 |
| Recovery | Preserves or restores valid state after conflict or instability | 06, 09, 13, 19 |
| Admission transaction | Selects one candidate for delivery before persistence | 28 |

One SRIP may occupy more than one class, but each individual output should state
which class it represents.

## 3. Provisional Precedence Stack

The following order is a review hypothesis, not a new normative rule:

1. **Non-bypassable safety and recursion boundaries** — `SRIP-06`.
2. **Explicit current authorization, consent, and protected autonomy bounds** —
   principally `SRIP-20`, with identity scope from `SRIP-13` and external
   identity evidence from `SRIP-21`.
3. **Legitimate governance and capture handling** — `SRIP-22`.
4. **Provenance, retrieval, and memory-influence admission** — `SRIP-14` and
   `SRIP-26`.
5. **Declared deterministic domain invariants** — for commerce, `SRIP-12`.
6. **Contradiction preservation and recovery** — `SRIP-19` and applicable
   recovery paths in `SRIP-06`, `SRIP-09`, and `SRIP-13`.
7. **Candidate measurement and admission** — `SRIP-27` supplies evidence and
   `SRIP-28` owns the pre-persistence commit point within all higher boundaries.
8. **Adaptive regulation and controlled perturbation** — `SRIP-03`, `SRIP-07`,
   `SRIP-08`, `SRIP-10`, and `SRIP-15`.
9. **Candidate generation, semantic optimization, and presentation choices** —
   `SRIP-18`, `SRIP-23`, and non-normative style mechanisms.

Higher precedence generally limits lower-precedence action. It does not permit a
higher layer to fabricate missing evidence or silently assume authority outside
its declared scope.

Precedence is not temporal ordering. Generation may occur before measurement,
but a generated candidate remains non-canonical until SRIP-27 evidence and the
SRIP-28 transaction are evaluated. SRIP-28 owns the commit point; it does not
override safety, authorization, governance, or deterministic domain authority.

## 4. Conflict Resolution Algorithm

For any proposed state transition or effect:

1. Identify the proposed action and the SRIP output that requested it.
2. Classify that output as evidence, recommendation, boundary, domain authority,
   governance authority, recovery, or effect execution.
3. Bind the action to actor, target, scope, time, source, and authority.
4. Evaluate non-bypassable safety constraints.
5. Evaluate current authorization, consent, identity, and autonomy constraints.
6. Evaluate provenance and memory-influence admission.
7. Apply applicable deterministic domain invariants.
8. Preserve unresolved valid conflict rather than forcing consensus.
9. Allow optimization or generation only within the remaining action envelope.
10. Measure target membership without treating dynamic stability as membership.
11. Apply the pre-persistence admission transaction and select at most one
    delivered candidate.
12. Prepare any staged effect intent and commit accepted runtime-local state
    with a recoverable binding to that intent, independently of effect release.
13. For consequential effects, verify the committed intent binding, revalidate
    current authority, and release only through the SRIP-24 boundary.
14. Record authorization, attempt, outcome observation, and verification as
    distinct SRIP-25 linked events or typed states.
15. Record the winning constraint, suppressed proposals, evidence quality, and
    resulting event or no-op.

Missing authority fails closed for effects. Missing evidence should produce an
unknown or deferred state rather than an invented authorization.

## 5. Representative Conflict Cases

### Relevant memory versus current authority

`SRIP-14` may retrieve relevant material. `SRIP-26` may still limit or reject
its influence because relevance does not establish current scope, consent, or
authority.

### Entropy regulation versus safety

`SRIP-10` may recommend variation and `SRIP-15` may propose perturbation.
`SRIP-06` can block the transition when recursion, instability, or containment
constraints apply.

### Self-model proposal versus autonomy

`SRIP-16` may report a recurring control mismatch. That report is evidence.
`SRIP-20` evaluates whether any boundary adjustment is authorized; the
self-model cannot authorize its own expansion.

### Dialectical candidate versus canonical promotion

`SRIP-23` may generate a candidate from contradiction preserved by `SRIP-19`.
The candidate does not delete the contradiction and cannot become canonical
solely because it is coherent. Applicable governance remains required.
`SRIP-27` may measure its target membership, but only `SRIP-28` may select it
for accepted delivery and downstream influence.

### Dynamic stability versus trajectory membership

`SRIP-10` may report stable dynamics while `SRIP-27` reports a displaced or
collapsed trajectory. Stability does not override membership. `SRIP-28` must
contain a candidate that lacks qualified admission evidence.

### Commerce semantics versus commerce state

`SRIP-18` may improve grounding and candidate assembly. `SRIP-12` retains
deterministic authority over valid commerce transitions and rejection rules.

### External effect versus transport success

`SRIP-24` owns effect staging, current-authority validation, release, retry,
compensation, and escalation. `SRIP-25` separately represents authorization,
attempt, outcome observation, and verification. A successful tool or transport
call does not retroactively establish valid authority or prove external
outcome. `SRIP-28` candidate admission does not authorize the effect.

## 6. Required Audit Fields

A future machine-readable control decision envelope should be able to expose:

- proposed action and originating SRIP;
- control class;
- actor, target, scope, and time bounds;
- evidence references and quality;
- required and observed authority;
- applicable constraints in evaluation order;
- winning rule and suppressed proposals;
- decision: allow, limit, defer, quarantine, reject, recover, or unknown;
- candidate, measurement, admission, and selected-delivery references;
- effect event and post-effect evidence, when applicable.

This review document does not define that schema. A schema would require a
separate normative or machine-readable-artifact decision.

## 7. Open Review Questions

1. Does safety always precede governance, including emergency governance?
2. How are conflicts between explicit user authorization and durable safety or
   identity invariants represented?
3. Does `SRIP-22` govern only institutional legitimacy, or runtime-local control
   authority as well?
4. Which recovery mechanism owns a conflict spanning identity, memory, and
   contradiction simultaneously?
5. Must every effect emit an `SRIP-25` event, or only implementations claiming
   the relevant environment profile?
6. Which precedence rules belong in existing SRIPs and which require a dedicated
   normative control-precedence proposal?
