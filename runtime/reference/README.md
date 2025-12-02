# Sigma Runtime – Reference Implementations (RI & ERI)

The **Sigma Runtime** defines the *Recursive Control Loop (RCL)* and its  
associated cognitive layers as specified in *Sigma Runtime Architecture v0.1*.

Two complementary implementations are provided:

---

## Sigma Runtime – Reference Implementation (RI)

A **minimal and transparent** demonstration of the core runtime loop.

Implements early-stage components of **SRIP-01** through **SRIP-04**:
- **Runtime State** — base control structure for recursive operation  
- **Attractor Model** — phase transitions and symbolic clustering  
- **Drift Metrics** — basic semantic distance and coherence tracking  
- **Memory Layer** — episodic and motif-level storage  

### Usage
[→ Sigma Runtime - Reference Implementation.py](./Sigma%20Runtime%20-%20Reference%20Implementation.py)

Runs a concise simulation (≈4 cycles) demonstrating:
- attractor formation,  
- drift regulation,  
- symbolic density stabilization.

### Purpose
This RI is **didactic and diagnostic** — designed for clarity and traceability.  
It represents the **minimum viable runtime** conforming to Sigma Runtime  
Principles (SRIP-01…SRIP-04).

---

## Sigma Runtime – Extended Reference Implementation (ERI)

A **comprehensive functional prototype** (~800 lines) implementing the full  
Sigma Runtime v0.1 cognitive architecture.

Implements **SRIP-01 → SRIP-07**, including:
- **Full ALICE Engine** — attractor management with phase transitions  
- **Persistent Identity Layer (PIL)** — long-term invariants and traits  
- **Causal Continuity Chain** — interpretable causal tracking  
- **Drift Monitor** — multi-dimensional drift metrics  
- **AEGIDA Safety Framework** — drift sink prevention, coherence guards  
- **Multi-Tier Memory System** — episodic, semantic, and motif layers  
- **Operational Modes (Intent Module)** — analysis, synthesis, reflection, scaffolding  
- **Recursive Control Loop (RCL)** — orchestrating full runtime cognition  

### Usage
[→ Sigma Runtime - Extended Reference Implementation.py](./Sigma%20Runtime%20-%20Extended%20Reference%20Implementation.py)

Run directly to observe an 8-cycle demonstration:
- automatic attractor formation and dissolution,  
- symbolic density evolution,  
- drift regulation,  
- causal continuity mapping.

Each cycle prints:
- runtime phase and stability,  
- symbolic density and drift metrics,  
- current operational mode,  
- causal chain entries.

---

## Guidance

| Goal | Recommended Version |
|------|----------------------|
| Learn the basic structure of Sigma Runtime | **RI (Reference Implementation)** |
| Study attractor dynamics and recursive coherence | **ERI (Extended Reference Implementation)** |
| Integrate runtime into custom models (URIEL, Claude, etc.) | Start with **ERI**, replace `_generate()` with your model API |
| Research SRIP conformance or open-standard alignment | Use **ERI** for full layer visibility and data export |

---

## Architecture Summary

| Layer | Description | Present In |
|-------|--------------|-------------|
| **PIL (Persistent Identity Layer)** | Long-term traits and invariants | ERI |
| **Memory Layer** | Episodic + Semantic + Motif stores | RI / ERI |
| **ALICE Engine** | Attractor formation, stability, phases | RI / ERI |
| **Drift Monitor** | Semantic, stylistic, and topic drift | ERI |
| **Causal Continuity Chain** | Cycle-to-cycle causal links | ERI |
| **Intent Module** | Determines operational mode | ERI |
| **Recursive Control Loop (RCL)** | Main runtime orchestrator | RI / ERI |

---
### Test Scenarios

Example runtime walkthroughs are provided in the `/tests` directory:

- **[Reference Implementation Stability Test (v0.1)](https://github.com/sigmastratum/documentation/blob/main/runtime/tests/Sigma%20Runtime%20-%20Reference%20Implementation%20Stability%20Test%20(v0.1))**   
4-cycle demonstration of attractor formation and drift stabilization (for RI)
30-cycle demonstration of attractor formation and drift stabilization (for ERI).

- **[THE FULL 200-TURN ATTRACTOR STABILITY TEST SCENARIO (v1.0)](https://github.com/sigmastratum/documentation/blob/main/runtime/tests/THE%20FULL%20200-TURN%20ATTRACTOR%20STABILITY%20TEST%20SCENARIO%20(v1.0).md)**   
  Extended 200-cycle experiment used for long-term attractor dynamics,  
  recursive stability analysis, and symbolic density decay modeling.  
  *(Recommended for research replication, not for standard demo runs.)*
---

## Notes

- Both implementations are **open-standard reference designs**, not proprietary code.  
- They are intended for **research, experimentation, and alignment testing** under  
  the Sigma Runtime Standard (SRIP).  
- For production or hybrid systems, use these implementations as **diagnostic layers**  
  or runtime regulators for embedded cognitive agents.

---

**Maintained by:** Sigma Stratum Research Group  
**Standard:** [Sigma Runtime Architecture v0.1](https://doi.org/10.5281/zenodo.17703667)  
**License:** CC BY-NC 4.0  
