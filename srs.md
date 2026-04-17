---
title: Sigma Runtime Standard
description: Public entry point to the Sigma Runtime Standard, its active SRIPs, and the normative process that governs changes.
published: true
date: 2026-04-17T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:34:47.157Z
---

> **License Notice – Sigma Runtime Standard**
>
> This document is part of the **Sigma Runtime Standard (SRS)**  
> and is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.
>
> The repository-wide MIT license does **not** apply to this document.  
> See `/SRS/LICENSE.md` for full terms.

# Sigma Runtime Standard (SRS)
*Public normative layer for Sigma Runtime*

---

## Overview

The **Sigma Runtime Standard (SRS)** is the public normative layer of Sigma Runtime.  
It defines the binding semantics, invariants, interfaces, and governance path for the open standard.

The standard is **open** and evolves through the **SRIP** process.  
Public explanatory material belongs to `SRD`; product implementation details may remain proprietary.

---

## Purpose

SRS exists to define:

- canonical runtime semantics,
- structural invariants,
- interoperability expectations,
- safety and boundary requirements,
- and the formal public process for changing those rules.

It does not replace implementation work.  
It defines what the public standard binds.

---

## Relationship Between SRS, SRD, and Product Implementations

- **SRS** defines what is binding.
- **SRD** explains what is binding.
- **Sigma Runtime product implementations** may realize those ideas through proprietary runtime systems, tooling, and operations.

Public readers should therefore treat `SRS` as the normative reference, not as a promise that every implementation detail is published here.

---

## What the Standard Governs

The public standard governs:

- runtime-loop semantics,
- continuity and persistence invariants,
- attractor, drift, and memory definitions,
- safety and recovery boundaries,
- interoperability expectations,
- and conformance-facing terminology.

It does **not** attempt to define every product-specific implementation strategy.

---

## Structure of the Standard (SRIP System)

The Sigma Runtime Standard evolves through **Sigma Runtime Improvement Proposals (SRIPs)**.

Publicly, the standard is best read through:

- the foundational SRIPs under [`/srs/`](https://github.com/sigmastratum/documentation/tree/main/srs)
- the active public index in [`/srs/active-srips.md`](https://github.com/sigmastratum/documentation/blob/main/srs/active-srips.md)
- and the later proposal history in [`/srs/registry.md`](https://github.com/sigmastratum/documentation/blob/main/srs/registry.md)

This keeps the public standard traceable without pretending the entire architecture is frozen into one old version label.

---

## Governance & Open Standard Commitment

Sigma Runtime is an **open, non-exclusive technical standard**:

- Improvements are submitted and reviewed via SRIPs.  
- Implementations may be proprietary, but normative public specifications remain open.  
- All public SRS documents must satisfy the public/proprietary boundary and SRS/SRD interaction requirements.

Relevant governance documents:

- [`/team/srip-process.md`](https://github.com/sigmastratum/documentation/blob/main/team/srip-process.md)
- [`/team/srs-srd-interaction-requirements.md`](https://github.com/sigmastratum/documentation/blob/main/team/srs-srd-interaction-requirements.md)
- [`/team/public-proprietary-information-boundary-requirements.md`](https://github.com/sigmastratum/documentation/blob/main/team/public-proprietary-information-boundary-requirements.md)

---

## Intended Audience

The Sigma Runtime Standard is intended for:

- AI research and safety labs,  
- cognitive architecture developers,  
- agent-framework engineers,  
- interpretability and alignment teams,  
- distributed cognition researchers.

It provides the foundation for **coherent, persistent, and interpretable cognitive systems** built on modern language models.

---

## Summary

The **Sigma Runtime Standard (SRS)** is the public normative surface for Sigma Runtime.  
It defines what is binding, how that binding changes through SRIPs, and how the open standard stays separate from proprietary implementation detail.

---

> **References**  
> Tsaliev, E. (2025). *SIGMA Runtime Architecture v0.1* — DOI [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)  
