---
title: SRIP Process
description: Formal definition of the Sigma Runtime Improvement Proposal lifecycle.
published: true
date: 2026-04-17T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:52:16.687Z
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
> [`/legal/IP-Policy`](https://github.com/sigmastratum/documentation/blob/main/legal/ip-policy.md).

---

# Sigma Runtime Improvement Proposal (SRIP) Process

The **SRIP Process** defines how the **Sigma Runtime Standard (SRS)** evolves through transparent, peer-reviewed contributions under the governance of the **Sigma Stratum Research Group (SSRG)**.

Each SRIP represents a proposed modification, extension, or clarification of the Sigma Runtime architecture.  
All accepted SRIPs are versioned, archived, and integrated into the canonical SRS specification, while all revisions and historical proposals are tracked in the **SRIP Registry**.

---

## 1. SRIP Lifecycle

| Stage | Description |
|--------|--------------|
| **1. Draft** | Initial specification authored by contributor(s). Must follow the SRIP template and include motivation, rationale, technical description, and required traceability data. |
| **2. Review** | Technical, conceptual, and information-boundary evaluation by the SSRG Steering Committee, Editorial Board, and designated reviewers. |
| **3. Revision** | Updates made based on reviewer and editor feedback. |
| **4. Approval** | Steering Committee votes to accept, defer, or reject the SRIP. |
| **5. Integration** | Editors merge the approved SRIP into the canonical Sigma Runtime Standard (SRS) branch and execute the required SRD synchronization review. |
| **6. Release** | The change is included in the next official Sigma Runtime Standard version only after the required SRD alignment check is truthful and complete. |

---

## 2. SRIP Numbering and Scope

- Each proposal is assigned an incremental ID (e.g., `SRIP-01`, `SRIP-02`, etc.).  
- `SRIP-00` defines foundational and procedural rules.  
- All subsequent SRIPs reference this base document to ensure interoperability and alignment.  
- Each SRIP must declare whether it introduces **normative** (binding) or **descriptive** (non-binding) content.

All SRIPs beginning with **SRIP-08** and later are tracked through the  
**Sigma Stratum SRIP Registry**, located under `/registry/` in the  
[`sigmastratum/documentation`](https://github.com/sigmastratum/documentation) repository.

This ensures that:
- all proposals, including drafts and superseded versions, remain publicly traceable;  
- archival continuity is maintained between revisions;  
- each SRIP, regardless of status (Draft, Active, or Deprecated), can be cited via a persistent link.

Only **Active** SRIPs are listed in the `/srs/active-srips.md` index,  
while the **Registry** contains the complete historical record.

Publication gate:
- all public SRIP materials must satisfy the [Public–Proprietary Information Boundary Requirements](/team/public-proprietary-information-boundary-requirements.md)
- any approved SRIP with explanatory impact must satisfy the [SRS–SRD Interaction Requirements](/team/srs-srd-interaction-requirements.md) before release alignment is claimed

---

## 3. Mandatory Traceability Data

Every SRIP proposal must include the following minimum traceability data:

- information class: `Open` or `Derived-Public`
- change class: `SRS-only` or `Mixed SRS+SRD`
- affected SRS artifact(s)
- affected SRD artifact(s), if any
- normative impact summary
- SRD synchronization action
- release alignment status

Allowed release alignment status values:

- `aligned`
- `aligned with deferred SRD sync`
- `no public-doc impact`

If a proposal cannot truthfully declare these fields, it is not ready for review.

---

## 4. Submission Guidelines

To submit a new SRIP:

1. Fork the [`sigmastratum/documentation`](https://github.com/sigmastratum/documentation) repository.  
2. Create a new branch named `srip-XX-your-title`.  
3. Draft your proposal following the [`/templates/SRIP-TEMPLATE.md`](https://github.com/sigmastratum/documentation/blob/main/templates/SRIP-TEMPLATE.md).  
4. Include the mandatory traceability and boundary data in the proposal body.  
5. Submit a pull request labeled `SRIP Proposal`.  
6. Engage in open discussion and peer review through the **Issues** or **Discussions** section.  

Upon approval, the SRIP will be merged and tagged for the next release cycle,  
and an archival copy will be stored in the `/registry/` directory.

---

## 5. Review and Oversight

All SRIPs are reviewed by:
- **SSRG Steering Committee** – ensures alignment with architecture and safety principles.  
- **Editorial Board** – verifies structure, clarity, and technical correctness.  
- **Safety Oversight Panel** – evaluates recursive safety, drift tolerance, and boundary implications.  

The Editorial Board must also verify:

- information-boundary compliance,
- SRS/SRD interaction compliance,
- and the truthfulness of the declared release alignment state.

---

## 6. Versioning and Archival

Each accepted SRIP is:
- integrated into the Sigma Runtime Standard (`/srs/`);  
- assessed for required synchronization in the Sigma Runtime Documentation (`/srd/`);  
- mirrored and versioned in the **SRIP Registry** (`/registry/`);  
- assigned a DOI through the **Sigma Stratum Zenodo Registry**; and  
- recorded in the official changelog for traceability.

This two-tier archival system (Active + Registry) ensures that the canonical runtime  
remains lightweight, while the Registry preserves a full evolutionary record  
of all proposals, drafts, and superseded versions.

---

## 7. Repository Control Boundary

The documentation repository is human-write-controlled.

Therefore:

- CI/CD may validate proposals but must not commit or push repository state,
- agents or runtime tooling must not mutate tracked repository state directly or indirectly,
- and final repository writes remain manual, operator-authenticated actions.

This rule applies to SRIP proposals the same way it applies to any other public document.

---

## 8. Principles

The SRIP process ensures:
- **Transparency** — all proposals and discussions are public.  
- **Traceability** — every SRIP has a unique ID, version, and DOI.  
- **Integrity** — normative changes require explicit review and approval.  
- **Continuity** — all revisions preserve interoperability across runtime versions.  

---

## 9. Contact

For general inquiries or submissions:  
**contact@sigmastratum.org**

**legal@sigmastratum.org**

---

**Summary:**  
The SRIP Process provides a structured path for the evolution of the Sigma Runtime Standard — ensuring every architectural change is transparent, reviewed, archived, and permanently recorded in the **Sigma Stratum Registry** as part of the open standard framework.
