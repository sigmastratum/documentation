> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-11: Compression & Memory Topology
**Version:** 1.0
**Status:** Active
**Applies to:** SIGMA Runtime ≥ v0.5.3
**Depends on:** SRIP-09 (LTM), SRIP-10 (AEP)
**Author:** Sigma Stratum Research Group
**Date:** 2026-01-30
**License:** CC BY-NC 4.0 / Canon CIL Applicable


---

## I. Purpose  
SRIP-11 defines the architecture of *structural memory compression* and *semantic topology* within Sigma Runtime.  
Its goal is to reduce redundancy in long-term storage while preserving continuity of reasoning across extended cycles (≥ 500–5000).  
Memory becomes *topological*: a self-organizing lattice of semantic nodes connected by relational weight rather than linear order.

---

## II. Core Concepts  

| Term | Description |
|------|--------------|
| **Rib Point** | A periodic semantic condensation summarizing ≈ 10–50 cycles into a stable concept node. |
| **Cluster** | A set of rib points forming a thematic region (≈ 250 cycles). |
| **Lattice** | Graph of clusters connected by semantic edges (continuity vectors). |
| **Continuity Vector** | The direction of reasoning across cycles — derived from semantic gradient rather than text. |
| **Density Coefficient** | Local measure of information per token (symbolic density). Used for adaptive compression. |
| **Phase Lineage** | Inherited reasoning state (phase → phase) tracked through edges with type `follows` or `transforms`. |
| **Anchor Facts Layer (AFL)** | A priority memory layer for low-similarity but high-importance facts (names, identifiers, constraints). |

---

## III. System Functions  

### 1. Dynamic Compression Loop  
Every N cycles (default = 10 or 50):  
- Compute semantic centroid of the last N embeddings.  
- Estimate symbolic density and entropy.  
- Generate a compressed representation (text + vector).  
- Store as Rib Point in the vector store and connect to its parents in the graph store.
```
Cycle → Embedding → Centroid → Rib Point → Cluster
```
### 2. Adaptive Retention  
Compression is not uniform:  
records with high density and low redundancy are retained longer;  
ephemeral ones are merged or pruned.  
Retention weight = `(density × coherence) / entropy`.

### 3. Topological Retrieval  
Recall operates through graph propagation rather than flat similarity:
- Input query → encode vector  
- Find nearest rib points → expand through connected edges weighted by phase lineage  
- Return contextual subgraph as memory summary.

### 4. Phase-Aware Recall
Memory is filtered by phase compatibility (`forming`, `stable`, `reflection`, `fragmenting`).
This prevents semantic cross-contamination between developmental stages of reasoning.

Phase compatibility matrix:
| Current Phase | Compatible Recall Phases |
|---------------|--------------------------|
| `forming` | forming, stable |
| `stable` | stable, reflection |
| `reflection` | reflection, stable, fragmenting |
| `fragmenting` | fragmenting, reflection |

### 5. Anchor Facts Layer (AFL)
Semantic similarity fails on certain anchor facts (e.g., names, identifiers, fixed constraints).
SRIP-11 defines a priority retrieval path that is **domain-agnostic** and **always available** in context.

**AFL Responsibilities:**
- Preserve low-similarity, high-importance facts (names, IDs, numbers, commitments).
- Inject anchor facts into every prompt (or into every memory recall).
- Operate independently of semantic similarity thresholds.

**AFL Retrieval Order:**
1. Anchor Context (first N cycles raw)
2. Known Facts (model-extracted structured facts)
3. Topological recall (Rib Points / Clusters)
4. Semantic similarity fallback

#### 5a. Anchor Buffer (Minimal Implementation)
First N cycles are stored verbatim and always injected into context.
```
cmt:
  anchor_buffer:
    enabled: true
    cycles: 8  # First N cycles always included as anchor context
```

#### 5b. Model-Driven Fact Extraction (AFL v2)
The model extracts key facts dynamically — not limited to first N cycles.

**Triggers (language-agnostic):**
- Early cycles: first N cycles (default: 3) — likely introductions
- Periodic: every N cycles (default: 10)

No hardcoded patterns. The model decides what to extract.

**Fact Categories (universal):**
- `identity`: name, age, role, profession
- `context`: location, goals, time constraints
- `constraints`: limitations, allergies, restrictions
- `relationships`: family, colleagues, dependencies
- `history`: past events, background
- `commitments`: promises, deadlines, agreements
- `preferences`: likes, dislikes, communication style

**Configuration:**
```
cmt:
  fact_extraction:
    enabled: true
    interval: 10           # Extract every N cycles
    early_cycles: 3        # Always extract on first N cycles
    min_confidence: 0.7    # Minimum confidence to store
    max_facts: 30          # Maximum facts to store
    # categories: [...]    # Optional: custom categories (domain adapter)
    # extraction_prompt: "..." # Optional: custom prompt
```

**Safety:** Only USER messages are used for extraction — assistant responses are context only.
This prevents the model from "inventing" facts from its own statements.

**Context Injection Format:**
```
[KNOWN FACTS — use these details in responses, especially summaries]
  IDENTITY:
    - name: Maria
    - age: 52
    - profession: accountant
  CONSTRAINTS:
    - allergy_penicillin: allergic to penicillin
  RELATIONSHIPS:
    - sister_condition: Hashimoto's thyroiditis
```

#### 5c. Domain Adapter (Optional, Pluggable)
```
cmt:
  domain_adapter: null  # or one of the following:
    # BASE
    # - "conversational"   # general assistant (recommended default)

    # SPECIALIZED
    # - "healthcare"       # medical AI (names, allergies, medications)
    # - "defense"          # military/security (callsign, clearance, constraints)
    # - "business"         # enterprise (role, company, KPIs, stakeholders)
    # - "education"        # learning (level, goals, progress)
    # - "legal"            # legal (client, case, jurisdiction, deadlines)
    # - "technical"        # engineering (project, stack, architecture)
```
Adapters define domain-specific entity extraction patterns but do not alter core AFL logic.
When `null`, only `anchor_buffer` + `fact_extraction` operate universally.

#### 5d. Identity-Adaptive Compression (v0.5.3)
Compression behavior can be customized per identity via the `behavior:` section in `traits_*.yaml`.
This section is **NOT injected into the prompt** — it controls internal system parameters only.

**Configuration:**
```yaml
# traits_iaso.yaml (example)
behavior:
  compression:
    list_tolerance: 0.6       # 0.0-1.0: how much to allow lists (>= 0.8 = no penalty)

  token_policy:
    base_limit: 900           # Override default token limit
    min_limit: 400            # Minimum allowed
    max_limit: 1200           # Maximum allowed
```

**Behavior:**
- `list_tolerance >= 0.8` → skip list penalty entirely
- `list_tolerance < 0.8` → penalty scaled by `(1 - list_tolerance)`
- `token_policy.base_limit` → overrides system default `max_completion_tokens`

**Use Cases:**
- **Iaso (medical):** Moderate list tolerance (0.6), shorter responses (900 tokens)
- **Default:** Moderate (0.5) for list_tolerance, system default for tokens

### 6. Compression Feedback
The **AEP (Adaptive Entropy Protocol)** monitors compression ratio and semantic loss per SRIP-10.

If semantic loss > threshold (default: 0.25), AEP triggers "phase regeneration":
→ expand compressed nodes temporarily for re-contextualization.

AEP integration points:
- `AEPController.monitor_compression()` — evaluates CR and SL after each Rib Point creation
- `AEPController.trigger_phase_regeneration()` — queues Rib Point for expansion
- Regeneration respects AEP equilibrium state (TI, SDC, L/N)

---

## IV. Data Structures

```python
@dataclass
class RibPoint:
    id: str                       # "RP-{start}-{end}"
    cycle_range: Tuple[int, int]  # (start_cycle, end_cycle) inclusive
    vector: List[float]           # Centroid embedding (384-dim for MiniLM)
    summary: str                  # Compressed text representation
    phase: str                    # Dominant ALICE phase during this range
    density: float                # Mean symbolic_density [0, 1]
    entropy: float                # 1 - mean(pairwise_cosine) [0, 1]
    lineage: List[str]            # Parent Rib Point IDs
    created_at: float             # Unix timestamp
    metadata: Dict[str, Any]      # Additional attributes

    @property
    def retention_weight(self) -> float:
        """Adaptive retention score: (density × coherence) / entropy"""
        coherence = 1.0 - self.entropy
        return (self.density * coherence) / max(0.01, self.entropy)

@dataclass
class Cluster:
    id: str                              # "CL-{index}"
    rib_points: List[str]                # Member Rib Point IDs (5-10)
    centroid: List[float]                # Cluster centroid embedding
    theme: str                           # Extracted theme label
    phase_distribution: Dict[str, int]   # Phase counts within cluster
    cohesion: float                      # Mean pairwise similarity [0, 1]
    created_at: float
```

**Storage:**
- **Graph Store:** `NetworkX` directed graph with typed edges (`follows`, `transforms`, `belongs_to`, `continuity`)
- **Vector Store:** `FAISS` index for Rib Point centroids and Cluster centroids (negative cycle IDs)

---

## V. Compression Policies  

| Policy | Description |
|---------|--------------|
| **per_section** | Compress each logical section (e.g., DN segment or topic). |
| **per_cycle** | Compress after N cycles of interaction. |
| **hybrid** | Alternate micro (10 cycles) and macro (50 cycles) compression. |
| **structural** | Triggered when density > threshold or semantic drift > 0.25. |

---

## VI. Metrics and Monitoring  

| Metric | Definition | Purpose |
|---------|-------------|----------|
| **Compression Ratio (CR)** | Tokens retained / Tokens input | Efficiency |
| **Semantic Loss (SL)** | 1 – cosine similarity(original, compressed) | Fidelity |
| **Topology Cohesion (TC)** | Average edge weight within cluster | Structural stability |
| **Phase Continuity (PC)** | Correlation of reasoning vectors across phases | Cognitive coherence |
| **Anchor Recall Integrity (ARI)** | Anchor facts retrieved / anchor facts declared | Reliability of AFL |
| **Fact Extraction Rate (FER)** | Facts extracted / extraction attempts | Quality of fact extraction |
| **Fact Coverage (FC)** | Categories with ≥1 fact / total categories | Breadth of fact capture |

---

## VII. Expected Outcomes  

- 10× reduction in token footprint for sessions > 500 cycles  
- Improved semantic continuity without context overflow  
- Dynamic memory lattice capable of autonomous reasoning summaries  
- Reliable recall of anchor facts without domain-specific hardcoding

---

**End of SRIP-11 v1.0**
*Sigma Stratum Research Group – 2026*
