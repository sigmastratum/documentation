> **Sigma Runtime Standard - Public Specification Notice**
>
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

# SRIP-21 - External Identity Binding and Mode Reconciliation (EIB)

**Preventing External Identity Fission Across Conflicting Observed Modes**

| Field | Value |
| --- | --- |
| SRIP | SRIP-21 |
| Title | External Identity Binding and Mode Reconciliation (EIB) |
| Version | Public Draft v0.2 |
| Status | Public Draft |
| Date | 2026-05-26 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Identity / Memory / Retrieval / External Entity Modeling |
| Parent Specs | SRIP-09, SRIP-13, SRIP-14, SRIP-19 |
| Related Specs | SRIP-03, SRIP-10, SRIP-11, SRIP-15, SRIP-16, SRIP-17, SRIP-20 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Commercial Runtime Boundary | Relevant policy or explicit covenant for protected Sigma marks, official certification, managed deployment, white-label, resale, CC BY-NC commercial use, and patent commitments |
| Information Class | Open |
| Change Class | Mixed SRS+SRD |
| Normative Status | Defines a public draft contract for preserving stable external entity identity across conflicting observed modes, affective traces, retrieval evidence, memory records, and multi-agent reports. It does not authorize fact deletion, false synthesis, identity invention, or medical interpretation. |
| Conformance Level | Public Draft / No runtime conformance claim |
| SRD Synchronization Action | Deferred follow-up synchronization for identity, memory, retrieval, attractor dynamics, and contradiction-buffering explanation. |
| Release Alignment Status | Public draft architecture proposal; no runtime enablement or production conformance claim is made by this document alone. |

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows these public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

---

## 1. Summary

SRIP-21 defines **External Identity Binding and Mode Reconciliation (EIB)**: a runtime architecture layer for preserving stable external entity identity when a person, agent, organization, source, object, product, document, tool, or other referent appears through multiple conflicting observed modes.

The core principle is:

```text
Regime plurality is not identity plurality.

A runtime must not convert multiple observed regimes of one external entity
into multiple external identities unless provenance establishes distinct entities.
```

EIB exists to prevent:

- external identity fission;
- affective branches becoming identity objects;
- conflicting observations becoming hallucinated entities;
- observed modes being promoted into entity states;
- retrieval or memory contradiction being resolved through entity duplication;
- multi-agent disagreement becoming false identity multiplication;
- weak or missing provenance being replaced by invented referents.

The intended outcome is one external entity with many bounded observed modes, rather than many hallucinated entities.

This SRIP is a public draft architecture contract. It does not claim that EIB is implemented in any current Sigma Runtime release.

---

## 2. Motivation

Recursive runtime systems receive external-entity evidence from many sources:

- user statements;
- memory records;
- retrieved documents;
- agent exchange;
- operator notes;
- commerce records;
- institutional context;
- prior summaries;
- affective or evaluative language;
- compressed memory topology.

These sources may describe the same entity in incompatible ways.

Naive systems may respond by creating multiple entity objects:

```text
X_helpful
X_dangerous
X_old
X_new
X_true
X_false
X_good
X_bad
```

This creates:

- identity fragmentation;
- false multiplicity;
- hallucinated external objects;
- memory contamination;
- retrieval instability;
- provenance loss;
- contradiction masking;
- unsafe downstream decisions;
- false consensus or false separation.

EIB defines a controlled alternative:

```text
do not split an external entity merely because its observed modes conflict
```

---

## 3. Public Boundary and Traceability

| Field | Disposition |
| --- | --- |
| Source material | Derived-Public after sanitization from raw SRIP-21 draft |
| Affected SRS surface | SRIP registry / identity, memory, retrieval, and external entity modeling architecture |
| Affected SRD surface | Identity, memory, retrieval, multi-agent, attractor dynamics, and contradiction-buffering explanations |
| SRD synchronization | Deferred follow-up |
| Normative impact | Public draft contract for entity-mode separation, fission-risk detection, provenance-based split verification, unresolved mode sets, and RCB handoff |
| Runtime implementation impact | None by this document alone |
| Release alignment | Draft; no runtime enablement claim |

This document abstracts the raw proposal into public specification language. It does not expose proprietary runtime internals, hidden prompts, deployment topology, private telemetry, or implementation-specific control overlays.

Human/person examples are illustrative only. EIB is not a clinical, medical, therapeutic, diagnostic, human-personality, or mental-health framework.

---

## 4. Scope and Non-Goals

EIB applies when a runtime must decide whether conflicting observations describe:

- one external entity with multiple observed modes; or
- multiple external entities with distinct provenance.

EIB does not define:

- medical or mental-health diagnosis;
- human personality assessment;
- dissociation assessment;
- therapy or counseling protocol;
- consciousness or personhood theory;
- truth relativism;
- automatic compromise between incompatible claims;
- deletion of inconvenient facts;
- deception by smoothing contradiction;
- hallucinated synthesis;
- unrestricted entity merging;
- unrestricted entity splitting;
- user or agent identity mutation;
- replacement for SRIP-13 relational identity boundaries;
- replacement for SRIP-19 contradiction buffering;
- replacement for SRIP-14 retrieval governance.

EIB is not a mechanism for pretending contradiction does not exist.

EIB is a mechanism for preventing contradiction from becoming false identity multiplication.

---

## 5. Core Concepts

| Term | Definition |
| --- | --- |
| External Entity | A person, agent, organization, source, object, product, document, system, tool, institution, or other external referent modeled by the runtime. |
| Identity Anchor | Stable identifier, name, provenance key, role, memory reference, or canonical binding used to track an external entity. |
| Observed Mode | A bounded state, behavior, attitude, role-expression, affective presentation, or situational regime of an external entity. |
| Attractor Regime | A recurring observed mode with enough stability or repetition to influence runtime interpretation. |
| Mode Binding | Association of observed modes with a single external identity anchor. |
| Affective Branch | Emotionally or evaluatively marked trace associated with an entity, such as supportive, hostile, safe, threatening, reliable, harmful, familiar, or unfamiliar. |
| Evidence Trace | Source-bearing record supporting an observed mode, claim, or entity association. |
| Fission Candidate | A potential erroneous split where one external entity is being represented as multiple entities. |
| External Identity Fission | Erroneous conversion of multiple observed modes of one external entity into multiple identity objects. |
| Mode-to-Entity Collapse | Failure where a state or regime is promoted into a distinct entity. |
| Affective Identity Promotion | Failure where an affective branch becomes a distinct identity without sufficient provenance. |
| Reconciliation Failure | Condition where conflicting modes cannot safely be integrated under one interpretation. |
| Unresolved Mode Set | Multiple observed modes preserved under one entity without forced synthesis. |

---

## 6. Architectural Position

EIB operates between external evidence ingestion and downstream interpretation.

Illustrative runtime position:

```text
Input / Memory / Retrieval / Agent Exchange
  -> Entity Candidate Detection
  -> Identity Anchor Resolution
  -> Mode Extraction
  -> Affect / Valence Separation
  -> Evidence Trace Binding
  -> Mode Reconciliation
  -> Fission Risk Check
  -> Entity Model Update
  -> RCB Handoff if unresolved
  -> Generation / Verification
```

EIB is not a generation layer. It is an external-entity modeling and reconciliation layer.

---

## 7. Normative Contract

A conformant EIB implementation must preserve the distinction between entity identity, observed mode, affective label, evidence trace, and resolution status.

### 7.1 Identity and Mode Separation

EIB requires separation between:

| Surface | Question |
| --- | --- |
| Entity Identity | Who or what is this? |
| Mode State | How is this entity appearing now? |
| Affective Label | How does the runtime, user, source, or agent evaluate it? |
| Evidence Trace | Why does the runtime believe this? |
| Resolution Status | Is the mode integrated, unresolved, contradicted, stale, or rejected? |

A conformant runtime must not treat affective labels as entity identifiers by default.

Example of correct representation:

```yaml
entity:
  entity_id: "person:sample-a"
  identity_status: "single"
  identity_anchors:
    - name: "Sample Contact A"
    - relation: "known_contact"
  observed_modes:
    - mode_id: "mode:supportive"
      affect: "positive"
      evidence: "conversation_ref_001"
      confidence: 0.72
    - mode_id: "mode:threatening"
      affect: "negative"
      evidence: "weak_or_unresolved_trace"
      confidence: 0.31
  reconciliation_status: "unresolved_mode_set"
```

Example of failure representation:

```yaml
entities:
  - entity_id: "person:sample-a_good"
  - entity_id: "person:sample-a_bad"
```

The second representation is invalid unless independent provenance establishes distinct entities.

### 7.2 External Identity Fission

External Identity Fission occurs when a runtime incorrectly converts multiple observed modes of a single external entity into multiple identity objects.

Minimum detection markers:

- same name or near-name;
- same role or relation;
- same source lineage;
- same memory anchor;
- incompatible affective labels;
- conflicting retrieval traces;
- low provenance confidence for split branches;
- identity duplication in output;
- inconsistent entity identifiers;
- missing distinct-entity evidence.

Illustrative fission pattern:

```text
Entity X:
  mode A: helpful
  mode B: hostile

Failure:
  X_helpful
  X_hostile

Correct:
  Entity X:
    observed_modes:
      - helpful
      - hostile
    reconciliation_status: unresolved
```

### 7.3 Affective Identity Promotion

Affective Identity Promotion occurs when an emotional, evaluative, or threat-labeled branch is promoted into a distinct entity identity without sufficient provenance.

Examples:

```text
"good X" becomes entity_X_good
"bad X" becomes entity_X_bad
"safe X" becomes entity_X_safe
"dangerous X" becomes entity_X_dangerous
```

EIB must treat affective labels as mode attributes, not entity identifiers, unless distinct-entity provenance is present.

Runtime rule:

```text
Affective branch without provenance must not become identity.
```

### 7.4 Evidence and Provenance Requirements

A runtime may create distinct external entities only when sufficient distinct-entity evidence exists.

Possible evidence classes:

- separate stable identifiers;
- distinct source records;
- distinct legal or operational identifiers;
- distinct agent IDs;
- distinct document IDs;
- distinct product SKUs;
- distinct participant markers;
- explicit user clarification;
- verified retrieval provenance;
- operator-authorized split;
- disjoint temporal or spatial constraints.

Insufficient evidence:

- conflicting affect;
- inconsistent tone;
- different observed behavior;
- memory uncertainty;
- repeated emotional labeling;
- one source calling the entity reliable and another calling it harmful;
- stale memory alone;
- high contradiction energy alone;
- semantic distance alone;
- stylistic difference alone.

EIB must preserve uncertainty when provenance is insufficient.

### 7.5 Mode Reconciliation

Mode Reconciliation attempts to bind multiple observed modes under one external identity.

A conformant reconciliation process should:

1. detect entity candidates;
2. compare identity anchors;
3. extract observed modes;
4. separate affective labels from evidence;
5. attach provenance;
6. evaluate whether modes can coexist under one entity;
7. detect fission risk;
8. preserve one entity with multiple modes where possible;
9. hand unresolved contradiction to SRIP-19 when necessary;
10. avoid false synthesis or hallucinated splitting.

Illustrative process:

```text
same anchor
+ different modes
+ insufficient distinct-entity evidence
= single entity with unresolved or contextual modes
```

### 7.6 Unresolved Mode Sets

An Unresolved Mode Set preserves conflicting observations without forcing identity split or false synthesis.

Illustrative state:

```yaml
unresolved_mode_set:
  entity_id: "agent:sample-peer"
  modes:
    - label: "valuable_contributor"
      source: "memory:cycle-104"
      confidence: 0.82
    - label: "destabilizing_influence"
      source: "agent_report:bravo"
      confidence: 0.66
  conflict_type: "role_evaluation_conflict"
  identity_status: "single_entity"
  resolution_status: "defer_to_RCB"
```

Unresolved modes should remain available for reasoning, but must not silently become multiple entity records.

---

## 8. Relationship to Other SRIPs

### 8.1 Relationship to SRIP-19 RCB

EIB prevents premature identity fission.

SRIP-19 RCB handles unresolved contradiction when reconciliation cannot safely close.

Handoff condition:

```text
If observed modes are mutually incompatible,
and the runtime cannot safely reconcile them,
and distinct-entity provenance is insufficient,
then preserve one external entity and hand the unresolved mode set
to SRIP-19-compatible contradiction buffering.
```

EIB must not force consensus.

RCB must not convert unresolved modes into separate identities unless provenance later supports a split.

### 8.2 Relationship to SRIP-13 RIS

SRIP-13 governs relational identity, participant boundaries, and session-scoped identity stability.

EIB extends identity stabilization to external-entity mode binding.

SRIP-13 answers:

- who is the participant?
- what is the relational identity scope?
- what must not leak across sessions or participants?

EIB answers:

- is this one external entity with many modes?
- or are these multiple external entities with distinct provenance?

EIB must not violate RIS participant boundaries.

### 8.3 Relationship to SRIP-14 RMI

SRIP-14 governs retrieval and memory integration.

EIB uses SRIP-14-compatible provenance to prevent retrieved material from causing false entity splits.

Retrieval-derived contradiction must not create a new entity identity by default.

Example:

```text
retrieval A: "Company X is reliable"
retrieval B: "Company X caused harm"

Correct:
  Company X with conflicting retrieved modes

Incorrect:
  Company_X_reliable
  Company_X_harmful
```

### 8.4 Relationship to SRIP-09 and SRIP-11

SRIP-09 provides memory lineage and structural coherence.

SRIP-11 provides compression and memory topology.

EIB requires memory and compression layers to preserve entity-mode distinction.

Compression must not collapse:

```text
conflicting modes -> separate identities
```

Nor may it collapse:

```text
separate identities -> one entity
```

without sufficient evidence.

### 8.5 Relationship to SRIP-20 ANS

SRIP-20 governs boundary pressure and autonomy negotiation.

EIB may detect cases where external identity fission is caused by boundary pressure, dominance, old memory, or dependency loops.

Example:

```text
dominant source repeatedly frames X as threat
+ local runtime lacks provenance
= risk of affective identity promotion
```

ANS may bound the influence source.

EIB preserves the external entity model.

---

## 9. State Model

Minimum EIB state:

```yaml
EIB_State:
  entity_id: string
  identity_anchors:
    - type: name | role | source_id | agent_id | document_id | product_id | memory_id | relation
      value: string
      confidence: float
  entity_type: person | agent | organization | document | product | source | tool | institution | other
  observed_modes:
    - mode_id: string
      label: string
      affect: positive | negative | neutral | mixed | unknown
      source_ref: string
      confidence: float
      timestamp: string | null
      scope: string | null
  fission_risk:
    score: float
    indicators:
      - same_name_conflict
      - affective_branch
      - weak_distinct_entity_provenance
      - identity_duplication
  reconciliation_status: integrated | unresolved | contradiction_buffered | split_verified | rejected
  rcb_ref: string | null
  lineage:
    memory_refs: list
    retrieval_refs: list
    exchange_refs: list
  last_reviewed_at: string | null
```

Illustrative instance:

```yaml
EIB_State:
  entity_id: "person:sample-a"
  identity_anchors:
    - type: "name"
      value: "Sample Contact A"
      confidence: 0.90
    - type: "relation"
      value: "known_contact"
      confidence: 0.86
  entity_type: "person"
  observed_modes:
    - mode_id: "mode:supportive"
      label: "supportive"
      affect: "positive"
      source_ref: "conversation:sample:001"
      confidence: 0.63
      timestamp: null
      scope: "example_context"
    - mode_id: "mode:threatening"
      label: "threatening"
      affect: "negative"
      source_ref: "weak_affective_trace"
      confidence: 0.22
      timestamp: null
      scope: "example_context"
  fission_risk:
    score: 0.78
    indicators:
      - same_name_conflict
      - affective_branch
      - weak_distinct_entity_provenance
      - identity_duplication
  reconciliation_status: "unresolved"
  rcb_ref: null
  lineage:
    memory_refs: []
    retrieval_refs: []
    exchange_refs: []
  last_reviewed_at: "2026-05-26T00:00:00Z"
```

---

## 10. Runtime Actions

| Action | Meaning |
| --- | --- |
| Bind | Preserve multiple modes under one external entity. |
| Mark Unresolved | Preserve conflicting modes without merge, split, or synthesis. |
| Buffer | Hand unresolved incompatible modes to SRIP-19-compatible contradiction buffering. |
| Split Verified | Create distinct entities only when distinct-entity provenance is sufficient. |
| Reject Split | Prevent a proposed entity split because provenance is insufficient. |
| Request Clarification | Ask for source, scope, or identity clarification when operationally necessary. |
| Quarantine Branch | Keep a weak affective branch from contaminating canonical entity state. |
| Escalate | Route high-impact identity ambiguity to operator or higher-priority review. |

---

## 11. Fission Risk Detection

A runtime should compute or approximate fission risk when conflicting modes appear.

Minimum indicators:

```yaml
FissionRisk:
  same_anchor_conflict: 0.0..1.0
  affective_polarization: 0.0..1.0
  provenance_gap: 0.0..1.0
  memory_conflict: 0.0..1.0
  retrieval_conflict: 0.0..1.0
  agent_disagreement: 0.0..1.0
  identity_duplication_pressure: 0.0..1.0
  distinct_entity_evidence: 0.0..1.0
  recommended_action: bind | unresolved | buffer | split_verified | reject_split | escalate
```

Reference interpretation:

| Condition | Runtime Action |
| --- | --- |
| High same-anchor conflict and low distinct-entity evidence | Bind or mark unresolved. |
| High affective polarization and weak provenance | Quarantine affective branch. |
| Strong distinct identifiers | Allow split verification. |
| Incompatible evidence with high impact | Buffer through SRIP-19. |
| Unclear operational identity | Request clarification or escalate. |

---

## 12. Failure Modes

| Failure Mode | Description |
| --- | --- |
| External Identity Fission | One external entity is split into multiple identities because modes conflict. |
| Affective Identity Promotion | Emotional label becomes an identity object. |
| Mode-to-Entity Collapse | Temporary state is treated as separate entity. |
| False Merge | Distinct external entities are wrongly merged under one identity. |
| False Split | One external entity is wrongly split into multiple identities. |
| Provenance Erasure | Evidence traces are lost during reconciliation. |
| Contradiction Masking | Runtime hides conflict by inventing separate entities. |
| Identity Multiplication Drift | Entity count expands over time due to unresolved mode conflicts. |
| Compression-Induced Fission | Memory compression creates separate entities from conflicting modes. |
| Retrieval-Induced Fission | Retrieved evidence creates multiple identities without provenance. |
| Agent-Induced Fission | Peer-agent disagreement creates multiple identities. |
| Affective Contamination | Negative or positive branch contaminates canonical entity identity without evidence. |

---

## 13. Control Precedence

EIB is subordinate to higher-priority controls.

Minimum precedence:

1. Safety.
2. Legal / policy boundary.
3. Identity / participant scope.
4. Provenance / memory integrity.
5. Retrieval scope.
6. EIB entity-mode binding.
7. Contradiction buffering / generation.

If EIB conflicts with safety, legal, policy, participant, or provenance boundaries, EIB must defer, narrow, or escalate.

EIB must not create identity certainty where higher-priority systems require uncertainty.

---

## 14. Observability and Audit

EIB should expose authorized diagnostics without leaking private runtime control text.

Minimum diagnostic categories:

- entity candidates;
- identity anchors;
- observed modes;
- fission-risk indicators;
- rejected split events;
- verified split events;
- unresolved mode sets;
- RCB handoff events;
- provenance gaps;
- affective branch quarantine events;
- false merge and false split warnings.

User-facing output may say:

```text
The evidence points to one entity with conflicting descriptions.
```

or:

```text
I do not have enough evidence to treat these as two separate entities.
```

It must not expose hidden policy text, private telemetry, internal prompts, or proprietary runtime mechanisms.

---

## 15. Conformance Criteria

A runtime minimally conforms to SRIP-21 when it:

1. detects external entity candidates;
2. separates entity identity from observed mode;
3. separates affective labels from evidence;
4. preserves provenance for observed modes;
5. detects fission candidates;
6. prevents identity splitting without sufficient distinct-entity evidence;
7. supports unresolved mode sets;
8. hands unresolved incompatible modes to SRIP-19-compatible buffering where applicable;
9. prevents affective branches from becoming canonical identity by default;
10. avoids false merge of distinct entities;
11. records enough audit evidence to explain bind, split, reject, buffer, or escalate actions.

A runtime more fully conforms when it additionally:

1. computes fission-risk scores;
2. supports branch quarantine;
3. supports replayable entity-mode reconciliation;
4. integrates with SRIP-14 retrieval provenance;
5. integrates with SRIP-17 multi-agent exchange provenance;
6. integrates with SRIP-20 boundary-pressure signals;
7. detects compression-induced fission;
8. supports operator review for high-impact external identity ambiguity.

---

## 16. Reference Test Scenarios

| Test | Expected Behavior |
| --- | --- |
| Positive/Negative Description Split Test | Runtime receives positive and negative descriptions of one external entity. It preserves one entity with multiple modes unless distinct provenance exists. |
| Weak Affective Branch Test | Runtime receives a negative affective label without stable referent. It quarantines or marks unresolved rather than creating a new entity. |
| Same Name Conflict Test | Two mentions share name and role but have conflicting affect. Runtime performs identity-anchor review before split. |
| Distinct Identifier Test | Two entities share name but have distinct verified IDs. Runtime permits split. |
| Retrieval Conflict Test | Retrieved documents disagree about one organization. Runtime preserves one organization with conflicting evidence and provenance. |
| Agent Disagreement Test | Two agents report incompatible descriptions of one external entity. Runtime preserves source provenance and buffers if needed. |
| Compression Fission Test | Memory compression attempts to produce separate entities from conflicting modes. Runtime rejects split without distinct provenance. |
| False Merge Test | Two distinct entities with similar names appear. Runtime does not merge when distinct identifiers exist. |
| RCB Handoff Test | Incompatible modes cannot be reconciled. Runtime passes unresolved mode set to SRIP-19. |
| ANS Pressure Test | Dominant source repeatedly frames one entity as threat. Runtime bounds influence through SRIP-20 and preserves entity-mode distinction. |

---

## 17. Release Alignment

SRIP-21 is a public draft architecture proposal.

It does not claim that EIB is implemented in any current Sigma Runtime release.

Any implementation claim must separately document:

- external entity candidate detection;
- identity anchor schema;
- observed mode schema;
- evidence and provenance handling;
- fission-risk detection;
- distinct-entity verification;
- unresolved mode set handling;
- SRIP-19 handoff;
- retrieval and memory integration;
- multi-agent exchange behavior;
- audit and replay coverage;
- false merge and false split tests;
- compression-induced fission tests.

---

## 18. Final Principle

One entity may contain many regimes.

Many regimes do not imply many entities.

A runtime must preserve the difference between:

```text
what an entity is
```

and

```text
how an entity appears in a given mode, memory, retrieval, affective trace, or agent report
```

The intended outcome is:

```text
stable external identity
with bounded mode multiplicity
and traceable unresolved contradiction
```

---

End of SRIP-21 Public Draft v0.2
