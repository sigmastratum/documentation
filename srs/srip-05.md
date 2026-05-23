> **Sigma Runtime Standard - Public Specification Notice**
> This document is part of the **Sigma Runtime Standard (SRS)** public specification layer.
>
> Specification License: CC BY 4.0.
> Implementation Safe Harbor: independent implementation permitted under public SRS/SRIP terms.
> Machine-readable artifacts: Apache License 2.0 where explicitly marked.
> Marks / Certification: governed by Sigma Marks and Certification Policy.
> Proprietary Runtime Assets: not licensed by this SRIP.
>
> Independent implementations of public SRS/SRIP normative requirements are welcome under the public specification terms.
> Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

# SRIP-05 — Interoperability Interface v1.0
**Sigma Runtime Improvement Proposal**

## Public Specification Metadata

| Field | Value |
|---|---|
| SRIP | SRIP-05 |
| Title | Interoperability Interface v1.0 |
| Version | Foundational Draft |
| Status | Draft / Foundational Lineage |
| Date | 2026-04-17 |
| Authors / Contributors | E. Tsaliev |
| Owning Layer | Interoperability / Safety Hooks |
| Parent Specs | SRIP-02, SRIP-03, SRIP-04, SRIP-06 |
| Related Specs | SRIP-09, SRIP-14, SRIP-17 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Commercial Runtime Boundary | Relevant policy or explicit covenant for protected Sigma marks, official certification, managed deployment, white-label, resale, CC BY-NC commercial use, and patent commitments |
| Information Class | Open |
| Change Class | SRS-only |
| Normative Status | Retained as foundational lineage with status note; not the active public interoperability contract unless introduced through an explicit successor reference or new proposal path. |
| Conformance Level | Conceptual / Foundational Lineage |
| SRD Synchronization Action | Deferred review |
| Release Alignment Status | Foundational lineage; no active production interoperability conformance claim is made by this document alone. |

> **Public Status Note**
> This document is retained as **foundational lineage with status note**, not as the active public interoperability baseline.
> Its packet schema, endpoints, and containment hooks remain useful for historical traceability, but they should not be read as the current public interoperability contract.
> Any active successor-facing public interoperability surface must be introduced through an explicit successor reference or new proposal path.

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows those public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

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

The requirements below describe the historical v1.0 interoperability model.
They are not current public certification criteria unless an active successor
document explicitly re-adopts them.

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

## 10 · Historical Future Work Note

Earlier drafts of this document referenced future interoperability, multimodal,
and runtime-discovery work before the current `SRIP-10`, `SRIP-11`, and
`SRIP-12` registry assignments existed.

Those draft references are lineage context only. Current interoperability and
multi-agent evolution is tracked through the public registry and explicit
successor references, including `SRIP-17` where applicable.

---

> **References**
> Tsaliev, E. (2025). *SIGMA Runtime v0.4.6 — Interoperability and External Field Protocols* — DOI _pending_
> Tsaliev, E. (2025). *SIGMA Runtime Architecture v0.1* — DOI [10.5281/zenodo.17703667](https://doi.org/10.5281/zenodo.17703667)
