---
title: SRIP Architecture Reading Order
description: Conceptual reading-order view for Sigma Runtime Improvement Proposals across architecture stacks.
published: true
date: 2026-07-17T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-05-14T00:00:00.000Z
---

> **Sigma Runtime Standard — Public Navigation License Notice**
>
> This non-normative navigation document is licensed under
> [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
> Referenced artifacts retain their own licenses. This notice does not grant
> trademark, certification, or patent rights.
>
> License revision: 2026-10-06, from CC BY-NC 4.0 to CC BY 4.0.
> See the [migration record](../legal/navigation-license-migration-2026-10-06.md)
> and [public specification policy](../legal/srs-public-specification-license.md).

# SRIP Architecture Reading Order

This page provides conceptual reading paths for Sigma Runtime Improvement Proposals.

It is a navigation view, not a numbering authority.

SRIP numbers remain immutable public proposal identifiers. The numerical registry records proposal history. This page may change as the architecture evolves.

For the authoritative numerical registry, see [`/srs/registry`](registry.md).

## Certification Boundary

This reading order is not a certification claim.

Reading or implementing SRS/SRIP documents does not imply official Sigma certification, endorsement, or use of Sigma marks.

For conformance terminology, see [`/srs/conformance/`](conformance/README.md).

---

## Canonical Rule

- SRIP numbers are assigned monotonically after public draft acceptance.
- SRIP numbers are not reassigned to improve conceptual order.
- Architecture relationships are expressed through `Parent Specs`, `Related Specs`, `Extends`, `Amends`, and `Supersedes`.
- Conceptual reading order is maintained here and in other index views.

This preserves citation stability while still allowing readers to follow the architecture in the order that best fits a given stack.

---

## Foundational Sequence

Read these first when entering the public standard:

1. [SRIP-00](srip-00.md) — Foundations and Scope
2. [SRIP-01](srip-01.md) — Canonical Runtime Loop
3. [SRIP-02](srip-02.md) — Attractor State Model and Metadata
4. [SRIP-03](srip-03.md) — Drift Metrics and Stabilization Algorithms
5. [SRIP-04](srip-04.md) — Memory Layer Architecture
6. [SRIP-05](srip-05.md) — Interoperability Interface
7. [SRIP-06](srip-06.md) — Safety and Recursion Boundaries
8. [SRIP-07](srip-07.md) — Symbolic Density Layer
9. [SRIP-08](srip-08.md) — Phase Vector Model and PRM

---

## Memory And Retrieval Sequence

Use this path for long-running memory, retrieval, and recall behavior:

1. [SRIP-04](srip-04.md) — Memory Layer Architecture
2. [SRIP-09-LTM](registry/SRIP-09-LTM.md) — Long-Term Memory and Structural Coherence Layer
3. [SRIP-11-SMC](registry/SRIP-11-SMC.md) — Structural Memory Compression (legacy CMT redirect retained)
4. [SRIP-14-RMI](registry/SRIP-14-RMI.md) — Retrieval and Memory Integration Layer
5. [SRIP-26-MIL](registry/SRIP-26-MIL.md) — Memory Influence Layer, when remembered or retrieved material must be evaluated before it may steer behavior
6. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when retrieved or recalled material describes one external entity through conflicting observed modes
7. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, when retrieved or recalled material applies pressure to runtime-local boundary state
8. [SRIP-18-CSI](registry/SRIP-18-CSI.md) — Commerce Semantic Integration Layer, when commerce context must be assembled from memory and runtime state

---

## Commerce Stack Sequence

Use this path for commerce-aware runtime behavior:

1. [SRIP-14-RMI](registry/SRIP-14-RMI.md) — retrieval and memory governance
2. [SRIP-18-CSI](registry/SRIP-18-CSI.md) — semantic commerce context assembly
3. [SRIP-12-CDS](registry/SRIP-12-CDS.md) — deterministic commerce decision state

In this stack, CDS remains the deterministic authority for commerce state and transition decisions. CSI supplies bounded semantic context. RMI governs memory and retrieval boundaries used by the assembly process.

This order is conceptual. It does not change the public SRIP numbers.

---

## Runtime Control And Stability Sequence

Use this path for control, drift, stability, and response-shaping behavior:

SRIP-20 and SRIP-22 are governance architecture drafts; SRIP-23 is a research
architecture draft. Their position in this reading path describes conceptual
dependencies, not implementation readiness. Consult
[SRS Specification Classes](specification-classes.md) and the
[SRIP Evidence Matrix](evidence-matrix.md) before making conformance claims.

1. [SRIP-03](srip-03.md) — Drift Metrics and Stabilization Algorithms
2. [SRIP-06](srip-06.md) — Safety and Recursion Boundaries
3. [SRIP-07](srip-07.md) — Symbolic Density Layer
4. [SRIP-08](srip-08.md) — Phase Vector Model and PRM
5. [SRIP-10-AEP](registry/SRIP-10-AEP.md) — Adaptive Entropy Protocol
6. [SRIP-13-RIS](registry/SRIP-13-RIS.md) — Relational Identity Stabilization
7. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when identity/mode separation is needed before contradiction buffering
8. [SRIP-15-ADP](registry/SRIP-15-ADP.md) — Attractor Dynamics and Controlled Perturbation Layer
9. [SRIP-19-RCB](registry/SRIP-19-RCB.md) — Recursive Contradiction Buffering
10. [SRIP-27-TMC](registry/SRIP-27-TMC.md) — Trajectory Membership and Collapse Measurement, when dynamic stability must be separated from target-attractor membership
11. [SRIP-28-TAL](registry/SRIP-28-TAL.md) — Trajectory Admission Loop, when measured candidates require pre-persistence delivery and influence authority
12. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization
13. [SRIP-22-GRC](registry/SRIP-22-GRC.md) — Governance Recursion and Collusion Boundary, when runtime control authority, certification, emergency override, or legitimacy state must be evaluated
14. [SRIP-23-DGL](registry/SRIP-23-DGL.md) — Dialectical Generation Layer, when preserved contradiction and attractor tension may generate non-canonical semantic candidates without deleting the source contradiction
15. [SRIP-16-RSM](registry/SRIP-16-RSM.md) — Recursive Self-Modeling

---

## Multi-Agent And Interoperability Sequence

Use this path for system integration, agent exchange, and multi-agent coordination:

1. [SRIP-05](srip-05.md) — Interoperability Interface
2. [SRIP-24-EIL](registry/SRIP-24-EIL.md) — Environment Interface Layer, when external contact must be classified as observation or effect with source, target, scope, authority, and evidence continuity
3. [SRIP-25-IEM](registry/SRIP-25-IEM.md) — Interaction Event Model, when the semantic unit crossing the environment boundary must be represented independently of transport or tool implementation
4. [SRIP-17-MAE](registry/SRIP-17-MAE.md) — Multi-Agent Exchange
5. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when agent disagreement describes the same external entity through conflicting observed modes
6. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, when exchanged artifacts apply influence or authority pressure to local runtime state
7. [SRIP-19-RCB](registry/SRIP-19-RCB.md) — Recursive Contradiction Buffering, when exchanged evidence or agent disagreement must remain unresolved without forced consensus
8. [SRIP-22-GRC](registry/SRIP-22-GRC.md) — Governance Recursion and Collusion Boundary, when exchanged artifacts carry governance, certification, authority, or marks claims

---

## Governance, Certification, And Legitimacy Sequence

Use this path for governance authority, certification integrity, marks boundary, emergency override, capture visibility, and fork/exit analysis:

1. [SRIP-05](srip-05.md) — Interoperability Interface, for lineage and compatibility boundaries
2. [SRIP-06](srip-06.md) — Safety and Recursion Boundaries, for non-bypassable safety constraints
3. [SRIP-13-RIS](registry/SRIP-13-RIS.md) — Relational Identity Stabilization, for participant and identity-boundary continuity
4. [SRIP-17-MAE](registry/SRIP-17-MAE.md) — Multi-Agent Exchange, for exchanged attestations and agent-origin evidence
5. [SRIP-19-RCB](registry/SRIP-19-RCB.md) — Recursive Contradiction Buffering, for unresolved governance evidence conflicts
6. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, for authority pressure on local runtime state
7. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, for stable identity of governors, authorities, validators, auditors, certification bodies, forks, and legal entities
8. [SRIP-22-GRC](registry/SRIP-22-GRC.md) — Governance Recursion and Collusion Boundary, for legitimacy states, collusion assumptions, capture handling, certification suspension, and fork/exit conditions
9. [SRIP-24-EIL](registry/SRIP-24-EIL.md) — Environment Interface Layer, for external governance surfaces, authority-bearing interaction, evidence continuity, and effect classification
10. [SRIP-25-IEM](registry/SRIP-25-IEM.md) — Interaction Event Model, for event-level evidence, authority, trace, and effect semantics

This sequence does not imply certification or production implementation. It is a review path for public specification readers.

---

## Environment Interaction And Effects Sequence

Use this path when a runtime trajectory receives external material or may affect an external system, store, channel, participant, tool, provider, or governance surface:

1. [SRIP-01](srip-01.md) — Canonical Runtime Loop, for trajectory continuation
2. [SRIP-05](srip-05.md) — Interoperability Interface, for public interface boundaries
3. [SRIP-14-RMI](registry/SRIP-14-RMI.md) — Retrieval and Memory Integration Layer, when retrieval, memory, or persistence is involved
4. [SRIP-26-MIL](registry/SRIP-26-MIL.md) — Memory Influence Layer, when retrieved, remembered, archived, or ledger material may influence behavior
5. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when external participants, agents, sources, or referents must be bound
6. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, when external material applies influence or authority pressure
7. [SRIP-22-GRC](registry/SRIP-22-GRC.md) — Governance Recursion and Collusion Boundary, when authority, legitimacy, certification, or capture boundaries matter
8. [SRIP-24-EIL](registry/SRIP-24-EIL.md) — Environment Interface Layer, for observation/effect classification and evidence-bearing contact with external reality
9. [SRIP-25-IEM](registry/SRIP-25-IEM.md) — Interaction Event Model, for the public semantic unit of boundary-crossing contact

This sequence does not imply certification or production implementation. It is a review path for public specification readers.

---

## Architecture Review Note

SRIPs may be reviewed as architecture design artifacts when they define boundaries, contracts, conformance expectations, risks, non-goals, lifecycle state, and acceptance criteria.

The current non-normative integration review is available through:

- [SRIP Architecture Synthesis](srip-architecture-synthesis.md);
- [SRIP Relationship Matrix](srip-relationship-matrix.md);
- [SRIP Control Precedence Review](srip-control-precedence.md);
- [SRIP Architecture Diagrams](srip-architecture-diagrams.md);
- [SRIP Relationship Evidence Audit](srip-relationship-audit.md).

TOGAF and similar enterprise architecture frameworks may be used as non-normative review lenses. They are not required dependencies for writing, citing, or implementing SRIPs.

The Sigma Runtime Standard remains open-standard-first and framework-independent.
