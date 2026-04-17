---
title: SRS–SRD Interaction Requirements
description: Mandatory process requirements for changes that interact with the Sigma Runtime Standard and the Sigma Runtime Documentation set.
published: true
date: 2026-04-15T22:30:00.000Z
tags:
editor: markdown
dateCreated: 2026-04-15T22:30:00.000Z
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

# SRS–SRD Interaction Requirements

This document defines the mandatory process for:
- interacting with the **Sigma Runtime Standard (SRS)**
- updating the **Sigma Runtime Documentation set (SRD)**
- keeping both layers synchronized when a change affects runtime semantics, architecture, safety, or explanatory documentation

This is a process requirement.
It does not replace the [`/team/srip-process.md`](https://github.com/sigmastratum/documentation/blob/main/team/srip-process.md) or the [`/team/contribution-process.md`](https://github.com/sigmastratum/documentation/blob/main/team/contribution-process.md).
It binds them together.

This requirement is subordinate to the information-boundary gate defined in:
- [`/team/public-proprietary-information-boundary-requirements.md`](https://github.com/sigmastratum/documentation/blob/main/team/public-proprietary-information-boundary-requirements.md)

---

## 1. Purpose

The repository contains two distinct but linked layers:

- **SRS** = normative standard and binding runtime semantics
- **SRD** = descriptive, explanatory, architectural, and educational documentation

The purpose of this requirement is to ensure that:
- SRS changes do not leave SRD materially outdated
- SRD changes do not silently redefine SRS semantics
- mixed changes remain traceable from proposal through release
- only publishable public-safe information enters the external documentation corpus

---

## 2. Canonical Rule

### 2.1 Source-of-truth rule

- **SRS is authoritative for normative runtime semantics**
- **SRD is authoritative for explanation, interpretation, and conceptual presentation**

### 2.2 Prohibition rule

SRD **must not** introduce new binding runtime requirements unless those requirements are already accepted in SRS or are being proposed through the SRIP path.

### 2.3 Alignment rule

Whenever SRS changes affect concepts explained in SRD, the SRD update **must** be assessed, tracked, and completed before the next release that claims alignment.

---

## 3. Change Classification Requirements

Every proposed change **must** be classified before review begins.

Allowed classes:

- **SRD-only**
  - descriptive clarification
  - editorial improvement
  - architectural explanation without normative change

- **SRS-only**
  - normative change with no current explanatory impact outside the standard layer

- **Mixed SRS+SRD**
  - normative change that also changes how the runtime must be explained, taught, or presented

A contributor **must** declare one of these classes in the proposal, issue, or pull request summary.

---

## 4. Interaction With SRS

When a change interacts with SRS, the contributor **must** identify:

1. affected SRS document or SRIP
2. whether the change is normative, descriptive, or mixed
3. whether the change requires:
   - a new SRIP
   - an amendment to an existing SRIP
   - only an editorial clarification

The following changes **must** go through the SRIP path:

- changes to canonical runtime loop semantics
- changes to attractor or drift definitions
- changes to memory-layer behavior or interoperability semantics
- changes to safety boundaries, alignment envelopes, or normative terminology
- changes that alter conformance expectations for implementations

---

## 5. SRD Update Requirements

When a change affects SRD, the contributor or editor **must** identify:

1. affected SRD pages
2. whether the current SRD language is still aligned
3. whether the update is:
   - immediate in the same change set
   - deferred but linked to an approved follow-up before release

SRD updates are required when an approved SRS change modifies:

- conceptual definitions
- architecture diagrams or layer descriptions
- safety explanation
- operational expectations
- terminology used by readers to interpret the standard

If an SRD page is knowingly behind SRS, it **must** be marked and tracked as pending synchronization in the review record.

---

## 6. Mandatory Process Flow

All mixed or SRS-interacting changes **must** follow this flow:

### Stage 0. Information Boundary Review

- classify the source material using the [Public–Proprietary Information Boundary Requirements](/team/public-proprietary-information-boundary-requirements.md)
- confirm that the contribution is `Open` or `Derived-Public`
- if the source is proprietary, sanitize and abstract it before SRS or SRD review continues

### Stage 1. Intake

- capture the change idea
- classify it as `SRD-only`, `SRS-only`, or `Mixed SRS+SRD`

### Stage 2. Impact Assessment

- identify affected SRS artifacts
- identify affected SRD artifacts
- decide whether SRIP is required

### Stage 3. Normative Path

- if the change is normative, open or amend the relevant SRIP path
- do not merge the normative claim directly into SRD as if it were already accepted

### Stage 4. Editorial Synchronization Plan

- define which SRD pages must change
- define whether those pages will be updated in the same PR or a linked follow-up

### Stage 5. Review

- Steering Committee reviews normative impact
- Editorial Board reviews structure, traceability, and SRD synchronization

### Stage 6. Integration

- merge the SRS change through the approved path
- merge the SRD synchronization update
- record any deferred synchronization explicitly

### Stage 7. Release Readiness

A release **must not** claim SRS/SRD alignment unless:

- accepted SRS changes have completed their required SRD updates
- or the remaining gaps are explicitly declared and accepted by the Editorial Board

---

## 7. Required Traceability Data

Any mixed or SRS-interacting contribution **must** include the following minimum traceability data:

- change class
- affected SRS document(s) or SRIP(s)
- affected SRD document(s)
- normative impact summary
- SRD synchronization action
- release target or follow-up target

Recommended format:

| Field | Required content |
| --- | --- |
| Change class | `SRD-only` / `SRS-only` / `Mixed SRS+SRD` |
| SRS impact | affected SRIP or SRS section |
| SRD impact | affected explanatory pages |
| Approval path | editorial review or SRIP review |
| Sync action | same PR or linked follow-up |
| Release note | aligned / pending-sync |

---

## 8. Responsibilities

### Contributors

Contributors **must**:
- classify the change correctly
- avoid placing new normative requirements only in SRD
- declare the SRD impact for any SRS-affecting change

### Editorial Board

The Editorial Board **must**:
- enforce the interaction requirements during review
- reject merges that create silent SRS/SRD drift
- maintain the repository’s traceability and alignment claims

### Steering Committee

The Steering Committee **must**:
- decide normative approval for SRIP-driven changes
- ensure that approved standard changes are not represented inaccurately in SRD

---

## 9. Acceptance Rules

A contribution is compliant with this requirement only if:

1. its change class is explicit
2. its SRS interaction is explicit when relevant
3. its SRD impact is explicit when relevant
4. normative content is not smuggled into SRD without SRIP handling
5. release alignment claims remain truthful

---

## 10. Summary

This requirement establishes one governing principle:

**SRS defines what is binding. SRD explains what is binding.**

Therefore:
- SRS cannot evolve without SRD impact review
- SRD cannot redefine SRS by implication
- mixed changes must remain traceable from proposal to release
