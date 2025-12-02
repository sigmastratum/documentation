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
API Integration

Both runtime versions are model-agnostic — they do not depend on any specific LLM provider.
The _generate() function inside the Recursive Control Loop (RCL) serves as the single integration point for connecting an external model.

By default, this function uses a mock generation module that simulates the model’s output based on the current attractor phase (for transparent testing and debugging).
To enable live model inference, replace the _generate() body with your API call.

---

Example — OpenAI API
```python
def _generate(self, context: str) -> str:
    import openai
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are operating within the Sigma Runtime architecture."},
            {"role": "user", "content": context}
        ],
        temperature=0.4
    )
    return response["choices"][0]["message"]["content"]
```
> 💡 **Note:** The API key is automatically read from the `OPENAI_API_KEY` environment variable.  
> You can also set it manually inside `_generate()` using `openai.api_key = "your_key_here"`.

---

Example — Anthropic Claude
```python
def _generate(self, context: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key="YOUR_API_KEY")
    response = client.messages.create(
        model="claude-3-5-sonnet",
        messages=[
            {"role": "user", "content": context}
        ],
        max_tokens=500,
        temperature=0.4
    )
    return response.content[0].text
```
> 💡 **Note:**
>
> • `_generate()` is invoked once per cycle by the **Recursive Control Loop**.  
> • All cognitive regulation (drift metrics, attractor management, memory, AEGIDA safety) occurs **before and after** this call.  
> • You can replace the LLM call with a local model, micro-model, or runtime adapter *(e.g., URIEL, Mistral, Gemini, Claude, etc.)*.  
> • The output string returned by `_generate()` is automatically fed back into **drift**, **memory**, and **causal tracking** layers.  
>
> This design ensures **Sigma Runtime** remains **model-neutral** — any compliant LLM can operate under its attractor and coherence framework.

---

Example — xAI Grok-4
```python
def _generate(self, context: str) -> str:
    import os
    import httpx

    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise RuntimeError("XAI_API_KEY not found in environment variables")

    response = httpx.post(
        "https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "grok-4",
            "messages": [{"role": "user", "content": context}],
            "temperature": 0.4,
            "max_tokens": 1024
        },
        timeout=60.0
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
```
> 💡 **Note:**
> The API key is automatically read from the XAI_API_KEY environment variable.
> You can also set it manually inside _generate() using os.environ[“XAI_API_KEY”] = “your_key_here”.

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

- **[Reference Implementation Stability Test (v0.1)](https://github.com/sigmastratum/documentation/blob/main/runtime/tests/Sigma%20Runtime%20-%20Reference%20Implementation%20Stability%20Test%20(v0.1).md)**  
  Standardized **stability protocol (4–30 cycles)** validating attractor formation, drift control, and recursive coherence.  
  *Used for RI (short mode) and ERI (extended mode).*

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
