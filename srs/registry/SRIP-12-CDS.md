> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-12: Commerce Decision State Layer (CDS)
**Version:** 1.2  
**Status:** Active Proposal / Partial Implementation  
**Depends on:** SRIP-09 (LTM), SRIP-10 (AEP), SRIP-11 (CMT)  
**Related Specs:** SRIP-13 (RIS)  
**Author:** Sigma Stratum Research Group  
**Date:** 2026-04-24  
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

---

## II. Problem Statement
Long-horizon ecommerce dialogues tend to drift toward option expansion:
- primary candidate is replaced without explicit user rejection;
- new brands are introduced mid-session without authorization;
- off-table lists mix user exclusions with internal candidate state;
- control rules leak into user-facing responses.

SRIP-12 resolves this via deterministic state, hard gates, structured persistence, and bounded hidden guidance.

---

## III. Conformance Scope

SRIP-12 defines the normative contract for deterministic commerce decision
control.

Bounded implementations may satisfy parts of this contract before full
conformance is complete. Typical bounded conformance may include:

- deterministic anchor selection;
- governed candidate-set derivation;
- rejection and invalidation handling;
- hidden control enforcement;
- bounded persistence and audit surfaces.

Full conformance requires replay-grade determinism, durable decision-state
handling, explicit invariant evidence, and sufficient auditability for release
acceptance.

---

## IV. Core Concepts

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
| **Enforcement Evidence** | Structured metadata describing validation, violations, rewrite class, and final handling mode. |

---

## V. Decision State Machine

### 1. Phases
| Phase | Behavior |
|------|----------|
| `discovery` | Collect constraints such as budget, use-case, exclusions, and style requirements. |
| `narrowing` | Propose up to configured candidate count and select anchor. |
| `anchored` | Anchor is locked; no new primary unless explicit unlock condition. |
| `reinforced` | Keep same anchor and adapt explanation to context refinements. |
| `transition` | Constraint change detected; re-evaluate anchor validity deterministically. |

### 2. Valid Transitions
1. `discovery -> narrowing` when minimum constraint threshold is met.  
2. `narrowing -> anchored` when primary candidate is selected and valid.  
3. `anchored -> reinforced` when user refines context without rejection or invalidation.  
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

Ordering metadata such as `ordering_version` and `ordering_inputs_hash` must be persisted for replay parity.

---

## VI. Enforcement Rules

The rules in this section are **decision invariants**. They define what must be true before a commerce response is released. They do not change the decision state machine in § V or the allowed-candidate derivation in § VII.

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
- replace anchor because model proposes a better fit;
- rotate primary due to stylistic novelty.

Primary can change only via explicit rejection or hard invalidation.

### 3. Constraint Change Semantics
Constraint changes are classified as:
- **soft refinement**: does not invalidate anchor and therefore keeps anchor;
- **hard invalidation**: incompatible with anchor and therefore returns to `narrowing`.

Soft refinements must not trigger automatic anchor replacement.

### 4. Rejection Rules
Rejection is valid when:
- user explicitly rejects current candidate, model, or brand; or
- user provides a hard constraint that invalidates current anchor.

On rejection:
- move current anchor to `rejected_candidates`;
- clear `primary_candidate`;
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
Internal controls such as state, allowed set, guard rules, and diagnostics are runtime-only and must not appear in user-facing text.

---

## VII. Allowed Candidate Derivation (Deterministic)

`allowed_candidates` must be derived by state, not by free-form model behavior.

Reference policy:

```text
if state == discovery and constraints < min_constraints_for_narrowing:
    allowed_candidates = []

elif state == narrowing and primary_candidate is null:
    allowed_candidates = deterministic_pool[:max_initial_candidates]

elif primary_candidate exists and not rejected and not invalidated:
    if user_explicitly_requests_alternative:
        allowed_candidates = [primary_candidate] + deterministic_secondaries[:alt_limit]
    else:
        allowed_candidates = [primary_candidate]

elif primary_candidate rejected or invalidated:
    allowed_candidates = deterministic_pool_excluding_exclusions_and_rejections[:max_initial_candidates]

else:
    allowed_candidates = []
```

Additional constraints:
- `allowed_candidates = []` means runtime asks for missing constraints and must not recommend products
- secondary candidates remain allowed only when explicitly requested or when state is `narrowing`
- off-table answers must not read from `allowed_candidates`

---

## VIII. Runtime Integration

A bounded deterministic CDS path may follow this sequence:

1. load decision state for session  
2. parse and merge user constraints  
3. detect rejection, invalidation, and off-table/off-domain signals  
4. transition state machine  
5. derive `allowed_candidates`  
6. build hidden commerce control instructions for generation  
7. generate response  
8. apply mention filtering, anchor/brand policy enforcement, and bounded rewrite or fallback behavior where needed  
9. persist updated decision state and decision evidence

Reference flow:
```text
User Input
  -> Constraint/Rejection Interpreter
  -> State Transition
  -> AllowedCandidates Derivation
  -> Hidden Guard Build
  -> LLM Generation
  -> Policy Filtering / Rewrite / Fallback
  -> Persist Decision State + Metadata
```

### 1. Invariant Validation and Enforcement

SRIP-12 still requires a deterministic handling path whenever generated commerce output violates the current decision state.

Bounded implementations may realize these invariants through candidate
derivation, mention filtering, deterministic transforms, or fallback handling.
The precise enforcement surface may vary, but the invariant contract does not.

### 2. Relationship to SRIP-13

CDS remains domain-specific. Its invariants are commerce decision invariants, not relational identity invariants.

The enforcement architecture is aligned with SRIP-13 in the following sense:
- generated output is evaluated against invariant-bearing runtime state rather than free-form style preference
- violations are derived from deterministic policy checks
- correction and fallback remain bounded
- enforcement evidence remains internal and auditable
- policy and control terminology must not leak into user-facing text

This alignment does not modify CDS phases, anchor rules, candidate ordering, or domain gating.

---

## IX. Data Model

One acceptable decision-state shape is:

```json
{
  "version": 1,
  "state": "discovery",
  "primary_candidate": {
    "model_id": null,
    "brand": null,
    "confidence": 0.0,
    "source_cycle": null
  },
  "secondary_candidates": [],
  "anchor_pool": [],
  "candidates_pool": [],
  "rejected_models": [],
  "rejected_candidates": [],
  "active_constraints": {
    "budget": null,
    "excludes": [],
    "excludes_brands": [],
    "excludes_models": [],
    "preferred_brands": [],
    "required_properties": [],
    "style_avoid": [],
    "use_case": null,
    "use_case_refinements": [],
    "materials": [],
    "silhouette": []
  },
  "user_exclusions": {
    "brands": [],
    "models": [],
    "style": []
  },
  "allow_new_brands": true,
  "surface_memory": {
    "repeat_streak": 0,
    "clarify_streak": 0,
    "last_model_mention_cycle": null,
    "last_response_hash": null
  },
  "ordering_version": 1,
  "ordering_inputs_hash": null,
  "last_event": null,
  "updated_at": null
}
```

Implementations may also expose cycle-level CDS metadata through runtime or
operator surfaces. Persisted state and per-cycle evidence are related but need
not be identical surfaces.

---

## X. Persistence and Recovery

### 1. Session Persistence
CDS state should be stored per session in structured form.

### 2. Checkpoint and Snapshot Integration
Checkpoint, snapshot, review, and reset surfaces are compatible with this SRIP
but are not themselves the normative core of the state machine.

### 3. Hydration
Hydration should:

- load persisted decision state if present;
- normalize it before reuse;
- avoid claiming replay parity unless replay-grade determinism is actually
  satisfied.

---

## XI. Configuration and Domain Gating

CDS is explicitly feature-gated by runtime profile/configuration.

Representative config shape:

```yaml
commerce_decision:
  enabled: true
  min_constraints_for_narrowing: 2
  max_initial_candidates: 2
  deterministic_ordering: true
  alt_limit_when_anchored: 1
  allow_new_brands_when_anchored: false
  signal_extraction_mode: model
  surface_mode: model_first
  factual_grounding_enabled: true
```

Commerce-specific rules should not silently apply outside commerce-governed
flows.

---

## XII. Observability and Metrics

Implementations should expose enough CDS telemetry to audit:

- decision transitions;
- anchor-lock violations;
- rejected or invalidated anchors;
- rewrite and fallback handling;
- allowed-candidate state;
- per-cycle decision evidence.

---

## XIII. Maturity Matrix

| Capability | Status |
|------|-------------|
| State machine and anchor semantics | Baseline |
| Deterministic allowed-candidate derivation | Baseline |
| Hidden commerce guidance and leakage suppression | Baseline / evolving |
| Per-session structured persistence | Partial / evolving |
| Decision-state review and reset APIs | Optional implementation surface |
| Ordering metadata for replay parity | Partial |
| Structured signal extraction and mention policy | Partial / evolving |
| Full invariant-assertion and deterministic-transform taxonomy | Implementation Pending |
| Full replay and scenario-validation closeout | Implementation Pending |
| Explicit operator-facing closeout evidence | Implementation Pending |

---

## XIV. Compliance and Acceptance Criteria

A release-complete implementation of CDS is compliant only if all pass:

1. no primary switch without explicit rejection or hard invalidation  
2. no new brand after anchor lock unless unlock condition is satisfied  
3. no constraint mutation without user input  
4. off-table answers match explicit exclusions and rejections only  
5. decision state survives restart and hydration without anchor loss  
6. hidden guard logic does not leak into user-facing responses  
7. same trace replay yields deterministic decision outcomes  
8. anchor selection is reproducible and tied to deterministic candidate ordering  
9. no secondary-to-primary auto-swap without explicit rejection or hard invalidation  
10. operator-visible CDS evidence is sufficient to audit decision transitions, violations, and rewrites

Bounded implementations may satisfy subsets of these criteria before full
conformance closes. Release-complete conformance requires the entire set.

---

## XV. Non-Goals
SRIP-12 does not:
- implement marketplace scraping or dynamic price feeds
- replace SRIP-09, SRIP-10, or SRIP-11 memory and entropy layers
- introduce language-specific keyword dictionaries as the primary decision mechanism
- turn commerce governance into a general-purpose moderation stack

CDS remains a deterministic governance overlay for commerce dialogue control.
