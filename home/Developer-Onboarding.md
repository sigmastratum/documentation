---
title: Developer Onboarding
description: Concise developer onboarding for the Sigma Runtime architecture. Explains core concepts, runtime loop, memory model, attractors, drift control, and integration patterns for building conformant runtime implementations.
published: true
date: 2025-12-02T04:41:29.920Z
tags: 
editor: markdown
dateCreated: 2025-11-30T10:23:15.634Z
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

# Sigma Runtime — Developer Onboarding v1.0  
*A practical engineering introduction to building Sigma Runtime systems.*

This document explains Sigma Runtime **in plain engineering terms**, without
theoretical language. It describes what it is, how it works, and how developers
can implement a minimal version.

If you can write Python and call an LLM API — you can build this.

---

## 1. What Sigma Runtime Is (Simple Definition)

**Sigma Runtime is an execution loop that stabilizes long-horizon LLM behavior.**

It wraps an LLM with:

- a *state object*  
- a *memory system*  
- a *recursive control loop (RCL)*  
- an *attractor monitor*  
- a *drift detector*  
- a *prompt builder*

The goal is simple:

> Keep the model coherent, consistent, resistant to drift, and stable across
> hundreds of recursive steps.

This is *not* a new model.  
This is *not* fine-tuning.  
This is an **external runtime layer**.

---

## 2. Why It’s Needed (Engineering Version)

LLMs are **stateless token generators**.

When used in long dialogs, they gradually:

- lose consistency  
- rewrite earlier meaning  
- drift off-topic  
- break persona  
- contradict themselves  
- lose task constraints  

Sigma Runtime fixes this by running an external loop that:

- detects drift early  
- reinforces stable patterns (“attractors”)  
- keeps memory consistent  
- reconstructs context every turn  
- controls the recursion  

Think of it as:  
**middleware for cognition**.

---

## 3. The Runtime Loop (RCL)

Every step of interaction runs through the **same canonical loop**:

1. **Ingest user input**  
2. **Update State**  
3. **Retrieve relevant memory**  
4. **Analyze symbols & patterns**  
5. **Detect drift**  
6. **Update attractor state**  
7. **Build prompt**  
8. **Call LLM**  
9. **Post-process output**  
10. **Store memory**  
11. **Return response**

This is the *entire runtime* in one diagram:

>User Input
↓
State Update
↓
Memory Retrieval
↓
Symbol/Pattern Analysis
↓
Drift Detector
↓
Attractor Monitor
↓
Prompt Builder
↓
LLM Call
↓
Output + Memory Save
↓
Return Response

---

## 4. Core Components (Engineering View)

### 4.1 Runtime State
Stores everything the LLM itself cannot:

- last N turns  
- extracted symbols  
- active attractor  
- drift score  
- task info  
- identity constraints  

It’s just a Python dict or class.

### 4.2 Memory
Three simple layers:

- **episodic** (previous turns or summaries)  
- **semantic** (embeddings / facts)  
- **symbolic motifs** (recurrent patterns)  

Memory retrieval = pull whatever is relevant.

### 4.3 Attractor Monitor
Tracks stable patterns that recur across turns.

Implementation is simple:

- detect recurring motifs  
- measure stability  
- detect phase changes  
- reinforce when coherent  
- reset when unstable  

No magic — it’s just pattern tracking.

### 4.4 Drift Detector
Tracks divergence from stable behavior using:

- embeddings  
- semantic similarity  
- style consistency  
- constraint-check violations  

If drift exceeds thresholds → correction.

### 4.5 Prompt Builder
Constructs a stable, minimal prompt every cycle:

- system rules  
- identity  
- behavior constraints  
- memory inserts  
- active attractor cues  
- user message  

This keeps context consistent across 100+ turns.

---

## 5. Minimal Reference Skeleton (Python Pseudocode)

This is the **minimal working Sigma Runtime structure**:

```python
class SigmaRuntime:
    def __init__(self, model):
        self.model = model
        self.state = {}
        self.memory = Memory()
        self.attractor = AttractorMonitor()
        self.drift = DriftDetector()

    def step(self, user_input):
        self.update_state(user_input)
        mem = self.memory.retrieve(self.state)

        symbols = extract_symbols(user_input)
        self.attractor.update(symbols)
        self.drift.update(self.state, symbols)

        prompt = build_prompt(self.state, mem, self.attractor)
        output = self.model(prompt)

        self.memory.store(user_input, output)
        self.state["last_output"] = output

        return output
```

Everything else is just filling in functions:
	•	update_state
	•	extract_symbols
	•	build_prompt
	•	memory retrieval/embedding
	•	drift thresholds
	•	attractor signatures

## 6. A Real-World Example (Minimal Case)

User:

“Help me build a 10-step migration plan.”

Runtime sequence:
	•	state updates
	•	memory checks past turns
	•	attractor monitor sees stable “project-planning” motifs
	•	drift detector checks structure
	•	prompt builder inserts:
	•	identity (“You are a project planning assistant.”)
	•	stable motifs (“steps”, “phased rollout”, “risk review”)
	•	last constraints
	•	LLM generates structured output
	•	runtime stores it

On turn 20, turn 50, turn 120 — structure remains consistent.

Without runtime → drift and collapse.

⸻

## 7. What Developers Actually Need to Build

An MVP runtime requires only:
	•	a state class
	•	an embedding model
	•	a simple memory store
	•	two small modules: AttractorMonitor + DriftDetector
	•	a deterministic prompt builder
	•	a loop

This fits in 150–250 lines of Python.

You do not need theory to build it.
You do not need training.
You do not need GPUs.

Just an LLM API.

⸻

## 8. What to Read First

For engineers:
	1. [Attractor Architectures (PDF) — shows how attractors behave](/attractor_architectures_in_llm_mediated_cognitive_fields.pdf)
	2. [Runtime Architecture v0.1 (PDF) — shows SL0–SL6 separation](/sigma_runtime_architecture_v0_1.pdf)

These two documents contain everything required to implement the runtime.

⸻

## 9. Summary

If you are a developer:
	•	Sigma Runtime = a loop + memory + pattern checks
	•	Attractors = stable patterns
	•	Drift = semantic divergence
	•	Runtime = middleware between user and LLM

You can build this today.
It is not complicated — it’s just structured recursion.



---
## Further Reading

For implementation details, runtime source code, and test scenarios, see:  
👉 [Sigma Runtime – Reference Implementations (RI & ERI)](https://github.com/sigmastratum/documentation/blob/main/runtime/reference/README.md)

This document contains:
- Full architectural overview (RI and ERI)
- Instructions for running both implementations
- Guidance on integration with external models (GPT, Claude, URIEL)
- Reference test scenarios for stability and drift validation

⸻

End of Developer Onboarding v1.0