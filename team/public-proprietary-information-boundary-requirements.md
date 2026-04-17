---
title: Public–Proprietary Information Boundary Requirements
description: Mandatory requirements for separating open documentation content from proprietary internal material before publication in SRS or SRD.
published: true
date: 2026-04-15T22:45:00.000Z
tags:
editor: markdown
dateCreated: 2026-04-15T22:45:00.000Z
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

# Public–Proprietary Information Boundary Requirements

This document defines the mandatory information-boundary policy for all materials considered for publication in:

- **SRS** — Sigma Runtime Standard
- **SRD** — Sigma Runtime Documentation
- **SRIP** proposals and related public review artifacts

This requirement exists because the `documentation` repository is a **public external corpus**.

---

## 1. Purpose

The Sigma Stratum program contains both:

- **open standard knowledge** that must remain public
- **proprietary implementation knowledge** that must remain internal

The purpose of this requirement is to ensure that public documentation:

- preserves the open standard
- does not leak internal implementation assets or confidential operations
- can still publish truthful architectural and normative material through controlled abstraction

---

## 2. Canonical Boundary Rule

Before any material is added to SRS, SRD, or SRIP review artifacts, it **must** be classified as one of:

- **Open**
- **Proprietary**
- **Derived-Public**

Only **Open** or **Derived-Public** material may be published in this repository.

**Proprietary** material must remain outside the public documentation set.

---

## 3. Classification Definitions

### 3.1 Open

Open material may be published directly.

Typical examples:

- normative runtime semantics
- public architectural concepts
- public safety principles
- public terminology and conformance rules
- public research framing
- sanitized examples that do not expose internal assets

### 3.2 Proprietary

Proprietary material must not be published directly in SRS or SRD.

Typical examples:

- internal research builds and non-public runtime revisions
- deployment topology, infrastructure details, and private recovery procedures
- secrets, credentials, tokens, keys, and private endpoints
- internal prompts, unpublished control overlays, and non-public configuration bundles
- customer, partner, operator, or internal user data
- internal evaluation corpora, raw experiment logs, and sensitive benchmark artifacts when not approved for public release
- unpublished implementation strategies that are intentionally kept outside the open standard

### 3.3 Derived-Public

Derived-Public material is public-safe content derived from proprietary or mixed internal sources.

It may be published only after abstraction and sanitization.

Typical examples:

- a public architectural pattern derived from internal implementation experience
- a normative requirement extracted from a private build without exposing the build itself
- a generalized incident lesson without secrets, host details, or internal-only operational steps

---

## 4. Publication Rules

### 4.1 SRS publication rule

SRS may publish:

- normative semantics
- interfaces
- invariants
- conformance rules
- safety envelopes

SRS must not publish unnecessary proprietary implementation detail merely because that detail exists internally.

### 4.2 SRD publication rule

SRD may publish:

- conceptual explanations
- diagrams
- rationale
- educational architecture narratives
- generalized operational lessons

SRD must not be used as a side channel for leaking proprietary internals that are excluded from SRS.

### 4.3 SRIP publication rule

SRIP proposals may reference proprietary origin context, but the public artifact must contain only:

- the publishable requirement
- the publishable rationale
- the publishable technical abstraction

If the proposal depends on proprietary evidence, that evidence must be summarized as **Derived-Public** rather than copied verbatim into the public repository.

---

## 5. Mandatory Boundary Review

Every contribution that touches SRS, SRD, or SRIP artifacts **must** pass an information-boundary review before technical review is considered complete.

Minimum review questions:

1. Is this material Open, Proprietary, or Derived-Public?
2. Does any part of the text expose secrets, internal-only procedures, or non-public implementation assets?
3. If the source is proprietary, has the content been sufficiently abstracted for public release?
4. Does the published text preserve the open standard without disclosing protected internals?

---

## 6. Required Sanitization For Derived-Public Content

If content is derived from proprietary material, the contributor or editor **must** remove or generalize:

- credentials and secrets
- internal paths not needed for public understanding
- server identities, private addresses, and unpublished operational endpoints
- internal-only prompts or control language
- raw partner, user, or operator data
- internal benchmark payloads unless explicitly approved for public release

Allowed replacements:

- generalized architecture descriptions
- normalized terminology
- abstract requirement statements
- sanitized examples
- bounded lessons learned

---

## 7. Traceability Requirements

When published content is **Derived-Public**, the review record **must** state:

- that the source included proprietary context
- that the published artifact is a sanitized abstraction
- which public artifact now carries the approved requirement or explanation

The public document does not need to expose the proprietary source itself.
It must only preserve truthful provenance at the review level.

---

## 8. Responsibilities

### Contributors

Contributors **must**:

- classify source material before writing for public release
- avoid copying proprietary material directly into public documents
- convert internal lessons into publishable abstractions when needed

### Editorial Board

The Editorial Board **must**:

- reject material that crosses the public/proprietary boundary incorrectly
- require sanitization when the source is not fully public
- ensure that SRS and SRD remain publishable as open external documents

### Steering Committee

The Steering Committee **must**:

- resolve disputes about whether a material class is publishable
- approve boundary exceptions only when the publication decision is intentional and traceable

---

## 9. Acceptance Rules

A contribution is compliant with this requirement only if:

1. the information class is explicit
2. proprietary material is not published directly
3. derived-public publication is sanitized and abstracted
4. the open standard remains complete enough to be useful without disclosing internal assets

---

## 10. Summary

This repository is public.

Therefore:

- **open standard content must stay open**
- **proprietary implementation content must stay internal**
- **public documentation may publish only Open or Derived-Public material**
