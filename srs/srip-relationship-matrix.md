---
title: SRIP Relationship Matrix
description: Non-normative matrix of SRIP roles, inputs, outputs, constraints, and architecture relationships.
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

# SRIP Relationship Matrix

Status: **Non-normative review draft**

This matrix is an integration aid. Individual SRIP documents remain the
authority for normative requirements, lifecycle status, dependencies, and
conformance claims.

## Matrix

| SRIP | Primary role | Consumes | Produces or strengthens | Principal constraints or handoffs |
| --- | --- | --- | --- | --- |
| 00 Foundations | Root vocabulary and architecture scope | Public standard purpose | Shared concepts and structural invariants | Bounds all later proposals; does not imply implementation |
| 01 Runtime Loop | Runtime continuation and accepted local-state commitment | Interaction input and runtime state | Ordered cycle, accepted local state, and feedback closure | External effect release remains SRIP-24 authority |
| 02 Attractor Model | Addressable attractor state | Runtime observations | Attractor metadata and lifecycle | Drift, identity, and safety constrain transitions |
| 03 Drift Metrics | Stability evidence and recovery triggers | Attractor and trajectory state | Drift classes, indices, stabilization signals | Metrics require evidence quality and bounded thresholds |
| 04 Memory Layer | Foundational memory contract | Runtime events and state | Persisted and recalled memory | Provenance, privacy, retrieval, and influence governance |
| 05 Interoperability | External interface lineage | Runtime state and exchange requests | Versioned exchange structures and safety hooks | Environment, identity, provenance, and authorization boundaries |
| 06 Safety Boundaries | Non-bypassable safety and recursion limits | Runtime and instability evidence | Safe-mode, isolation, and recovery constraints | Precedes optimization and generation controls |
| 07 Symbolic Density | Semantic pressure evidence | Runtime language and attractor state | Density signals and regulation guidance | Must not turn stylistic metrics into authority claims |
| 08 Phase Model | Phase evidence and regulation lineage | Runtime telemetry | Phase vectors and synchronization signals | Safety and evidence-quality constraints |
| 09 LTM-SC | Durable structural continuity | Memory records and runtime lineage | Long-term graph, temporal anchors, recovery traces | Privacy, provenance, retention, and influence admission |
| 10 AEP | Entropy and crystallization regulation | Drift, density, phase, and trajectory evidence | Entropy signals and bounded control recommendations | Cannot override safety, identity, autonomy, or governance |
| 11 SMC | Structural memory compression and topology | Long-term memory records | Rib points, clusters, anchors, compressed recall | Must preserve lineage and avoid authority creation by compression |
| 12 CDS | Deterministic commerce state authority | Validated commerce scope and candidates | Stable commerce state and deterministic transitions | CSI semantics cannot override CDS invariants |
| 13 RIS | Relational and identity stabilization | Participant, session, temporal, and naming evidence | Identity boundaries and stabilization actions | Safety precedence; must not invent ontology or identity authority |
| 14 RMI | Retrieval and injection governance | Query, memory, source, and provenance evidence | Retrieval envelope and bounded injection | Safety, identity, autonomy, and memory-influence admission |
| 15 ADP | Controlled perturbation | Stability evidence and approved perturbation sources | Bounded variation and return conditions | Safety, contradiction preservation, and governance |
| 16 RSM | Reflective evidence | Runtime telemetry and bounded snapshots | Self-model observations and control proposals | Evidence only; no consciousness or self-authorization claim |
| 17 MAE | Multi-agent exchange | Local and external agent artifacts | Provenanced exchange and local reintegration | Identity, contradiction, autonomy, and governance boundaries |
| 18 CSI | Commerce semantic integration | RMI-governed context and runtime bundle | Grounded commerce semantic scope | CDS retains deterministic decision authority |
| 19 RCB | Contradiction preservation and recovery | Incompatible but potentially valid states | Buffered contradiction, energy, and resolution readiness | Must not hide conflict or force consensus |
| 20 ANS | Autonomy and influence boundary control | Influence, consent, delegation, and identity evidence | Negotiated boundary state, event-time delegation validity, and current revalidation | Historical validity does not grant current invocation authority |
| 21 EIB | External identity and mode reconciliation | External observations, provenance, and modes | Stable external entity binding or unresolved mode set | Must preserve uncertainty and hand unresolved conflict to RCB |
| 22 GRC | Governance legitimacy and capture boundary | Authority, evidence, certification, and collusion assumptions | Legitimacy state, immutable governance epochs, contestability, suspension, and fork/exit conditions | Safety remains non-bypassable; integrity proof alone is not legitimacy |
| 23 DGL | Controlled semantic candidate generation | Preserved contradiction and bounded perturbation | Non-canonical candidate structures with lineage | RCB source remains intact; governance required for promotion |
| 24 EIL | Environment observation/effect boundary | External contact and runtime intent | Staged, authorized, released, retried, compensated, or escalated effects | Current release authority is distinct from candidate admission and local commit |
| 25 IEM | Transport-independent event semantics | Environment interactions | Epoch-bound typed events and append-only lineage | Authorization, attempt, outcome, and verification remain distinct and action-inert |
| 26 MIL | Memory influence admission and routing | Remembered, retrieved, archived, or ledger material | Admitted, limited, routed, evolved, or rejected influence | Availability and relevance do not create current authority |
| 27 TMC | Target-relative trajectory measurement | Candidate, frozen authority, accepted-local reference, and competing-regime evidence | Membership state with explicit validity | Evidence only; cannot admit, reject, deliver, persist, or mutate candidates |
| 28 TAL | Pre-persistence candidate admission | TMC membership, AEP dynamics, boundary state, lineage, and recovery evidence | Admit, hold, reject, boundary-only, or contain-review transaction | Single writer for candidate delivery only; it does not release external effects |

## Cross-Cutting Reinforcement Chains

| Property | Reinforcement chain |
| --- | --- |
| Continuity | `01 -> 04 -> 09 -> 11 -> 14 -> 26` |
| Stability | `02 -> 03 -> 07/08/10 -> 06 -> 15/19` |
| Identity integrity | `13 -> 21 -> 19`, constrained by `20` and `22` |
| Governed novelty | `15 -> 19 -> 23 -> 22` |
| External accountability | `05 -> 24 -> 25 -> 17`, constrained by `21/22` |
| Effect integrity | `28 -> 01 -> 24 -> 25`, with current delegation revalidation by `20` and governance epochs by `22` |
| Commerce grounding | `14 -> 18 -> 12` |
| Reflective control | `16 -> 20 -> 22`, with `16` remaining evidence-only |
| Trajectory integrity | `02/03/08/10/15/19 -> 27 -> 28 -> 26`, with `27` evidence-only and `28` owning admission |

## Matrix Maintenance Rule

If this matrix disagrees with a canonical SRIP, the SRIP wins. The disagreement
should be logged as an integration-review issue before either document is
changed.
