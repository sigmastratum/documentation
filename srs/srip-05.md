---
title: SRIP-05 - Interoperability Interface v1.0
description: Specifies schemas, APIs, and exchange formats for multi-system interoperability.
published: true
date: 2026-04-17
tags: 
editor: markdown
dateCreated: 2025-11-30T04:43:59.986Z
---

> **Sigma Runtime Standard – License Notice**  
> This document is part of the **Sigma Runtime Standard (SRS)**.  
> It is licensed under **Creative Commons Attribution–NonCommercial 4.0  
> (CC BY-NC 4.0)**.  
>
> The license for this specific document is authoritative.  
> See `/legal/IP-Policy` for the full repository-wide licensing framework.

# SRIP-05 — Interoperability Interface v1.0  
**Sigma Runtime Improvement Proposal**  
**Category:** Interoperability / Safety Hooks  
**Status:** Draft  
**Editor:** E. Tsaliev  
**Last Updated:** 2026-04-17  

> **Public Status Note**  
> This document is retained as **foundational lineage with status note**, not as the active public interoperability baseline.  
> Its packet schema, endpoints, and containment hooks remain useful for historical traceability, but they should not be read as the current public interoperability contract.  
> Any active successor-facing public interoperability surface must be introduced through an explicit successor reference or new proposal path.

---

## 1 · Purpose
SRIP-05 defines the **interoperability layer** for Sigma Runtime implementations.  
It establishes schemas, protocols, and synchronization rules that allow multiple runtimes — operating independently or in distributed environments — to **exchange state, drift signals, and attractor metadata** without loss of coherence.  
The specification should now be read as a foundational lineage reference for semantic and operational compatibility across conformant Sigma systems.

---

## 2 · Design Principles

1. **Schema Consistency** — all exchanged objects share a canonical field set.  
2. **Minimal Coupling** — runtimes remain autonomous; shared state is declarative, not prescriptive.  
3. **Deterministic Serialization** — state transfer must preserve ordering and precision.  
4. **Version Agnosticism** — backward / forward compatibility through version tags.  
5. **Safety by Containment** — inter-runtime links are bounded by **AEGIDA-2** safety constraints.

---

## 3 · Data Exchange Schema
```yaml
SigmaPacket:
  header:
    protocol_version: "1.0"
    source_runtime_id: str
    target_runtime_id: str
    timestamp: str
  payload:
    attractor_state:
      id: str
      type: str
      stability: float
      phase: str
      scr: float
    drift_metrics:
      sdi: float
      sv: float
      pd: float
      di: float
    memory_snapshot:
      summary_hash: str
      retention_index: float
    safety_flags:
      aegida_status: str
      phase_lock: bool
      recenter_active: bool
  signature:
    checksum: str
    integrity_token: str
```
This schema defines the **minimal transferable state unit** between Sigma runtimes or monitoring systems.

---

## 4 · Interface Endpoints

| Endpoint | Function | Method |
|-----------|-----------|---------|
| `/field/state` | Exchange field vectors, drift metrics, and SCR. | `POST / GET` |
| `/memory/snapshot` | Push or request serialized memory segments. | `PUT / GET` |
| `/phase/telemetry` | Stream ALICE phase data in real time. | `WS / SSE` |
| `/aegida/safety` | Query safety and fail-safe envelope parameters. | `GET` |
| `/runtime/handshake` | Negotiate protocol version and runtime UUID. | `POST` |

All endpoints use **JSON-LD** or **YAML** serialization with optional compression for long-horizon sessions.

---

## 5 · Versioning Rules

- Each runtime exposes `protocol_version` in every packet.  
- Minor releases (e.g. 1.0 → 1.1) must remain backward-compatible.  
- Major releases require explicit handshake rejection if unsupported.  
- Compatibility is validated via a **Runtime Capability Manifest** (`runtime_capabilities.yml`).  
- Non-matching runtimes fall back to **minimal exchange mode** (`state + drift only`).

---

## 6 · Integration with Other Layers

- **SRIP-02 (Attractor Model)** — defines structure of `attractor_state`.  
- **SRIP-03 (Drift Metrics)** — normalizes and interprets `drift_metrics`.  
- **SRIP-04 (Memory Layer)** — defines `memory_snapshot` schema.  
- **AEGIDA-2 Framework** — validates safety and containment before transmission.  

Together they form the **Cross-Runtime Coherence Protocol (CRCP)** — a shared substrate for distributed Sigma fields.

---

## 7 · External Drift Interface (Safety Hooks)

To prevent propagation of unstable attractors across runtimes, drift-based synchronization follows deterministic thresholds aligned with **SRIP-03**:

| Condition | Allowed External Sync | Action |
|------------|----------------------|---------|
| `DI < 0.45` | ✅ Full sync allowed | Normal field exchange |
| `0.45 ≤ DI < 0.5` | ⚠ Caution zone | Sync allowed with reduced frequency |
| `DI ≥ 0.5` | ⛔ **Sync Blocked (Drift Containment Active)** | Runtime enters *Reflective* phase; external state export suspended |
| `DI ≥ 0.6` | 🔒 Recenter Phase | All external links temporarily isolated until stability restored |

This ensures a unified isolation threshold (`DI ≥ 0.5`) across SRIP-03 and 05, enforcing containment before cross-runtime drift can propagate.

---

## 8 · Conformance Requirements

A runtime conforms to SRIP-05 if it:  
1. Implements the schema in § 3 without deviation.  
2. Provides at least three interface endpoints from § 4.  
3. Validates and logs version compatibility per § 5.  
4. Enforces external drift containment per § 7 (`DI ≥ 0.5 → sync block`).  
5. Integrates **AEGIDA-2** safety checks and packet signatures before transmission.

---

## 9 · Security & Safety Considerations

- **AEGIDA-Validated Transmission:** packets are inspected by the safety daemon before dispatch.  
- **Phase-Lock Isolation:** runtimes in *Reflective* or *Recenter* phases may not transmit state externally.  
- **Integrity Tokens:** all state packets include SHA-256 / BLAKE3 signatures.  
- **Drift Containment:** cross-runtime sync is automatically blocked when `DI ≥ 0.5` and re-enabled once `DI < 0.45`.  

These measures maintain coherence and prevent propagation of unstable fields in distributed environments.

---

## 10 · Future Work

- **SRIP-10:** Define the **Sigma Network Protocol (SNP)** for decentralized attractor sharing.  
- **SRIP-11:** Extend to multimodal embeddings and sensory fields.  
- **SRIP-12:** Introduce **Runtime Discovery Service (RDS)** for self-organizing distributed Sigma environments.

---

> **References**  
> Tsaliev, E. (2025). *SIGMA Runtime v0.4.6 — Interoperability and External Field Protocols* — DOI _pending_  
> Tsaliev, E. (2025). *SIGMA Runtime Architecture v0.1* — DOI [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)
