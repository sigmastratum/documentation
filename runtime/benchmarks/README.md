# SIGMA Runtime Benchmark Plan (v0.1 ERI)

## Goal
Benchmark **SIGMA Runtime (v0.1 ERI)** against a baseline LLM agent to measure:
- Token efficiency  
- Coherence stability  
- Latency  
- Drift control performance  

Reference: [SIGMA Runtime ERI (v0.1)](https://github.com/sigmastratum/documentation/blob/main/runtime/reference/README.md)

---

## 1. Setup

**Environment**
- Python ≥ 3.10  
- OpenAI API (or equivalent)  
- `pandas`, `matplotlib`, `loguru`  
- Local copy of SIGMA Runtime ERI reference  

**Hardware**
- Same GPU/CPU for both runs  
- Disable caching in SDKs (e.g. OpenAI, HuggingFace)

---

## 2. Metrics

| Metric | Description |
|--------|--------------|
| **Token Usage** | Total tokens consumed per 100 steps |
| **Latency** | Average response time per generation |
| **Drift Index (DI)** | Semantic deviation from initial intent (0–1) |
| **Recovery Rate (RR)** | % of cycles where coherence was restored automatically |
| **Session Length Before Breakdown** | Number of coherent turns before failure |

---

## 3. Baseline Agent

A simple looped LLM context appending agent used as control.

```python
context = []
for i in range(200):
    prompt = "\n".join(context[-5:]) + "\nUser: " + input_text
    output = llm(prompt)
    context.append(output)
```
Characteristics
	•	No memory optimization
	•	No drift control
	•	No selective context compression
	•	Increasing token load per iteration
	•	Rapid coherence decay beyond ~50 steps

---

## 4. SIGMA Runtime Agent

Implements the [SIGMA Runtime ERI (v0.1)](https://github.com/sigmastratum/documentation/blob/main/runtime/reference/README.md) loop:
context → _generate() → model output → drift + stability + memory update → causal continuity → context rebuild.

```python
from sigma_runtime import SigmaRuntime

sigma = SigmaRuntime(model="gpt-4-turbo")

for i in range(200):
    response = sigma.run(input_text)
    sigma.update(response)
```

---

Core Components
	•	Multi-Tier Memory (short-term, episodic, long-term)
	•	Drift Monitor (semantic deviation tracking)
	•	Stability Engine (phase control: STABLE / REFLECTION / FRAGMENTING)
	•	Persistent Identity Layer (PIL)
	•	Causal Continuity Chain (CCC) for closed-loop context rebuild

---

## 5. Benchmark Procedure

### Step 1 — Setup
Run both agents (Baseline and SIGMA Runtime) under identical conditions:
- Same model (e.g., `gpt-4-turbo`)
- Same system prompt / seed task
- Fixed temperature (e.g., `0.7`)
- Same iteration length (200–500 turns)

### Step 2 — Logging
Record metrics every 10 steps:
- Token usage (`prompt_tokens + completion_tokens`)
- Latency (average API response time)
- Drift Index (semantic similarity to iteration 0)
- Coherence recovery events
- Cumulative cost

### Step 3 — Evaluation
After completion:
- Plot **Token Usage vs Step** — expected flattening for SIGMA  
- Plot **Drift Index vs Step** — expected slower decay  
- Compute total operational cost difference (expected 35–60% savings)  
- Qualitative check: continuity and identity retention across sessions

---

## 6. Expected Results

| Metric | Baseline Agent | SIGMA Runtime (ERI v0.1) | Δ Improvement |
|--------|----------------|---------------------------|----------------|
| Avg. Tokens per Iteration | 1800–2500 | 900–1300 | ↓ 40–55% |
| Coherence Retention (200 turns) | <30% | >80% | ↑ ~2.7× |
| Drift Accumulation Rate | High (diverges after ~40 steps) | Low (stable up to 200+) | ↓ ~70% |
| Correction / Retry Count | Frequent | Minimal | ↓ 60–80% |
| Total API Cost (200 turns) | 1.00× baseline | 0.45–0.65× | ↓ 35–55% |
| Runtime Latency | Increasing with step count | Stable | ↓ 25–40% |

### Interpretation
- **Token Efficiency**: Selective context insertion and identity persistence reduce redundant payload.  
- **Cognitive Stability**: Drift control and phase modulation preserve semantic structure.  
- **Economic Impact**: Operational efficiency compounds at scale — up to **2× runtime longevity** with **half the cost**.

## 7. Deliverables

Each benchmark run should produce:

### Data
- `baseline_log.json` — per-step metrics for standard agent  
- `sigma_log.json` — per-step metrics for SIGMA Runtime  
- `summary.csv` — aggregated statistics across runs  

### Visuals
- Token Efficiency Curve  
- Drift vs Step Graph  
- Cost Efficiency Chart  
- Stability Phase Map (optional heatmap of drift/stability transitions)  

### Analysis
A 1-page summary comparing:
- Mean token usage  
- Coherence retention curves  
- Cost reduction percentage  
- Observed qualitative differences in reasoning continuity  

### Publication
Upload final report + visuals to:
- GitHub: `documentation/benchmarks/`  
- Optional: Zenodo for DOI versioning  
Include reference to  
[`SIGMA Runtime ERI v0.1`](https://github.com/sigmastratum/documentation/blob/main/runtime/reference/README.md)

---

