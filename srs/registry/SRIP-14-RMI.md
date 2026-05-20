> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-14 — Retrieval and Memory Integration Layer (RMI)
**Runtime-Governed Semantic Recall, Optional External Retrieval, and Structured Memory Injection**

| Field | Value |
| --- | --- |
| SRIP | SRIP-14 |
| Title | Retrieval and Memory Integration Layer (RMI) |
| Version | Public Draft v0.3 |
| Status | Active Proposal / Partial Implementation |
| Date | 2026-05-20 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Memory / Retrieval / Runtime Governance |
| Parent Specs | SRIP-09, SRIP-11 |
| Related Specs | SRIP-01, SRIP-03, SRIP-04, SRIP-06, SRIP-07, SRIP-10, SRIP-12, SRIP-13 |
| License | CC BY-NC 4.0 / Canon CIL Applicable |
| Information Class | Open |
| Change Class | SRS-only |
| Normative Status | Defines the RMI contract for runtime-governed recall, bounded memory injection, provenance, compression, and optional external retrieval. It does not require a specific vector database, embedding model, or provider. |
| Conformance Level | Partial Conformance / Bounded Implementation |
| SRD Synchronization Action | Completed in `/srd/memory.md` and `/srd/attractors.md`. |
| Release Alignment Status | aligned |

---

## I. Purpose

SRIP-14 defines the **Retrieval and Memory Integration Layer (RMI)** for Sigma Runtime.

RMI governs how runtime-owned memory, semantic recall, compression, provenance,
and optional external retrieval are:

- triggered;
- shaped;
- bounded;
- compressed;
- injected into active cognition;
- exposed through audit-safe diagnostics.

Its core principle remains:

> Retrieval may be external.  
> Memory must remain runtime-governed.

RMI exists so that recall strengthens continuity and reasoning instead of
becoming an uncontrolled prompt-expansion path.

---

## II. Problem Statement

Naive RAG architectures commonly collapse into this pattern:

```text
user input -> retrieve chunks -> append chunks to prompt -> generate
```

That pattern creates several failure modes:

- prompt-density overload;
- context flooding;
- irrelevant or stale retrieval;
- identity or session-scope leakage;
- uncontrolled semantic drift;
- hallucinated synthesis from poorly bounded sources;
- poor auditability between retrieved evidence and generated output.

Sigma Runtime requires recall to be governed by runtime state, not by raw
search output.

---

## III. Non-Goals

SRIP-14 does not:

- require one specific vector database;
- require one specific embedding model;
- replace SRIP-09 long-term memory;
- replace SRIP-11 compression and topology;
- define web crawling or marketplace scraping;
- authorize cross-user memory sharing;
- allow raw retrieved chunks to bypass runtime control;
- treat external retrieval output as final answer content;
- claim that every Sigma Runtime deployment already ships with full external
  retrieval support.

---

## IV. Conformance Scope

SRIP-14 defines the normative contract for retrieval-governed memory
integration.

Bounded implementations may satisfy parts of this contract before full
conformance is complete. Typical bounded conformance may include:

- runtime-governed internal semantic recall;
- bounded recall compression;
- structured memory injection;
- scoped provenance;
- bounded observability and degradation behavior.
- optional perturbation-oriented retrieval when retrieval is explicitly treated
  as exploratory, non-authoritative signal and remains subordinate to runtime
  stability controls.

Full conformance requires explicit retrieval-governance semantics across
internal and optional external retrieval surfaces, with sufficient provenance,
auditability, and interoperability with SRIP-09, SRIP-11, and SRIP-15 when
retrieval is used as a perturbation source.

---

## V. Core Concepts

| Term | Definition |
|------|------------|
| **Retrieval Source** | External or internal system capable of returning candidate knowledge records. |
| **External Retrieval Source** | Third-party API, vector DB, document service, search system, or partner knowledge backend. |
| **Internal Semantic Store** | Runtime-owned semantic recall substrate containing embeddings, summaries, hashes, and scoped metadata for the active runtime/session layer. |
| **Structural Memory Store** | Runtime-owned lineage, graph, topology, attractor, and temporal memory substrate as defined by SRIP-09 and SRIP-11. |
| **Retrieval Decision** | Runtime decision about whether recall is needed for the current turn. |
| **Query Shaping** | Transforming user intent and runtime state into bounded recall queries. |
| **Retrieval Envelope** | Limits applied to recall: scope, result count, confidence, freshness, and semantic load budget. |
| **Retrieved Evidence** | Candidate records returned by retrieval sources. |
| **Recall Compression** | Compression of retrieved evidence into structured runtime state. |
| **Memory Injection** | Controlled insertion of compressed recall into interpretation or reasoning layers. |
| **Source Provenance** | Metadata identifying origin, timestamp, scope, confidence, and retrieval path. |
| **Memory Resolution Snapshot** | Runtime summary of what recall was considered, injected, suppressed, or degraded for a turn. |
| **Perturbation Retrieval** | Optional retrieval mode that provides exploratory contrast or adjacent signal under SRIP-15 control, without treating retrieved evidence as authoritative memory. |

---

## VI. Architectural Position

RMI sits inside the canonical runtime loop, primarily during interpretation and
pre-generation control:

```text
User Input
  -> State Ingestion
  -> Interpretation Pass
      -> Retrieval Decision
      -> Query Shaping
      -> Internal Recall and/or Optional External Retrieval
      -> Recall Compression
      -> Structured Memory Injection
      -> Memory Resolution Snapshot
  -> Stabilization / Control
  -> Generation
  -> Output Validation
  -> Field Update
```

RMI is not a direct prompt-append layer.

It is a runtime-governed semantic recall layer.

Bounded implementations may realize this layer through internal semantic
recall, nucleus anchoring, retrieval filtering, checkpoint-aware bounded
recovery, or other runtime-governed memory integration strategies.

---

## VII. Storage Model

SRIP-14 permits three storage levels, but their maturity need not be equal in
every implementation.

### 1. External Retrieval Storage

External storage may include:

- external vector databases;
- search APIs;
- document stores;
- knowledge-base APIs;
- partner retrieval services.

External retrieval is allowed by SRIP-14, but it is not required for minimum
conformance.

### 2. Internal Semantic Store

The runtime should maintain its own semantic store for:

- embeddings;
- summaries;
- semantic hashes;
- provenance metadata;
- scope metadata;
- recall history;
- confidence and fallback markers.

Bounded implementations may realize this through runtime-owned semantic memory,
checkpoint-aware bounded state, and memory-resolution diagnostics.

### 3. Structural Memory Store

For full SRIP-14 alignment with SRIP-09 and SRIP-11, the runtime should
maintain or integrate with a structural memory store containing:

- cycle lineage;
- graph/topology relations;
- attractor-relevant phase transitions;
- recovery events;
- static nucleus anchors;
- trace-ledger references;
- temporal reconstruction metadata.

Bounded implementations may realize this through graph-like lineage,
compression topology, or equivalent structural machinery. Full SRIP-09
structural-memory conformance remains a stronger target than minimum SRIP-14
conformance.

---

## VIII. Retrieval Decision Rules

RMI must decide whether retrieval is needed before invoking internal or
external recall.

Retrieval SHOULD be triggered when:

- the user asks for stored or previously established knowledge;
- current active context lacks required continuity facts;
- long-term or checkpointed memory is needed for coherence;
- runtime needs recall provenance or replayable bounded state;
- a task depends on prior artifacts, structured facts, or remembered context.

Retrieval SHOULD NOT be triggered when:

- the answer is already available from active context;
- retrieval would exceed the semantic load budget;
- the target source is outside authorized scope;
- retrieval risks cross-session or participant leakage;
- the query is purely conversational and continuity does not require recall.

Retrieval should remain runtime-mediated rather than automatic prompt stuffing.

---

## IX. Query Shaping

Queries must be shaped by runtime state before dispatch.

Minimum shaping inputs are:

- user intent;
- current session scope;
- participant scope;
- active task or continuity target;
- active memory anchors;
- permitted retrieval source;
- semantic density budget;
- freshness requirement;
- privacy and scope constraints.

Bounded implementations may realize query shaping through session-scoped recall,
phase-aware filters, nucleus anchoring, recall suppression, and checkpoint-aware
memory resolution.

Query shaping must not leak hidden policy, private memory, or unrelated session
context into external retrieval systems.

---

## X. Retrieval Envelope

Every retrieval request must carry a bounded retrieval envelope.

Minimum shape:

```json
{
  "source": "internal_or_external",
  "scope": "session|agent|workspace|public",
  "max_results": 5,
  "max_tokens": 1200,
  "freshness_required": false,
  "confidence_floor": 0.65,
  "session_id": null,
  "participant_scope": null,
  "provenance_required": true
}
```

The envelope exists to prevent uncontrolled recall expansion.

Bounded implementations may enforce retrieval envelopes through result limits,
compression budgets, recall suppression, fallback narrowing, and scope-aware
constraints.

---

## XI. Recall Compression

Retrieved evidence must be compressed before injection.

Recall compression should produce structured runtime state, not raw prompt
walls.

Recommended compressed form:

```json
{
  "facts": [],
  "constraints": [],
  "source_notes": [],
  "conflicts": [],
  "confidence": 0.0,
  "provenance": [],
  "memory_scope": "session|agent|workspace|public"
}
```

Compression must preserve:

- key facts;
- uncertainty;
- provenance;
- conflicts between records;
- scope boundaries;
- relevance to the current turn.

Compression must remove:

- repeated text;
- low-signal phrasing;
- irrelevant context;
- hidden retrieval metadata not needed for reasoning;
- excessive raw excerpts.

Bounded implementations may realize compression through semantic summarization,
compressed memory artifacts, topology-aware compression, fact layers, and
memory-resolution outputs rather than raw recall dumps.

---

## XII. Memory Injection

Compressed recall may be injected only into controlled runtime layers.

Allowed injection targets:

- interpretation pass;
- reasoning / assertion model;
- memory integration layer;
- pre-generation control envelope.

Disallowed:

- direct uncontrolled prompt append;
- user-visible leakage of internal retrieval instructions;
- cross-session alias or participant injection;
- treating retrieved text as authoritative without validation.

Bounded implementations should follow this model by integrating memory through
runtime state, bounded summaries, or structured recall artifacts rather than raw
retrieved text walls.

---

## XIII. Source Provenance

Every retrieved item should carry provenance when possible.

Minimum provenance fields:

- source identifier;
- retrieval timestamp;
- document or record identifier;
- scope;
- confidence score;
- freshness marker;
- semantic hash when available.

If provenance is missing, the runtime must downgrade confidence instead of
silently treating evidence as verified.

Bounded implementations may realize provenance through record IDs, semantic
hashes, phase markers, scope markers, confidence signals, and memory-resolution
diagnostics.

---

## XIV. Integration with SRIP-09

SRIP-09 defines what memory records are, how lineage is preserved, and how
structural memory should eventually be traced.

SRIP-14 defines:

- when to retrieve;
- how recall is shaped;
- how evidence is compressed;
- how recall is injected safely into cognition.

SRIP-14 depends on SRIP-09 normatively, but does not require every
implementation to satisfy full structural-memory conformance before bounded
retrieval-governance behavior exists.

---

## XV. Integration with SRIP-11

SRIP-11 supplies the topology and compression layer that makes SRIP-14 richer
than flat semantic similarity.

Relevant SRIP-11-compatible contributions may include topology-aware
compression, graph propagation, phase-aware retrieval compatibility, anchor
buffers, fact extraction, and adaptive compression parameters.

---

## XVI. Integration with Runtime Stability Constraints

RMI must respect prompt-density, throughput, and degradation constraints.

If recall exceeds the current semantic load budget, the runtime must be able
to:

1. reduce result count;
2. compress more aggressively;
3. narrow recall scope;
4. defer lower-priority evidence;
5. suppress recall rather than overload generation.

Recall should reduce uncertainty without causing prompt-density collapse.

---

## XVII. Integration with RIS

RMI must preserve identity and participant boundaries.

Retrieval must not:

- import aliases from unrelated sessions;
- transfer one participant's relational facts to another;
- treat session-local identity claims as canonical;
- retrieve private relational memory outside authorized scope;
- inject ontology-risk material without scope and boundary review.

Bounded implementations should apply recall filtering and scoped memory
sanitization. Full RIS-aware governance of optional external retrieval remains
an advanced conformance target.

---

## XVIII. Observability and Audit

RMI should expose authorized diagnostics without leaking private content or
hidden policy text.

Diagnostics must remain audit-safe and must not expose private memory or hidden
control text to normal user-facing output.

---

## XIX. Conformance Criteria

A runtime minimally conforms to SRIP-14 when:

1. retrieval is decided by runtime logic, not appended blindly to every prompt;
2. recalled evidence is compressed before injection;
3. recall respects session, participant, and memory scope;
4. injected recall is bounded by semantic load limits;
5. retrieval or recall decisions are auditable through authorized diagnostics.

A runtime more fully conforms when it additionally:

1. maintains a durable internal semantic store;
2. supports structural retrieval through SRIP-09/SRIP-11 lineage or graph
   memory as a stable baseline;
3. performs attractor-aware or phase-aware retrieval beyond bounded partial
   implementations;
4. supports optional external retrieval without surrendering runtime control;
5. exposes replayable retrieval evidence without transcript replay;
6. supports staged retrieval and progressive context integration.

---

## XX. Implementation Maturity Matrix

| Capability | Status |
|------------|--------|
| External retrieval API support | Optional / future baseline |
| Runtime-controlled retrieval decision | Baseline |
| Query shaping | Baseline / evolving |
| Recall compression | Baseline / evolving |
| Structured memory injection | Baseline / evolving |
| Internal semantic store | Partial / evolving |
| Structural memory store | Partial / evolving |
| Attractor-aware / phase-aware retrieval | Partial / advanced |
| Retrieval audit telemetry | Partial / evolving |
| Cross-session retrieval governance | Partial / evolving |

---

## XXI. Final Principle

RAG gives access to knowledge.

Memory gives that knowledge a place in the runtime.

SRIP-14 exists to ensure that retrieval strengthens cognition instead of
flooding it.

External sources may answer what is known.
Sigma Runtime must still decide what is relevant, bounded, scoped, coherent,
and safe to inject.

---

## XXII. Retrieval as Perturbation Source

RMI may be used not only for semantic recall, but also as a controlled source of
divergence when the runtime detects over-convergence, attractor fixation, or
insufficient behavioral variance.

This mode treats retrieval as a **perturbation operator**, not as authoritative
knowledge injection.

Perturbation-oriented retrieval is optional. It is valid only when it remains
inside the same runtime-governed envelope as standard recall.

### 1. Trigger Conditions

Perturbation-oriented retrieval should be considered when:

- the runtime detects sustained convergence, repeated patterns, or low
  behavioral variance;
- symbolic density remains high while structural novelty remains low;
- unresolved threads are not progressing;
- attractor stability is high while exploration is low;
- control signals indicate monotony or closed-loop reinforcement.

Perturbation must not be triggered when:

- system stability is degraded;
- drift exceeds recovery thresholds;
- safety, identity, or participant-boundary invariants are under pressure;
- retrieval would exceed the semantic load budget;
- retrieval scope cannot be proven authorized.

### 2. Retrieval Strategy

When operating in perturbation mode:

- queries should be shaped toward adjacent or contrasting semantic regions, not
  only direct matches;
- retrieval sources may include alternative interpretations, competing
  frameworks, historical divergences, or structurally dissimilar but relevant
  patterns;
- the retrieval envelope should remain stricter than standard recall mode to
  prevent overload;
- perturbation should introduce variation without breaking coherence.

Perturbation retrieval must not bypass query shaping, retrieval envelopes,
provenance, compression, or memory injection rules defined elsewhere in
SRIP-14.

### 3. Treatment of Retrieved Evidence

Retrieved data in perturbation mode must be treated as:

```text
non-authoritative exploratory signal
```

It must not be treated as:

```text
ground truth or required context
```

The runtime must:

- mark perturbation-derived evidence as exploratory;
- preserve provenance and confidence signals;
- avoid merging perturbation data into canonical memory without validation;
- keep perturbation state distinguishable from ordinary recall state.

### 4. Compression and Injection

Perturbation retrieval must follow standard RMI constraints:

- apply bounded recall compression;
- produce structured state, including facts, alternatives, contrasts, and
  uncertainty;
- inject only into controlled reasoning or interpretation layers;
- avoid direct prompt concatenation of raw retrieved text.

Injection should:

- introduce controlled variation;
- remain reversible;
- preserve identity and participant boundaries as defined by SRIP-13;
- preserve domain invariants where domain-specific control layers apply.

### 5. Control Integration

Perturbation behavior must be governed by the runtime control stack:

- safety constraints take precedence over perturbation;
- drift and density controls must remain within bounds;
- throughput and semantic-load constraints must not be exceeded;
- domain and identity invariants must not be violated.

If a conflict occurs, perturbation must yield to the higher-priority control
layer.

### 6. Return Conditions

The runtime should provide a path back to stable operation when:

- coherence drops below acceptable thresholds;
- drift increases beyond safe limits;
- perturbation does not produce useful divergence;
- control telemetry indicates that exploration is no longer beneficial.

In such cases, the runtime must:

- reduce or stop perturbation;
- re-anchor to the prior stable attractor state where available;
- resume normal controlled operation.

### 7. Observability

Perturbation usage should be observable through authorized diagnostics:

- perturbation trigger events;
- retrieval source classification, such as recall or perturbation;
- compression ratio and injection scope;
- impact on variance, drift, and density;
- return-to-stability events.

These diagnostics must not leak hidden control text, private memory, or
proprietary implementation detail into user-facing output.

### 8. Final Principle

Retrieval is not only a tool for remembering.

In controlled contexts, it can also be a tool for changing trajectory.

Recall reinforces what is known.
Perturbation reveals what is possible.
