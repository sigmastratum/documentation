> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-12: Commerce Decision State Layer (CDS)
**Version:** 1.1  
**Status:** Draft / Implementation Pending  
**Implementation Target:** SIGMA Runtime >= v0.6.x  
**Depends on:** SRIP-09 (LTM), SRIP-10 (AEP), SRIP-11 (CMT)  
**Related Specs:** SRIP-13 (RIS)  
**Author:** Sigma Stratum Research Group  
**Date:** 2026-04-11  
**License:** CC BY-NC 4.0 / Canon CIL Applicable

---

## I. Purpose
SRIP-12 defines a deterministic **Commerce Decision State Layer (CDS)** for product-selection dialogues.

Its goals are to:
- lock a primary recommendation (anchor) once sufficient constraints exist;
- prevent unauthorized anchor replacement;
- process explicit rejection and hard constraint invalidation correctly;
- enforce brand/candidate governance over long conversations;
- keep decision control internal and prevent policy leakage into user-facing text;
- align commerce enforcement terminology with the SRIP-13 invariant enforcement architecture.

This is a **runtime business-control layer**, not a style layer.

Implementation status: SRIP-12 defines the target CDS architecture and
conformance requirements. It is not considered production-ready until runtime
implementation, scenario testing, and replay validation are complete.

---

## II. Problem Statement
Long-horizon ecommerce dialogues tend to drift toward option expansion:
- primary candidate is replaced without explicit user rejection;
- new brands are introduced mid-session without authorization;
- off-table lists mix user exclusions with internal candidate state;
- control rules leak into user-facing responses.

SRIP-12 resolves this via deterministic state, hard gates, and structured persistence.

---

## III. Core Concepts

| Term | Description |
|------|-------------|
| **Decision Context Store** | Per-session structured state for commerce decision control. |
| **Primary Anchor** | Current primary candidate (model + brand) protected by lock rules. |
| **Allowed Candidates** | The only candidate set that may be proposed in the current turn. |
| **User Exclusions** | Explicitly excluded brands/models provided by the user. |
| **Rejected Candidates** | Candidates explicitly rejected by the user during the session. |
| **Decision Phase** | Runtime state: `discovery`, `narrowing`, `anchored`, `reinforced`, `transition`. |
| **Hard Gate** | Binary runtime guard that blocks invalid candidate/brand transitions. |
| **Off-Table Contract** | Deterministic output = `user_exclusions + rejected_candidates` only. |
| **Decision Assertion Model** | Structured representation of generated commerce claims against the current decision state. |
| **Decision Invariant** | A deterministic rule that must remain true after generation, such as anchor lock or off-table integrity. |
| **Deterministic Transform** | Bounded correction that restores decision invariants without changing the decision state machine. |
| **Fallback Response** | Minimal compliant response used when invariants cannot be restored by deterministic transform. |
| **Enforcement Evidence** | Structured metadata describing validation, violations, transform class, and final handling mode. |

---

## IV. Decision State Machine

### 1. Phases
| Phase | Behavior |
|------|----------|
| `discovery` | Collect constraints (budget, use-case, exclusions, style requirements). |
| `narrowing` | Propose up to configured candidate count and select anchor. |
| `anchored` | Anchor is locked; no new primary unless explicit unlock condition. |
| `reinforced` | Keep same anchor and adapt explanation to context refinements. |
| `transition` | Constraint change detected; re-evaluate anchor validity deterministically. |

### 2. Valid Transitions
1. `discovery -> narrowing` when minimum constraint threshold is met.  
2. `narrowing -> anchored` when primary candidate is selected and valid.  
3. `anchored -> reinforced` when user refines context without rejection/invalidation.  
4. `anchored|reinforced -> transition` on explicit constraint change.  
5. `transition -> anchored` if anchor remains valid.  
6. `transition -> narrowing` if anchor is rejected or invalidated.

### 3. Anchor Selection Rule (Mandatory)
**Anchor selection moment** is defined at the first recommendation turn in `narrowing` where runtime emits a candidate list.

Primary anchor is:
- the first candidate in the deterministic ordered candidate list;
- unless user explicitly selects another candidate from the same list.

If user does not explicitly choose, first candidate is considered selected by default and state transitions to `anchored`.

### 4. Deterministic Candidate Ordering (Mandatory)
For identical constraints and identical pool inputs, candidate ordering must be identical.

Deterministic ordering contract:
1. sort by candidate score (descending);  
2. tie-break by normalized brand (ascending);  
3. tie-break by normalized model_id (ascending).  

Ordering metadata (`ordering_version`, `ordering_inputs_hash`) must be persisted per decision turn for replay parity.

---

## V. Enforcement Rules

The rules in this section are **decision invariants**. They define what must be
true before a commerce response is released. They do not change the decision
state machine in § IV or the allowed-candidate derivation in § VI.

### 1. Anchor Lock (Mandatory)
If all are true:
- primary anchor exists;
- user did not reject primary;
- constraints do not invalidate primary;

then:
- introducing a new primary candidate is forbidden;
- new-brand introduction is forbidden unless unlock conditions are met.

This rule is **binary** (hard gate), not probabilistic.

### 2. Anchor Auto-Swap Ban (Mandatory)
When anchor is locked, the runtime must not:
- silently promote secondary candidate to primary;
- replace anchor because model proposes a "better fit";
- rotate primary due to stylistic novelty.

Primary can change only via explicit rejection or hard invalidation.

### 3. Constraint Change Semantics
Constraint changes are classified as:
- **soft refinement**: does not invalidate anchor (keep anchor);
- **hard invalidation**: incompatible with anchor (reject anchor, transition to `narrowing`).

Soft refinements (for example additional context like occasional travel) must not trigger automatic anchor replacement.

### 4. Rejection Rules
Rejection is valid when:
- user explicitly rejects current candidate/model/brand; or
- user provides a hard constraint that invalidates current anchor.

On rejection:
- move current anchor to `rejected_candidates`;
- clear `primary_anchor`;
- set phase to `narrowing`.

### 5. Off-Table Contract
When user asks what is off-table, runtime must return only:
- explicit `user_exclusions` (brands/models);
- explicit `rejected_candidates`.

It must never include:
- current candidate pool;
- inferred bans;
- hidden runtime decisions.

### 6. Policy Leakage Ban
Internal controls (state, allowed set, guard rules, diagnostics) are runtime-only and must not appear in user-facing text.

---

## VI. Allowed Candidate Derivation (Deterministic)

`allowed_candidates` must be derived by state, not by free-form model behavior.

Reference policy:

```text
if state == discovery and constraints < min_constraints_for_narrowing:
    allowed_candidates = []

elif state == narrowing and primary_anchor is null:
    allowed_candidates = deterministic_pool[:max_initial_candidates]

elif primary_anchor exists and not rejected and not invalidated:
    if user_explicitly_requests_alternative:
        allowed_candidates = [primary_anchor] + deterministic_secondaries[:alt_limit]
    else:
        allowed_candidates = [primary_anchor]

elif primary_anchor rejected or invalidated:
    allowed_candidates = deterministic_pool_excluding_exclusions_and_rejections[:max_initial_candidates]

else:
    allowed_candidates = []
```

Additional constraints:
- `allowed_candidates = []` means runtime asks for missing constraints and must not recommend products.
- Secondary candidates remain allowed only when explicitly requested or when state is `narrowing`.
- `off-table` answers must not read from `allowed_candidates`.

---

## VII. Runtime Integration

CDS is integrated into each runtime cycle through deterministic hooks:

1. Load decision state for session.  
2. Parse and merge user constraints.  
3. Detect rejection/invalidation events.  
4. Transition state machine.  
5. Derive `allowed_candidates` (hard gate).  
6. Build hidden control instructions for generation.  
7. Generate response.  
8. Build a decision assertion model from the generated response.  
9. Validate the assertion model against decision invariants.  
10. Apply deterministic enforcement if invariants are violated.  
11. Persist updated decision state and enforcement evidence.

### 1. Invariant Validation and Enforcement (Mandatory)

If generated response violates CDS invariants, runtime must follow one
deterministic handling path:

1. **Reject unsent response** at invariant validation stage.  
2. Apply a bounded deterministic transform grounded only in current decision state.
3. Re-validate the transformed response against the same decision invariants.
4. If still non-compliant, emit a fallback response grounded only in current valid anchor/constraints.
5. Persist violation event, transform class, fallback state, and final handling mode in metadata.

Runtime must never forward non-compliant output to user.

Reference flow:
```text
User Input
  -> Constraint/Rejection Interpreter
  -> State Transition
  -> AllowedCandidates Derivation
  -> Hidden Guard Build
  -> LLM Generation
  -> Invariant Validation / Enforcement
  -> Persist Decision State + Metadata
```

### 2. Relationship to SRIP-13

CDS remains domain-specific. Its invariants are commerce decision invariants,
not relational identity invariants.

The enforcement architecture is aligned with SRIP-13 in the following sense:

- generated output is evaluated through a structured assertion model;
- violations are derived from invariant checks, not free-form style preference;
- correction is deterministic and bounded;
- fallback is used only when invariants cannot be restored;
- enforcement evidence remains internal and auditable;
- policy and control terminology must not leak into user-facing text.

This alignment does not modify CDS phases, anchor rules, candidate ordering, or
domain gating.

---

## VIII. Data Model

```json
{
  "version": 1,
  "state": "discovery",
  "primary_anchor": {
    "model_id": null,
    "brand": null,
    "confidence": 0.0,
    "source_cycle": null
  },
  "candidates_pool": [],
  "allowed_candidates": [],
  "rejected_candidates": [],
  "user_exclusions": {
    "brands": [],
    "models": []
  },
  "active_constraints": {
    "budget": null,
    "use_case": null,
    "preferences": [],
    "avoids": []
  },
  "allow_new_brands": true,
  "transition_event": null,
  "violations": [],
  "updated_at": null
}
```

---

## IX. Persistence and Recovery

### 1. Session Persistence
CDS state is stored per session in structured form (for example `session_decision_state` table or equivalent store object).

### 2. Checkpoint Integration
Runtime checkpoint payloads must include full decision state snapshot.

### 3. Hydration
On runtime restore:
- load persisted decision state if present;
- if absent, bootstrap deterministically from message history and metadata;
- recover anchor/candidate/exclusion semantics before next generation.

---

## X. Configuration and Domain Gating

CDS is explicitly feature-gated by system profile:

```yaml
commerce_decision:
  enabled: true
  min_constraints_for_narrowing: 2
  max_initial_candidates: 2
  deterministic_ordering: true
  alt_limit_when_anchored: 1
  allow_new_brands_when_anchored: false
  enforcement_mode: transform
```

For non-commerce domains (for example healthcare, defense, business advisory), CDS is disabled:

```yaml
commerce_decision:
  enabled: false
```

This ensures no commerce-specific rules are applied outside ecommerce profiles.

---

## XI. Observability and Metrics

CDS adds decision-control telemetry:
- `decision_transitions_total`
- `anchor_lock_violations_total`
- `anchor_auto_swap_blocked_total`
- `new_brand_blocked_total`
- `primary_rejections_total`
- `constraint_invalidations_total`
- `deterministic_transforms_total`
- `fallback_responses_total`
- `invariant_violations_total`

Each cycle should include decision state and enforcement evidence in trace metadata.

---

## XII. Compliance and Acceptance Criteria
An implementation of CDS is compliant only if all pass:

1. No primary switch without explicit rejection or hard invalidation.  
2. No new brand after anchor lock unless unlock condition is satisfied.  
3. No constraint mutation without user input.  
4. Off-table answers match explicit exclusions/rejections only.  
5. Decision state survives restart/hydration without anchor loss.  
6. Hidden guard logic does not leak into user-facing responses.  
7. Same trace replay yields deterministic decision outcomes.
8. Anchor selection is reproducible and tied to deterministic candidate ordering.
9. No secondary-to-primary auto-swap without explicit rejection or hard invalidation.

---

## XIII. Non-Goals
SRIP-12 does not:
- implement marketplace scraping or dynamic price feeds;
- replace SRIP-09/10/11 memory and entropy layers;
- introduce language-specific keyword dictionaries as the primary decision mechanism.

CDS is a deterministic governance overlay for commerce dialogue control.
