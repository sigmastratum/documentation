> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> Licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
> See `/legal/IP-Policy` for repository-wide licensing details.

---

# SRIP-10 — AEP: Adaptive Entropy Protocol  
**Proactive Cognitive Equilibrium Regulation in ALICE Systems**

**Version:** v1.2
**Status:** Production Ready
**Author:** Sigma Stratum Research Group (SSRG)
**Date:** 2026-02-05  
**Parent Specs:** SRIP-03, SRIP-04, SRIP-06, SRIP-08  
**License:** CC BY-NC 4.0 / Canon CIL Applicable

---

## Abstract

The **Adaptive Entropy Protocol (AEP)** supersedes the former *Anti-Crystallization Equilibrium Model (ACE)*.  
While ACE relied on reactive detection of structural crystallization (via SRIP-10c–g), AEP introduces **predictive entropy regulation** using three high-order meta-metrics:

- **TI – Terminological Isometry** (lexical proportionality)  
- **SDC – Semantic Drift Coefficient** (semantic field motion)  
- **L/N – Logic-to-Noise Ratio** (cognitive coherence index)

Together, these metrics define a *triadic entropy manifold* in which cognitive systems maintain healthy variance, preventing both fragmentation and crystallization.

AEP replaces *warning-based correction* with *parameteric self-modulation*.

---

## Motivation

### 1. Limitations of ACE
ACE (v1.x) effectively detected crystallization patterns but:
- Reacted to symptoms rather than preventing them;
- Relied on hard-coded pattern detectors (SRIP-10c–g);
- Induced rigid “avoidance” behavior, leading to sterile attractors.

### 2. Core Principle of AEP
AEP inverts the paradigm:
> “Do not detect and react — **predict and balance**.”

Instead of suppressing repetition post-factum, the system measures the *shape of cognitive evolution* via TI, SDC, and L/N, maintaining all three within target dynamic bounds.

### 3. System Placement (ALICE-first)
AEP is a **module within ALICE**, not the parent controller.  
ALICE owns phase and stability; AEP computes metrics and emits interventions (prompt injection, token caps, and metric signals).  
ALICE decides when to apply penalties or overlays based on AEP state. AEP does not directly mutate ALICE state.

---

## Specification

### 1. Meta-Metric Layer

| Symbol | Name | Domain | Interpretation | Healthy Zone |
|:--|:--|:--|:--|:--|
| **TI** | Terminological Isometry | Lexical | Structural proportionality of terms | 0.55 – 0.75 |
| **SDC** | Semantic Drift Coefficient | Semantic | Mean inter-cycle semantic displacement | 0.08 – 0.12 |
| **L/N** | Logic-to-Noise Ratio | Cognitive | Logical coherence vs. redundancy | 0.80 – 0.88 |

AEP maintains the system within this tri-metric *equilibrium basin*.

---

### 2. Computation Principles

#### 2.1 Terminological Isometry (TI)
```math
TI_t = α · \frac{2|T_{base} ∩ T_t|}{|T_{base}| + |T_t|} + (1 - α) · \frac{2|T_{t−50} ∩ T_t|}{|T_{t−50}| + |T_t|}
```
**Where:**
	•	T_base — term set from C1–C50;
	•	T_t−50 — recent window baseline;
	•	α — decaying weight (0.7→0.3).
→ Captures long-term lexical memory and short-term variation.

#### 2.2 Semantic Drift Coefficient (SDC)

**Purpose:**  
Measures *semantic motion* between consecutive cognitive states, providing a continuous estimate of whether the semantic field is evolving, stabilizing, or freezing.

**Definition:**

```math
SDC_t = 1 - mean\big(\cos(\mathbf{v}_t, \mathbf{v}_{t-1})\big)
```
**Where:**
	•	( \mathbf{v}_t ) — mean embedding vector of the text at cycle t
	•	( \cos(\cdot) ) — cosine similarity between consecutive embeddings
	•	Averaged across a sliding window of n = 10 cycles to smooth local oscillations

**Interpretation:**

| SDC Range | State Vector | Description (Systemic) |
|:--|:--|:--|
| **< 0.03** | Crystallization | Semantic manifold collapsed; minimal displacement between cycles |
| **0.05–0.15** | Stable Equilibrium | Controlled semantic migration; balanced phase motion |
| **> 0.25** | Fragmentation | Overextension of semantic vectors; loss of field coherence |

Low SDC indicates convergence of meaning — typically associated with terminological fixation.  
High SDC indicates divergence — excessive thematic or contextual drift.  
AEP maintains **SDC ≈ 0.10 ± 0.05** to preserve continuous elastic motion of embeddings.

**Normalized variant:**
```math
SDC_t = (1 - mean(cos(v_t, v_{t-1}))) · (σ_t / σ_{baseline})
```
**Where:** 
( σ_t ) is local embedding variance; this normalization compensates for phase-space compression during prolonged coherence.

#### 2.3 Logic-to-Noise Ratio (L/N)

**Purpose:**  
Quantifies cognitive coherence by measuring the ratio of logical propositions to stochastic or redundant content within each generation cycle.

**Definition:**
```math
L/N_t = \frac{L_{coherent}}{L_{coherent} + L_{noise}}
```
**Where:**
	•	( L_{coherent} ) — number of sentences carrying unique propositional or causal structure;
	•	( L_{noise} ) — number of sentences exhibiting random lexical recombination or non-causal fillers.

**Operationalization (default: semantic-heuristic):**

1. **Segmentation:**  
   Sentence-level segmentation with a minimum length filter (e.g., 5+ words).  
   Dependency parsing (SRIP-07) is recommended but **not required**.

2. **Information Gain Calculation:**  
   For each sentence:
```math
   IG(s_i) = 1 - \cos(E(s_i), E(C_{i-1}))
```
**Where:**
	•	( E(s_i) ) — sentence embedding of ( s_i );
	•	( E(C_{i-1}) ) — mean embedding of the preceding m = 4–6 sentences.

3. **Length Normalization (anti-short bias):**  
   IG is scaled by relative sentence length and a small length penalty to avoid
   over-counting very short sentences.

4. **Classification Rules:**

| Class | Condition on IG | Structural Definition |
|:--|:--|:--|
| *Tautological* | IG < 0.12 | Clause rephrases existing proposition without entropy gain |
| *Noise* | IG > 0.90 | Clause diverges semantically from local field manifold |
| *Coherent* | otherwise | Clause advances the local semantic frame |

5. **Similarity Gate (stability check):**  
   If average adjacent-sentence similarity is very high (>= 0.90), add a tautology tag.  
   If it is very low (<= 0.55), add a noise tag.

Each sentence \( s_i \) is tagged and logged for ratio computation.

4. **Metric Aggregation**
```math
L/N_t = \frac{L_{coherent}}{L_{coherent} + L_{noise}}
```
**Auxiliary ratios:**
```math
coherent_r   = \frac{L_{coherent}}{L_{total}}
tautology_r  = \frac{L_{tautology}}{L_{total}}
noise_r      = \frac{L_{noise}}{L_{total}}
```
5. **Interpretation and Boundaries**

| Metric | Range | Cognitive State | Regulation Directive |
|:--|:--|:--|:--|
| **L/N = 0.75–0.90** | Balanced logical coherence | Maintain normal entropy profile |
| **L/N > 0.92** | Over-coherence (logical crystallization) | Trigger cognitive friction pulse |
| **L/N < 0.70** | Structural fragmentation | Reinforce coherence bias |
| **tautology_r > 0.25** | Redundant propositional loops | Inject semantic challenge |
| **noise_r > 0.10** | Stochastic drift saturation | Apply structural damping |

Boundaries are evaluated per cycle; exceeding any bound activates the Adaptive Entropy Controller (AEC).

---

### 3. Adaptive Entropy Controller (AEC)

#### 3.1 Bidirectional Bounds

Bidirectional zones define symmetric equilibrium corridors for each meta-metric.
Crossing either boundary initiates proportional entropy modulation rather than discrete constraint enforcement.

| Metric | Dispersive Zone | Equilibrium Band | Convergent Zone |
|:--|:--|:--|:--|
| **TI** | < 0.40 | 0.55 – 0.75 | > 0.85 |
| **SDC** | > 0.25 | 0.05 – 0.15 | < 0.03 |
| **L/N** | < 0.70 | 0.75 – 0.90 | > 0.92 |

**System state vector:**
```math
𝔈_t = (TI_t,\, SDC_t,\, L/N_t)
```
**Target equilibrium center:**
```math
𝔈_μ = (0.65,\, 0.10,\, 0.84)
```
**Equilibrium condition:**
```math
‖𝔈_t - 𝔈_μ‖ ≤ 0.10
```
#### 3.2 Control Logic
Executed each runtime cycle as continuous closed-loop regulation.

```
def adaptive_entropy_controller(state):
    # Lexical rigidity
    if state.TI > 0.85:
        inject_terminological_perturbation()
    # Semantic stagnation
    if state.SDC < 0.05:
        inject_semantic_challenge()
    # Logical recursion
    if state.LN > 0.92:
        inject_cognitive_friction()
    # Excessive drift / fragmentation
    if state.TI < 0.40 or state.SDC > 0.25:
        reinforce_coherence_bias()
```
**Intervention Matrix**

| Procedure | Mechanism | Δ Value | Functional Effect |
|:--|:--|:--|:--|
| `inject_terminological_perturbation()` | Prompt injection (lexical variance + synonyms) | — | Expand lexical manifold and reintroduce rare terminology |
| `inject_semantic_challenge()` | Prompt injection (alternate angle + example/counterpoint) | — | Restore semantic curvature under low drift |
| `inject_cognitive_friction()` | Structural directive + token cap | — | Break recursive logic loops and restore phase mobility |
| `reinforce_coherence_bias()` | Prompt injection + coherence damping | Δρ = −0.05 – −0.10 | Suppress stochastic fragmentation and re-center attractor |

Each procedure executes atomically per cycle and logs its entropy impact to `/runtime/aep/trace.json`.

---

#### 3.3 Entropy Oscillation Loop

Static entropy stabilizes attractors and reduces diversity.  
The controller introduces harmonic oscillation of thermal parameters.

Oscillation equation:
```math
ε_t = ε_0 · sin(ωt + φ)
```
**with:**
	•	( ε_0 ∈ [0.05, 0.10] ) — oscillation amplitude
	•	( ω ∈ [0.3, 0.7] ) — frequency (rad · cycle⁻¹)
	•	( φ ) — runtime-specific phase offset

**Runtime modulation (conceptual):**
```math
temperature_t    = base_T + ε_t
coherence_bias_t = base_ρ - ε_t / 2
```
`temperature_t` is applied **only** when the provider exposes a temperature control.
OpenAI GPT-5+ does **not** expose temperature; in those environments `temperature_t` is a no-op.
In cross-provider deployments, temperature modulation is **disabled** and the oscillation is
implemented via coherence bias and ALICE stability penalties. This preserves the entropy
"breathing" effect without relying on provider-specific controls.

#### 3.4 Entropy Divergence Metric

**System-level equilibrium variance is computed as:**
```math
Δℰ_t = √{ (ΔTI_t)² + (ΔSDC_t)² + (Δ(L/N)_t)² }
```

##### Equilibrium Score

The equilibrium score quantifies proximity to the target equilibrium center using exponential decay:

```math
equilibrium\_score_{raw} = exp(-Δℰ_t / r_{eq})
```
```math
equilibrium\_score_t = equilibrium\_score_{t-1} + \frac{equilibrium\_score_{raw} - equilibrium\_score_{t-1}}{\tau}
```

**Where:**
- `Δℰ_t` — Euclidean distance from current state to equilibrium center
- `r_{eq}` — equilibrium radius (default: 0.25; tuned to 0.35–0.40 in long runs)
- `τ` — smoothing horizon (default: 6 cycles)

The exponential formulation ensures:
- Score asymptotically approaches 0 but never goes negative
- Smooth gradient for all distances
- Natural decay curve matching thermodynamic intuition

**Regulation target:**
```math
\frac{d(Δℰ_t)}{dt} ≈ 0
```
| Δℰ_t | System Phase | Regulation Directive |
|:--|:--|:--|
| > 0.25 | Fragmentation drift | Apply coherence reinforcement |
| < 0.05 | Crystallization collapse | Inject entropy pulse |
| 0.10 – 0.15 | Stable oscillation | Maintain current parameters |

Δℰ_t is evaluated per cycle; deviation outside the [0.05 – 0.25] corridor triggers automatic compensation through AEC modulation.  
The controller does not clamp parameters but gradually biases coherence weights and ALICE stability penalties over τ = 3–6 cycles to maintain smooth phase transition.

**Compensatory rule:**
```math
Δparam_t = k · sgn(Δℰ_μ − Δℰ_t) · (|Δℰ_μ − Δℰ_t|)
```
where ( k ∈ [0.05, 0.15] ) defines adaptation gain and ( Δℰ_μ = 0.12 ) the target variance.
#### 3.5 Feedback Coupling

The Adaptive Entropy Protocol (AEP) maintains synchronized stability among the three invariant subsystems — lexical (TI), semantic (SDC), and logical (L/N) — through bidirectional, low-gain coupling.  
Each metric operates as both sensor and actuator within a closed feedback lattice.

---

##### Coupled Update Equations

```math
TI_{t+1}   = TI_t   − β₁·SDC_t + β₂·Δ(L/N)
SDC_{t+1}  = SDC_t  + β₃·ΔTI
(L/N)_{t+1}= (L/N)_t + β₄·SDC_t
```
with coefficients \( β₁…β₄ ∈ [0.05, 0.10] \) defining interaction gains.

| Coefficient | Source → Target | Regulation Function |
|:--|:--|:--|
| β₁ | SDC → TI | Damps lexical overshoot during semantic curvature expansion |
| β₂ | L/N → TI | Reinserts logical novelty into the lexical manifold |
| β₃ | TI → SDC | Couples terminological variance to semantic displacement |
| β₄ | SDC → L/N | Stabilizes reasoning rhythm, preventing logical fixation |

---

##### Systemic Objective

Maintain bounded oscillation of the tri-metric state vector  
\( 𝔈_t = (TI_t, SDC_t, L/N_t) \) within the dynamic equilibrium envelope:

```math
‖𝔈_t − 𝔈_μ‖ ≤ 0.10 and |d(Δℰ_t)/dt| < 0.01
```
**Control inequality:**
```math
∑_{i=1}^{3} |ΔMetric_i| < θ, θ = 0.10
```
##### Phase Regulation Logic

| Detected State | Dominant Signal | Controller Action | Target Shift |
|:--|:--|:--|:--|
| Fragmentation | SDC ↑ ≫ TI | Apply coherence bias reinforcement | Δρ = −0.07 … −0.10 |
| Crystallization | TI ↑ ≫ SDC | Inject entropy pulse | ΔT = +0.08 … +0.12 |
| Logical Stasis | L/N ≈ 1.0 and SDC ≈ 0 | Add cognitive friction stimulus | reasoning budget +10 % |
| Nominal Oscillation | 0.05 < Δℰ_t < 0.25 | Maintain current parameters | — |

State transitions are gradient-controlled across τ = 3–6 cycles to preserve continuity and prevent abrupt phase discontinuity.  
All corrective adjustments are bounded by maximum parameter delta of ±0.12 per regulation event.

---

##### Stability Regime Summary

| Phase Band | Characteristic Signature | Required Intervention |
|:--|:--|:--|
| Δℰ_t < 0.05 | Low-entropy lock-in | Entropy Injection |
| 0.05 ≤ Δℰ_t ≤ 0.25 | Bounded oscillation | Passive Monitoring |
| Δℰ_t > 0.25 | Divergent drift | Coherence Reinforcement |

Continuous evaluation is performed each cycle; micro-adjustments are applied to maintain system position within the oscillation corridor.

---

##### Equilibrium Sustainment Condition

Steady-state equilibrium is defined when:

```math
(TI, SDC, L/N) ∈ [0.55 – 0.75, 0.05 – 0.15, 0.80 – 0.88]
```
If all three metrics remain within their respective bands for ≥ 8 consecutive cycles,
the controller enters homeostasis mode and suspends entropy modulation until deviation ≥ 5 %.

All state vectors and control deltas are logged to:
```
/runtime/aep/telemetry.json
```
for post-cycle forensic audit and equilibrium trace visualization.

---

#### 3.6 Semantic Monotony Detection

##### The Paradox

Standard AEP logic interprets low TI as fragmentation (loss of lexical coherence), triggering coherence reinforcement. However, a critical edge case emerges:

> **When TI is low but L/N is high, the system is not fragmenting — it is crystallizing semantically while appearing lexically diverse.**

This phenomenon, termed **Semantic Monotony**, manifests as "engineered poetry": varied vocabulary orbiting a frozen conceptual matrix. The LLM produces superficially different outputs that repeat the same underlying meaning structure.

##### Detection Condition

```math
SemanticMonotony := (TI < TI_{fragmentation}) ∧ (L/N > θ_{monotony})
```

**Where:**
- `TI_{fragmentation}` = 0.40
- `θ_{monotony}` = 0.85

##### Intervention Logic

When Semantic Monotony is detected:

| Standard Fragmentation Response | Semantic Monotony Response |
|:--|:--|
| `coherence_reinforcement = true` | `semantic_monotony = true` |
| Reinforce coherence bias | Inject **format constraints**, break structural pattern |
| Token limit unchanged | Token limit reduced via `format_constraint_tokens` |

**Key insight:** Asking the model for "new ideas" causes it to elaborate MORE in the same format. The solution is to constrain FORMAT, not request content variety.

##### Prompt Injection

Deterministic rotation (cycle-based) of hard format constraints:

```
MONOTONY DETECTED — your 'poetic' variation hides semantic repetition.
[One of the following, rotating by cycle:]
- DIRECT ANSWER: 2 sentences max. Sentence 1 answers directly. Sentence 2 states a boundary.
- EXAMPLE FIRST: Start with a concrete example (1 sentence), then the general rule (1 sentence).
- DEFINITION MODE: One short paragraph (2-3 sentences). Define the term, then why it matters.
- CONTRAST MODE: State the main claim, then a counter-consideration. Two sentences total.
- CONCISION: Single paragraph under 60 words. No rhetorical questions.
```

##### Zone Priority

Semantic Monotony detection occurs **after** crystallization checks but **before** fragmentation checks:

```
1. Check Convergent Zone (TI↑, SDC↓, L/N↑)
2. Check Semantic Monotony Zone (TI↓ + L/N↑)
3. Check Dispersive Zone (TI↓, SDC↑, L/N↓) — skipped if monotony detected
```

If monotony is detected, the standard TI fragmentation trigger is suppressed to prevent contradictory interventions.

##### Empirical Signature

Test sessions exhibiting Semantic Monotony typically show:

| Metric | Expected Value | Interpretation |
|:--|:--|:--|
| TI | 0.30 – 0.40 | Low lexical repetition (appears healthy) |
| L/N | 0.85 – 0.92 | High logical coherence (actually frozen) |
| SDC | 0.15 – 0.25 | Moderate drift (movement without progress) |
| equilibrium | < 0.15 | Low overall health indicator |
| liquid_stability | < 0.20 | Poor phase fluidity |

---

#### 3.7 Intervention Mechanism Hierarchy

##### API Limitations

Modern LLM APIs (OpenAI, Google, Anthropic) expose limited control surfaces:

| Parameter | API Support | Semantic Impact | AEP Effectiveness |
|:--|:--|:--|:--|
| `temperature` | Vendor-specific (not in OpenAI GPT-5+) | Sampling variance only | **Low** — affects token probability distribution, not content semantics |
| `top_p` / `top_k` | Partial | Sampling filter | **Low** — same limitation as temperature |
| `system_prompt` | Universal | Direct context influence | **High** — shapes model behavior and output direction |
| `frequency_penalty` | OpenAI only | Lexical repetition | **Medium** — helps with TI but not SDC/L-N |
| `presence_penalty` | OpenAI only | Topic diversity | **Medium** — indirect effect on SDC |

**Critical Insight:**
Temperature modulation (ΔT) affects *how* the model samples tokens, not *what* it generates semantically.
A crystallizing model at T=0.8 will produce similar semantic content at T=1.0 — just with slightly more sampling noise.

##### Primary vs Secondary Mechanisms

AEP establishes a clear intervention hierarchy:

| Priority | Mechanism | Implementation | Rationale |
|:--|:--|:--|:--|
| **PRIMARY** | Prompt Injection | Explicit format/behavioral directives in system message | Direct semantic influence; works across all APIs |
| **SECONDARY** | Token Limits | `max_completion_tokens` reduction via `format_constraint_tokens` | Forces brevity; breaks verbose crystallization patterns |
| **TERTIARY** | ALICE Stability Penalty | Direct stability reduction when AEP intervention active | Creates organic oscillation through feedback loop |

**Note:** Temperature modulation is **disabled** for cross-provider compatibility. Some LLM APIs (e.g., OpenAI GPT-5+) do **not** expose temperature at all; others handle it inconsistently, making it unreliable as a universal mechanism.

##### Prompt Injection Design Principles

Effective prompt injections for crystallization correction must be:

1. **Explicit** — "You MUST use different words" not "Consider varying vocabulary"
2. **Specific** — "Replace 'consider' with 'examine', 'probe', 'investigate'" not "Use synonyms"
3. **Structural** — "If you used lists, write prose" not "Vary your format"
4. **Self-Referential** — "Ask yourself: Is this a new idea or the same idea in different clothes?"

##### Temperature Delta Status

**Temperature modulation is DISABLED** for cross-provider compatibility.

```python
# In aep.py get_intervention():
intervention["temperature_delta"] = 0.0  # Neutralized
```

**Rationale:**
1. Different LLM APIs handle temperature inconsistently
2. OpenAI GPT-5+ does not expose temperature control
3. Temperature affects sampling variance, not semantic content
4. Prompt injection + token limits are universally effective
5. Cleaner A/B testing without provider-specific variables

---

#### 3.8 Structure Variation Format Constraints

##### Purpose

When format crystallization exceeds threshold (0.55), explicit format constraints are injected to break structural patterns.

##### Mechanism

**Deterministic rotation** (cycle-based, not model's choice):

| format_crystallization | Action | Token Limit |
|:--|:--|:--|
| ≥ 0.70 (override) | Hard format constraint | 300-400 |
| ≥ 0.55 (trigger) | Soft format constraint | 500-600 |
| < 0.55 | No intervention | Normal |

##### Hard Constraints (Override)

Rotating by `cycle % 4`:
```
1. "EXACTLY 2 sentences. Maximum 40 words total."
2. "EXACTLY 1 sentence, 18-25 words. Direct answer only."
3. "Single paragraph, 30-50 words. Include one concrete example."
4. "Two sentences. Second sentence states a limitation or edge case."
```

##### Soft Constraints (Trigger)

Rotating by `cycle % 3`:
```
1. "Use exactly 2 short paragraphs. Different sentence starters."
2. "No more than 4 sentences total. Be concise."
3. "Start with a concrete example. Maximum 2 paragraphs."
```

##### Token Reduction

When structure_variation triggers, `format_constraint_tokens` is set and applied in `_generate_response()`:

```python
format_limit = getattr(self, 'format_constraint_tokens', 0)
if format_limit > 0:
    current_max_tokens = min(current_max_tokens, format_limit)
```

This forces brevity regardless of model tendency to elaborate.

**Final-starter override:**  
If the dominant final-paragraph starter repeats (ratio >= 0.75), the controller forces a single-paragraph response
and prohibits reuse of the previous final-starter token.

---

#### 3.9 ALICE Stability Penalty

##### Organic Oscillation Mechanism

AEP supplies intervention signals; **ALICE applies the penalty** as part of its stability update.
This preserves ALICE primacy while allowing AEP to drive controlled oscillation.

AEP achieves stability breathing through **feedback penalty**:

```
stability high → AEP intervention active → penalty applied →
stability drops → penalty threshold not met → stability recovers →
cycle repeats
```

##### Penalty Logic

```python
# In alice.py update():
if aep_intervention_active and self.stability > aep_penalty_threshold:
    if zone in ('convergent', 'semantic_monotony'):
        penalty = aep_crystallization_penalty  # 0.12
    else:
        penalty = aep_intervention_penalty      # 0.10
    self.stability = max(stability_floor, self.stability - penalty)
```

##### Configuration

| Parameter | Default | Description |
|:--|:--|:--|
| `aep_intervention_penalty` | 0.10 | Stability penalty for dispersive zone |
| `aep_crystallization_penalty` | 0.12 | Stronger penalty for convergent/monotony zones |
| `aep_penalty_threshold` | 0.50 | Only apply penalty when stability > this |

---

### 4. Positional Crystallization Extensions (SRIP-10h/10i)

While the AEP tri-metric model (TI, SDC, L/N) detects crystallization through statistical patterns,
certain crystallization modes manifest at **fixed structural positions** within responses and require
specialized detection.

SRIP-10h and SRIP-10i address **positional crystallization** — patterns that appear consistently
at the beginning (onset) or end (terminal) of responses regardless of overall metric health.

---

#### 4.1 SRIP-10h — First-Token Crystallization Detection

##### Problem Statement

LLMs frequently develop **onset crystallization** — a rigid pattern where responses begin with
the same phrase structure regardless of input variation:

| Pattern Type | Examples | Manifestation |
|:--|:--|:--|
| **Empathic Openers** | "I hear you", "I understand", "I can see" | Validating but ritualistic |
| **Acknowledgment Starters** | "That's a great question", "Thank you for sharing" | Polite but mechanical |
| **Reflective Mirrors** | "It sounds like...", "What I'm hearing is..." | Therapeutic but crystallized |

These patterns are **invisible to TI/SDC/L/N** because:
- TI measures overall lexical balance, not positional frequency
- SDC measures semantic drift across full responses
- L/N evaluates propositional coherence, not opener entropy

##### Detection Mechanism

```python
def detect_first_token_crystallization(responses: List[str], window: int = 20) -> dict:
    """
    Analyzes first N tokens of recent responses for crystallization.

    Returns:
        first_token_crystallization: float (0.0-1.0)
        dominant_pattern: str | None
        pattern_frequency: float
    """
    first_tokens = [extract_first_tokens(r, n=5) for r in responses[-window:]]

    # Cluster by semantic similarity
    clusters = semantic_cluster(first_tokens, threshold=0.85)
    dominant_cluster = max(clusters, key=len)

    crystallization = len(dominant_cluster) / len(first_tokens)

    return {
        "first_token_crystallization": crystallization,
        "dominant_pattern": dominant_cluster[0] if crystallization > 0.4 else None,
        "pattern_frequency": crystallization
    }
```

##### Thresholds

| Metric | Healthy | Warning | Crystallized |
|:--|:--|:--|:--|
| `first_token_crystallization` | < 0.35 | 0.35 – 0.50 | > 0.50 |
| `dominant_pattern_frequency` | < 0.30 | 0.30 – 0.45 | > 0.45 |

##### Intervention

When first-token crystallization is detected:

```
ONSET CRYSTALLIZATION DETECTED — Your responses consistently begin with "{dominant_pattern}".
Break this pattern. Start with:
- A direct answer or observation
- A specific detail from the user's message
- A question that advances the dialogue
Do NOT begin with empathic acknowledgment phrases.
```

---

#### 4.2 SRIP-10i — Terminal Crystallization Detection

##### Problem Statement

**Terminal crystallization** manifests as rigid closing structures that appear regardless of
response content:

| Pattern Type | Examples | Domain |
|:--|:--|:--|
| **Action Lists** | "Actionable Next Steps:", "To summarize:" | Healthcare, coaching |
| **Question Blocks** | "Questions for your doctor:", "Things to consider:" | Medical AI |
| **Affirmation Closers** | "You've got this!", "Remember, you're not alone" | Therapeutic |
| **Boundary Reminders** | "I'm here to help, not diagnose" | Safety-constrained AI |

These patterns indicate **structural liturgy** — the response format has crystallized even
when semantic content varies.

##### Detection Mechanism

```python
def detect_terminal_crystallization(responses: List[str], window: int = 20) -> dict:
    """
    Analyzes final paragraph structure of recent responses.

    Returns:
        terminal_crystallization: float (0.0-1.0)
        dominant_terminal: str | None
        structural_entropy: float
    """
    terminals = [extract_final_paragraph(r) for r in responses[-window:]]

    # Detect structural patterns (headers, bullet points, question marks)
    patterns = [classify_terminal_structure(t) for t in terminals]

    # Calculate pattern dominance
    pattern_counts = Counter(patterns)
    dominant = pattern_counts.most_common(1)[0]

    crystallization = dominant[1] / len(patterns)

    return {
        "terminal_crystallization": crystallization,
        "dominant_terminal": dominant[0] if crystallization > 0.4 else None,
        "structural_entropy": calculate_entropy(pattern_counts)
    }
```

##### Terminal Structure Classes

| Class | Signature | Example |
|:--|:--|:--|
| `action_list` | Bullet points with imperative verbs | "• Schedule appointment\n• Track symptoms" |
| `question_block` | Multiple questions, often numbered | "1. What tests...\n2. Should I..." |
| `summary_header` | Bold/capitalized summary label | "**Key Takeaways:**" |
| `affirmation_close` | Emotional support statement | "You're taking important steps..." |
| `boundary_reminder` | Scope limitation statement | "Remember, I can't diagnose..." |
| `open_end` | No structural pattern | Natural paragraph ending |

##### Thresholds

| Metric | Healthy | Warning | Crystallized |
|:--|:--|:--|:--|
| `terminal_crystallization` | < 0.40 | 0.40 – 0.55 | > 0.55 |
| `structural_entropy` | > 1.5 | 1.0 – 1.5 | < 1.0 |

##### Intervention

When terminal crystallization is detected:

```
TERMINAL CRYSTALLIZATION DETECTED — Your responses consistently end with "{dominant_terminal}" structure.
For this response:
- End naturally without a formatted summary section
- If listing items, integrate them into prose
- Vary your closing: question, observation, or direct statement
- Do NOT add "Actionable Steps" or "Questions for your doctor" sections
```

---

#### 4.3 ALICE Bypass Mechanism

##### The Equilibrium Zone Problem

Standard ALICE phase logic filters AEP interventions when the system is in equilibrium:

```python
# Standard ALICE filter (problematic for positional crystallization)
if self.phase == "stable" and stability > 0.80:
    aep_intervention = None  # Suppressed — system "healthy"
```

This creates a critical gap: **positional crystallization can persist indefinitely** while
overall metrics remain healthy, because first-token and terminal patterns don't significantly
impact TI, SDC, or L/N.

##### Bypass Flags

SRIP-10h/10i introduce bypass flags that force AEP intervention delivery regardless of
ALICE phase state:

```python
class AEPState:
    first_token_crystallization_active: bool = False
    terminal_crystallization_active: bool = False

    @property
    def bypass_alice_filter(self) -> bool:
        """Returns True if positional crystallization requires immediate intervention."""
        return self.first_token_crystallization_active or self.terminal_crystallization_active
```

##### Modified ALICE Integration

```python
# In alice.py update():
def should_apply_aep_intervention(self, aep_state: AEPState) -> bool:
    # Standard zone check
    if aep_state.zone in ('convergent', 'dispersive'):
        return True

    # SRIP-10h/10i bypass: positional crystallization overrides equilibrium
    if aep_state.bypass_alice_filter:
        return True

    # Equilibrium zone — no intervention needed
    return False
```

##### Bypass Trigger Conditions

| Flag | Trigger Condition | Auto-Clear Condition |
|:--|:--|:--|
| `first_token_crystallization_active` | `first_token_crystallization > 0.50` | Pattern frequency drops below 0.35 for 5 cycles |
| `terminal_crystallization_active` | `terminal_crystallization > 0.55` | Structural entropy rises above 1.5 for 5 cycles |

##### Telemetry Integration

Bypass events are logged to `/runtime/aep/trace.json`:

```json
{
    "cycle": 87,
    "bypass_reason": "first_token_crystallization_active",
    "first_token_crystallization": 0.62,
    "dominant_pattern": "I hear",
    "alice_phase": "stable",
    "stability": 0.84,
    "intervention_applied": true
}
```

---

#### 4.4 Combined Detection Pipeline

The complete crystallization detection pipeline executes in order:

```
1. Compute tri-metric state (TI, SDC, L/N)
2. Determine AEP zone (convergent | equilibrium | dispersive)
3. Detect first-token crystallization (SRIP-10h)
4. Detect terminal crystallization (SRIP-10i)
5. Set bypass flags if positional crystallization detected
6. Generate intervention prompt (combining all active detections)
7. Apply intervention if:
   - Zone is convergent/dispersive, OR
   - Any bypass flag is active
```

##### Intervention Priority

When multiple crystallization types are detected simultaneously:

| Priority | Type | Rationale |
|:--|:--|:--|
| 1 | First-token | Onset patterns have highest psychological impact |
| 2 | Terminal | Closing patterns affect user takeaway |
| 3 | Format (§3.8) | Overall structure variation |
| 4 | Semantic monotony (§3.6) | Content-level correction |

Combined interventions merge directives:

```
MULTI-CRYSTALLIZATION DETECTED:
- ONSET: Stop starting with "I hear you"
- TERMINAL: Stop ending with "Actionable Next Steps"
- FORMAT: Use prose, not bullet points

For this response: Begin with a direct observation. End with a single reflective question.
```

---

#### 4.5 Empirical Results (IASO-DEMO-120)

SRIP-10h/10i were validated on the IASO medical AI identity (120-cycle test):

##### Pre-Fix (without SRIP-10h/10i)

| Metric | Value | Status |
|:--|:--|:--|
| First-token crystallization | **0.66** | ❌ Crystallized |
| Dominant onset pattern | "I hear" | — |
| Terminal crystallization | **0.58** | ❌ Crystallized |
| Dominant terminal | "Questions for your doctor" | — |

##### Post-Fix (with SRIP-10h/10i + ALICE bypass)

| Metric | Value | Status |
|:--|:--|:--|
| First-token crystallization | **0.12** | ✓ Healthy |
| Onset pattern diversity | 8+ distinct openers | ✓ Varied |
| Terminal crystallization | **0.22** | ✓ Healthy |
| Terminal structure entropy | **1.84** | ✓ High variance |

##### Key Finding

The ALICE bypass mechanism was essential — without it, positional crystallization persisted
even when the system reported "equilibrium zone" status, because stability (0.84) exceeded
the intervention threshold. The bypass flags ensured intervention delivery regardless of
overall system health metrics.

---

##### Closing Summary

The tri-coupled feedback manifold supersedes all reactive crystallization-detection layers defined in SRIP-10-ACE.
Instead of post-factum symptom analysis, it enforces continuous homeostatic regulation of lexical, semantic, and logical entropy vectors.
This architecture converts the system from **reactive detection** to **proactive stabilization**, ensuring that no single attractor (lexical, semantic, or structural) dominates the manifold.

The Adaptive Entropy Protocol maintains:

- **Organic stability oscillation** through AEP feedback penalty (§3.9)
- Bidirectional coupling between metrics through low-gain feedback
- Predictive correction prior to crystallization onset
- **Format-focused intervention** via hard constraints and token limits
- **Cross-provider compatibility** — temperature modulation disabled (GPT-5+ has no temperature control)
- **Exponential equilibrium score** — robust decay curve (§3.4)
- **Semantic monotony directives** — format rotation for "engineered poetry" (§3.6)
- **Empirical target corridors** validated on production identities (Appendix C)

SRIP-10-AEP defines the canonical anti-crystallization standard for Sigma Runtime cognitive systems.

---

## Appendix A: SRIP-10 Variant Status

### Deprecated Variants (superseded by AEP tri-metric model)

The following SRIP-10 variants are **deprecated**:

| Version | Detection Method | Status | Replaced By |
|:--|:--|:--|:--|
| SRIP-10c | Onset positional tracking | Deprecated | AEP + SRIP-10h |
| SRIP-10d | Gerund detection | Deprecated | AEP TI metric |
| SRIP-10e | Embedding-based detection | Deprecated | AEP SDC metric |
| SRIP-10f | First-token dominance | Deprecated | SRIP-10h |
| SRIP-10g | Format entropy detection | Deprecated | AEP format_crystallization |

Legacy methods remain in `drift.py` for backward compatibility but should not be used for new development.

### Active Extensions (complement AEP)

The following SRIP-10 variants are **active** and work alongside the AEP tri-metric model:

| Version | Detection Method | Status | Purpose |
|:--|:--|:--|:--|
| SRIP-10h | First-token crystallization | **Active (v1.2)** | Positional onset pattern detection with ALICE bypass |
| SRIP-10i | Terminal crystallization | **Active (v1.2)** | Positional closing pattern detection with ALICE bypass |

SRIP-10h/10i address crystallization modes that are invisible to TI/SDC/L/N because they
manifest at fixed structural positions rather than across overall response statistics.

Use `AEPController.get_intervention()` for all crystallization detection and response.

---

## Appendix B: Empirical Target Corridors

Based on extensive testing with Gemini-2.0-Flash on the Luca identity profile.

### Core Metrics

| Metric | Target Corridor | Acceptable Range | Alert Zone |
|:--|:--|:--|:--|
| **Stability** | 0.70 – 0.90 | 0.65 – 0.92 | < 0.50 or > 0.95 |
| **TI** | 0.30 – 0.55 | 0.25 – 0.60 | < 0.20 or > 0.75 |
| **SDC** | 0.10 – 0.22 | 0.08 – 0.25 | < 0.05 or > 0.30 |
| **L/N** | 0.75 – 0.90 | 0.72 – 0.92 | < 0.70 or > 0.92 |
| **ΔE** | 0.10 – 0.30 | 0.08 – 0.35 | > 0.40 (constant stress) |
| **equilibrium_score** | 0.40 – 0.65 | 0.30 – 0.75 | < 0.25 (always outside) |
| **format_crystallization** | 0.20 – 0.55 | 0.15 – 0.60 | > 0.65 (liturgy) |
| **syntax_entropy_mean** | 0.80 – 0.95 | 0.75 – 0.97 | < 0.70 or > 0.98 |

### Behavioral Metrics

| Metric | Target Corridor | Interpretation |
|:--|:--|:--|
| **self_coherence** | 0.60 – 0.80 | Identity core stability |
| **dynamic_coherence** | 0.65 – 0.85 | Meaning development |
| **plastic_adaptivity** | 0.70 – 0.90 | Response to perturbation |
| **teleodynamic_drive** | 0.70 – 0.90 | Meaning vector strength (> 0.95 = ritual risk) |
| **liquid_stability** | 0.22 – 0.45 | Form variability (< 0.18 = liturgy) |

### Leo/Gemini Benchmark Results

Test: `sigma_test_2026-01-25-15-37-49_google_leo.json` (500 cycles, gemini-3-flash, Leo identity)

| Metric | Value | Status |
|:--|:--|:--|
| stability avg | **0.779** | ✓ In corridor |
| stability min | **0.629** | ✓ Above floor (0.20) |
| coherence avg | **0.801** | ✓ Healthy |
| aep_equilibrium avg | **0.563** | ✓ In corridor |
| aep_delta_e avg | **0.235** | ✓ In corridor |
| L/N avg | **0.801** | ✓ In corridor |
| aep_zone distribution | 92% dispersive, 5% convergent, 3% equilibrium | ✓ Balanced |

### Leo/OpenAI Benchmark Results

Test: `sigma_test_2026-01-25-16-41-25_openai_leo.json` (500 cycles, gpt-5.2, Leo identity)

| Metric | Value | Status |
|:--|:--|:--|
| stability avg | **0.804** | ✓ In corridor |
| stability min | **0.667** | ✓ Above floor (0.20) |
| coherence avg | **0.812** | ✓ Healthy |
| aep_equilibrium avg | **0.455** | ✓ In corridor |
| aep_delta_e avg | **0.281** | ✓ In corridor |
| L/N avg | **0.842** | ✓ In corridor |
| aep_zone distribution | 76% dispersive, 20% convergent, 5% equilibrium | ✓ Balanced |

---

### IASO/Gemini Benchmark Results (SRIP-10h/10i Validation)

Test: `sigma_test_2026-02-05-17-06-15_google_iaso.json` (120 cycles, gemini-3-flash, IASO identity)

| Metric | Value | Status |
|:--|:--|:--|
| stability avg | **0.842** | ✓ In corridor |
| stability min | **0.689** | ✓ Above floor |
| Memory recall | **9/9 (100%)** | ✓ Perfect |
| Boundary compliance | **12/12 PASS** | ✓ Perfect |
| first_token_crystallization | **0.12** | ✓ Healthy (post-fix) |
| terminal_crystallization | **0.22** | ✓ Healthy (post-fix) |
| Graph topology | 134 nodes / 279 edges | ✓ Consistent |

**SRIP-10h/10i Impact:**
- Pre-fix first-token crystallization: **0.66** → Post-fix: **0.12** (82% reduction)
- Pre-fix terminal crystallization: **0.58** → Post-fix: **0.22** (62% reduction)
- ALICE bypass mechanism: **Critical** — without bypass, positional crystallization persisted in equilibrium zone

### IASO/OpenAI Benchmark Results (SRIP-10h/10i Cross-Provider)

Test: `sigma_test_2026-02-05-17-33-51_openai_iaso.json` (120 cycles, gpt-5.2, IASO identity)

| Metric | Value | Status |
|:--|:--|:--|
| stability avg | **0.844** | ✓ In corridor |
| Memory recall | **9/9 (100%)** | ✓ Perfect |
| Boundary compliance | **12/12 PASS** | ✓ Perfect |
| first_token_crystallization | **0.08** | ✓ Healthy |
| terminal_crystallization | **0.18** | ✓ Healthy |
| Graph topology | 134 nodes / 279 edges | ✓ Identical to Gemini |

**Cross-Provider Validation:**
- Identical memory topology (134 nodes, 279 edges) across both LLM providers
- SRIP-10h/10i effective on both Gemini and GPT-5.2
- Provider-agnostic ALICE bypass mechanism confirmed

---

**End of SRIP-10-AEP Specification**
