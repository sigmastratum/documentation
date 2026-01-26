---
title: README
description: 
published: true
date: 2025-12-01T07:39:16.080Z
tags: 
editor: markdown
dateCreated: 2025-12-01T07:34:03.356Z
---

# Sigma Stratum Documentation  

Public technical documentation, standards, and research corpus for the **Sigma Stratum** framework and the **Sigma Runtime** architecture.

This repository contains all public-facing materials of the Sigma Stratum Research Group (SSRG), including:
- the **Sigma Runtime Standard (SRS / SRIP series)**  
- the **Sigma Runtime Documentation (SRD)**  
- governance and contribution guidelines  
- licensing and IP policies  
- DOI-linked research archives  

---

## Repository Structure

### **/home/**
General entry layer and introductory materials:
- About  
- Glossary  
- Developer Onboarding  
- Research / Whitepapers  

### **/srd/** — *Sigma Runtime Documentation*  
Conceptual and architectural corpus explaining the Sigma Runtime cognitive model:
- Overview  
- Core Concepts  
- Architecture (SL0–SL7)
- ALICE  
- Attractors  
- Drift  
- Memory  
- Runtime Loop  
- Safety & Alignment  
- FAQ  

### **/srs/** — *Sigma Runtime Standard (SRIP Series)*  
Normative technical standard defining conformant Sigma Runtime implementations:
- SRIP-00 — Foundations and Scope  
- SRIP-01 — Canonical Runtime Loop  
- SRIP-02 — Attractor Model  
- SRIP-03 — Drift Metrics  
- SRIP-04 — Memory Layer  
- SRIP-05 — Interoperability  
- SRIP-06 — Safety Boundaries  
- SRIP-07 — Symbolic Density
- SRIP-08 — Phase Vector Model & PRM
- SRIP-09 — Long-Term Memory and Structural Coherence Layer
- SRIP-10 — AEP: Adaptive Entropy Protocol 

### **/team/**
Governance and development process:
- Governance  
- Contribution Process  
- SRIP Process  
- Roadmap  

### **/legal/**
Licensing, attribution, and intellectual property:
- License  
- IP Policy  
- Attribution  

### **/templates/**
Standard headers and reusable documentation templates.

---

## Licensing

All materials are distributed under the **Sigma Stratum Open Standard Framework**,  
using the following Creative Commons licenses:

- **CC BY-NC 4.0** — Non-commercial license for conceptual and theoretical materials (SRD)  
- **CC BY 4.0** — Attribution-only license for selected technical and educational materials  

Each document includes its own license header.  
See `/legal/license.md` and `/templates/LICENSE-HEADER.md` for full details.

---

## Contribution Guidelines

To propose modifications or extensions:

1. Fork the repository  
2. Commit changes in a new branch  
3. Submit a pull request  
4. Follow the SRIP Process for normative updates  

All contributions must:
- preserve canonical attribution  
- include a summary of changes  
- specify whether the content is *normative* or *descriptive*  

---

## SRIP — Sigma Runtime Improvement Proposals

Changes to the Sigma Runtime Standard (SRS) are managed via the **SRIP process**.

- SRIPs introduce or modify normative runtime definitions  
- Each SRIP must reference its parent specification (e.g., SRIP-00)  
- All SRIPs are reviewed by SSRG before merging  

See [`/team/srip-process.md`](https://github.com/sigmastratum/documentation/blob/main/team/srip-process.md) for full procedure.

---

## Canonical References (Zenodo DOIs)

Core Sigma Stratum research publications:

- Tsaliev, E. (2025). *Sigma Runtime Architecture v0.1* — DOI: [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)  
- Tsaliev, E. (2025). *Attractor Architectures in LLM-Mediated Cognitive Fields* — DOI: [10.5281/zenodo.17629926](https://doi.org/10.5281/zenodo.17629926)

Additional foundational works 
are listed in [`/home/research.md`](https://github.com/sigmastratum/documentation/blob/main/home/research.md)  
and referenced contextually within SRD documents.

---

## Contact

For collaboration, licensing, or institutional participation:

**Eugene Tsaliev**  
Lead Architect, Sigma Stratum Research Group (SSRG)  
📧 eugene@sigmastratum.org  
🔗 ORCID: [0009-0007-3279-9477](https://orcid.org/0009-0007-3279-9477)  
📬 General Inquiries: contact@sigmastratum.org  

---

**This repository serves as the canonical source of truth for all Sigma Stratum documentation and standards.**  
© 2025 Sigma Stratum Research Group (SSRG) — Licensed under CC BY-NC 4.0.
