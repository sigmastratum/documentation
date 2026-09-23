---
title: Environment Interaction and Events
description: Human-readable guide to SRIP-24 EIL and SRIP-25 IEM.
published: true
date: 2026-09-23T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-06-27T00:00:00.000Z
---

> **Sigma Stratum Documentation - License Notice**
> This document is part of the **Sigma Runtime Standard (SRS)** and the
> **Sigma Runtime Documentation (SRD)**.
>
> It is licensed under **Creative Commons Attribution-NonCommercial 4.0
> (CC BY-NC 4.0)**.
>
> The license for this specific document is authoritative.
> For the full framework, see [`/legal/IP-Policy`](https://github.com/sigmastratum/documentation/blob/main/legal/ip-policy.md).

# Environment Interaction and Events

## Public Specification Boundary

This SRD document explains the public SRS/SRIP specification layer. It does not
license or disclose proprietary Sigma Runtime implementation assets unless
explicitly marked.

The SRIPs discussed here are public draft architecture proposals. This page does
not claim that the corresponding runtime behavior is implemented, enabled, or
production-conformant.

---

## Why This Guide Exists

Long-running agents do not only answer prompts.

Over time, they also:

- retrieve old material;
- receive external evidence;
- act on tools or systems;
- affect memory;
- interact with users, agents, files, providers, and governance surfaces.

The public Sigma Runtime Standard needs vocabulary for external contact without
turning the runtime into a workflow engine, tool framework, or planner.

SRIP-24 and SRIP-25 form a connected explanatory block:

| SRIP | Plain-language question | Short answer |
| --- | --- | --- |
| [SRIP-24 EIL](/srs/registry/SRIP-24-EIL) | Where does a stabilized runtime trajectory meet external reality? | At a governed environment boundary. |
| [SRIP-25 IEM](/srs/registry/SRIP-25-IEM) | What crosses that boundary? | Interaction events: observations entering runtime and effects leaving runtime. |

Short version:

```text
EIL explains governed external contact.
IEM explains the semantic unit of that contact.
```

---

## SRIP-24 EIL: Contact Is Not Cognition

Once a runtime has a stabilized trajectory, it may need to interact with
something outside itself:

- a user;
- another agent;
- a memory store;
- a retrieval system;
- a file;
- a provider;
- a tool;
- a governance surface;
- a communication channel.

SRIP-24 defines the **Environment Interface Layer (EIL)** as the public draft
architecture boundary for that contact.

The simplest rule is:

```text
Behavior governs cognition.
EIL governs contact.
```

This distinction matters because external contact can change more than text.
It can change memory, trigger costs, notify humans, write files, call systems,
or create evidence that future runtime cycles inherit.

### What EIL Separates

EIL keeps several things from collapsing into each other:

| Distinction | Why it matters |
| --- | --- |
| Observation vs truth | Reading something does not make it true. |
| Observation vs authority | Receiving input does not grant permission. |
| Capability vs permission | A tool being available does not mean it should be used. |
| Retrieval vs current fact | Retrieved material may be old, scoped, partial, or contested. |
| Task success vs governance success | An action can complete while the evidence or authority path becomes questionable. |

EIL is therefore not a tool framework.

It is the boundary layer that asks whether external contact is allowed,
bounded, evidenced, scoped, and contestable.

---

## SRIP-25 IEM: The Unit Of Contact Is An Interaction Event

SRIP-25 defines the **Interaction Event Model (IEM)**.

If EIL is the boundary, IEM is the public semantic model for what crosses the
boundary.

An interaction event is a bounded, attributable, evidence-bearing contact
between runtime and environment.

It is not:

- a workflow step;
- a planner action;
- an event bus;
- a database schema;
- a provider API;
- a transport protocol;
- a tool call by itself.

It is a public semantic unit.

### Observation Events

Observation events move from environment to runtime.

Examples:

- a user message;
- a retrieval result;
- a provider response;
- a webhook;
- a file read;
- telemetry;
- another agent's message.

Observation can influence understanding.

Observation does not directly authorize behavior, memory persistence, external
action, or truth claims.

### Effect Events

Effect events move from runtime to environment.

Examples:

- a provider request;
- a tool execution;
- a memory write;
- a notification;
- a filesystem write;
- a database mutation;
- a human escalation.

Effect can change external reality.

Effects require stronger governance than observations.

### Why Event Semantics Matter

Instead of asking only:

```text
Which tool was called?
```

IEM asks:

```text
Which interaction event occurred?
What was its direction?
What was its source and target?
What authority applied?
What evidence remains?
What effect class was involved?
Can it be audited, replayed, contested, or bounded?
```

This shifts the public architecture from tool-centric execution toward
event-centric governance.

### One Effect, Several Linked Events

An intended effect is not one status flag that moves from "allowed" to
"successful." The public model keeps different claims separate:

```text
interaction candidate
  -> authorization decision
  -> effect attempt
  -> outcome observation
  -> verification decision
```

Each step adds a linked event. It does not rewrite the prior event. This makes
it possible to say that an action was properly authorized, transport succeeded,
and the external outcome is still unknown. It also preserves contradictory
read-back without erasing the original authorization or attempt.

Events bind to the authority and governing references applicable when they
occurred. Later policy, delegation, schema, or profile changes do not rewrite
their historical interpretation. Historical validity also does not grant
permission to invoke the action again.

The event lineage is evidence only. It does not execute retries, replay work,
or authorize effects.

### Semantic Effect Transaction

SRIP-24 treats consequential external effects as a bounded semantic
transaction. The runtime may commit accepted local state while keeping an
external effect staged. Release requires current authority and applicable
validation at the effect boundary.

After release, failures are described honestly as missing acknowledgement,
unknown or contradictory outcome, retry, compensation, or escalation. An
irreversible effect is not called rolled back merely because local state was
restored.

Targets differ. Some support idempotency, read-back, or compensation and some
do not. A declared profile exposes those limits rather than promising a
universal transaction mechanism.

An unknown outcome does not mean that nothing happened. Before retrying, the
runtime reconciles the result or establishes applicable duplicate-effect
protection. Otherwise it blocks automatic retry and escalates, except where
current authority explicitly accepts a bounded retry with recorded duplication
risk. Multiple successful receipts can describe one effect without duplicating
that effect. Read-back is one source of outcome evidence, not the only one;
a target completion receipt may suffice where its semantics support the claim.

---

## How The Two Layers Work Together

One way to read the block is:

```text
Contact with the external world
  -> SRIP-24 EIL
  -> governed boundary review

Unit crossing that boundary
  -> SRIP-25 IEM
  -> interaction event
```

Another way:

```text
EIL: May the trajectory contact the environment?
IEM: What contact event occurred?
```

They solve adjacent boundary problems and should not be confused with semantic
evolution layers such as SRIP-23 DGL.

---

## Example: Retrieval

A runtime retrieves a document.

Without EIL/IEM, this may be treated as:

```text
The runtime knows this.
```

With EIL/IEM, it is more precise:

```text
An observation event occurred.
The target was runtime interpretation.
The source was retrieval.
The material has provenance and scope.
It may be old, partial, private, or contested.
It does not automatically become truth or memory.
```

If the runtime later writes a summary to memory, that is a different event:

```text
An effect event occurred.
The target was memory state.
The write requires stronger authority and evidence.
```

---

## Common Misreadings

| Misreading | Correct reading |
| --- | --- |
| EIL is a tool framework. | EIL is a boundary layer for governed external contact. |
| IEM is an event bus or schema. | IEM is a public semantic model for interaction events. |
| Authorization means the effect happened. | Authorization, attempt, outcome observation, and verification are separate linked events. |
| A previously valid delegation permits another call. | Historical validity is preserved, but every new invocation requires current authority. |
| Restoring local state rolls back an external effect. | External reversal requires target-specific evidence; otherwise the result is retry, compensation, escalation, or an unresolved outcome. |
| Observation means truth. | Observation means material entered the runtime boundary. |
| Capability means permission. | Capability only means an action surface exists. |
| Task success means governance success. | Governance success requires authority, scope, and evidence continuity. |

---

## Status

SRIP-24 and SRIP-25 are public draft architecture proposals.

This SRD page provides explanatory synchronization for readers. It does not
claim runtime implementation, production enablement, conformance, certification,
or release alignment beyond the public draft status of the linked SRIPs.

---

## Related SRIPs

- [SRIP-24 EIL](/srs/registry/SRIP-24-EIL)
- [SRIP-25 IEM](/srs/registry/SRIP-25-IEM)
- [SRIP-21 EIB](/srs/registry/SRIP-21-EIB)
- [SRIP-22 GRC](/srs/registry/SRIP-22-GRC)
