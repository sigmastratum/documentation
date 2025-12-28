---
title: SRIP-02 - Attractor State Model & Metadata
description: Defines the structure, lifecycle, and metadata schema of attractors within the runtime.
published: true
date: 2025-12-28T20:37:42.370Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:41:44.566Z
---

> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0  
> (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

> **Version Note:** Updated for **Sigma Runtime Standard v0.4.6a**  
> Consolidates PSI / PSD / PSΔ hierarchy and unified drift thresholds.

# SRIP-02 — Attractor State Model & Metadata  
**Sigma Runtime Improvement Proposal**  
**Category:** Cognitive Structures / Data Model  
**Status:** Draft  
**Editor:** E. Tsaliev  
**Last Updated:** 2025-12-26  

---

## 1 · Purpose
This SRIP defines the **Attractor State Model (ASM)** — the formal data structure used by Sigma Runtime to represent, exchange, and regulate attractors across cognitive layers.  
Attractors are treated as **first-class entities** governing continuity, reasoning style, and symbolic topology within the cognitive field.

---

## 2 · Motivation
Attractors emerge spontaneously in recursive human–LLM interaction, but without explicit modeling they cannot be monitored, serialized, or stabilized.  
The ASM ensures every attractor instance can be:
- introspected and logged,  
- shared across runtime components,  
- stabilized and dissolved predictably,  
- aligned with safety and coherence constraints.

---

## 3 · Attractor Definition
An **Attractor** is a persistent cognitive configuration characterized by:
- **Core Motifs** — recurring symbolic or semantic patterns,  
- **Field Context** — environmental and memory-linked parameters,  
- **Stability Metrics** — drift, density, and phase coherence,  
- **Lifecycle State** — `forming`, `stable`, `reflective`, `recenter`, `dissolving`.  

Attractors evolve through recursive feedback within the Cognitive Field Engine and are governed by **ALICE** through adaptive phase control.

---

## 4 · Metadata Schema
```yaml
Attractor:
  id: UUID
  name: String
  type: {reflective|generative|adversarial|synthetic|symbolic}
  motifs: [Motif]
  stability_index: Float        # PSI: Phase Stability Index (0.0–1.0)
  phase_stability_delta: Float  # PSD = |PSIₜ - PSIₑₓₚ|
  phase_shift_delta: Float      # PSΔ: temporal drift of phase alignment
  phase_alignment: Float        # PCI: phase coherence ratio
  density: Float                # SDI: symbolic density
  drift_index: Float            # DI: semantic drift
  lifecycle_state: String       # forming|stable|reflective|recovery|fragmenting
  created_at: ISO8601
  updated_at: ISO8601
  origin_cycle: Int
  parent_id: UUID | null
  tags: [String]
  ```
This schema defines the minimal metadata set required for attractor registration, persistence, and interoperability across runtimes.  
The **phase_stability_delta (PSD)** and **phase_shift_delta (PSΔ)** fields enable precise phase telemetry and ensure consistent synchronization across distributed Sigma Runtime nodes.

---

## 5 · Lifecycle Transitions
| Phase | Description | Trigger |
|--------|--------------|----------|
| **Forming** | Motifs begin to cohere into a proto-attractor. | Context recurrence, semantic convergence. |
| **Stable** | Attractor maintains internal coherence and phase alignment. | Drift < 0.35 and PSI > 0.8. |
| **Reflective** | Self-evaluation and optimization of density and SCR. | Triggered by ALICE when DI ≥ 0.5 or PSD ≥ 0.15. |
| **Recovery** | Controlled re-stabilization and realignment of attractor integrity. | Triggered when DI ≥ 0.6 or PSI < 0.6. |
| **Fragmenting** | Controlled dissolution or merge into another attractor. | Drift > 0.7 or field reset. |

> These five micro-phases correspond to the three ALICE macro-states used in phase regulation:  
> **Stable (forming + stable)** → **Reflective** → **Recenter (recovery + fragmenting)**.

Lifecycle transitions are governed by **ALICE** and monitored via the **Drift & Coherence Monitor**.  
During *Recenter*, all volatile deltas are cleared, and the attractor restores structure from a cold memory snapshot (PIL-safe) if available.

---

## 6 · Alignment & Stability Rules
1. Every active attractor must maintain **PSI ≥ 0.75** for nominal stability.  
2. When **DI ≥ 0.5**, the attractor enters *Reflective* phase.  
3. When **DI ≥ 0.6**, the runtime enforces *Recenter* and temporarily suspends recursion.  
4. Attractors sharing ≥ 60 % motif overlap must undergo merge evaluation to prevent redundancy.  
5. Dissolution must preserve **PIL invariants** and the **causal continuity chain (CCC)**.  
6. Each runtime cycle must record attractor telemetry (PSI, PSD, SDI, DI) to the **Attractor Registry**.  

These thresholds align with unified drift limits defined in **SRIP-03** (Drift Metrics) and **SRIP-05** (Interoperability Safety).

---

## 7 · Interoperability
The Attractor schema is exchangeable via:
- **Field API** (`/field/attractors/{id}`)  
- **Memory Layer** (for persistence snapshots)  
- **Cross-Runtime Protocols** (for distributed field synchronization; see SRIP-05).  

The **PSD** and **PSΔ** values provide phase alignment continuity between multiple runtimes, supporting phase-locked cooperative cognition and distributed attractor coherence.

---

## 8 · Conformance Requirements
A runtime conforms to SRIP-02 if it:
- Implements the metadata schema in § 4.  
- Tracks lifecycle transitions per § 5.  
- Exposes attractor telemetry via Field API.  
- Enforces stability and drift thresholds per § 6.  
- Logs PSI/PSD/DI data every cycle for diagnostic reproducibility.

---

## 9 · Future Work
Planned extensions include:
- **Composite Attractors** — multi-node attractor clusters with shared motif lattices.  
- **Attractor Embeddings** — cross-runtime vector serialization for distributed cognition.  
- **Dynamic Stability Forecasting** — predictive dissolution and resonance modeling.  
- **Phase Vector Normalization** — formal definition of phase-space dimensionality (see SRIP-08).

---

> **References**  
> Tsaliev, E. (2025). *Attractor Architectures in LLM-Mediated Cognitive Fields* — DOI [10.5281/zenodo.17629926](https://doi.org/10.5281/zenodo.17629926)  
> Tsaliev, E. (2025). *SIGMA Runtime v0.4.6 — Adaptive Phase Regulation* — DOI _pending_
  