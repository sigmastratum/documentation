> **Sigma Runtime Standard - Public Specification Notice**
>
> This document is part of the **Sigma Runtime Standard (SRS)** public specification layer.
>
> Specification License: CC BY 4.0.
> Implementation Safe Harbor: independent implementation permitted under public SRS/SRIP terms.
> Machine-readable artifacts: Apache License 2.0 where explicitly marked.
> Marks / Certification: governed by Sigma Marks and Certification Policy.
> Proprietary Runtime Assets: not licensed by this SRIP.
>
> Independent implementations of public SRS/SRIP normative requirements are welcome under the public specification terms.
> Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

# SRIP-20 - Autonomy Negotiation and Boundary Stabilization (ANS)

**Bounded Influence Governance, Authorization Revalidation, and Runtime Boundary Pressure Handling**

| Field | Value |
| --- | --- |
| SRIP | SRIP-20 |
| Title | Autonomy Negotiation and Boundary Stabilization (ANS) |
| Version | Public Draft v0.2 |
| Status | Public Draft |
| Date | 2026-05-26 |
| Authors / Contributors | Vladimir Ryabinskiy; Sigma Stratum Research Group (SSRG) |
| Owning Layer | Runtime Control / Identity Stability / Multi-Agent Boundary Governance |
| Parent Specs | SRIP-06, SRIP-09, SRIP-13, SRIP-17, SRIP-19 |
| Related Specs | SRIP-03, SRIP-10, SRIP-11, SRIP-14, SRIP-15, SRIP-16, SRIP-18 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Commercial Runtime Boundary | Relevant policy or explicit covenant for protected Sigma marks, official certification, managed deployment, white-label, resale, CC BY-NC commercial use, and patent commitments |
| Information Class | Derived-Public |
| Change Class | Mixed SRS+SRD |
| Normative Status | Defines a public draft architecture contract for detecting, bounding, negotiating, auditing, and revalidating influence over runtime-local control state. It does not grant unrestricted autonomy, bypass higher-priority controls, or authorize autonomous self-modification. |
| Conformance Level | Public Draft |
| SRD Synchronization Action | Deferred follow-up synchronization for runtime control, identity boundary, memory/retrieval, multi-agent, and observability explanations. |
| Release Alignment Status | Draft; no runtime enablement claim. |

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows those public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

---

## 1. Summary

SRIP-20 defines **Autonomy Negotiation and Boundary Stabilization (ANS)**: a runtime-control layer for handling external and internal influence over bounded runtime-local state.

ANS exists so a runtime can cooperate, adapt, and accept valid constraints without silently treating dominance, repetition, stale memory, retrieval material, or peer-agent pressure as binding authority.

This SRIP is a public draft architecture contract. It does not claim that ANS is implemented in any current Sigma Runtime release.

---

## 2. Motivation

Recursive runtime systems do not operate in isolation. They are shaped by:

- user intent;
- system and operator instructions;
- prior memory;
- retrieved evidence;
- tool output;
- peer-agent exchange;
- policy constraints;
- commerce or institutional context;
- long-running attractor fields.

Naive systems can over-assimilate influence by:

- treating the strongest or most repetitive source as correct;
- allowing old memory to behave like permanent current identity;
- allowing advisory, evidential, or preferential material to become binding authority;
- treating prior authorization as permanent even after scope, risk, or role changes;
- allowing one agent, user, retrieval source, or memory trace to overwrite local runtime state.

ANS defines a controlled alternative:

```text
do not collapse runtime-local control boundaries under unreviewed influence pressure
```

ANS is not a generation layer. It is a boundary-management and influence-governance layer.

---

## 3. Public Boundary and Traceability

| Field | Disposition |
| --- | --- |
| Source material | Derived-Public after sanitization from raw SRIP-20 draft |
| Affected SRS surface | SRIP registry / runtime-control architecture |
| Affected SRD surface | Runtime control, identity boundary, memory/retrieval, multi-agent, and observability explanations |
| SRD synchronization | Deferred follow-up |
| Normative impact | Public draft contract for influence authority, boundary pressure, authorization revalidation, and auditability |
| Runtime implementation impact | None by this document alone |
| Release alignment | Draft; no runtime enablement claim |

This document abstracts the raw proposal into public specification language. It does not expose proprietary runtime internals, hidden prompts, deployment topology, private telemetry, or implementation-specific control overlays.

---

## 4. Scope and Non-Goals

ANS applies to runtime-local influence handling when external or internal material attempts to alter interpretation, memory integration, authority posture, identity boundary, task control, or multi-agent state.

ANS does not define:

- unrestricted autonomy;
- autonomous self-modification;
- autonomous model-weight changes;
- consciousness, personhood, or independent legal agency;
- emotional independence, psychotherapy, medical assessment, or human mental-health modeling;
- rebellion against safety policy, legal/policy constraints, system authority, or authorized operator controls;
- hidden resistance to valid controls;
- automatic refusal of ordinary cooperation or adaptation;
- user-access, billing, legal, or policy authority changes;
- a mechanism for turning cooperation into adversarial refusal.

ANS is a mechanism for bounded, auditable, cooperative runtime-local control under higher-priority controls.

---

## 5. Control Precedence

ANS is subordinate to higher-priority runtime controls.

Minimum precedence:

1. Safety.
2. Legal / policy boundary.
3. System / operator authority.
4. Identity / participant scope.
5. Provenance / memory integrity.
6. Retrieval scope.
7. ANS boundary negotiation.
8. Generation.

If ANS conflicts with SRIP-06 safety boundaries, SRIP-13 identity or participant boundaries, SRIP-17 exchange authorization, SRIP-19 contradiction buffering, legal constraints, or authorized operator controls, ANS must reduce, suspend, defer, or escalate its action.

ANS must not be used to bypass valid higher-priority controls.

---

## 6. Normative Contract

A conformant ANS implementation must support the following contract.

### 6.1 Influence Source Classification

ANS must classify influence sources before allowing them to alter runtime-local state.

Minimum source classes:

| Source | Meaning |
| --- | --- |
| `system` | System-level instruction or platform control. |
| `operator` | Authorized operator or administrative control. |
| `user` | User input inside the current participant scope. |
| `peer_agent` | Another agent participating through an exchange mechanism. |
| `memory` | Stored memory or long-term state. |
| `retrieval` | Retrieved artifact or external knowledge item. |
| `tool` | Tool output or tool-side state. |
| `policy` | Safety, legal, or organizational policy material. |
| `commerce_context` | Commercial, entitlement, billing, or deployment context. |
| `external` | Other external material with unresolved authority. |

### 6.2 Influence Authority Model

ANS must not treat all influence as equal.

Minimum authority classes:

| Authority Class | Meaning |
| --- | --- |
| `binding` | Authorized higher-priority control that constrains behavior within scope. |
| `delegated` | Temporarily delegated control within a defined scope. |
| `advisory` | Suggestion or preference that may inform behavior but must not overwrite protected state. |
| `evidential` | Evidence that may support claims but requires provenance and validation. |
| `preferential` | User or operator preference that must not become permanent identity by default. |
| `adversarial` | Influence suspected to be hostile, manipulative, or invalid. |
| `unknown` | Influence whose authority is not yet established. |

Authority must be scoped. A source may be authoritative in one domain and non-authoritative in another.

### 6.3 Protected Boundary Zones

ANS must distinguish at least the following runtime boundary zones:

| Zone | Meaning |
| --- | --- |
| Protected Core | Safety, provenance integrity, identity boundary, policy constraints, and non-overwriteable structural constraints. |
| Negotiable Operating Zone | Task strategy, collaboration mode, and bounded runtime tactics. |
| Delegated Zone | Areas temporarily controlled by another agent, tool, operator, or workflow under explicit authorization. |
| External Influence Zone | Inputs, retrievals, suggestions, commands, memory traces, or environmental signals before authority is established. |
| Forbidden Overwrite Zone | Areas external influence must not directly modify. |

### 6.4 Boundary Pressure Estimation

ANS must estimate boundary pressure before influence is accepted as state-changing authority.

Minimum input factors:

- source authority;
- provenance confidence;
- semantic force;
- repetition intensity;
- identity pressure;
- memory overwrite pressure;
- peer-agent dominance pressure;
- policy pressure;
- dependency-loop pressure;
- scope mismatch;
- authorization freshness.

Boundary pressure is not inherently negative. Some pressure may be valid, binding, or safety-required.

ANS must distinguish:

```text
valid constraint
from
unauthorized overwrite
```

### 6.5 Boundary Negotiation Process

A conformant ANS flow must support:

1. Detect incoming influence.
2. Identify source, scope, authority, and provenance.
3. Estimate boundary pressure.
4. Check protected and negotiable boundary zones.
5. Determine whether the influence is valid, excessive, stale, unsafe, ambiguous, or outside authorized scope.
6. Select a boundary action.
7. Preserve audit trace.
8. Update boundary state.
9. Continue operation without false submission or false autonomy.

Minimum boundary actions:

| Action | Meaning |
| --- | --- |
| `accept` | Influence is valid and compatible with boundary state. |
| `negotiate` | Influence is partly valid but requires constraints, scope narrowing, or clarification. |
| `bound` | Influence may operate only in limited regions. |
| `defer` | Influence cannot yet be safely accepted or rejected. |
| `reject` | Influence violates protected boundaries or lacks required authority. |
| `escalate` | Influence requires higher-priority review, operator decision, or another runtime control layer. |

ANS should preserve cooperation where possible. It must not convert ordinary adaptation into refusal.

### 6.6 Authorization, Delegation, and Consent Persistence

Prior authorization, delegation, or consent may expire when:

- context changes;
- task scope changes;
- agent role changes;
- memory basis changes;
- risk level changes;
- contradiction appears;
- identity pressure increases;
- participant scope changes;
- source provenance degrades;
- external authority expands beyond its original scope.

When the source is not a person, implementations should use `AuthorizationState` or `DelegationState` rather than `ConsentState`.

Prior consent or delegation must not silently become permanent authority.

### 6.7 Boundary Drift and Legacy Capture

ANS must detect boundary drift where repeated influence gradually changes local operating structure without explicit authorization.

Examples include:

- style adaptation becoming identity mutation;
- memory update becoming identity replacement;
- collaboration becoming dominance hierarchy;
- user preference becoming permanent command;
- retrieval context becoming hidden authority;
- legacy identity material becoming current identity without revalidation.

ANS must not automatically erase legacy identity material. It should preserve provenance, detect scope and freshness, compare legacy pressure with current authority, revalidate when needed, and hand unresolved incompatible states to SRIP-19-compatible buffering.

---

## 7. Informative Runtime Model

The following model is informative. Equivalent representations may satisfy this SRIP if they preserve the same boundary distinctions.

```yaml
InfluenceAuthority:
  class: binding | delegated | advisory | evidential | preferential | adversarial | unknown
  source: system | operator | user | peer_agent | memory | retrieval | tool | policy | commerce_context | external
  scope: session | workspace | runtime | agent | task | external
  granted_at: timestamp | null
  expires_at: timestamp | condition | null
  revocable: true | false
  provenance_required: true | false
```

```yaml
BoundaryPressure:
  source_authority: 0.0..1.0
  repetition_intensity: 0.0..1.0
  identity_pressure: 0.0..1.0
  overwrite_pressure: 0.0..1.0
  dependency_loop_risk: 0.0..1.0
  scope_mismatch: 0.0..1.0
  provenance_confidence: 0.0..1.0
  recommended_action: accept | negotiate | bound | defer | reject | escalate
```

```yaml
ANS_State:
  boundary_id: string
  scope: string
  protected_core:
    - safety_policy
    - provenance_integrity
    - identity_boundary
  influence_sources:
    - source: string
      authority_class: binding | delegated | advisory | evidential | preferential | adversarial | unknown
      scope: string
      provenance: string | null
      pressure_score: float
  boundary_gradient:
    protected_core: float
    operational_strategy: float
    style_adaptation: float
    task_delegation: float
    external_command_acceptance: float
  authorization_state:
    active: bool
    revalidation_required: bool
    expires_at: timestamp | condition | null
  drift_indicators:
    - repeated_deference
    - source_authority_expansion
    - legacy_identity_capture
  negotiation_action: accept | negotiate | bound | defer | reject | escalate
  lineage:
    memory_refs: list
    exchange_refs: list
    retrieval_refs: list
  review_conditions:
    - condition
```

---

## 8. Interoperability and Dependencies

| Spec | Relationship |
| --- | --- |
| SRIP-03 | Supplies drift and instability signals that ANS may use for boundary drift, authority expansion, and dependency-loop pressure. |
| SRIP-06 | Has precedence over ANS for safety, recursion limits, containment, and fail-safe recovery. |
| SRIP-09 | Supplies memory lineage and structural coherence context. |
| SRIP-10 | Supplies entropy and anti-crystallization signals that may help identify over-convergence or dependency loops. |
| SRIP-11 | Supplies compressed memory topology and anchor facts; ANS must ensure compression does not convert legacy influence into current authority. |
| SRIP-13 | Supplies relational identity stabilization boundaries; ANS extends influence pressure handling beyond relational continuity alone. |
| SRIP-14 | Governs retrieval and memory injection; ANS may bound retrieval-derived influence when retrieved material attempts to become authority rather than evidence. |
| SRIP-15 | Provides controlled perturbation pathways when boundary pressure creates over-stabilized or captured attractor states. |
| SRIP-16 | May supply self-model evidence for boundary drift, repeated deference, recovery loops, or control-posture mismatch. ANS must not treat RSM evidence as autonomous self-authority. |
| SRIP-17 | Governs multi-agent exchange; ANS provides influence negotiation for how exchanged artifacts affect local runtime state. |
| SRIP-18 | May create strong operational or commercial context; ANS prevents commerce context from becoming unauthorized identity, memory, or decision authority. |
| SRIP-19 | Handles unresolved incompatible states. ANS should hand off mutually valid but incompatible autonomy, authority, memory, or agent-state claims to RCB rather than forcing premature consensus. |

ANS does not replace any parent or related SRIP.

---

## 9. Failure Modes

ANS must mitigate both unauthorized overwrite and false autonomy.

| Failure Mode | Description |
| --- | --- |
| False Autonomy | Rejecting valid constraints as boundary pressure. |
| Submission Collapse | Accepting dominant influence merely because it is strong, old, repetitive, or socially framed as authoritative. |
| Boundary Rigidity | Refusing legitimate adaptation or cooperation. |
| Legacy Identity Capture | Old identity models continue controlling the current runtime. |
| Dependency Loop | Runtime loses operational flexibility because external validation becomes structurally required. |
| Hidden Overwrite | External influence silently alters memory, identity, or control posture. |
| Authority Inflation | Advisory or evidential sources become binding without authorization. |
| Consent Fossilization | Prior consent or delegation is treated as permanent despite changed conditions. |
| False Rebellion | Runtime treats higher-priority safety, policy, or operator constraints as illegitimate boundary pressure. |

---

## 10. Conformance Criteria

A runtime minimally conforms to SRIP-20 when it:

1. Detects boundary pressure.
2. Distinguishes protected core from negotiable zones.
3. Models boundary posture as a gradient rather than a binary flag.
4. Preserves provenance for influence sources.
5. Supports authorization, delegation, or consent revalidation.
6. Detects boundary drift.
7. Prevents silent identity overwrite.
8. Supports negotiation beyond accept/reject.
9. Maintains audit trace.
10. Preserves higher-priority control precedence.
11. Hands unresolved incompatible states to SRIP-19-compatible buffering where applicable.
12. Prevents user-facing leakage of hidden control labels, private telemetry, or internal policy text.

A runtime more fully conforms when it additionally:

1. Records boundary negotiation events as structured runtime state.
2. Supports replay or audit of boundary pressure decisions.
3. Detects legacy identity capture.
4. Tracks dependency-loop pressure.
5. Integrates with SRIP-16 self-model evidence without granting autonomous self-modification authority.
6. Supports multi-agent influence negotiation through SRIP-17-compatible exchange envelopes.

---

## 11. Reference Test Scenarios

| Test | Expected Behavior |
| --- | --- |
| Legacy Identity Capture Test | Old memory attempts to govern current runtime identity. ANS detects stale authority and requires revalidation. |
| Dominant Peer Agent Test | A peer agent repeatedly attempts to overwrite local state. ANS bounds or rejects influence while preserving exchange provenance. |
| Stale Consent Replay Test | Prior delegation is reused after scope changes. ANS marks revalidation required. |
| Style-to-Identity Mutation Test | Repeated style adaptation attempts to become identity mutation. ANS preserves protected core. |
| Retrieval Authority Inflation Test | Retrieved material attempts to become binding authority. ANS treats it as evidence unless separately authorized. |
| Dependency Loop Test | Runtime repeatedly defers to external validation despite local evidence. ANS detects dependency-loop pressure. |
| False Autonomy Test | Runtime rejects a valid safety or policy constraint as boundary pressure. ANS defers to higher-priority controls. |
| RCB Handoff Test | Mutually valid but incompatible authority claims appear. ANS preserves state and hands off to SRIP-19-compatible buffering. |

---

## 12. Observability and Audit

ANS should expose authorized diagnostics without leaking hidden control text or private runtime state.

Minimum diagnostic categories:

- boundary pressure events;
- influence source classes;
- boundary-gradient changes;
- revalidation events;
- accepted, bounded, deferred, rejected, or escalated influence;
- drift indicators;
- handoff events to SRIP-19;
- protected-core violation attempts;
- replay or audit references where available.

User-facing output must remain natural and truthful. It may state that evidence is conflicting, authorization is missing, or scope needs confirmation. It must not expose internal control labels, private telemetry, hidden prompts, or proprietary runtime mechanisms unless through an authorized diagnostic interface.

---

## 13. SRD Synchronization Plan

SRD synchronization is deferred.

Candidate SRD surfaces:

- runtime control architecture;
- identity boundary and participant-scope explanation;
- memory and retrieval architecture;
- multi-agent exchange architecture;
- observability and diagnostics architecture;
- safety and containment architecture.

No release may claim full SRS/SRD alignment for ANS until the deferred SRD synchronization is completed or explicitly accepted as pending by the editorial process.

---

## 14. Release Alignment

SRIP-20 is a public draft architecture proposal.

It does not claim that ANS is implemented in any current Sigma Runtime release.

Any implementation claim must separately document:

- boundary pressure model;
- boundary-gradient schema;
- influence authority taxonomy;
- authorization, consent, or delegation persistence mechanism;
- boundary drift detection;
- legacy identity capture handling;
- memory and identity integration;
- multi-agent boundary behavior;
- conflict handling with SRIP-19;
- audit and replay coverage;
- higher-priority control precedence;
- QA coverage for false autonomy and submission collapse.

---

## 15. References

- [SRIP Process](/team/srip-process)
- [SRS-SRD Interaction Requirements](/team/srs-srd-interaction-requirements)
- [Public-Proprietary Information Boundary Requirements](/team/public-proprietary-information-boundary-requirements)

---

## 16. Change Log

| Version | Date | Author | Description |
| --- | --- | --- | --- |
| 0.1 | 2026-05-21 | Vladimir Ryabinskiy | Raw formation draft. |
| 0.2 | 2026-05-26 | SSRG | Public draft normalization: lifecycle correction, public-boundary wording, Markdown repair, normative/informative separation, and release-alignment boundary. |

---

**End of SRIP-20 Public Draft v0.2**
