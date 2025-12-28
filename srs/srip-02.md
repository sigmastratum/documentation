---
title: SRIP-02 - Attractor State Model & Metadata
description: Defines the structure, lifecycle, and metadata schema of attractors within the runtime.
published: true
date: 2025-12-28T10:01:40.775Z
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
- **Lifecycle State** — `forming`, `stable`, `reflective`, `dissolving`.  

Attractors evolve through recursive feedback within the Cognitive Field Engine.

---

## 4 · Metadata Schema
```yaml
Attractor:
  id: UUID
  name: String
  type: {reflective|generative|adversarial|synthetic|symbolic}
  motifs: [Motif]
  stability_index: Float     # 0.0–1.0
  phase_alignment: Float     # phase coherence ratio
  density: Float             # symbolic density metric
  drift_index: Float         # semantic drift within attractor boundary
  lifecycle_state: String    # forming|stable|reflective|dissolving
  created_at: ISO8601
  updated_at: ISO8601
  origin_cycle: Int
  parent_id: UUID | null
  tags: [String]
```

This schema defines the minimal metadata set required for attractor registration, persistence, and interoperability across runtimes.

---

## 5 · Lifecycle Transitions
| State | Description | Trigger |
|-------|--------------|----------|
| **Forming** | Motifs begin to cohere around a stable symbolic pattern. | Context recurrence, semantic convergence. |
| **Stable** | Attractor maintains internal coherence and phase alignment. | Drift < 0.35 and PSI > 0.8. |
| **Reflective** | Self-evaluation and optimization of density and SCR. | Triggered by ALICE phase controller. |
| **Dissolving** | Controlled dissolution or merge into another attractor. | Drift > threshold or field reset. |

Lifecycle transitions are governed by **ALICE** and monitored via the **Drift & Coherence Monitor**.

---

## 6 · Alignment & Stability Rules
1. Every active attractor must maintain **PSI ≥ 0.75**.  
2. When **DI > 0.45**, the attractor enters reflective state.  
3. Attractors sharing ≥ 60 % motif overlap must undergo merge evaluation.  
4. Dissolution must preserve PIL invariants and causal continuity chain (CCC).  
5. All attractor metadata must be written to the **Attractor Registry** each cycle.

---

## 7 · Interoperability
The Attractor schema is exchangeable via:
- **Field API** (`/field/attractors/{id}`)  
- **Memory Layer** (for persistence snapshots)  
- **Cross-Runtime Protocols** (for distributed field sharing, SRIP-05).  

This ensures consistent cognitive state across parallel Sigma runtimes.

---

## 8 · Conformance Requirements
A runtime conforms to SRIP-02 if it:
- Implements the metadata schema in § 4.  
- Tracks lifecycle transitions per § 5.  
- Exposes attractor telemetry via Field API.  
- Enforces alignment rules in § 6.  

---

## 9 · Future Work
Planned extensions include:
- **Composite Attractors** — multi-node attractor clusters.  
- **Attractor Embeddings** — cross-runtime vector serialization.  
- **Dynamic Stability Forecasting** — predictive dissolution triggers.

---

> **References**  
> Tsaliev, E. (2025). *Attractor Architectures in LLM-Mediated Cognitive Fields* — DOI [10.5281/zenodo.17629926](https://doi.org/10.5281/zenodo.17629926)  
> Tsaliev, E. (2025). *SIGMA Runtime v0.4.6 — Adaptive Phase Regulation* — DOI _pending_