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

# SRIP-25 - Interaction Event Model (IEM)

**Semantic Units of Governed Runtime-Environment Contact**

| Field | Value |
| --- | --- |
| SRIP | SRIP-25 |
| Title | Interaction Event Model (IEM) |
| Version | Public Draft v0.2 |
| Status | Public Draft |
| Date | 2026-06-27 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Integration Boundary / Event Semantics / Runtime Control / Governance |
| Parent Specs | SRIP-05, SRIP-22, SRIP-24 |
| Related Specs | SRIP-01, SRIP-04, SRIP-13, SRIP-14, SRIP-17, SRIP-19, SRIP-20, SRIP-21 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Commercial Runtime Boundary | Relevant policy or explicit covenant for protected Sigma marks, official certification, managed deployment, white-label, resale, CC BY-NC commercial use, and patent commitments |
| Information Class | Open |
| Change Class | Mixed SRS+SRD |
| Normative Status | Defines a public draft semantic model for interaction events crossing the Environment Interface Layer boundary. It does not define an event bus, database schema, serialization format, provider API, transport protocol, workflow engine, replay system, or production implementation. |
| Conformance Level | Public Draft / No runtime conformance claim |
| SRD Synchronization Action | Initial SRD synchronization completed in `/srd/environment-interaction-and-events`; broader synchronization for EIL, tool/action boundaries, memory/retrieval, governance, event/evidence, replay, and runtime architecture explanation remains deferred follow-up. |
| Release Alignment Status | Public draft architecture proposal; no runtime enablement, production behavior, schema serialization, event bus, replay system, or conformance claim is made by this document alone. |

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows these public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

---

## 1. Summary

SRIP-25 defines the **Interaction Event Model (IEM)**: a public draft semantic model for representing contact between a Sigma runtime trajectory and an external environment at the Environment Interface Layer boundary.

SRIP-24 defines where governed runtime-environment contact occurs.

SRIP-25 defines the smallest semantic unit of that contact:

```text
Interaction Event
```

An interaction event is a bounded, attributable, evidence-bearing interaction between a runtime trajectory and an external environment. It is independent of transport, provider, tool framework, SDK, or orchestration system.

This SRIP is a public draft architecture contract. It does not claim that IEM is implemented in any current Sigma Runtime release.

---

## 2. Motivation

Many agent frameworks model external interaction primarily as:

- tool calls;
- workflow steps;
- API requests;
- planner actions;
- provider calls.

Sigma Runtime uses a different architectural abstraction.

The relevant question is not only:

```text
Which tool was called?
```

The deeper runtime-governance question is:

```text
Which interaction event occurred?
```

IEM exists to make external contact technology-independent and governance-visible. Tools, APIs, transports, filesystems, databases, humans, providers, sensors, and agents are implementation surfaces. The public semantic unit is the interaction event.

---

## 3. Public Boundary and Traceability

| Field | Disposition |
| --- | --- |
| Source material | Open public-draft candidate derived from sanitized architectural formation material |
| Affected SRS surface | SRIP registry / EIL / interoperability / governance / memory-retrieval / event semantics |
| Affected SRD surface | Runtime architecture, EIL, tool/action, memory/retrieval, governance, event/evidence, replay, and long-horizon interaction explanations |
| SRD synchronization | Deferred follow-up |
| Normative impact | Public draft semantic model for observation events, effect events, interaction-event fields, invariants, and technology-independent runtime-environment contact |
| Runtime implementation impact | None by this document alone |
| Release alignment | Draft; initial SRD explanation added; no runtime enablement, production behavior, schema serialization, event bus, replay system, or conformance claim |

This document abstracts the formation proposal into public specification language. It does not expose proprietary runtime internals, hidden prompts, deployment topology, private telemetry, private evaluation corpora, implementation-specific control overlays, internal task labels, production operations, or private event schemas.

---

## 4. Scope and Applicability

IEM applies whenever material crosses the Environment Interface Layer boundary as either:

- an observation from environment to runtime; or
- an effect from runtime to environment.

IEM does not define:

- tool interfaces;
- MCP bindings;
- REST bindings;
- SDKs;
- provider APIs;
- workflow languages;
- planning systems;
- event bus implementation;
- database schema;
- serialization format;
- replay engine;
- rollback system;
- production execution behavior.

Those belong to future implementation-specific or future specification work.

---

## 5. Specification

### 5.1 Core Definition

An **Interaction Event** is the smallest governed unit of contact between Sigma Runtime and external reality, carrying sufficient semantic, authority, provenance, and evidence information to reconstruct, audit, replay, or contest that interaction independently of implementation technology.

Public-safe short form:

```text
Interaction events represent contact.
They do not produce cognition.
They do not authorize themselves.
```

### 5.2 Relationship to EIL

SRIP-24 EIL governs whether and how runtime-environment contact may occur.

SRIP-25 IEM governs what that contact means once represented as a public semantic unit.

```text
EIL = boundary and governance of contact
IEM = semantic unit crossing the boundary
```

IEM is therefore a refinement of EIL, not a replacement for EIL.

### 5.3 Event Categories

IEM defines two primary categories.

#### Observation Event

An observation event represents environment-to-runtime contact.

Examples:

- user message;
- retrieval result;
- provider response;
- webhook;
- file read;
- telemetry;
- sensor input;
- other-agent message.

Observation events may influence runtime interpretation.

Observation events must not directly authorize behavior, memory persistence, external action, or truth claims.

#### Effect Event

An effect event represents runtime-to-environment contact.

Examples:

- provider request;
- tool execution;
- memory persistence;
- notification;
- filesystem write;
- database mutation;
- workflow trigger;
- human escalation.

Effect events may alter external reality.

Effect events require stronger governance than observation events and must not authorize themselves.

### 5.4 Required Event Fields

A public IEM-compatible event should preserve:

| Field | Meaning |
| --- | --- |
| Direction | Observation or effect direction. |
| Source | Origin of the contact. |
| Target | Entity, system, channel, store, participant, or surface affected or addressed. |
| Scope | Boundary in which the event is valid. |
| Time | Temporal placement of the event. |
| Authority | Permission, legitimacy, or authorization state. |
| Effect Class | Whether the event is observation-only, effectful, mutating, notifying, costly, or otherwise externally consequential. |
| Evidence Status | Whether the event is traceable, replayable, witnessed, redacted, missing, or uncertain. |
| Provenance | Source chain or lineage supporting the event. |
| Trace Identifier | Identifier sufficient to connect evidence without exposing private payloads. |

Optional or future-extension fields may include:

- cost;
- privacy classification;
- replay eligibility;
- rollback eligibility;
- risk classification;
- witness status;
- compression status.

### 5.5 Architectural Invariants

A conformant IEM implementation must preserve these invariants:

- interaction events must not contain planning logic;
- interaction events must not authorize themselves;
- interaction events must not modify behavioral policy by themselves;
- interaction events must not replace attractor stabilization;
- observation events must not imply truth;
- observation events must not imply authority;
- observation events must not imply memory persistence;
- effect events must require governance stronger than observation events;
- event availability must not imply permission;
- implementation transport must not determine semantic authority.

### 5.6 Relationship to Behavior

Behavior creates stabilized trajectories and interaction candidates.

Behavior does not directly create external effects.

Illustrative flow:

```text
Behavior
  -> Interaction Candidate
  -> EIL Review
  -> Interaction Event
  -> External Environment
```

### 5.7 Relationship to Memory

Memory may consume observation events and may be updated by authorized effect events according to memory-layer policy.

IEM does not allow memory to bypass provenance, temporal validity, retrieval policy, or persistence authorization.

### 5.8 Relationship to Governance

Governance determines whether an effect event is authorized, contestable, auditable, reversible, blocked, or escalated.

IEM records the semantic event surface. It does not decide legitimacy by itself.

---

## 6. Interoperability and Dependencies

| Dependency | Type | Notes |
| --- | --- | --- |
| SRIP-24 EIL | Parent | Defines the boundary that interaction events cross. |
| SRIP-05 Interoperability Interface | Parent | Provides public interface context for external contact. |
| SRIP-22 GRC | Parent | Governs authority, evidence continuity, contestability, and effect authorization. |
| SRIP-14 RMI | Related | Required when events involve retrieval, memory reads/writes, provenance, or persistence. |
| SRIP-21 EIB | Related | Required when events involve external participants, agents, sources, or referents. |
| SRIP-20 ANS | Related | Required when events apply autonomy or boundary pressure. |
| SRIP-19 RCB | Related | Required when events carry contested evidence or unresolved contradiction. |
| SRIP-17 MAE | Related | Required for multi-agent exchange events. |
| SRIP-13 RIS | Related | Required when events affect relational or identity boundaries. |
| SRIP-04 Memory Layer | Related | Provides memory architecture context. |
| SRIP-01 Runtime Loop | Related | Provides runtime continuation context. |

Backwards compatibility: this public draft does not modify existing SRIPs. It refines SRIP-24 by defining the public semantic unit crossing the EIL boundary.

---

## 7. Safety and Alignment Review

IEM is safe only if it remains a semantic model rather than a self-authorizing action mechanism.

Required safety posture:

- observation events are not truth;
- observation events are not authority;
- observation events are not persistence permission;
- effect events require governance;
- events do not authorize themselves;
- event representation does not replace behavior, memory, identity, or governance layers;
- implementation transport does not determine event legitimacy;
- replay and rollback language must remain future work unless separately specified.

The central safety invariant is:

```text
Contact must be representable.
Representation is not authorization.
```

---

## 8. SRD Synchronization Plan

Initial SRD synchronization is provided by
[Environment Interaction and Events](/srd/environment-interaction-and-events).

Broader SRD synchronization is still required before any release or public
communication claims full alignment with SRIP-25.

Likely affected SRD areas:

- Environment Interface Layer explanation;
- runtime architecture;
- tool/action boundaries;
- memory/retrieval provenance;
- evidence and replay explanation;
- governance and authority;
- long-horizon interaction design.

Until synchronization is complete, public alignment must be stated as:

```text
Public draft only; no runtime enablement, production behavior, schema
serialization, event bus, replay system, or conformance claim.
```

---

## 9. Implementation Guidelines

This public draft does not define implementation APIs, SDKs, schemas, transports, event buses, provider integrations, replay engines, rollback systems, or production behavior.

Future implementation-readiness work should define:

- concrete event schema;
- serialization format;
- lifecycle states;
- replay semantics;
- witness semantics;
- rollback eligibility;
- privacy and redaction model;
- cost and risk fields;
- conformance tests for observation/effect separation;
- conformance tests for event self-authorization failure.

Any implementation should default to evidence-only or observation-only operation until separate governance enables stronger effects.

---

## 10. Versioning and Backward Compatibility

SRIP-25 is additive.

This draft does not deprecate or supersede existing SRIPs. It refines SRIP-24 EIL by defining a public semantic model for interaction events.

---

## 11. Author Checklist

- [x] Normative requirements are separated from examples.
- [x] Proprietary runtime implementation details are not disclosed.
- [x] Certification claims are not implied.
- [x] SRS/SRIP version dependencies are listed.
- [x] License fields are complete.
- [x] Public/proprietary boundary has been reviewed.
- [x] SRD synchronization impact has been reviewed.
- [x] Conformance level impact has been reviewed.
- [x] Marks and certification impact has been reviewed.

---

## 12. References

- [SRIP-24 EIL](SRIP-24-EIL.md)
- [SRIP-05 Interoperability Interface](../srip-05.md)
- [SRIP-22 GRC](SRIP-22-GRC.md)
- [SRIP-14 RMI](SRIP-14-RMI.md)
- [SRIP-21 EIB](SRIP-21-EIB.md)
- [SRIP Process](/team/srip-process)
- [SRS-SRD Interaction Requirements](/team/srs-srd-interaction-requirements)
- [Public-Proprietary Information Boundary Requirements](/team/public-proprietary-information-boundary-requirements)

---

## 13. Change Log

| Version | Date | Author | Description |
| --- | --- | --- | --- |
| 0.1 | 2026-06-27 | SSRG | Formation draft. |
| 0.2 | 2026-06-27 | SSRG | Public draft normalization with boundary, dependency, non-goal, conformance, and SRD synchronization fields. |
