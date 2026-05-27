---
title: SRIP Architecture Reading Order
description: Conceptual reading-order view for Sigma Runtime Improvement Proposals across architecture stacks.
published: true
date: 2026-05-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-05-14T00:00:00.000Z
---

> **Sigma Stratum Documentation – License Notice**
> This document is part of the **Sigma Runtime Standard (SRS)** and the
> **Sigma Stratum Documentation Set (SRD)**.
>
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0
> (CC BY-NC 4.0)**.
>
> The license for this specific document is authoritative.
> For the full framework, see
> [`/legal/IP-Policy`](https://sigmastratum.org/legal/ip-policy).

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
3. [SRIP-11-CMT](registry/SRIP-11-CMT.md) — Compression and Memory Topology
4. [SRIP-14-RMI](registry/SRIP-14-RMI.md) — Retrieval and Memory Integration Layer
5. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when retrieved or recalled material describes one external entity through conflicting observed modes
6. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, when retrieved or recalled material applies pressure to runtime-local boundary state
7. [SRIP-18-CSI](registry/SRIP-18-CSI.md) — Commerce Semantic Integration Layer, when commerce context must be assembled from memory and runtime state

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

1. [SRIP-03](srip-03.md) — Drift Metrics and Stabilization Algorithms
2. [SRIP-06](srip-06.md) — Safety and Recursion Boundaries
3. [SRIP-07](srip-07.md) — Symbolic Density Layer
4. [SRIP-08](srip-08.md) — Phase Vector Model and PRM
5. [SRIP-10-AEP](registry/SRIP-10-AEP.md) — Adaptive Entropy Protocol
6. [SRIP-13-RIS](registry/SRIP-13-RIS.md) — Relational Identity Stabilization
7. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when identity/mode separation is needed before contradiction buffering
8. [SRIP-15-ADP](registry/SRIP-15-ADP.md) — Attractor Dynamics and Controlled Perturbation Layer
9. [SRIP-19-RCB](registry/SRIP-19-RCB.md) — Recursive Contradiction Buffering
10. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization
11. [SRIP-16-RSM](registry/SRIP-16-RSM.md) — Recursive Self-Modeling

---

## Multi-Agent And Interoperability Sequence

Use this path for system integration, agent exchange, and multi-agent coordination:

1. [SRIP-05](srip-05.md) — Interoperability Interface
2. [SRIP-17-MAE](registry/SRIP-17-MAE.md) — Multi-Agent Exchange
3. [SRIP-21-EIB](registry/SRIP-21-EIB.md) — External Identity Binding and Mode Reconciliation, when agent disagreement describes the same external entity through conflicting observed modes
4. [SRIP-20-ANS](registry/SRIP-20-ANS.md) — Autonomy Negotiation and Boundary Stabilization, when exchanged artifacts apply influence or authority pressure to local runtime state
5. [SRIP-19-RCB](registry/SRIP-19-RCB.md) — Recursive Contradiction Buffering, when exchanged evidence or agent disagreement must remain unresolved without forced consensus

---

## Architecture Review Note

SRIPs may be reviewed as architecture design artifacts when they define boundaries, contracts, conformance expectations, risks, non-goals, lifecycle state, and acceptance criteria.

TOGAF and similar enterprise architecture frameworks may be used as non-normative review lenses. They are not required dependencies for writing, citing, or implementing SRIPs.

The Sigma Runtime Standard remains open-standard-first and framework-independent.
