---
title: SRIP Process
description: Formal definition of the Sigma Runtime Improvement Proposal lifecycle.
published: true
date: 2026-05-14T00:00:00.000Z
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
| **0. Candidate** | Intake proposal before public numbering or public draft acceptance. Used for external or early architectural proposals that still require boundary, scope, and related-spec review. |
| **1. Formation Draft v0.1** | Initial specification authored by contributor(s). Must follow the SRIP template and include motivation, rationale, technical description, and required traceability data. |
| **2. Public Draft v0.2+** | Public-review-ready draft with normalized metadata, public boundary classification, non-goals, conformance scope, and truthful SRD synchronization state. |
| **3. Implementation-Ready Architecture** | Public draft mature enough to guide implementation planning. Requires layer boundary, contracts, conformance expectations, risk boundaries, and acceptance criteria. It does not claim that implementation already exists. |
| **4. Active Proposal** | Steering Committee accepts the SRIP as an active normative proposal. |
| **5. Partial Implementation** | One or more implementations satisfy a bounded subset of the SRIP while full conformance remains open. |
| **6. Aligned** | Public SRS/SRD synchronization is complete or truthfully declared as aligned for the approved release state. |
| **7. Superseded / Deprecated** | Historical state for proposals replaced or retired by later SRIPs while preserving persistent references. |

---

## 1A. Draft Advancement Pipeline

The SRIP draft pipeline separates private or editorial formation from a public
registry draft.

### Draft v0.1 — Formation Draft

`Draft v0.1` is the formation stage. It may exist as an authoring draft,
editorial intake, or registry candidate, but it is not yet a public-review-ready
SRIP.

Before advancement, the draft must pass:

1. information-boundary classification as `Open` or `Derived-Public`;
2. SRS/SRD impact classification as `SRS-only`, `SRD-only`, or `Mixed SRS+SRD`;
3. affected-artifact identification;
4. normative-impact summary;
5. SRD synchronization decision;
6. release-alignment status declaration.

If these fields are missing or not truthful, the draft must remain at `v0.1`.

### Public Draft v0.2+

`Public Draft v0.2` is the first public-review-ready version.

To advance from `v0.1` to `Public Draft v0.2`, editors must ensure that:

- the document has the public license notice;
- metadata is normalized and complete;
- the information class is publishable;
- the change class is not ambiguous;
- normative language is separated from explanatory SRD content;
- any required SRD synchronization is completed or explicitly deferred;
- conformance scope and non-goals are present;
- implementation maturity is not overclaimed;
- release alignment is truthful.

After `Public Draft v0.2`, later draft versions may refine terminology,
conformance, examples, or synchronization evidence, but they must not remove the
traceability fields.

Publication rule:

- a `v0.1` draft may be discussed or reviewed internally;
- a `Public Draft v0.2+` draft may be cited as a public SRIP draft;
- an `Active` SRIP still requires the normal approval and integration stages.

---

## 2. SRIP Numbering and Scope

- Each proposal is assigned an incremental ID (e.g., `SRIP-01`, `SRIP-02`, etc.).
- `SRIP-00` defines foundational and procedural rules.
- All subsequent SRIPs reference this base document to ensure interoperability and alignment.
- Each SRIP must declare whether it introduces **normative** (binding) or **descriptive** (non-binding) content.

SRIP numbers are immutable proposal identifiers.

Numbering rules:

- numbers are assigned monotonically after a proposal is accepted into the public draft path;
- numbers are not reassigned to preserve logical reading order;
- published SRIP numbers are never changed after citation;
- dependency order, implementation order, and reader navigation are handled by indexes and architecture reading-order views, not by renumbering;
- a candidate may be tracked without a final number until boundary and scope review are complete.

This means a later-numbered SRIP may logically precede an earlier-numbered SRIP in a particular architecture stack. The number records proposal history; the reading-order index records conceptual navigation.

All SRIPs beginning with **SRIP-09** and later are tracked through the
**Sigma Stratum SRIP Registry**, located under `/srs/registry/` in the
[`sigmastratum/documentation`](https://github.com/sigmastratum/documentation) repository.

This ensures that:
- all proposals, including drafts and superseded versions, remain publicly traceable;
- archival continuity is maintained between revisions;
- each SRIP, regardless of lifecycle stage, can be cited via a persistent link after public draft acceptance.

Publicly relevant active, draft, and implementation-ready proposals are listed in the `/srs/active-srips.md` index, while the **Registry** contains the complete historical record.

Publication gate:
- all public SRIP materials must satisfy the [Public–Proprietary Information Boundary Requirements](/team/public-proprietary-information-boundary-requirements.md)
- any approved SRIP with explanatory impact must satisfy the [SRS–SRD Interaction Requirements](/team/srs-srd-interaction-requirements.md) before release alignment is claimed

---

## 2A. Architecture Classification and Reading Order

Each SRIP should declare or be classified by:

- `Track`: foundational, runtime-control, memory-retrieval, commerce, multi-agent, observability, safety, privacy, governance, or another named track;
- `Architecture Layer`: business, data, application, runtime, control, integration, telemetry, or governance;
- `Extends`: SRIPs whose contract is extended;
- `Amends`: SRIPs whose normative contract is changed;
- `Supersedes`: SRIPs replaced by the proposal;
- `Parent Specs`: mandatory normative dependencies;
- `Related Specs`: relevant but non-parent specifications.

Architecture reading order is maintained separately from numerical order.

Recommended public navigation views:

- numerical registry;
- foundational sequence;
- runtime-control sequence;
- memory and retrieval sequence;
- commerce stack sequence;
- multi-agent and interoperability sequence.

For example, a commerce implementation may be easier to read as:

1. RMI - retrieval and memory governance;
2. CSI - commerce semantic integration;
3. CDS - deterministic commerce decision state.

This does not require renumbering any SRIP.

---

## 2B. Architecture Review and TOGAF Compatibility

SRIPs may function as architecture design artifacts when they define:

- layer boundary;
- contracts or interfaces;
- conformance expectations;
- non-goals;
- risk boundaries;
- lifecycle and acceptance criteria;
- synchronization impact with SRD.

The SRIP process is open-standard-first and framework-independent.

TOGAF or similar enterprise-architecture methods may be used as a non-normative review lens. They are not binding dependencies for writing, reviewing, citing, or implementing SRIPs.

Architecture-impacting SRIPs should be reviewable across:

- business impact;
- data impact;
- application/runtime impact;
- technology assumptions;
- governance, risk, and conformance impact.

This compatibility discipline helps reviewers identify gaps without making the Sigma Runtime Standard dependent on TOGAF terminology, certification, or process.

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
and an archival copy will be stored in the `/srs/registry/` directory.

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
- mirrored and versioned in the **SRIP Registry** (`/srs/registry/`);
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
