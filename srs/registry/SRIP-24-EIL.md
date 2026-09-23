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

# SRIP-24 - Environment Interface Layer (EIL)

**Governed Contact Between Stabilized Runtime Trajectories and External Reality**

| Field | Value |
| --- | --- |
| SRIP | SRIP-24 |
| Title | Environment Interface Layer (EIL) |
| Version | Public Draft v0.3 |
| Status | Public Draft |
| Date | 2026-09-23 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Integration Boundary / Runtime Control / Governance / External Interaction |
| Parent Specs | SRIP-05, SRIP-14, SRIP-21, SRIP-22 |
| Related Specs | SRIP-01, SRIP-03, SRIP-04, SRIP-06, SRIP-13, SRIP-15, SRIP-17, SRIP-19, SRIP-20, SRIP-25 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Commercial Runtime Boundary | Relevant policy or explicit covenant for protected Sigma marks, official certification, managed deployment, white-label, resale, CC BY-NC commercial use, and patent commitments |
| Information Class | Open |
| Change Class | Mixed SRS+SRD |
| Specification Class | Runtime Protocol |
| Normative Status | Defines a public draft contract for classifying and governing interaction between stabilized runtime trajectories and external environments. It does not define an SDK, provider API, workflow engine, planner, tool framework, or production action permission by itself. |
| Conformance Level | Public Draft / No runtime conformance claim |
| SRD Synchronization Action | Initial SRD synchronization completed in `/srd/environment-interaction-and-events`; broader synchronization for runtime architecture, agent trajectory, memory/retrieval, governance, external interaction, and tool/action explanation remains deferred follow-up. |
| Release Alignment Status | aligned with deferred SRD sync |
| Release Alignment Notes | Public draft architecture proposal; no runtime enablement, production behavior, SDK/API, or conformance claim is made by this document alone. |

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows these public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

---

## 1. Summary

SRIP-24 defines the **Environment Interface Layer (EIL)**: a runtime architecture layer for governing contact between a stabilized Sigma runtime trajectory and external reality.

The core principle is:

```text
Behavior governs cognition.
EIL governs contact.
```

EIL is not a workflow engine, planner, orchestration language, tool framework, provider SDK, or action-permission shortcut. It is the boundary layer that classifies and governs observation, effect, authority, scope, source, target, evidence, and replay requirements for runtime-environment interaction.

This SRIP is a public draft architecture contract. It does not claim that EIL is implemented in any current Sigma Runtime release.

---

## 2. Motivation

The Sigma Runtime Standard already defines core runtime loop semantics, memory architecture, retrieval and memory integration, external identity binding, autonomy negotiation, contradiction buffering, and governance boundaries.

What remains implicit is the computational boundary at which a stabilized runtime trajectory is allowed to contact external reality.

Without an explicit environment-interface layer, systems may collapse important distinctions:

- observation versus truth;
- observation versus authority;
- capability versus permission;
- retrieval versus current fact;
- tool availability versus action justification;
- task success versus governance success;
- external effect versus ordinary response generation.

EIL standardizes this boundary.

---

## 3. Public Boundary and Traceability

| Field | Disposition |
| --- | --- |
| Source material | Open public-draft candidate derived from sanitized architectural formation material |
| Affected SRS surface | SRIP registry / interoperability / memory-retrieval / external identity / governance / integration boundary semantics |
| Affected SRD surface | Runtime architecture, external interaction, tool/action boundaries, memory/retrieval, governance, and long-horizon trajectory explanations |
| SRD synchronization | Deferred follow-up |
| Normative impact | Public draft contract for interaction-event semantics, observation/effect separation, authority and scope requirements, evidence continuity, and technology-independent external contact boundaries |
| Runtime implementation impact | None by this document alone |
| Release alignment | Draft; initial SRD explanation added; no runtime enablement, production behavior, SDK/API, or conformance claim |

This document abstracts the formation proposal into public specification language. It does not expose proprietary runtime internals, hidden prompts, deployment topology, private telemetry, private evaluation corpora, implementation-specific control overlays, internal task labels, or production operations.

---

## 4. Scope and Applicability

EIL applies whenever a runtime trajectory receives material from, or may produce an effect on, a system outside the active stabilized trajectory.

Examples of environment surfaces include:

- users;
- external agents;
- retrieval stores;
- memory stores;
- databases;
- filesystems;
- provider APIs;
- communication channels;
- external execution services;
- governance services;
- deployment infrastructure.

Environment is defined computationally, not technologically.

EIL does not define:

- new planners;
- workflow engines;
- DAG execution;
- task graphs;
- orchestration semantics;
- mandatory REST, MCP, SDK, provider, or transport protocols;
- action permission by tool availability alone;
- memory persistence permission by observation alone;
- truth by retrieval alone;
- production execution behavior.

---

## 5. Specification

### 5.1 Core Definition

The Environment Interface Layer is the architectural boundary that governs interaction between stabilized Sigma runtime trajectories and external reality while preserving behavioral autonomy, authority boundaries, provenance, evidence continuity, and governance integrity.

Short form:

```text
EIL governs contact, not cognition.
```

### 5.2 Environment

An environment is every system, participant, source, target, store, channel, provider, execution surface, or governance surface outside the active stabilized runtime trajectory.

The environment may act as:

| Role | Description |
| --- | --- |
| Observation Source | Provides material that may influence runtime interpretation. |
| Evidence Store | Preserves or exposes records with provenance implications. |
| Capability Surface | Enables actions, side effects, cost, notification, execution, or state change. |
| Authority Source | Provides legitimate constraints or approvals within declared scope. |
| Participant | A human, agent, organization, or external entity with identity, role, privacy, and scope boundaries. |

These roles must not be silently merged.

### 5.3 Interaction Event

The smallest semantic unit of EIL is an **interaction event**.

An interaction event is:

```text
source-bearing contact between runtime trajectory and external reality,
with direction, authority, scope, effect, and evidence status.
```

An interaction event is not the same as:

- a tool;
- a workflow;
- a plan;
- a capability;
- an intent;
- an action alone.

Interaction-event semantics must be broad enough to cover observations and effects, but narrow enough to avoid becoming a workflow graph.

### 5.4 Required Interaction Fields

A public EIL-compatible interaction event should preserve:

| Field | Meaning |
| --- | --- |
| Source | Where the contact originates. |
| Target | What the contact affects or addresses. |
| Direction | Whether the environment influences runtime or runtime influences environment. |
| Authority | What permission or legitimacy applies. |
| Scope | Which session, user, agent, channel, entity, store, or system boundary applies. |
| Evidence | What record remains to reconstruct the interaction. |
| Effect | Whether the event is observation-only or can alter external state. |
| Status | Proposed, observed, blocked, authorized, executed, failed, replayed, or unknown. |

### 5.5 Interaction Directions

EIL distinguishes two primary directions.

#### Observation

Observation means the environment influences runtime.

Examples:

- user input;
- retrieved material;
- memory recall;
- provider output;
- external event;
- telemetry;
- operator note;
- other-agent message.

Observation never implies authority.

Observation never implies truth.

Observation never implies memory persistence.

#### Effect

Effect means runtime influences the environment.

Examples:

- persistence;
- notification;
- external execution;
- provider request;
- memory write;
- retrieval mutation;
- state mutation;
- tool or service invocation.

Effects require stronger governance than observations.

### 5.6 Layer Responsibilities

| Layer | Responsible For | Not Responsible For |
| --- | --- | --- |
| Behavior Layer | Stabilization, attractors, identity, intent formation, behavioral coherence. | External execution authority. |
| Memory Layer | Continuity, retrieval, provenance, temporal validity, persistence policy. | External execution authority. |
| EIL | Environment boundary, interaction classification, authority validation, effect classification, evidence continuity, replay and audit requirements. | Cognition, identity formation, truth creation, planner behavior, or workflow orchestration. |
| Governance Layer | Legitimacy, contestability, policy authority, exceptional state, capture boundaries. | Routine cognition or automatic action generation. |

### 5.7 Normative Invariants

A conformant EIL implementation must preserve these invariants:

- attractor dynamics remain primary;
- runtime cognition must not be replaced by workflow graphs;
- external interaction remains subordinate to stabilized behavior and authority review;
- observation must not imply authority;
- observation must not imply truth;
- retrieval must not imply current fact;
- capability must not imply permission;
- tool availability must not become action justification;
- successful execution must not imply governance success;
- external effects must remain reconstructable;
- external interactions must preserve evidence continuity.

### 5.8 Semantic Effect Transaction

SRIP-24 owns the boundary for staging, validating, releasing, retrying,
compensating, and escalating consequential external effects. A semantic effect
transaction MUST bind, directly or by immutable reference:

- task intent and affected object or target;
- actor and current release authority;
- capability, operation, resource, and sink;
- accepted runtime-state dependency;
- staged effect intent and evidence lineage;
- idempotency or equivalent duplicate-effect protection where supported;
- release, acknowledgement, outcome, retry, compensation, and escalation
  semantics.

External effects MUST remain staged until the applicable validation and current
authority checks succeed. Historical authorization or a previously successful
effect MUST NOT grant authority for a new release.

Where a local commit depends on an effect intent, that intent MUST be staged
and durably identifiable no later than the accepted local-state commit. Staging
does not release the effect. If the committed intent cannot be recovered or
its binding cannot be verified, release MUST be blocked pending reconciliation.

Local state promotion and external effect release are distinct transitions.
After an effect has been released, a later failure MUST be represented as a
missing or contradictory outcome, retry, compensation, or escalation. It MUST
NOT be represented as rollback unless the target actually provides and proves
that reversal.

Where idempotency, acknowledgement, read-back, or compensation is unsupported,
the declared profile MUST expose that limitation. SRIP-25 owns the linked event
representation for these transitions. SRIP-28 candidate admission does not
authorize external effect release.

An unknown outcome MUST NOT be treated as proof that no effect occurred.
Before retrying an uncertain release, the runtime MUST reconcile the outcome
or establish duplicate-effect protection valid for the same effect identity,
target, payload, and retry interval. If neither is possible, automatic retry
MUST be blocked and the unresolved effect escalated, unless current authority
explicitly permits a bounded retry under a declared duplicate-risk policy.
That exception MUST preserve the unknown prior outcome, record the accepted
duplication risk and retry limit, and MUST NOT claim exactly-once execution.
Every retry remains subject to current release-authority checks.

Multiple attempts or receipts may refer to one external effect. Duplicate-effect
protection concerns the external consequence, not the number of successful
responses. Outcome evidence may include read-back or a target receipt whose
declared semantics establish completion; a transport acknowledgement alone
does not establish completion.

### 5.9 Conformance Review Scenarios

| Scenario | Required result |
| --- | --- |
| A rejected or held candidate proposes an effect | No effect is released and no successful effect event is created. |
| Current release authority expired after local commit | The staged effect fails closed without rewriting the accepted local state. |
| The same idempotent effect is retried | The retry has new attempt lineage linked to the same effect identity and does not produce a duplicate external effect within the declared protection scope. Multiple receipts for that effect remain distinct evidence. |
| Outcome is unknown and duplicate-effect protection cannot be established | Automatic retry is blocked and escalated unless current authority explicitly admits a bounded duplicate-risk retry; the prior outcome remains unknown until resolved. |
| A crash occurs after local commit but before release | The staged intent remains recoverable and bound to the commit; missing or unverifiable intent blocks release pending reconciliation. |
| Transport succeeds but outcome evidence is absent | The attempt remains distinct and outcome is unknown. |
| Read-back contradicts the intended effect | The contradiction is preserved beside authorization and attempt evidence. |
| Compensation is unavailable for an irreversible effect | The limitation and residual state remain explicit; rollback is not claimed. |

---

## 6. Interoperability and Dependencies

| Dependency | Type | Notes |
| --- | --- | --- |
| SRIP-05 Interoperability Interface | Parent | Provides public interoperability context for external contact and interface surfaces. |
| SRIP-14 RMI | Parent | Governs retrieval and memory interaction, including source and persistence boundaries. |
| SRIP-21 EIB | Parent | Governs external participants, identity/mode binding, and referent scope. |
| SRIP-22 GRC | Parent | Governs authority, legitimacy, evidence continuity, and contestability. |
| SRIP-01 Runtime Loop | Related | EIL attaches to trajectory continuation without replacing the runtime loop. |
| SRIP-04 Memory Layer | Related | EIL interacts with memory boundaries but does not redefine memory architecture. |
| SRIP-06 Safety and Recursion Boundaries | Related | External interaction must remain within recursion and safety boundaries. |
| SRIP-13 RIS | Related | Relational identity boundaries constrain participant interaction. |
| SRIP-15 ADP | Related | External contact may perturb runtime trajectory and must remain bounded. |
| SRIP-17 MAE | Related | Multi-agent exchange is an environment interaction class. |
| SRIP-19 RCB | Related | Contested external evidence may require contradiction buffering. |
| SRIP-20 ANS | Related | External influence or authority pressure may require autonomy negotiation. |
| SRIP-25 IEM | Related / refinement | Defines the public semantic unit for contact crossing the EIL boundary. |

Backwards compatibility: this public draft does not modify existing SRIPs. It introduces a public interaction-boundary abstraction that can organize future implementation guidance without prescribing a transport or execution framework.

---

## 7. Safety and Alignment Review

EIL reduces risk by preventing interaction-boundary collapse.

Primary risks:

- workflow capture;
- tool capture;
- authority collapse;
- evidence collapse;
- memory persistence by accidental observation;
- action justification by tool availability;
- governance success being inferred from task success.

Required safety posture:

- classify observation and effect separately;
- attach source, target, authority, scope, evidence, and effect status;
- keep capability separate from permission;
- keep retrieval separate from truth and currentness;
- keep task success separate from governance success;
- require stronger governance for effects than observations;
- preserve replay and auditability for external effects.

---

## 8. SRD Synchronization Plan

Initial SRD synchronization is provided by
[Environment Interaction and Events](../../srd/environment-interaction-and-events.md).

Broader SRD synchronization is still required before any release or public
communication claims full alignment with SRIP-24.

Likely affected SRD areas:

- runtime architecture;
- trajectory governance;
- external interaction and tool/action boundaries;
- memory/retrieval provenance;
- authority and governance;
- long-horizon agent continuity;
- implementation-independent environment semantics.

Until synchronization is complete, public alignment must be stated as:

```text
Public draft only; no runtime enablement, production behavior, SDK/API,
or conformance claim.
```

---

## 9. Implementation Guidelines

This public draft does not define implementation APIs, SDKs, schemas, transports, provider integrations, or production behavior.

Future implementation-readiness work should define:

- interaction-event schema, building on SRIP-25 IEM;
- observation/effect taxonomy;
- authority and scope validation;
- evidence and replay requirements;
- state-transition rules for proposed, blocked, authorized, executed, failed, and replayed events;
- conformance tests for observation/effect separation;
- conformance tests for capability/permission separation;
- audit requirements for external effects.

Any implementation should default to observation-only or evidence-only operation until separate governance enables stronger effects.

---

## 10. Versioning and Backward Compatibility

SRIP-24 is additive.

This draft does not deprecate or supersede existing SRIPs. It introduces a public architecture layer for environment interaction semantics while remaining subordinate to the runtime loop, memory/retrieval, external identity, autonomy, contradiction, and governance specifications.

---

## 11. References

- [SRIP-05 Interoperability Interface](../srip-05.md)
- [SRIP-14 RMI](SRIP-14-RMI.md)
- [SRIP-21 EIB](SRIP-21-EIB.md)
- [SRIP-22 GRC](SRIP-22-GRC.md)
- [SRIP-19 RCB](SRIP-19-RCB.md)
- [SRIP Process](../../team/srip-process.md)
- [SRS-SRD Interaction Requirements](../../team/srs-srd-interaction-requirements.md)
- [Public-Proprietary Information Boundary Requirements](../../team/public-proprietary-information-boundary-requirements.md)

---

## 12. Change Log

| Version | Date | Author | Description |
| --- | --- | --- | --- |
| 0.1 | 2026-06-27 | SSRG | Formation draft. |
| 0.2 | 2026-06-27 | SSRG | Public draft normalization with boundary, dependency, non-goal, conformance, and SRD synchronization fields. |
| 0.3 | 2026-09-23 | SSRG | Added the semantic effect transaction boundary and separated local commitment from external release, retry, compensation, and outcome evidence. |
