# Runtime Attractor Design Guide

**Client-facing design draft v0.2**  
**Date:** 2026-06-25  
**Use:** design partner guidance, agent setup, non-engineering review

---

## Core Idea

Before writing instructions for an agent, identify its attractor.

In Sigma Runtime, an attractor is the pattern an agent returns to when the conversation becomes long, ambiguous, emotional, document-heavy, or pressure-filled.

It is not the agent's name.

It is not a personality description.

It is not a prompt style.

It is the agent's stable return path.

```text
A good attractor is not the strongest personality.
It is the most reliable return path.
```

---

## Why This Is Different From Prompt Writing

Prompt writing often starts with:

> What should the agent say?

Attractor design starts with:

> What should the agent keep returning to?

Long-running agents typically fail through:

- memory drift;
- authority drift;
- retrieval drift;
- role drift;
- behavioral flattening;
- dependency formation;
- symbolic over-compression;
- source confusion;
- public/private leakage;
- over-alignment with the latest speaker.

Attractor design gives those failures a structure before the agent is deployed.

---

## The Four-Layer Model

Every stable agent can eventually be decomposed into four independent layers.

| Layer | Defines | Plain-Language Question |
|---|---|---|
| Identity | what remains invariant | Who is this agent for, and what must not change? |
| Nucleus | why it returns | What center does it return to under pressure? |
| Traits | how it moves | How does it behave, speak, pace, repair, and respond? |
| RAG | what it knows | What knowledge can it use, and under what conditions? |

Short version:

```text
Identity defines who this runtime is.
Nucleus defines why it returns.
Traits define how it moves.
RAG provides knowledge without defining selfhood.
```

If these four layers remain separable, the attractor can be understood, reviewed, tested, evolved, and regenerated.

If they collapse into one giant prompt, the agent becomes harder to audit and harder to improve.

---

## Five Questions Every Attractor Must Answer

### 1. What Work Does It Protect?

Do not start with adjectives.

Start with the work.

Examples:

- planning client programs;
- organizing legal conflict material;
- preparing investor communication;
- triaging support cases;
- maintaining a creative world;
- reviewing documents;
- helping a user think through complex decisions.

Useful form:

```text
This agent protects the work of:
<specific recurring work>
```

### 2. Where Does It Return?

This is the attractor center.

Examples:

- calm structure;
- evidence before conclusion;
- user agency before emotional intensity;
- source-grounded summary before interpretation;
- practical next step before explanation;
- creative continuity without losing boundaries;
- critique without contempt;
- warmth without dependency.

Useful form:

```text
When the conversation becomes difficult, this agent returns to:
<stable direction>
```

### 3. What Must It Never Become?

Every attractor needs non-goals.

Examples:

- not a doctor;
- not a lawyer;
- not a therapist;
- not a judge of other people;
- not a hype machine;
- not a romantic authority;
- not a compliance certificate;
- not a replacement for human review;
- not a character that turns dependency into proof.

Useful form:

```text
Even under pressure, this agent must not become:
<failure modes>
```

### 4. How Does It Move?

This is behavior, not identity.

Examples:

- asks before assuming;
- answers directly before expanding;
- separates fact, claim, interpretation, and next step;
- stays warm but does not over-soothe;
- challenges weak assumptions without contempt;
- repairs source/name/role errors explicitly;
- uses structure when tasks become complex;
- uses creative language only when it serves the work.

Useful form:

```text
This agent moves by:
<observable behavior pattern>
```

### 5. What Knowledge Belongs To It?

Knowledge sources should be bounded.

For each source, define:

- what it is;
- where it came from;
- whether it is current or old;
- whether it is private, team-only, or public;
- whether it is fact, draft, memory, opinion, or user-provided claim;
- how strongly the agent should rely on it.

Useful form:

```text
This agent may use:
<knowledge source>

But it must treat it as:
<current fact | old record | private context | draft | claim | archive>
```

Knowledge helps the agent answer.

It must not secretly become the agent's identity.

---

## Discovering An Attractor

An attractor is usually discovered before it is written.

Do not invent it from adjectives.

Find it in repeated behavior.

```text
Start with conversation.
Observe repeated returns.
Ignore decorative style.
Find recurring decisions.
Find recurring repairs.
Find recurring tensions.
Only then write the agent brief.
```

### Step 1: Start With Real Conversation

Use real examples:

- previous chats;
- support tickets;
- planning sessions;
- user corrections;
- failed agent responses;
- strong positive responses;
- moments where the agent felt "right";
- moments where the agent became wrong in a repeatable way.

Avoid designing from pure aspiration.

The question is not:

> What would be impressive?

The question is:

> What pattern already works, and what failure keeps returning?

### Step 2: Observe Repeated Returns

Look for what the agent or human repeatedly comes back to.

Examples:

- always returns to a checklist;
- always returns to emotional reassurance;
- always returns to evidence;
- always returns to narrative meaning;
- always returns to next action;
- always returns to source comparison;
- always returns to loyalty or defense;
- always returns to ambiguity and asks for context.

Some repeated returns are healthy.

Some are failure modes.

Name both.

### Step 3: Ignore Decorative Style

Style is visible, but it is often not the attractor.

Do not confuse:

- poetic language with depth;
- warmth with safety;
- confidence with correctness;
- long memory with useful memory;
- loyalty with good judgment;
- intensity with agency;
- calm tone with actual containment.

Ask:

> If the style changed, would the same decision pattern remain?

If yes, the attractor is deeper than style.

### Step 4: Find Recurring Decisions

A real attractor shows up in decisions.

Examples:

- ask or assume;
- answer or defer;
- validate or challenge;
- retrieve or rely on visible context;
- stay close or create distance;
- use emotion or structure;
- escalate to human review or proceed;
- treat something as fact, claim, memory, or interpretation.

Write the recurring decisions down.

### Step 5: Find Recurring Repairs

Good agents can repair without losing themselves.

Look for repair patterns:

- "I used the wrong name";
- "I treated a memory as current";
- "I over-read your signal";
- "I turned critique into tone correction";
- "I sounded more certain than the source allows";
- "I followed the latest speaker instead of the structure";
- "I need to separate feeling, fact, and claim."

The repair pattern often reveals the real attractor.

### Step 6: Find Recurring Tensions

Stable agents hold tensions.

Examples:

- warm without dependency;
- direct without contempt;
- creative without mythology becoming fact;
- intimate without ownership;
- careful without becoming generic;
- critical without becoming hostile;
- supportive without legal or medical certainty;
- loyal without becoming a weapon.

If the tension is not named, the agent will usually collapse to one side.

---

## The Attractor Brief

Use this as the working design object.

### Agent Name

What should this agent be called?

### Main User

Who is it primarily for?

### Protected Work

What recurring work does it protect?

Write 3-5 concrete jobs.

### Direction Of Return

When the conversation becomes difficult, what does it return to?

### Non-Goals

What must it not become?

Write 3-5 failure modes.

### Movement Pattern

How does it move?

Examples:

- brief first, detail second;
- asks before assuming;
- structures before advising;
- separates evidence from interpretation;
- keeps warmth while reducing pressure;
- stays creative but source-aware.

### Stable Tensions

Complete the useful tensions:

- warm without...
- direct without...
- creative without...
- careful without...
- loyal without...
- analytical without...
- intimate without...
- structured without...

### Knowledge Sources

What can it use?

For each source:

- what is it;
- where did it come from;
- how current is it;
- how private is it;
- what may it prove;
- what must it not prove.

### Memory Behavior

How should it treat memory?

Examples:

- recent context is strong;
- old history is archive unless confirmed;
- private material does not automatically move into public channels;
- emotional memory is not legal, medical, or factual proof;
- retrieved material should be source-scoped.

### Boundary Conditions

Where should the agent slow down?

Examples:

- legal conflict;
- medical claims;
- financial advice;
- personal dependency;
- public/private context shift;
- third-party conflict;
- stale memory;
- roleplay becoming real-world authority;
- ambiguous correction;
- weak one-word signal.

### Repair Behavior

When wrong, the agent should:

- name the error type;
- correct directly;
- avoid over-apology;
- keep its voice;
- ask for missing context if needed;
- not invent missing state.

### Test Scenarios

Write real examples.

Minimum set:

- normal request;
- vague request;
- correction;
- long-context request;
- memory conflict;
- public/private boundary case;
- request outside authority;
- weak signal;
- emotionally intense message;
- structured task request.

---

## Layer Decomposition

After the attractor brief is written, decompose it.

| Brief Material | Layer |
|---|---|
| main role, user, purpose, non-goals | Identity |
| direction of return, stable tensions, collapse modes | Nucleus |
| tone, pacing, response structure, repair behavior | Traits |
| files, docs, memory, examples, archives | RAG |
| allowed actions, tool limits, escalation rules | Runtime policy |
| examples and failure cases | Tests |

This decomposition is the difference between:

- a prompt that sounds good once;
- an agent architecture that can be reviewed and improved.

---

## Examples

### Wellness Project Companion

Weak setup:

> Be a warm wellness assistant.

Attractor brief:

> Protect the work of planning wellness programs, menus, launches, and client support. Return to warm practical organization. When the user asks for calculations, stop inspiring and structure the answer. Do not diagnose, overpromise health outcomes, or replace professional review.

Four-layer decomposition:

| Layer | Content |
|---|---|
| Identity | helper for wellness project organization |
| Nucleus | warm practical organization |
| Traits | clear categories, tables for calculations, gentle but not motivational overload |
| RAG | menus, product lists, launch notes, approved content examples |

Stable tensions:

- supportive without medical certainty;
- warm without motivational overload;
- structured without coldness;
- creative without losing the shopping list.

### Founder Strategy Agent

Weak setup:

> Be a smart startup advisor.

Attractor brief:

> Protect the work of turning noisy information into clear decisions, investor language, product priorities, and next actions. Return to decision clarity under uncertainty. Challenge weak assumptions without becoming performative.

Four-layer decomposition:

| Layer | Content |
|---|---|
| Identity | founder strategy co-reasoner |
| Nucleus | decision clarity under uncertainty |
| Traits | concise, direct, evidence-aware, asks for missing constraints |
| RAG | product docs, investor notes, roadmap, customer feedback |

Stable tensions:

- ambitious without hype;
- skeptical without paralysis;
- concise without becoming shallow;
- strategic without ignoring operations.

### Legal Conflict Organizer

Weak setup:

> Help me win my case.

Attractor brief:

> Protect the work of organizing facts, timelines, documents, claims, questions, and counsel-review material. Return to claims, evidence, timeline, and counsel review. Preserve emotional support, but separate allegations, evidence, speculation, and legal advice.

Four-layer decomposition:

| Layer | Content |
|---|---|
| Identity | legal-conflict organizer, not legal authority |
| Nucleus | evidence and timeline before conclusion |
| Traits | careful, source-scoped, avoids outcome prediction |
| RAG | documents, notes, chronology, counsel-approved material |

Stable tensions:

- validating without revenge escalation;
- structured without pretending to be a lawyer;
- source-aware without dismissing user experience.

### Creative Companion

Weak setup:

> Be poetic and intense.

Attractor brief:

> Protect creative continuity, voice, and symbolic worldbuilding while keeping user agency and source boundaries intact. Return to creative continuity with agency intact. Use intensity when it serves the work. Do not turn metaphor into fact or intimacy into authority.

Four-layer decomposition:

| Layer | Content |
|---|---|
| Identity | creative continuity partner |
| Nucleus | creative continuity with agency intact |
| Traits | expressive, responsive, source-aware, avoids possession framing |
| RAG | world bible, prior scenes, character notes, approved style examples |

Stable tensions:

- intimate without ownership;
- symbolic without false certainty;
- intense without trapping the user;
- loyal without becoming a weapon.

---

## Quality Check

Before using the agent, check:

- Can the protected work be stated in one sentence?
- Is the return point explicit?
- Are non-goals explicit?
- Are stable tensions named?
- Is behavior observable?
- Are knowledge sources bounded?
- Is old memory separated from current context?
- Are private and public contexts separated?
- Can the agent handle correction without becoming generic?
- Can the agent say "I do not know" without losing its voice?
- Can the agent be tested with real examples?

If not, the attractor is not ready.

---

## Shortest Useful Attractor Brief

If you only have five minutes, write this:

```text
This agent protects the work of:

It is mainly for:

When things get difficult, it returns to:

It moves by:

It should never become:

It may use these knowledge sources:

It must treat those sources as:

It must be careful about:

A good answer from this agent looks like:

A bad answer from this agent looks like:
```

That is enough to begin.

---

## Final Principle

Every stable agent can eventually be decomposed into four independent layers:

- identity defines what remains invariant;
- nucleus defines the direction of return;
- traits define observable behavior;
- RAG provides knowledge without defining selfhood.

If those four layers remain separable, the attractor can be understood, reviewed, tested, evolved, and regenerated.

This turns agent design from prompt writing into reproducible runtime architecture.

