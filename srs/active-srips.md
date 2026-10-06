---
title: Active SRIPs — Sigma Runtime Standard
description: Public index of the active Sigma Runtime Improvement Proposal surface, including foundational SRIPs and later registry proposals.
published: true
date: 2026-07-17T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-12-28T09:46:38.133Z
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

# Active SRIPs — Sigma Runtime Standard

This page indexes the currently active public `SRIP` surface.

It is intentionally version-light.
Readers should use this page as a public navigation layer, while consulting each individual SRIP for its own exact status, date, and scope.

## Licensing And Conformance Summary

SRS/SRIP documents are part of the Sigma Runtime Standard public specification layer.

Independent implementation of public SRS/SRIP normative requirements is permitted under the public specification terms.

Independent implementations are welcome. Sigma Runtime product assets, official certification, Sigma marks, white-label deployment, managed Sigma deployment, resale, and CC BY-NC commercial use use their own published policies or written terms.

References:

- [SRS Public Specification License](/legal/srs-public-specification-license)
- [Sigma IP, Licensing, and Certification Policy](/legal/ip-licensing-certification-policy)
- [SRS Conformance](/srs/conformance/)
- [SRS Metric Registry](/srs/metric-registry)
- [SRS Specification Classes](/srs/specification-classes)
- [SRIP Evidence Matrix](/srs/evidence-matrix)

---

## Foundational SRIPs

| ID | Title | Category | Stage |
|----|--------|-----------|--------|
| [SRIP-00](/srs/srip-00) | **Foundations & Scope** | Foundational | Consult document header |
| [SRIP-01](/srs/srip-01) | **Canonical Runtime Loop** | Architectural / Runtime | Consult document header |
| [SRIP-02](/srs/srip-02) | **Attractor State Model & Metadata** | Cognitive Architecture | Consult document header |
| [SRIP-03](/srs/srip-03) | **Drift Metrics & Stabilization Algorithms** | Metrics / Coherence | Consult document header |
| [SRIP-04](/srs/srip-04) | **Memory Layer Architecture** | Memory / Continuity | Consult document header |
| [SRIP-05](/srs/srip-05) | **Interoperability Interface** | Communication / API | Consult document header |
| [SRIP-06](/srs/srip-06) | **Safety & Recursion Boundaries** | Alignment / Safety | Consult document header |
| [SRIP-07](/srs/srip-07) | **Symbolic Density Layer** | Semantic Dynamics | Consult document header |
| [SRIP-08](/srs/srip-08) | **Phase Vector Model & PRM** | Control / Telemetry | Consult document header |

---

## Registry Proposals And Extensions

Later proposals and extensions are tracked in the public registry:

| SRIP | Title | Public status |
|------|--------|---------------|
| [SRIP-09-LTM](/srs/registry/SRIP-09-LTM) | Long-Term Memory and Structural Coherence Layer | Consult document header |
| [SRIP-10-AEP](/srs/registry/SRIP-10-AEP) | Adaptive Entropy Protocol | Consult document header |
| [SRIP-11-SMC](/srs/registry/SRIP-11-SMC) | Structural Memory Compression | Consult document header; legacy CMT redirect retained |
| [SRIP-12-CDS](/srs/registry/SRIP-12-CDS) | Commerce Decision State Layer | Consult document header |
| [SRIP-13-RIS](/srs/registry/SRIP-13-RIS) | Relational Identity Stabilization | Consult document header |
| [SRIP-14-RMI](/srs/registry/SRIP-14-RMI) | Retrieval and Memory Integration Layer | Consult document header |
| [SRIP-15-ADP](/srs/registry/SRIP-15-ADP) | Attractor Dynamics and Controlled Perturbation Layer | Consult document header |
| [SRIP-16-RSM](/srs/registry/SRIP-16-RSM) | Recursive Self-Modeling | Consult document header |
| [SRIP-17-MAE](/srs/registry/SRIP-17-MAE) | Multi-Agent Exchange | Consult document header |
| [SRIP-18-CSI](/srs/registry/SRIP-18-CSI) | Commerce Semantic Integration Layer | Consult document header |
| [SRIP-19-RCB](/srs/registry/SRIP-19-RCB) | Recursive Contradiction Buffering | Consult document header |
| [SRIP-20-ANS](/srs/registry/SRIP-20-ANS) | Autonomy Negotiation and Boundary Stabilization | Governance Architecture Draft |
| [SRIP-21-EIB](/srs/registry/SRIP-21-EIB) | External Identity Binding and Mode Reconciliation | Consult document header |
| [SRIP-22-GRC](/srs/registry/SRIP-22-GRC) | Governance Recursion and Collusion Boundary | Governance Architecture Draft |
| [SRIP-23-DGL](/srs/registry/SRIP-23-DGL) | Dialectical Generation Layer | Research Architecture Draft |
| [SRIP-24-EIL](/srs/registry/SRIP-24-EIL) | Environment Interface Layer | Consult document header |
| [SRIP-25-IEM](/srs/registry/SRIP-25-IEM) | Interaction Event Model | Consult document header |
| [SRIP-26-MIL](/srs/registry/SRIP-26-MIL) | Memory Influence Layer | Consult document header |
| [SRIP-27-TMC](/srs/registry/SRIP-27-TMC) | Trajectory Membership and Collapse Measurement | Consult document header |
| [SRIP-28-TAL](/srs/registry/SRIP-28-TAL) | Trajectory Admission Loop | Consult document header |

Deprecated or superseded entries remain traceable through the registry as part of the public historical record.

---

## Governance Notes

- `SRIP` changes must follow the [`/team/srip-process.md`](/team/srip-process.md).
- Numerical order is historical. Conceptual reading order is maintained in [`/srs/architecture-reading-order`](/srs/architecture-reading-order).
- Normative changes with explanatory impact must satisfy the [`/team/srs-srd-interaction-requirements.md`](/team/srs-srd-interaction-requirements.md).
- Public artifacts must satisfy the [`/team/public-proprietary-information-boundary-requirements.md`](/team/public-proprietary-information-boundary-requirements.md).
- Release alignment claims must remain truthful if `SRD` synchronization is still pending.

---

## Reference

> Tsaliev, E. (2025). **Sigma Runtime Standard v0.1** — *Attractor-Based Cognitive Architecture for Long-Horizon Reasoning*
> DOI: [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)
