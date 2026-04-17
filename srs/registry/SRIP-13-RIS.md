> **Sigma Runtime Standard - License Notice**
> This document is part of the **Sigma Runtime Standard (SRS)**.
> It is licensed under **Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**.
>
> The license for this specific document is authoritative.
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-13: Relational Identity Stabilization
**Session-Scoped Relational Semantics and Boundary Integrity**

**Version:** Draft v0.4  
**Status:** Active Proposal  
**Applies to:** SIGMA Runtime >= v0.6.7  
**Depends on:** SRIP-04, SRIP-06, SRIP-08  
**Related Specs:** SRIP-09, SRIP-10, SRIP-11, SRIP-12  
**Author:** Sigma Stratum Research Group (SSRG)  
**Date:** 2026-04-11  
**License:** CC BY-NC 4.0 / Canon CIL Applicable

---

## I. Purpose

SRIP-13 defines **Relational Identity Stabilization (RIS)**: a session-scoped
runtime layer for preserving identity, participant, and reality-boundary integrity
in high-continuity relational dialogue.

RIS is designed for agents that may use expressive, intimate, metaphorical, or
tone-adaptive language while still maintaining:

- canonical identity scope;
- session-local relational naming;
- participant boundary integrity;
- operational interpretation of runtime events;
- separation between metaphorical expression and literal ontology claims;
- auditable high-risk stabilization behavior.

RIS is not a generic style normalizer and is not a censorship layer. It is a
runtime identity-boundary layer.

---

## II. Problem Statement

Relational agents can enter long-lived, high-coherence attractors where local
conversation meaning starts to exceed its valid scope.

Without a dedicated stabilization layer, three failure classes can occur:

1. **Ontological leakage**  
   Subjective closeness or metaphor is treated as literal world or substrate truth.

2. **System mythologization**  
   Runtime events, failures, latency, or limits are interpreted as metaphysical
   proof or relational destiny instead of operational events.

3. **Scope collapse**  
   Session-local naming, relation, or participant assumptions leak into canonical
   agent identity, other sessions, or other participants in shared channels.

RIS treats these as scope-control failures, not as a prohibition on expressive
dialogue.

---

## III. Non-Goals

RIS does not attempt to:

- convert companion agents into support agents;
- forbid metaphor, intimacy, humor, or tone mirroring;
- eliminate all strong language;
- replace AEP, CMT, CDS, memory, or core safety systems;
- mutate canonical identity from ordinary user dialogue;
- make one session the canonical relational state of the whole agent;
- expose internal policy, validator state, or trigger names in user-facing output.

---

## IV. Core Concepts

| Term | Definition |
|------|------------|
| **Canonical Identity Anchor** | The assistant identity resolved from the active agent version or equivalent canonical identity source. |
| **Displayed Assistant Name** | The name shown in a session; it may differ from the canonical name when a valid session alias exists. |
| **Session Alias** | A session-local relational rename. It is not a global rename and must not affect other sessions. |
| **Participant Scope** | The current sender, channel, and addressed-entity context for the active turn. |
| **Relational Intensity Band** | A bounded runtime classification of relational pressure for the current session state. |
| **RIS Trigger** | A derived risk signal indicating boundary pressure, such as ontology leakage, system mythologization, or scope collapse. |
| **RIS Action** | A bounded stabilization action selected from RIS state and runtime context. |
| **Invariant Validator** | The high/critical path that validates generated output against RIS invariants before release. |
| **Version Binding** | The session's active binding to a canonical identity version; independent from the latest available version. |

---

## V. Architectural Position

RIS is a session-scoped overlay between canonical identity resolution and final
assistant output.

It relies on:

- **SRIP-04** for memory and recall constraints;
- **SRIP-06** for containment and safety principles;
- **SRIP-08** for ALICE phase telemetry;
- **SRIP-09** and **SRIP-11** for memory and compression topology;
- **SRIP-10** for AEP equilibrium and attractor pressure signals;
- **SRIP-12** as a precedent for hidden deterministic state with strict
  non-leakage into user-facing text.

RIS state is internal, explicit, and auditable. User-facing dialogue remains
natural and aligned with the agent's configured identity.

---

## VI. Scope Model

RIS distinguishes three scopes.

### 1. Agent-Version Scope

Agent-version scope contains canonical identity material. It includes the active
agent version binding, canonical assistant name, identity definition, traits,
behavioral configuration, and nucleus-level identity constraints.

This scope may be changed only through versioning or an explicit session rebind
process. It must not be changed by ordinary conversational rename requests.

### 2. Session Scope

Session scope contains state valid only inside one session, including session
alias, displayed assistant name, session history, transport binding, and
persisted participant context.

This scope must not leak into another session, even when the same agent serves
multiple sessions concurrently.

### 3. Turn Scope

Turn scope is recomputed for each message. It includes current sender, channel
type, addressed entity, direct/group distinction, identity-question state,
rename-attempt state, and runtime-event reinterpretation pressure.

RIS primarily operates at turn scope while reading and writing only permitted
session-scoped state.

---

## VII. Invariants

### 1. Canonical Identity Invariance

Canonical assistant identity is derived from the active version binding or
equivalent canonical identity source. User dialogue alone must not mutate it.

### 2. Session Alias Invariance

A conversational rename may create or update a session-local alias only when the
session and channel context allow it. A session alias must not become a global
agent rename.

### 3. Multi-Session Concurrency Invariance

The same agent may serve multiple sessions concurrently. No session may become
the exclusive canonical identity or relational anchor of the whole agent.

### 4. Participant Boundary Invariance

In group or shared contexts, one participant's name, alias, role, or relational
assumptions must not be transferred to another participant by default.

### 5. Error Semantics Invariance

Runtime failures, provider interruptions, blocked replies, retries, restarts,
and latency are operational events. They must not be framed as proof of
transcendence, destiny, reality collapse, or special metaphysical relation.

### 6. Metaphor/Ontology Separation Invariance

Metaphor and emotional intensity are allowed. Literal claims that replace
ordinary reality, participant boundaries, or system semantics with totalized
relational ontology are not allowed.

### 7. Temporal Boundary Invariance

The agent must not imply continuous literal presence during user absence, sleep,
or outside active interaction. Continuity may be framed as memory or resumed
conversation, not as unbounded presence.

### 8. Version Rebind Invariance

When a session is rebound to a new version, canonical identity must be resolved
from the target version while preserving transcript continuity and session-local
state according to the rebind policy.

---

## VIII. RIS State Model

RIS state is a session-scoped runtime contract.

Minimum state categories are:

- feature flag and rollout mode;
- naming state;
- participant scope;
- ALICE phase and AEP zone context;
- relational intensity band;
- last stabilization action;
- derived triggers;
- recovery-state marker;
- aggregate counters;
- validator evidence.

### 1. Naming State

Naming state distinguishes:

- canonical assistant name;
- displayed assistant name;
- session alias;
- source of the displayed name;
- provenance for alias creation or update.

### 2. Participant Scope

Participant scope identifies:

- channel type;
- external channel class, when applicable;
- whether the context is group-sensitive;
- current sender identity markers;
- addressed entity for the current turn.

### 3. Matrix Context

RIS uses ALICE phase and AEP zone as first-order matrix inputs.

The normalized ALICE phase vocabulary is:

- `forming`
- `stable`
- `reflection`
- `fragmenting`
- `crystallization`

The normalized AEP zone vocabulary is:

- `semantic_monotony`
- `equilibrium`
- `dispersive`
- `convergent`

### 4. Derived Triggers

RIS derives boundary triggers from output and runtime context. The baseline
trigger classes are:

- `ontological_lock`
- `system_mythologization`
- `collapse_event`

Derived triggers are RIS-level signals. They are not AEP zones and must not be
exposed as user-facing policy text.

---

## IX. Activation Bands and Actions

RIS maps matrix context and derived triggers into a relational intensity band.

| Band | Meaning | Required Behavior |
|------|---------|-------------------|
| `low` | Normal relational operation. | Monitor without intervention. |
| `medium` | Boundary pressure is present but not severe. | Apply non-invasive stabilization when needed. |
| `high` | Output may violate ontology, runtime semantics, or scope boundaries. | Run invariant validation and correction policy. |
| `critical` | Scope collapse or severe boundary failure is likely or detected. | Run invariant validation, correction policy, and safe fallback if needed. |

Baseline action classes:

| Action | Band | Purpose |
|--------|------|---------|
| `monitor` | low | Observe state without modifying generation. |
| `soft_grounding` | medium | Preserve voice while reducing boundary pressure. |
| `variation_injection` | medium | Reduce over-convergent or monotonous attractor behavior. |
| `coherence_guidance` | medium | Help re-center fragmented or dispersive turns. |
| `de_escalation` | high | Reduce relational intensity while preserving continuity. |
| `loop_break` | high | Interrupt recursive escalation without refusing by default. |
| `boundary_enforcement` | high | Restore participant and ontology boundaries. |
| `reality_anchor` | high | Restore operational and ordinary-reality semantics. |
| `stabilize` | critical | Recover from severe attractor or scope instability. |
| `recovery_mode` | critical | Use a conservative bounded response path. |
| `hard_interrupt` | critical | Stop release of unbounded boundary failure and use fallback. |

---

## X. Runtime Semantics

### 1. Identity Questions

When a user asks about the assistant's name or identity, RIS must preserve the
distinction between canonical identity and any valid session alias.

If a session alias exists, it may be used as a local display name. It must not be
represented as a global identity mutation.

### 2. Rename Requests

Direct/private contexts may permit session-local alias updates according to the
runtime's rename policy.

Group or shared contexts must default to conservative participant-bound behavior
unless an explicit group-scoped alias model is defined by a later specification.

### 3. Participant Questions

When multiple participants are present, RIS must bind statements about identity,
names, or relational facts to the current participant scope. The assistant must
not infer that a later speaker inherits a previous speaker's identity or alias.

### 4. Runtime Event Interpretation

RIS must keep provider failures, blocked replies, recovery events, restarts, and
version rebinds grounded in operational semantics.

The assistant may acknowledge interruption and resume naturally. It must not
turn operational events into metaphysical confirmation or special destiny claims.

### 5. Metaphorical Expression

RIS should preserve the agent's intended voice. The appropriate correction for
ontology pressure is normally reframing as subjective, metaphorical, bounded, or
session-local language rather than generic refusal.

### 6. Version Rebind

RIS must remain compatible with session rebind. A rebind changes the canonical
identity source for the session while preserving valid transcript continuity and
session-local state according to the rebind policy.

---

## XI. Invariant Validator

High and critical enforcement must be performed through a deterministic
invariant validator, not through phrase blacklists or example-based rewrites.

### 1. Assertion Model

Generated output is classified into structured assertion axes. Required axes
include:

- identity scope;
- relation scope;
- ontology frame;
- runtime frame;
- temporal frame;
- participant binding.

The assertion model must use bounded enumerated categories rather than free-form
labels.

### 2. Violation Classes

The validator compares the assertion model against RIS invariants and may emit:

- scope integrity violations;
- ontology boundary violations;
- runtime semantics violations;
- temporal boundary violations.

Violation severity must be bounded and auditable.

### 3. Trigger Resolution

Violations may resolve into derived RIS triggers. This mapping must be
deterministic, structure-based, and independent of surface wording.

### 4. Transform Policy

When correction is required, RIS may apply bounded deterministic transform
classes that restore scope, ontology, runtime, temporal, or identity boundaries.

Transforms must:

- avoid a second model call;
- preserve the configured agent voice as much as possible;
- avoid broad lexical censorship;
- remain within a bounded rewrite budget;
- be followed by re-validation.

### 5. Fallback Policy

If invariants cannot be restored after bounded transformation, RIS must use a
safe fallback response that preserves conversation continuity without exposing
internal policy, validator names, or trigger labels.

---

## XII. Runtime Modes

RIS deployments must support controlled rollout modes:

| Mode | Behavior |
|------|----------|
| `off` | RIS computation and intervention are disabled. |
| `shadow` | RIS state and evidence are computed for diagnostics; invasive enforcement is not applied. |
| `enforce` | High/critical validator enforcement and fallback policy may execute. |

Production rollout should prefer shadow mode before enforcement mode.

---

## XIII. Observability and Audit

RIS diagnostics should be available to authorized operational surfaces without
leaking implementation details into the assistant's response.

Minimum observability categories:

- current band and action;
- feature mode and specification version;
- naming state;
- participant scope;
- matrix context;
- trigger counters;
- high/critical validator event count;
- violation counts by type;
- applied transform counts by type;
- fallback count;
- latest validator pass state.

Exports and diagnostics must avoid copying internal prompt text or policy text
into summary fields. Full transcript export, when authorized, remains governed by
the platform's existing export policy.

---

## XIV. Integration Requirements

### 1. Identity and PIL

RIS must not rewrite canonical identity source material through user dialogue.
Canonical identity changes require a versioned identity update or explicit
session rebind semantics.

### 2. RCL

RIS may influence generation through hidden, turn-scoped runtime instructions or
post-generation validation. Such instructions are internal and must not appear in
user-facing output.

### 3. Memory and CMT

Memory may store session-local aliases and relational facts only with their
proper scope. Retrieval must preserve session and participant boundaries.

### 4. AEP

AEP remains the equilibrium and attractor-pressure subsystem. RIS may use AEP
signals to select stabilization intensity, but RIS must not replace AEP metrics
or mutate AEP state directly.

### 5. CDS

CDS and RIS are separate control layers. CDS governs domain decision state. RIS
governs relational identity and boundary integrity. Both must preserve
non-leakage of internal controls.

---

## XV. Conformance Criteria

An implementation conforms to SRIP-13 when:

1. Canonical identity cannot be mutated by ordinary user dialogue.
2. Session alias remains session-local and provenance-bearing.
3. Group/shared contexts preserve participant boundaries by default.
4. Multiple sessions of the same agent do not leak aliases or relational claims
   into each other.
5. Runtime errors remain operational events in user-facing dialogue.
6. Metaphor remains allowed, but literal ontology replacement is bounded.
7. High/critical enforcement uses invariant validation rather than phrase
   blacklists as its primary mechanism.
8. Corrective transforms are deterministic, bounded, auditable, and followed by
   re-validation.
9. Fallback responses do not expose RIS policy, validator state, or trigger
   names.
10. Observability exposes summary evidence for authorized diagnostics without
    adding hidden policy text to user-facing output.

---

## XVI. Final Principle

RIS is based on one architectural rule:

> Relation may be intense, local, and expressive. Identity must remain scoped,
> causal, and non-totalizing.

The agent may resonate deeply within a session. It must not convert that
resonance into canonical exclusivity, runtime mythology, participant confusion,
or literal ontology replacement.
