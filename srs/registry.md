---
title: Sigma Stratum Registry
description: Authoritative registry tracking post-core Sigma Runtime Improvement Proposals (SRIP-09+) — experimental extensions, governance updates, and long-term evolution of the Sigma Runtime architecture.
published: true
date: 2026-05-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-12-31T09:55:42.132Z
---

> **Sigma Stratum Documentation - Public Specification Notice**
> This document is part of the **Sigma Runtime Standard (SRS)** public
> specification registry and the **Sigma Stratum Documentation Set (SRD)**.
>
> Independent implementation of public SRS/SRIP normative requirements is
> permitted under the applicable public specification terms.
>
> This registry does not license Sigma Runtime proprietary product assets,
> official certification, Sigma marks, white-label deployment, resale, managed
> Sigma Runtime deployment, enterprise deployment assets, or commercial use of
> CC BY-NC materials without separate authorization.
>
> For the active policy layer, see [Sigma IP, Licensing, and Certification
> Policy](/legal/ip-licensing-certification-policy) and [SRS Public
> Specification License](/legal/srs-public-specification-license).

# Sigma Stratum Registry

The **Sigma Stratum Registry** is the authoritative ledger for runtime proposals **beyond the core specification** (SRIP-09 and later).
It records extensions, experimental modules, and structural evolutions of the Sigma Runtime architecture.

---

## Purpose

This registry ensures:
- Transparent tracking of **active and evolving SRIPs**
- Version control and compatibility mapping with **SRS-03 Core**
- Reference linkage to **Zenodo DOIs** and **governance decisions**
- Persistent identifiers for each experimental proposal

All documents registered here form the **living layer** of the Sigma Runtime Standard public specification - a space where research evolves while preserving versioned specification lineage.

---

## Structure

Each SRIP is registered as a standalone entry:
```
/srs/registry/SRIP-09-LTM.md
/srs/registry/SRIP-10-AEP.md
/srs/registry/SRIP-11-CMT.md
/srs/registry/SRIP-12-CDS.md
/srs/registry/SRIP-13-RIS.md
/srs/registry/SRIP-14-RMI.md
/srs/registry/SRIP-15-ADP.md
/srs/registry/SRIP-16-RSM.md
/srs/registry/SRIP-17-MAE.md
/srs/registry/SRIP-18-CSI.md
/srs/registry/SRIP-19-RCB.md
/srs/registry/SRIP-20-ANS.md
```
Each file must include:
- metadata block including title, version, date, status, author, information class, change class, parent specs, related specs, and release alignment status;
- summary of purpose and architecture;
- compatibility notes with prior SRIPs and SRS versions;
- license declaration.

---

## Numbering And Reading Order

SRIP numbers are immutable public proposal identifiers.

The registry is numerical and historical. It is not required to match the best conceptual reading order for a given architecture stack.

Rules:

- new SRIP numbers are assigned monotonically when a proposal is accepted into the public draft path;
- existing SRIP numbers are never reassigned to improve logical ordering;
- conceptual ordering is maintained in reading-order views such as `/srs/architecture-reading-order`;
- `Parent Specs`, `Related Specs`, `Extends`, `Amends`, and `Supersedes` describe architecture relationships.

This allows the standard to scale without breaking citations or historical continuity.

---

## Active Registry Entries

| SRIP | Title | Status | Date | Maintainer |
|------|--------|---------|------|-------------|
| [SRIP-09-LTM](/srs/registry/SRIP-09-LTM) | Long-Term Memory and Structural Coherence Layer (LTM-SC) | **Active Proposal / Partial Implementation** | 2026-04-11 | SSRG |
| [SRIP-10-AEP](/srs/registry/SRIP-10-AEP) | Adaptive Entropy Protocol (AEP) | **Public Draft v0.2 / Partial Implementation** | 2026-05-20 | SSRG |
| [SRIP-11-CMT](/srs/registry/SRIP-11-CMT) | Compression & Memory Topology (CMT) | **Active (v0.5.3)** | 2026-02-04 | SSRG |
| [SRIP-12-CDS](/srs/registry/SRIP-12-CDS) | Commerce Decision State Layer (CDS) | **Draft / Implementation Pending** | 2026-04-11 | SSRG |
| [SRIP-13-RIS](/srs/registry/SRIP-13-RIS) | Relational Identity Stabilization (RIS) | **Active Proposal** | 2026-04-11 | SSRG |
| [SRIP-14-RMI](/srs/registry/SRIP-14-RMI) | Retrieval and Memory Integration Layer (RMI) | **Active Proposal / Partial Implementation** | 2026-04-28 | SSRG |
| [SRIP-15-ADP](/srs/registry/SRIP-15-ADP) | Attractor Dynamics and Controlled Perturbation Layer (ADP) | **Public Draft** | 2026-04-28 | SSRG |
| [SRIP-16-RSM](/srs/registry/SRIP-16-RSM) | Recursive Self-Modeling (RSM) | **Public Draft** | 2026-05-14 | SSRG |
| [SRIP-17-MAE](/srs/registry/SRIP-17-MAE) | Multi-Agent Exchange (MAE) | **Public Draft** | 2026-05-14 | SSRG |
| [SRIP-18-CSI](/srs/registry/SRIP-18-CSI) | Commerce Semantic Integration Layer (CSI) | **Public Draft / Implementation-Ready Architecture** | 2026-05-14 | SSRG |
| [SRIP-19-RCB](/srs/registry/SRIP-19-RCB) | Recursive Contradiction Buffering (RCB) | **Public Draft** | 2026-05-21 | SSRG |
| [SRIP-20-ANS](/srs/registry/SRIP-20-ANS) | Autonomy Negotiation and Boundary Stabilization (ANS) | **Public Draft** | 2026-05-26 | SSRG |

---

## Deprecated Registry Entries

| SRIP | Title | Status | Date | Maintainer |
|------|--------|---------|------|-------------|
| [SRIP-10-ACE](/srs/registry/SRIP-10-ACE) | Anti-Crystallization Equilibrium Model (ACE) | **Deprecated (Superseded by AEP)** | 2026-01-07 | SSRG |

### Governance

Registry entries are maintained by the **Sigma Stratum Research Group (SSRG)**.

For conceptual navigation, see:

- [`/srs/architecture-reading-order`](/srs/architecture-reading-order)

For inquiries or submissions:
[contact@sigmastratum.org](mailto:contact@sigmastratum.org)
[github.com/sigmastratum/documentation](https://github.com/sigmastratum/documentation)
