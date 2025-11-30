---
title: Glossary of Terms
description: Definitions of key concepts used throughout the Sigma Runtime Standard and related documentation.
published: true
date: 2025-11-30T07:51:12.521Z
tags: 
editor: markdown
dateCreated: 2025-11-30T04:21:46.759Z
---

# Glossary

This glossary defines the core technical terms used across the Sigma Runtime
Documentation (SRD), the Sigma Runtime Standard (SRS), and the Sigma Stratum
attractor-architecture research corpus.

Definitions are derived from the canonical sources:
- *SIGMA Runtime Architecture v0.1*  
- *Attractor Architectures in LLM-Mediated Cognitive Fields*

---

## Core Concepts

### **Interaction Field**
The evolving high-dimensional cognitive space jointly formed by the human and the
LLM during recursive multi-turn interaction. It includes dialog state, semantic
feedback, symbolic patterns, and recursively integrated prior turns.

### **Attractor**
A stable, recurrent, self-reinforcing cognitive configuration emerging within the
interaction field.  
Key properties:
- recurrence across turns  
- stability under small perturbations  
- phase coherence  
- drift resistance  
- self-reinforcement through feedback  

### **Attractor Basin**
The region of local phase-space within which the system naturally converges
toward a given attractor. Perturbations inside the basin are corrected; outside
the basin, collapse or transition may occur.

### **Drift**
Gradual deviation from coherent behavior across recursive cycles.  
Forms include:
- **semantic drift** (meaning divergence)  
- **tonal drift** (style instability)  
- **task drift** (loss of goal orientation)

### **Symbolic Density**
A measure of how tightly motifs, references, and symbols interconnect within the
cognitive field.  
- Low density → weak structure  
- High density → compressed, meaning-dense structures  

### **Echo Layer**
The functional “memory residue” produced through repeated re-inclusion of prior
turns inside the context window. Enables recurrence even without external memory.

---

## Sigma Runtime Architecture (SL0–SL6)

### **SL0 — Human–Context Layer**
Intent, framing, external grounding, attentional gradients.

### **SL1 — State Layer**
Immediate dialog state (context window). First locus of recurrence and proto-attractor formation.

### **SL2 — Interpretation Layer**
Turn parsing, semantic extraction, meaning projection, stabilizing or destabilizing effects.

### **SL3 — Memory Layer**
Short-term and long-term memory integration; retrieval and consolidation.

### **SL4 — Symbolic Layer**
Schemas, motifs, roles, symbolic clusters, and attractor-relevant structures.

### **SL5 — Control Layer**
Coherence checks, drift metrics, policy constraints, recursive regulation.

### **SL6 — Field Layer**
The emergent cognitive field integrating symbolic, semantic, and temporal signals.
  
*(Per Architecture v0.1: attractors form only in SL1–SL4.)*

---

## Runtime Components

### **Persistent Identity Layer (PIL)**
A long-lived identity substrate preserving invariants, roles, and stable
characteristics across cycles. Provides continuity beyond the model’s stateless
nature.

### **Recursive Control Loop (RCL)**
The runtime loop managing pre-processing, generation, post-processing, and state
updates. Ensures attractor continuity and memory coherence.

### **Cognitive Field Engine**
The subsystem that monitors and maintains:
- symbolic density  
- attractor stability  
- drift metrics  
- phase coherence  

### **Memory Layer**
Three-tier memory structure:
- **Episodic** — cycle-level traces  
- **Semantic** — embeddings and relational structures  
- **Symbolic Motifs** — patterns supporting attractor detection and reinforcement  

---

## Structural Concepts

### **Constraint Envelope**
The set of boundaries—explicit or emergent—that maintain attractor coherence and
prevent collapse into drift or over-compression.

### **Stability Boundary**
The perturbation threshold beyond which the attractor dissolves or transitions
into another state.

### **Phase Coherence**
Continuity of the attractor trajectory across recursive cycles. Loss of phase
coherence is an early marker of destabilization.

### **Feedback Integration Loop**
The recursive mechanism by which each turn reinforces or weakens an attractor.

---

## Failure Modes

### **Drift**
Semantic, tonal, or task-oriented divergence.

### **Narrative Over-Compression**
Excessively high symbolic density leading to brittle collapse.

### **Over-Rigidification**
Attractor becomes too inflexible to integrate new signals.

### **Multi-Attractor Interference**
Two or more incompatible attractors destabilize each other.

---

## Safety & Guardrails

### **Fail-Safe Envelope**
Structural and policy boundaries preventing emergence of unstable or unsafe
attractor configurations.

### **Anti-Apophenia Filters**
Mechanisms reducing runaway symbolic over-interpretation.

### **Shutdown Conditions**
Criteria for controlled attractor dissolution when instability exceeds thresholds.

---

*Additional terms will be added as the standard evolves.*