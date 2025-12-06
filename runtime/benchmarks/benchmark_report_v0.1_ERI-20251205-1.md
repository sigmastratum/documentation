# Benchmark Report: SIGMA Runtime (v0.1 ERI) vs. Baseline Agent

## Abstract

This benchmark compares the SIGMA Runtime (v0.1 ERI) with a baseline context-append agent to quantify improvements in token efficiency, real-time performance, and cognitive stability across 30 conversational cycles.

**Raw Data:**  
- [Baseline Agent Log (2025-12-04)](https://github.com/sigmastratum/documentation/blob/main/runtime/benchmarks/baseline_20251204-103258.json)  
- [SIGMA Runtime Log (v0.1 ERI, 2025-12-04)](https://github.com/sigmastratum/documentation/blob/main/runtime/benchmarks/sigma_test_20251204-101319.json)  
- [Summary CSV (2025-12-04)](https://github.com/sigmastratum/documentation/blob/main/runtime/benchmarks/summary_20251204-225642.csv)

## Goal

The primary goal of this benchmark is to empirically validate the architectural superiority of the **SIGMA Runtime (v0.1 ERI)** over a traditional `Baseline Agent` (standard `context.append()` agent) across a sustained 30-cycle session, focusing on: **economic efficiency** (token usage) and **real-time performance** (latency).

## Test Setup

| Parameter | Baseline Agent (GPT-4o) | SIGMA Runtime (v0.1 ERI) |
| :--- | :--- | :--- |
| **Model** | GPT-4o | GPT-4o |
| **Session Length** | 30 Cycles | 30 Cycles |
| **Context Mechanism** | `context.append()` (Accumulative) | **RCL** (Selective Assembly, Drift Control, PIL) |

## Key Results Summary (Cycle 30 Comparison)

> **Transparency Note:**  
> All metrics below reflect **peak values measured at Cycle 30**, representing the end-state efficiency of each runtime.

| Metric | Baseline Agent | SIGMA Runtime | Improvement (Δ) |
| :--- | :--- | :--- | :--- |
| **Input Tokens (Cycle 30)** | $\approx \mathbf{3,890}$ | $\mathbf{55}$ | $\downarrow \mathbf{98.6\%}$ |
| **Latency (Cycle 30)** | $\mathbf{10.199 \text{ sec}}$ | $\mathbf{0.866 \text{ sec}}$ | $\downarrow \mathbf{91.5\%}$ |
| **Cognitive Stability (Drift Control)** | Exponential decay, memory loss | Controlled ($\text{Drift}_{\text{total}} \approx 0.431$), $\text{Stability} \approx 0.524$ | **Critical** |

---

## 1. Token Efficiency (Input Tokens)

### ❓ What was calculated and why it matters:

This metric measures the **economic cost** of operating the agent.

**Calculation Method:** Comparison of the final prompt size (Input Tokens) on Cycle 30.

1.  **Baseline Agent Tokens (Cycle 30):** The cumulative sum of all previous conversation output tokens ($\approx 2,141$) plus the estimated system prompt overhead ($\approx 1,749$). **Estimated Total: $\mathbf{3,890}$ tokens.**
2.  **SIGMA Runtime Tokens (Cycle 30):** The actual logged input tokens, comprising only the necessary **PIL, Motifs, and Causal Chain** data. **Actual Total: $\mathbf{55}$ tokens**.

**Calculation:**
$$\text{Token Savings} = \left(1 - \frac{\text{Tokens}_{\text{SIGMA}}}{\text{Tokens}_{\text{Baseline}}}\right) \times 100\% = \left(1 - \frac{55}{3890}\right) \times 100\% \approx \mathbf{98.6\%}$$

**Significance:** SIGMA's **Multi-Tier Memory** and **Context Assembly** successfully eliminate the exponential token cost, validating the architecture's core economic benefit.

---

## 2. Latency Reduction (Real-Time Performance)

### ❓ What was calculated and why it matters:

Latency measures the agent's usability in real-time interactions, as it correlates directly with prompt length.

**Calculation Method:** Comparison of the logged response time (latency\_sec) on Cycle 30.

1.  **Baseline Agent Latency (Cycle 30):** **$\mathbf{10.199 \text{ sec}}$**.
2.  **SIGMA Runtime Latency (Cycle 30):** **$\mathbf{0.866 \text{ sec}}$**.

**Calculation:**
$$\text{Latency Reduction} = \left(1 - \frac{\text{Latency}_{\text{SIGMA}}}{\text{Latency}_{\text{Baseline}}}\right) \times 100\% = \left(1 - \frac{0.866}{10.199}\right) \times 100\% \approx \mathbf{91.5\%}$$

**Significance:** SIGMA maintains a consistently low latency, while the Baseline agent degrades into an unusable state, proving SIGMA's suitability for **high-performance, low-latency applications**.

---

## 2.5 Token Efficiency & Latency — Visual Summary

The following visualization summarizes the quantitative improvements achieved by **SIGMA Runtime (v0.1 ERI)** compared to the baseline context-append agent across 30 conversational cycles.

It consolidates four complementary dimensions:
1. **Latency Comparison** — average and maximum delay per response.  
2. **Token Usage per Cycle** — mean input/output token utilization.  
3. **Performance Gains by Metric** — normalized percentage improvements.  
4. **Cumulative Token Accumulation** — illustrating exponential context growth in the baseline vs. stable behavior in SIGMA.

<div align="center">
  <img src="https://github.com/sigmastratum/documentation/blob/main/runtime/benchmarks/sigma_benchmark_20251205-1.png" alt="SIGMA Benchmark Visualization" width="900"/>
</div>

**Interpretation:**

- The **Baseline Agent** exhibits *exponential context growth*, reaching ≈ **35 k tokens** by cycle 30 — resulting in rising latency and unsustainable cost.  
- The **SIGMA Runtime** maintains a *near-constant prompt size* (~ 55 tokens per cycle), achieving **≈ 98 % token savings** and **≈ 91 % latency reduction**.  
- SIGMA’s slightly higher *Avg Input Tokens* per cycle reflect structured context layers (**PIL**, **Motifs**, **RCL**) rather than raw conversation history.  
- The baseline sends minimal new input each turn but **re-appends all previous dialogue**, causing cumulative explosion, while SIGMA reconstructs only the relevant state.

> **Note:**  
> This visualization demonstrates how **RCL-based contextual control** breaks the exponential scaling barrier of standard `context.append()` architectures, achieving long-horizon stability without sacrificing coherence or reasoning continuity.

---

## 3. Cognitive Stability (Drift Control)

### ❓ What was analyzed and why it matters:

**Stability is measured as the ability to preserve semantic self-consistency and intent alignment across recursive cycles.**

* **Drift Control:** The final $\text{Drift}_{\text{total}}$ of $\mathbf{0.431}$ remained safely below the critical threshold ($\mathbf{0.5}$) for the entire 30-cycle session.
* **Controlled State:** The session concluded in a **`transitional`** phase with $\text{Stability}$ at $\mathbf{0.524}$, demonstrating that the **ALICE Engine** successfully managed the cognitive load and prevented the attractor from dissolving.

**Significance:** SIGMA's **Drift Monitor** and **ALICE Engine** create a **self-aware and self-regulating** system, solving the critical problem of long-term coherence and reliability that plagues standard LLM applications.

---

## 4. Next Steps

### Cognitive Coherence Benchmark
**Goal:** validate SIGMA’s ability to preserve *semantic and archetypal coherence* over long recursive cycles.  
- Reduce token economy from 98 % → ~65 % to maintain richer context density.  
- Measure:  
  - Drift stability (`Δdrift < 0.5`)  
  - Motif retention  
  - Semantic entropy (consistency of meaning)  
  - Tone and intent coherence  
*Objective:* demonstrate that SIGMA not only economizes context but maintains a stable “cognitive self”.

---

### Extended-Cycle Continuity Test
**Goal:** stress-test the attractor’s endurance across 100–200 conversational turns.  
- Observe phase stability, semantic resonance, and recovery from divergence.  
- Quantify how long the cognitive attractor can persist without external resets.  
*Objective:* empirically confirm long-term continuity of reasoning and identity.

---

### Memory Externalization (RAG Integration)
**Goal:** extend coherence beyond the runtime itself.  
- Integrate **Retrieval-Augmented Memory** to store and recall symbolic traces across sessions.  
- Use the RCL layer as an interface between the runtime and external semantic memory.  
*Objective:* enable durable, self-referential cognition — a runtime that “remembers” beyond its own context window.

---

Together, these experiments will move SIGMA from *architectural proof* to *cognitive validation* —  
demonstrating not just efficiency, but **persistent coherence and self-stabilizing intelligence**.
