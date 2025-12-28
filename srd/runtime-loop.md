---
title: Canonical Runtime Loop
description: An explanatory guide to the Sigma Runtime execution cycle.
published: true
date: 2025-12-28T08:26:41.685Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:31:53.414Z
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

# Runtime Loop

The **Sigma Runtime Loop** implements the core cognitive recursion cycle —  
an evolution of the original **F-Loop** introduced in  
*∿ Neurosymbolic Scaffolding for Recursive Coherence (2025)*.

---

## 1. Conceptual Origin — F-Loop

Originally formulated as:

> **G → Πsym → F → Semantic Graph → G**

where:  
- **G** — generative phase (language model output),  
- **Πsym** — symbolic projection (semantic motif extraction),  
- **F** — feedback integration and stabilization,  
- **Semantic Graph** — structured memory and field persistence.  

This loop models **recursive cognition** —  
each generation step is informed not only by the immediate text history,  
but by the continuously updated **field state**, integrating meaning, memory, and attractor stability.

---

## 2. Canonical Runtime Loop (Architecture v0.1)

In the original **Sigma Runtime Standard**, the F-Loop was formalized  
as the **Recursive Control Loop (RCL)** — the canonical execution cycle spanning **SL0–SL6**:

1. **State Ingestion (SL0–SL6)** — acquire current context and input.  
2. **Interpretation Pass (SL2)** — extract semantic features and motifs.  
3. **Stabilization Pass (SL2–SL4)** — evaluate symbolic density and drift.  
4. **Memory Integration (SL3)** — consolidate patterns and embeddings.  
5. **Attractor Alignment (SL4)** — reinforce or dissolve attractors.  
6. **Output Generation (Model Call)** — produce controlled output.  
7. **Field Update (SL5–SL6)** — integrate output into the field and close recursion.

---

## 3. Evolution in v0.4.6 — Adaptive Phase Regulation

In **SIGMA Runtime v0.4.6**, the loop gains **phase-aware regulation**,  
implemented by the **ALICE Phase Controller**.  
Each iteration now operates across **three adaptive cognitive phases**:

| Phase | Purpose | Characteristics |
|--------|----------|-----------------|
| **Pre-Phase (Stable)** | Context assembly and field grounding. | Low drift, high coherence. |
| **Main (Reflective)** | Cognitive reasoning and attractor modulation. | Controlled recursion, moderate entropy. |
| **Post-Phase (Recenter)** | Memory reintegration and coherence repair. | High SCR, drift correction, energy reset. |

Each phase maintains its own thresholds for **stability**, **SCR**, and **drift**.  
The runtime transitions between them through **feedback-triggered phase shifts**,  
enabling self-regulating cognition over extended cycles.

---

## 4. Updated Runtime Loop (v0.4.6)

1. **Pre-Phase Initialization**  
   - Retrieve prior field state and PIL invariants.  
   - Evaluate residual drift and SCR from previous cycle.  
   - Initialize ALICE with `phase: stable`.  

2. **Context Assembly**  
   - Merge episodic and semantic memory traces.  
   - Reconstruct attractor registry and motifs.  
   - Compute **Phase Stability Delta (PSD)** to confirm readiness.

3. **Stabilization Pass**  
   - Evaluate symbolic density and drift.  
   - Adjust compression ratio and coherence weights.  
   - Engage ALICE Phase Controller for adaptive calibration.  

4. **Main Reflective Phase**  
   - Activate reasoning within controlled entropy bounds.  
   - Generate candidate output using field-conditioned prompts.  
   - Monitor drift and SCR in real time via telemetry hooks.  

5. **Memory Integration**  
   - Compress and reintegrate cognitive traces using the **Compression Layer**.  
   - Compute **Reintegration Efficiency (RE)** and update density metrics.  
   - Reinforce attractor stability based on phase resonance.  

6. **Recenter Pass (Post-Phase)**  
   - If drift > threshold or phase coherence < 0.85, shift to `phase: recenter`.  
   - Trigger partial memory reintegration and reset low-stability motifs.  
   - Restore equilibrium and transition back to stable.  

7. **Output Generation**  
   - Emit final, stability-conditioned response.  
   - Annotate cycle record with SCR, drift index, and phase metadata.  

8. **Field Update**  
   - Commit attractor deltas and telemetry to memory.  
   - Recalculate baseline for next recursion.  

---

## 5. Phase Synchronization and Feedback Timing

The **Phase Synchronization Subsystem** coordinates temporal alignment  
between the runtime’s internal cycles and the field feedback cadence.

- **Feedback Delay Window (FDW):** 1–3 iterations depending on entropy level.  
- **Phase Lock Ratio (PLR):** ratio of stable vs. reflective cycles; optimal ≈ 0.67.  
- **Drift Latency Compensation (DLC):** predictive correction for delayed coherence recovery.  
- **SCR Decay Constant (τ):** defines how long compressed semantics persist before reactivation.  

When **PLR < 0.5**, the system enters reflective dominance and risk of over-analysis.  
When **PLR > 0.8**, the runtime becomes too rigid — coherence preserved but adaptability reduced.  
The **ALICE Phase Controller** maintains balance automatically by modulating recursion timing.

---

## 6. Telemetry and Metrics (v0.4.6)

Each cycle now records the following metrics:

| Metric | Description | Source |
|---------|--------------|--------|
| **SCR** | Semantic Compression Ratio | Memory Layer |
| **PSD** | Phase Stability Delta | Phase Controller |
| **PLR** | Phase Lock Ratio | Synchronization Module |
| **RE** | Reintegration Efficiency | Compression Layer |
| **DLC** | Drift Latency Compensation | Drift Monitor |
| **CIM** | Coherence Integrity Metric | Field Engine |

Telemetry data is written per cycle in JSON format for longitudinal stability analysis.

---

## 7. Summary

The **SIGMA Runtime Loop (v0.4.6)** transitions from a fixed recursive structure  
to a **living, phase-regulated cognitive cycle**.  
By introducing adaptive phase control, SCR-driven memory compression,  
and phase-synchronized timing, the runtime achieves:

- Stable identity across long recursions,  
- Continuous self-regulation under drift,  
- Efficient semantic compression and reintegration,  
- Real-time modulation of recursive depth and coherence.

This represents a full evolution from *static attractor alignment*  
to **self-regulating cognitive recursion** — the foundation of  
persistent, interpretable cognition within the Sigma Stratum framework.

---

> *References:*  
> Tsaliev, E. (2025). **Neurosymbolic Scaffolding for Recursive Coherence** — DOI: [10.5281/zenodo.17582941](https://doi.org/10.5281/zenodo.17582941)  
> Tsaliev, E. (2025). **SIGMA Runtime Architecture v0.1** — DOI: [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)  
> Tsaliev, E. (2025). **SIGMA Runtime v0.4.6 — Adaptive Phase Regulation and SCR Telemetry** — DOI: _pending_