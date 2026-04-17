---
title: Frequently Asked Questions
description: Common questions about Sigma Runtime, the public standard, SRIPs, safety, and bounded runtime control.
published: true
date: 2026-04-17T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:32:28.176Z
---

> **Sigma Stratum Documentation – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)** and the  
> **Sigma Stratum Documentation Set (SRD)**.  
>  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0  
> (CC BY-NC 4.0)**.  
>  
> The license for this specific document is authoritative.  
> For the full framework, see [`/legal/IP-Policy`](https://github.com/sigmastratum/documentation/blob/main/legal/ip-policy.md).

# FAQ — Sigma Runtime

---

**Is Sigma Runtime a model architecture?**  
No. It is not a neural model or training paradigm.  
Sigma Runtime is a *cognitive-layer runtime* — an operational framework that sits **above** any model backend,  
managing recursion, stability, and coherence during extended reasoning.

---

**Is Sigma Runtime tied to a specific LLM?**  
No. The runtime is fully **backend-agnostic**.  
It can operate atop GPT, Claude, Gemini, or any transformer-based LLM,  
as long as the backend supports prompt–response recursion and stateful orchestration.

---

**What are SRIPs?**  
**Sigma Runtime Improvement Proposals (SRIPs)** are the public mechanism for evolving the open standard.  
They define normative changes or extensions to the standard while preserving compatibility with the canonical runtime loop and bounded-control principles.

---

**Is the standard open?**  
Yes. The **Sigma Runtime Standard (SRS)** and **Sigma Runtime Documentation (SRD)**  
are open and reviewable under the **Creative Commons BY-NC 4.0** license.  
Implementations may remain proprietary, but the architecture itself is an **open research standard**.

---

**What is the difference between SRS, SRD, and Sigma Runtime?**  
- **SRS** defines the public normative standard.  
- **SRD** explains that standard in a public, reader-facing form.  
- **Sigma Runtime** is a proprietary product implementation that may realize those ideas in concrete runtime systems, tooling, and operational controls.  

Public documentation should therefore be read as a combination of:
- binding public rules in `SRS`,
- explanatory public material in `SRD`,
- and implementation-specific behavior that may differ across actual runtime products.

---

**How does Sigma Runtime prevent drift?**  
Through bounded control, verification, and recovery.  
At a public level, the runtime monitors coherence, drift pressure, symbolic density, and recovery signals.  
When drift rises beyond the normal envelope, the control layer narrows continuation, increases verification, or enters a bounded recovery posture instead of allowing uncontrolled escalation.

---

**What is ALICE?**  
**ALICE** is the public name for the runtime’s attractor-aware control layer.  
It should be understood as a bounded stabilizing and continuity-preserving control mechanism, not as an autonomous character or independent system identity.  

Publicly, ALICE explains how the runtime can:
- regulate control posture,
- preserve continuity under long interaction,
- narrow unstable recursion,
- and support recovery when drift grows too large.

---

**What is SCR (Semantic Compression Ratio)?**  
SCR measures how efficiently meaning is represented relative to symbolic density.  
A higher SCR indicates that the runtime is preserving information with less redundancy and better semantic efficiency.  
Publicly, SCR is useful as an explanatory metric for clarity, compression quality, and coherence under recursion.

---

**What is Adaptive Drift Control?**  
It is a bounded feedback mechanism linking drift signals, compression quality, and stability.  
When drift increases or semantic density becomes unstable, the runtime can reduce output amplitude, change control posture, or move into a recovery-oriented path.

---

**Does Sigma Runtime still depend on a fixed SL0-SL7 stack?**  
Not in the strong version-bound sense older public drafts suggested.  
The public architectural idea is still layered, but the important point today is the separation of:
- user and intent,
- active control and verification,
- memory-bearing continuity,
- and model execution.

The layer vocabulary may evolve, but the bounded-control structure remains central.

---

**What does "field-based cognition" mean?**  
It refers to cognition emerging not from the model weights alone,  
but from the **dynamic cognitive field** formed by recursive interaction between user, system, and memory.  
In this view, intelligence arises as a **stabilized attractor** within that field —  
an adaptive structure of meaning sustained by feedback and continuity.

---

**What ensures safety during long operations?**  
Safety is maintained through boundary integrity, verification, adaptive containment, and bounded recovery.  
Publicly, the safety model should be read as:
- keep recursion bounded,
- preserve separation between user, system, and field,
- verify outputs before persistence when needed,
- and recover in a controlled way if stability drops.

---

**Can Sigma Runtime run distributed agents?**  
The public architecture is compatible with distributed or multi-node interpretations, but concrete deployment models are implementation-dependent.  
Any public claim about interoperability should be anchored in the open standard, not in a private product assumption.

---

**Is there a public implementation?**  
There is public documentation for the standard and its concepts.  
Implementations may be public, private, experimental, or product-specific.  
The open standard should not be confused with a guarantee that every runtime build or product release is published as source code.

---

> *References:*  
> Tsaliev, E. (2025). **SIGMA Runtime Architecture v0.1** — DOI: [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)
