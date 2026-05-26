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

For the authoritative numerical registry, see [`/srs/registry`](/srs/registry).

## Certification Boundary

This reading order is not a certification claim.

Reading or implementing SRS/SRIP documents does not imply official Sigma certification, endorsement, or use of Sigma marks.

For conformance terminology, see [`/srs/conformance/`](/srs/conformance/).

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

1. [SRIP-00](/srs/srip-00) — Foundations and Scope
2. [SRIP-01](/srs/srip-01) — Canonical Runtime Loop
3. [SRIP-02](/srs/srip-02) — Attractor State Model and Metadata
4. [SRIP-03](/srs/srip-03) — Drift Metrics and Stabilization Algorithms
5. [SRIP-04](/srs/srip-04) — Memory Layer Architecture
6. [SRIP-05](/srs/srip-05) — Interoperability Interface
7. [SRIP-06](/srs/srip-06) — Safety and Recursion Boundaries
8. [SRIP-07](/srs/srip-07) — Symbolic Density Layer
9. [SRIP-08](/srs/srip-08) — Phase Vector Model and PRM

---

## Memory And Retrieval Sequence

Use this path for long-running memory, retrieval, and recall behavior:

1. [SRIP-04](/srs/srip-04) — Memory Layer Architecture
2. [SRIP-09-LTM](/srs/registry/SRIP-09-LTM) — Long-Term Memory and Structural Coherence Layer
3. [SRIP-11-CMT](/srs/registry/SRIP-11-CMT) — Compression and Memory Topology
4. [SRIP-14-RMI](/srs/registry/SRIP-14-RMI) — Retrieval and Memory Integration Layer
5. [SRIP-20-ANS](/srs/registry/SRIP-20-ANS) — Autonomy Negotiation and Boundary Stabilization, when retrieved or recalled material applies pressure to runtime-local boundary state
6. [SRIP-18-CSI](/srs/registry/SRIP-18-CSI) — Commerce Semantic Integration Layer, when commerce context must be assembled from memory and runtime state

---

## Commerce Stack Sequence

Use this path for commerce-aware runtime behavior:

1. [SRIP-14-RMI](/srs/registry/SRIP-14-RMI) — retrieval and memory governance
2. [SRIP-18-CSI](/srs/registry/SRIP-18-CSI) — semantic commerce context assembly
3. [SRIP-12-CDS](/srs/registry/SRIP-12-CDS) — deterministic commerce decision state

In this stack, CDS remains the deterministic authority for commerce state and transition decisions. CSI supplies bounded semantic context. RMI governs memory and retrieval boundaries used by the assembly process.

This order is conceptual. It does not change the public SRIP numbers.

---

## Runtime Control And Stability Sequence

Use this path for control, drift, stability, and response-shaping behavior:

1. [SRIP-03](/srs/srip-03) — Drift Metrics and Stabilization Algorithms
2. [SRIP-06](/srs/srip-06) — Safety and Recursion Boundaries
3. [SRIP-07](/srs/srip-07) — Symbolic Density Layer
4. [SRIP-08](/srs/srip-08) — Phase Vector Model and PRM
5. [SRIP-10-AEP](/srs/registry/SRIP-10-AEP) — Adaptive Entropy Protocol
6. [SRIP-13-RIS](/srs/registry/SRIP-13-RIS) — Relational Identity Stabilization
7. [SRIP-15-ADP](/srs/registry/SRIP-15-ADP) — Attractor Dynamics and Controlled Perturbation Layer
8. [SRIP-19-RCB](/srs/registry/SRIP-19-RCB) — Recursive Contradiction Buffering
9. [SRIP-20-ANS](/srs/registry/SRIP-20-ANS) — Autonomy Negotiation and Boundary Stabilization
10. [SRIP-16-RSM](/srs/registry/SRIP-16-RSM) — Recursive Self-Modeling

---

## Multi-Agent And Interoperability Sequence

Use this path for system integration, agent exchange, and multi-agent coordination:

1. [SRIP-05](/srs/srip-05) — Interoperability Interface
2. [SRIP-17-MAE](/srs/registry/SRIP-17-MAE) — Multi-Agent Exchange
3. [SRIP-20-ANS](/srs/registry/SRIP-20-ANS) — Autonomy Negotiation and Boundary Stabilization, when exchanged artifacts apply influence or authority pressure to local runtime state
4. [SRIP-19-RCB](/srs/registry/SRIP-19-RCB) — Recursive Contradiction Buffering, when exchanged evidence or agent disagreement must remain unresolved without forced consensus

---

## Architecture Review Note

SRIPs may be reviewed as architecture design artifacts when they define boundaries, contracts, conformance expectations, risks, non-goals, lifecycle state, and acceptance criteria.

TOGAF and similar enterprise architecture frameworks may be used as non-normative review lenses. They are not required dependencies for writing, citing, or implementing SRIPs.

The Sigma Runtime Standard remains open-standard-first and framework-independent.
