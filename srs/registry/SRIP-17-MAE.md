> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-17 - Multi-Agent Exchange (MAE)
**Bounded Cross-Runtime Exchange, Provenance, and Multi-Agent Continuity**

| Field | Value |
| --- | --- |
| SRIP | SRIP-17 |
| Title | Multi-Agent Exchange (MAE) |
| Version | Public Draft v0.2 |
| Status | Public Draft |
| Date | 2026-05-20 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Interoperability / Multi-Agent Exchange / Provenance Boundary |
| Parent Specs | SRIP-03, SRIP-05, SRIP-06, SRIP-08, SRIP-09, SRIP-10, SRIP-11 |
| Related Specs | SRIP-13, SRIP-14, SRIP-15, SRIP-16 |
| License | CC BY-NC 4.0 / Canon CIL Applicable |
| Information Class | Open |
| Change Class | Mixed SRS+SRD |
| Normative Status | Defines a bounded public proposal for multi-agent exchange between Sigma-compatible runtimes. It does not define an always-on mesh, shared hidden memory, autonomous collective agency, or a production deployment claim. |
| Conformance Level | Public Draft |
| SRD Synchronization Action | Completed in `/srd/architecture.md`, `/srd/memory.md`, `/srd/safety.md`, `/srd/runtime-loop.md`, and `/srd/faq.md`. |
| Release Alignment Status | Draft; no runtime enablement claim. |

---

## I. Purpose

SRIP-17 defines **Multi-Agent Exchange (MAE)**: a bounded protocol surface for exchanging structured state, memory evidence, control telemetry, or semantic deltas between Sigma-compatible runtimes.

The purpose of MAE is not to create a hidden collective agent. The purpose is to make cross-runtime cooperation possible while preserving identity boundaries, provenance, consent, safety containment, and local control authority.

In public SRS terms, MAE is an interoperability proposal layered above the foundational SRIP-05 lineage. SRIP-05 remains historical baseline material; SRIP-17 describes the successor-facing exchange boundary for multi-agent or multi-runtime operation.

---

## II. Problem Statement

Long-running systems may need more than one runtime participant:

- separate agents collaborating on related work;
- specialized agents exchanging bounded evidence;
- operator-controlled multi-agent workflows;
- research environments comparing multiple runtime trajectories;
- future external integrations with Sigma-compatible runtimes.

Without a bounded exchange protocol, these workflows risk:

- leaking private state between agents;
- importing unstable drift from one runtime into another;
- treating retrieved material as authoritative without provenance;
- creating hidden feedback loops;
- collapsing distinct identities or roles into one shared field;
- exposing implementation-specific internals as if they were public contract.

MAE defines the public boundary needed to exchange useful state without dissolving local runtime control.

---

## III. Non-Goals

MAE does not define:

- a global autonomous agent mesh;
- shared hidden memory across users or agents;
- automatic consensus or group cognition;
- unrestricted agent-to-agent communication;
- production network endpoints or deployment topology;
- a guarantee that all Sigma Runtime products expose multi-agent exchange;
- permission to bypass user consent, workspace boundaries, or safety controls.

MAE enables bounded exchange. It does not merge agents into a single authority.

---

## IV. Conformance Scope

A conformant MAE implementation must:

1. Require explicit exchange authorization at the relevant operator, user, workspace, or system boundary.
2. Preserve local runtime sovereignty: incoming data is evidence, not command authority.
3. Attach provenance, source identity, timestamp, scope, and integrity metadata to exchange artifacts.
4. Enforce drift, safety, and memory-containment gates before import or export.
5. Keep exchanged artifacts distinguishable from native memory until validated.
6. Provide an audit trail for exchange events, rejections, and accepted reintegration.
7. Support downgrade or refusal when protocol versions, trust scope, or stability state do not match.

---

## V. Core Concepts

| Concept | Description |
|---|---|
| **Exchange Artifact** | A bounded unit of shared state, semantic delta, memory evidence, or telemetry. |
| **Exchange Envelope** | The metadata wrapper carrying source, target, scope, provenance, integrity, and policy constraints. |
| **Local Sovereignty** | The rule that each runtime retains authority over whether and how incoming artifacts affect its own state. |
| **Provenance Boundary** | The requirement that imported material remains attributable to its source until validated and reintegrated. |
| **Exchange Gate** | A safety and policy checkpoint that approves, narrows, quarantines, or rejects incoming and outgoing artifacts. |
| **Coherence Impact** | The measured or estimated effect of an exchange on drift, density, phase, and identity stability. |
| **Exchange Session** | A bounded interaction window for one or more artifacts between known parties under defined scope. |

---

## VI. Architectural Position

MAE sits between ordinary runtime state and external exchange surfaces.

It may use evidence from:

- SRIP-03 drift and stabilization metrics;
- SRIP-05 interoperability lineage;
- SRIP-06 safety and recursion boundaries;
- SRIP-08 phase and telemetry evidence;
- SRIP-09 memory and structural coherence;
- SRIP-10 AEP entropy posture;
- SRIP-11 compression and topology;
- SRIP-14 retrieval and memory integration;
- SRIP-15 controlled perturbation;
- SRIP-16 self-model evidence.

MAE must not bypass these layers. It is an exchange boundary, not a privileged backdoor.

---

## VII. Exchange Model

### 1. Handshake

Before exchange, parties should establish:

- runtime or agent identity;
- protocol version;
- allowed scope;
- trust class;
- consent or operator authorization;
- supported artifact types;
- safety and stability posture.

### 2. Artifact Preparation

The exporting runtime prepares a bounded artifact:

- compressed summary;
- semantic delta;
- memory evidence reference;
- telemetry snapshot;
- retrieval result with provenance;
- control-state observation.

Raw private state should not be exported unless explicitly authorized and safe for the target scope.

### 3. Exchange Gate

The exchange gate evaluates:

- authorization;
- source trust;
- artifact size and scope;
- provenance completeness;
- drift or instability risk;
- user/workspace boundary constraints;
- whether the artifact can be imported as evidence only.

The gate may accept, narrow, quarantine, or reject the artifact.

### 4. Local Reintegration

Accepted artifacts enter the target runtime as evidence. They do not become native memory, identity, or policy by default.

Reintegration should pass through the normal memory, control, and safety paths before affecting long-term state.

---

## VIII. Exchange Envelope

The following structure is illustrative. Implementations may vary if equivalent boundaries are preserved.

```yaml
ExchangeEnvelope:
  protocol: "srip-17-mae"
  version: "0.2"
  exchange_id: str
  source:
    runtime_id: str
    agent_id: str | null
    workspace_scope: str | null
  target:
    runtime_id: str
    agent_id: str | null
    workspace_scope: str | null
  artifact:
    type: "semantic_delta | memory_evidence | telemetry_snapshot | control_observation"
    content_ref: str
    summary: str
    compression_profile: str | null
  provenance:
    created_at: str
    source_trace_refs: list[str]
    integrity_hash: str
    retention_class: str
  constraints:
    allowed_use: list[str]
    expires_at: str | null
    user_visible: bool
    reintegration_required: bool
```

---

## IX. Monitoring and Metrics

| Metric | Definition | Purpose |
|---|---|---|
| **Exchange Acceptance Rate (EAR)** | Share of artifacts accepted after gating. | Detects whether exchange scope is too broad or too restrictive. |
| **Exchange Drift Impact (EDI)** | Drift change observed after artifact reintegration. | Tracks destabilizing exchange effects. |
| **Provenance Completeness (PC)** | Completeness of source, scope, timestamp, and integrity metadata. | Prevents untraceable material from becoming state. |
| **Cross-Agent Recall Fidelity (CARF)** | Accuracy of recalling imported evidence with source attribution preserved. | Measures whether exchange helps without corrupting memory. |
| **Quarantine Rate (QR)** | Share of artifacts held for review or narrowed import. | Indicates safety pressure or trust mismatch. |
| **Exchange Latency (EL)** | Time between artifact creation, gate decision, and target availability. | Measures operational responsiveness. |

---

## X. Safety and Governance

MAE must preserve:

- user and workspace boundaries;
- role and agent identity boundaries;
- consent and authorization boundaries;
- provenance and auditability;
- safety containment for unstable imported material;
- revocation or expiry where scope requires it.

Incoming exchange data should be treated as untrusted until it passes the exchange gate. Even accepted material should remain labeled as externally sourced until reintegration validates it for the local runtime.

MAE must support refusal. A runtime may reject exchange because of missing consent, unsupported version, insufficient provenance, unstable drift state, unsafe content, excessive scope, or policy conflict.

---

## XI. Interoperability With SRIP-05

SRIP-05 remains the foundational lineage for cross-runtime schemas and interoperability concepts.

SRIP-17 does not silently replace SRIP-05. Instead, it defines a successor-facing public proposal for bounded multi-agent exchange:

- SRIP-05 explains the historical interoperability substrate;
- SRIP-17 defines exchange authorization, provenance, gating, and reintegration boundaries;
- implementations should explicitly state which surfaces they support.

---

## XII. Expected Outcomes

If implemented within these boundaries, MAE should enable:

- safer multi-agent workflows;
- explicit provenance for exchanged evidence;
- controlled sharing between specialized agents;
- reduced risk of hidden cross-agent contamination;
- auditable import/export events;
- better separation between collaboration and memory collapse.

The intended outcome is cooperative runtime operation with clear boundaries, not uncontrolled collective cognition.

---

## XIII. Release Alignment

SRIP-17 is a public draft architecture proposal. It does not claim that MAE is fully implemented in any current release.

Any implementation claim must separately document:

- enabled exchange surfaces;
- authorization and consent model;
- artifact types supported;
- exchange-gate behavior;
- retention and deletion policy;
- audit and operator visibility;
- QA coverage for provenance loss, boundary leakage, and drift propagation.

---

**End of SRIP-17 Public Draft v0.2**  
*Sigma Stratum Research Group - 2026*
