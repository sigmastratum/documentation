---
title: SRIP Architecture Synthesis
description: Non-normative integration view of the Sigma Runtime Improvement Proposal architecture.
published: true
date: 2026-07-17T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-07-17T00:00:00.000Z
---

> **Sigma Runtime Standard - Public Integration Notice**
>
> This non-normative integration document is licensed under Creative Commons
> Attribution 4.0 International (`CC BY 4.0`). It does not amend canonical
> SRIPs or grant implementation, certification, or runtime authority.

# SRIP Architecture Synthesis

Status: **Non-normative review draft**

Review lineage: initial architecture synthesis by Volodymyr Riabinskyi in
`git:9ee173584c41d779401d1dba5488d86179c46281`; publication repair preserves
canonical SRIP authority and current SRIP-00 through SRIP-28 coverage.

This document explains how the public Sigma Runtime Improvement Proposals form
one architecture. It does not amend an SRIP, create a conformance requirement,
or replace the numerical registry or the architecture reading-order page.

The canonical meaning, lifecycle status, and conformance claim of each proposal
remain in that proposal's own header and normative sections.

## 1. Why This View Exists

The SRIP corpus intentionally keeps proposals independently reviewable and
versionable. That separation protects citation stability, but makes several
system-level questions difficult to answer from one document:

- which proposals define foundations and which specialize them;
- which proposals supply evidence and which are allowed to make decisions;
- which proposals amplify capabilities and which constrain them;
- where memory, identity, authority, and environment effects meet;
- which control boundary has precedence when two valid mechanisms disagree.

This synthesis provides that missing integration view without merging the SRIPs
into one normative monolith.

## 2. Interpretation Rules

Relationships in this document use the following vocabulary.

| Relationship | Meaning |
| --- | --- |
| `depends_on` | The source contract requires concepts or invariants defined by the target. |
| `extends` | The source adds a capability without replacing the target contract. |
| `specializes` | The source applies a general contract to a narrower domain. |
| `constrains` | The source limits behavior otherwise permitted by the target. |
| `provides_evidence_to` | The source supplies observations; the target retains decision authority. |
| `governs` | The source controls whether an action or state transition is authorized. |
| `feeds` | The source supplies data or state used by the target. |
| `recovers` | The source defines handling after a violated or unstable condition. |
| `amends` | The source changes the normative meaning of the target. This must be declared by the affected SRIPs. |
| `supersedes` | The source replaces the target while preserving historical traceability. |

An edge in this review draft is an architectural interpretation, not by itself
a normative amendment. Any new `amends` or `supersedes` claim requires a
separate SRIP-specific review.

## 3. Architecture In One Sentence

Sigma Runtime receives evidence-bearing events, continues a bounded trajectory,
uses memory as governed influence rather than unquestioned authority, regulates
drift and crystallization, protects identity and autonomy, preserves unresolved
contradiction, permits controlled formation of new semantic structures, and
executes external effects only through explicit authority and governance
boundaries.

## 4. Layer Map

### 4.1 Foundations and runtime physics

`SRIP-00` through `SRIP-08` define the common world in which later proposals
operate:

- `SRIP-00` defines scope and foundational vocabulary;
- `SRIP-01` defines the canonical runtime loop;
- `SRIP-02` makes attractors addressable runtime entities;
- `SRIP-03` makes drift observable and actionable;
- `SRIP-04` defines the memory architecture;
- `SRIP-05` defines interoperability boundaries;
- `SRIP-06` defines recursion and safety limits;
- `SRIP-07` defines symbolic-density pressure;
- `SRIP-08` defines phase representation and regulation lineage.

These proposals define the architecture's coordinate system. Later proposals
should specialize or constrain it rather than silently redefine it.

### 4.2 Memory, retrieval, and influence

The memory sequence separates persistence, compression, retrieval, and
behavioral influence:

1. `SRIP-04` defines memory as a runtime layer.
2. `SRIP-09` adds durable structural coherence and lineage.
3. `SRIP-11` adds compression and topological recall.
4. `SRIP-14` governs retrieval, provenance, compression, and injection.
5. `SRIP-26` governs whether remembered or retrieved material may influence
   current behavior.

The key invariant is that availability is not authority. A memory can exist, be
retrievable, and be relevant while still lacking permission to steer the
current runtime state.

### 4.3 Runtime regulation and recovery

`SRIP-03`, `SRIP-06`, `SRIP-07`, `SRIP-08`, and `SRIP-10` provide signals and
limits for runtime stability. `SRIP-13`, `SRIP-15`, and `SRIP-19` then apply
specialized control:

- `SRIP-13` protects identity, participant, temporal, and relational bounds;
- `SRIP-15` permits bounded perturbation without uncontrolled destabilization;
- `SRIP-19` preserves incompatible states without false consensus or immediate
  collapse.

Regulation should not optimize one metric by violating a higher boundary. For
example, entropy optimization cannot override safety or identity invariants.

### 4.4 Self-model, autonomy, and governance

`SRIP-16` supplies reflective evidence but does not grant self-authority.
`SRIP-20` evaluates influence, delegation, consent, and autonomy pressure.
`SRIP-22` evaluates the legitimacy of the governance mechanisms themselves.

This creates three distinct levels:

1. observation of the runtime (`SRIP-16`);
2. negotiation of local influence and boundaries (`SRIP-20`);
3. legitimacy, capture, contestability, and emergency authority (`SRIP-22`).

Evidence about a controller is not permission for that controller to expand its
own authority.

### 4.5 External identity, agents, and contradiction

`SRIP-17` governs multi-agent exchange. `SRIP-21` prevents observations of
different modes from being collapsed into unstable external identity claims.
`SRIP-19` preserves unresolved conflicts, while `SRIP-23` may use bounded
dialectical tension to propose new semantic candidates.

Generation does not erase its source contradiction. A candidate produced by
`SRIP-23` remains non-canonical until the applicable validation and governance
path authorizes promotion.

### 4.6 Environment contact and effects

`SRIP-24` defines the boundary between the runtime and an environment.
`SRIP-25` defines the semantic event that crosses that boundary. `SRIP-05` and
`SRIP-17` provide interoperability and multi-agent specializations.

The central distinction is observation versus effect:

- an observation can update evidence without claiming effect authority;
- an effect requires explicit target, scope, authorization, result, and audit
  semantics;
- transport success does not by itself prove semantic success or legitimacy.

Effect processing adds a second strict separation:

```text
accepted local-state commit
!= candidate admission
!= external effect release
!= observed or verified external outcome
```

`SRIP-01` owns accepted local-state commitment. `SRIP-28` owns generated
candidate admission only. `SRIP-24` owns effect staging, current-authority
validation, release, retry, compensation, and escalation. `SRIP-25` owns the
typed, append-only event anchors for authorization, attempt, outcome
observation, and verification. Historical validity is preserved without
granting current invocation authority.

### 4.7 Commerce specialization

The commerce stack is a domain specialization of the general retrieval and
control architecture:

1. `SRIP-14` governs retrieval and memory inputs;
2. `SRIP-18` assembles bounded semantic commerce context;
3. `SRIP-12` retains deterministic authority over commerce decision state.

Semantic relevance can improve a decision surface, but it must not silently
replace deterministic decision invariants.

### 4.8 Trajectory measurement and candidate admission

`SRIP-27` and `SRIP-28` add a boundary that dynamic regulation and governance
alone do not provide:

1. `SRIP-27` measures whether a candidate belongs to the intended trajectory
   and reports explicit measurement validity.
2. `SRIP-28` owns the single pre-persistence admission transaction and decides
   which candidate, if any, may become delivered and influential state.

The separation is strict:

```text
dynamic stability != target membership
TMC measures; TAL admits
```

TMC cannot deliver or reject a candidate. TAL cannot rewrite TMC evidence.
Generated, held, rejected, and recovery candidates remain non-canonical until
the applicable TAL decision selects admitted lineage.

## 5. Capability and Constraint Pairs

The architecture becomes clearer when each capability is paired with the layer
that bounds it.

| Capability | Strengthened by | Bounded by |
| --- | --- | --- |
| Long-horizon continuity | SRIP-04, 09, 11 | SRIP-14 provenance and SRIP-26 influence admission |
| Retrieval relevance | SRIP-14 | SRIP-06 safety, SRIP-13 identity, SRIP-20 autonomy |
| Adaptive regulation | SRIP-03, 07, 08, 10 | SRIP-06 safety and declared control precedence |
| Controlled novelty | SRIP-15, 23 | SRIP-19 contradiction preservation and SRIP-22 governance |
| Self-observation | SRIP-16 | no self-authorization; SRIP-20 and SRIP-22 retain boundary authority |
| Multi-agent learning | SRIP-17 | SRIP-21 identity, SRIP-19 contradiction, SRIP-22 legitimacy |
| External action | SRIP-24, 25 | explicit authorization, evidence continuity, and governance |
| Commerce grounding | SRIP-18 | SRIP-14 retrieval governance and SRIP-12 deterministic decision state |
| Trajectory continuity | SRIP-02, 03, 08, 10, 15, 19 | SRIP-27 measurement validity and SRIP-28 pre-persistence admission |

## 6. End-to-End Runtime Interpretation

A complete architecture path can be read as:

1. An interaction event crosses an environment boundary (`SRIP-24`, `SRIP-25`).
2. The runtime loop admits it as evidence (`SRIP-01`).
3. Identity, source, mode, and provenance are resolved (`SRIP-13`, `SRIP-14`,
   `SRIP-21`).
4. Relevant memory is retrieved and compressed (`SRIP-09`, `SRIP-11`,
   `SRIP-14`).
5. Memory influence is admitted, limited, archived, or rejected (`SRIP-26`).
6. Drift, density, phase, and entropy signals are evaluated (`SRIP-03`,
   `SRIP-07`, `SRIP-08`, `SRIP-10`).
7. Safety, autonomy, and governance boundaries constrain the available actions
   (`SRIP-06`, `SRIP-20`, `SRIP-22`).
8. Contradiction is buffered when valid states cannot yet be reconciled
   (`SRIP-19`).
9. Controlled perturbation, provider generation, or dialectical generation may
   produce a candidate (`SRIP-15`, `SRIP-23`).
10. Target membership is measured independently of dynamic stability
    (`SRIP-27`).
11. The candidate is admitted, held, rejected, or contained before accepted
    persistence and downstream influence (`SRIP-28`).
12. Only selected admitted lineage may acquire memory influence (`SRIP-26`) or
    become an externally visible effect.
13. Any external effect returns through an authorized environment event
    (`SRIP-24`, `SRIP-25`).

Not every runtime must implement every step. A conformance profile should name
the supported path, omitted proposals, and known deviations.

## 7. Review Questions Exposed By The Synthesis

This integration view surfaces questions that cannot be settled by navigation
alone:

1. Which foundational SRIPs are mandatory for each conformance profile?
2. Are all `Parent Specs` relationships directionally consistent?
3. Which metrics are evidence only, and which may trigger state transitions?
4. Is control precedence consistent across safety, identity, autonomy, memory,
   domain, and governance layers?
5. Which proposal owns authorization for each externally visible effect?
6. Are TMC measurement validity and TAL admission authority kept separate in
   every conformance profile?
7. Which dependency and status claims can be validated automatically?

Answers that change an SRIP's normative meaning must be handled as separate,
reviewable SRIP amendments.

## 8. Companion Artifacts

- [`srip-relationship-matrix.md`](srip-relationship-matrix.md) provides a
  proposal-by-proposal integration matrix.
- [`srip-control-precedence.md`](srip-control-precedence.md) provides a
  provisional conflict-resolution model.
- [`srip-dependency-graph.yaml`](srip-dependency-graph.yaml) provides a
  machine-readable canonical-parent graph plus a selected integration overlay.
- [`srip-relationship-audit.md`](srip-relationship-audit.md) records canonical
  coverage and the evidence status of integration edges.
- [`architecture-reading-order.md`](architecture-reading-order.md) remains the
  reader-navigation view.
- [`registry.md`](registry.md) remains the numerical registry authority.

## 9. Change Policy

Changes to this synthesis must remain descriptive unless accompanied by an
approved amendment to every affected normative SRIP. A synthesis edit must not
silently create a new parent, precedence rule, conformance requirement, or
implementation claim.
