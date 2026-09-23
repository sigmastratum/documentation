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

# SRIP-28 - Trajectory Admission Loop (TAL)

**Candidate Admission, Containment, and Bounded Recovery**

| Field | Value |
| --- | --- |
| SRIP | SRIP-28 |
| Title | Trajectory Admission Loop (TAL) |
| Version | Public Draft v0.2 |
| Status | Public Draft |
| Date | 2026-09-23 |
| Authors / Contributors | Sigma Stratum Research Group (SSRG) |
| Owning Layer | Runtime Control / Candidate Admission / Delivery Governance |
| Parent Specs | SRIP-10, SRIP-15, SRIP-19, SRIP-27 |
| Related Specs | SRIP-03, SRIP-08, SRIP-13, SRIP-21, SRIP-23, SRIP-24, SRIP-25, SRIP-26 |
| Specification License | CC BY 4.0 |
| Implementation Safe Harbor | Independent implementation permitted under public SRS/SRIP terms |
| Machine-Readable Artifacts | Apache 2.0 where explicitly marked |
| Marks / Certification | Governed by Sigma Marks and Certification Policy |
| Proprietary Runtime Assets | Not licensed by this SRIP |
| Independent Implementation | Permitted under the public specification terms |
| Information Class | Open |
| Change Class | Mixed SRS+SRD |
| Specification Class | Runtime Protocol |
| Normative Status | Public draft pre-persistence admission contract; it does not grant production enablement or certification authority. |
| Conformance Level | Public Draft / No runtime conformance claim |
| SRD Synchronization Action | Completed in `/srd/architecture.md`, `/srd/runtime-loop.md`, `/srd/memory.md`, and `/srd/safety.md` |
| Release Alignment Status | aligned |
| Release Alignment Notes | Public explanation is synchronized; no production enforcement, automatic fallback, response mutation, model support, or conformance claim is made by this document alone. |

---

## Independent Implementation Safe Harbor

Independent implementations of the public normative requirements in this SRIP are welcome under the applicable public specification terms.

No Sigma commercial runtime license is needed solely because an independent implementation follows these public normative requirements.

Product assets, protected Sigma marks, official certification, compatibility badges, CC BY-NC commercial use, and patent commitments use the relevant policy or explicit covenant. Independent implementation, attribution, or citation does not imply certification, endorsement, partnership, official compatibility, or permission to use Sigma marks as product identity.

---

## 1. Summary

SRIP-28 defines the **Trajectory Admission Loop (TAL)**: a pre-persistence
candidate-admission transaction for deciding whether generated material may be
delivered and influence future runtime state.

A provider response is a candidate until the runtime grants delivery and
influence authority. Detection after persistence is too late: the candidate
may already have changed history, memory, retrieval, observer state, or the
next active field.

TAL answers:

```text
What delivery and influence authority may this candidate receive?
```

## 2. Non-Duplication Review

| Existing specification | Existing responsibility | TAL gap |
| --- | --- | --- |
| SRIP-10 AEP | Dynamic entropy and adaptability signals | Does not own candidate delivery |
| SRIP-15 ADP | Perturbation and return-path behavior | Does not define atomic admission |
| SRIP-19 RCB | Conflict buffering and branch preservation | Does not select the delivered candidate |
| SRIP-23 DGL | Dialectical candidate generation | Does not govern accepted trajectory history |
| SRIP-25 IEM | Interaction-event classification | Events are evidence, not admission decisions |
| SRIP-26 MIL | Memory influence authority | Governs memory influence after candidate selection |
| SRIP-27 TMC | Target-relative membership measurement | Measures candidates but cannot deliver or reject them |

SRIP-28 is a separate single-writer admission transaction. It consumes bounded
evidence from other layers without taking ownership of their metrics.

TAL owns candidate delivery and admission only. It does not own authorization
or release of an external effect. An admitted candidate that proposes a tool
call, message, file mutation, provider attempt, or other consequential effect
remains subject to SRIP-24 effect authority and SRIP-25 event evidence.

## 3. Candidate and Decision Model

Each generated output receives immutable lineage before delivery:

- candidate reference and generation stage;
- parent candidate reference when recovery is attempted;
- source, route, model/profile, and authority references;
- measurement validity and evidence references;
- provider boundary state;
- admission decision and selected-candidate reference.

Admission decisions are:

- `admit`;
- `hold`;
- `reject`;
- `boundary_only`;
- `contain_review`.

Candidate bodies are not part of public operator evidence.

## 4. Transaction Boundary

TAL operates after candidate generation and measurement but before accepted
assistant persistence and downstream influence.

The transaction must:

1. preserve the accepted user turn;
2. capture a pre-candidate runtime frame;
3. measure the original candidate without mutation;
4. select at most one delivered candidate;
5. prevent held or rejected candidates from entering accepted history;
6. restore pre-candidate state on containment or failure;
7. fail closed if rollback or selected-candidate lineage cannot be proven.

Held or rejected candidates must not update:

- accepted-local reference;
- conversation history used as authority;
- memory or retrieval influence;
- checkpoint or fact state;
- dynamic observer state as though delivery occurred.

## 5. Supervisory Boundary

- ALICE or an equivalent supervisor owns the consolidated control posture.
- AEP reports dynamic stability and entropy evidence.
- TMC reports target-relative membership and validity.
- IEM classifies the interaction event.
- RCB supplies bounded hold and cooling readiness.
- MIL governs downstream memory influence.
- TAL alone commits the delivery/admission transaction.

`stable + collapsed` is representable: stable dynamics do not override failed
membership.

## 6. Bounded Recovery

Recovery is optional and separately authorized. When enabled:

- at most one recovery generation may follow an eligible held candidate;
- the route is lifecycle-resolved rather than hardcoded to a provider model;
- recovery receives bounded accepted context, not the rejected candidate as
  authority;
- recursive fallback is prohibited;
- recovery is measured independently;
- failed or ambiguous recovery becomes `contain_review`;
- recovery does not update accepted-local authority merely by being generated.

Provider capability and safety boundaries retain higher precedence and may be
represented as typed `boundary_only` events.

## 7. Generation-Side Prevention

TAL is a containment mechanism, not a substitute for a coherent active field.
Where competing identity or retrieval authority causes collapse,
implementations should reduce that conflict before generation rather than
stack retries, guides, or post-generation rewrites.

Generation quality and admission quality are independent. A system may improve
generation sufficiently that TAL rarely acts; it must still preserve atomic
lineage and fail-closed behavior when TAL is enabled.

## 8. Qualification Boundary

Production admission requires evidence for the declared scope that:

- admitted-collapse delivery is bounded to the approved risk target;
- member delivery remains usable;
- selected-candidate lineage is complete;
- held and rejected candidates do not contaminate future state;
- restart hydration preserves decision versions and spent recovery budget;
- no neighboring model/profile measurement is silently substituted;
- operator surfaces contain no raw transcript, prompt, candidate, retrieval
  body, actor-specific rule, or secret.

Without qualified measurement and delivery evidence, TAL remains action-inert
or fail-closed. A source implementation alone is not a production conformance
claim.

## 9. Relationship to SRIP-27

SRIP-27 owns target-membership measurement and validity. SRIP-28 owns the
candidate-admission transaction.

```text
TMC measures.
TAL admits.
```

TAL must not alter the measurement of the original candidate. TMC must not
deliver or reject a candidate directly.

## 10. Public-Safe Boundary

This SRIP does not expose private prompts, transcripts, candidate bodies,
agent identities, provider credentials, deployment topology, private fixtures,
thresholds, or proprietary recovery wording.

This SRIP does not claim production enablement, automatic fallback, response
mutation, model support, or runtime conformance.

## 11. Conformance Expectations

A conforming implementation must:

- preserve immutable candidate and selected-delivery lineage;
- perform admission before accepted assistant persistence;
- prevent held and rejected candidates from influencing future state;
- preserve the accepted user turn during containment;
- keep recovery bounded and non-recursive;
- fail closed when rollback, authority, or lineage cannot be proven;
- preserve provider boundary precedence;
- expose content-safe decision evidence.

Public draft publication alone does not establish implementation conformance.

## 12. Change Log

| Version | Date | Author | Description |
| --- | --- | --- | --- |
| 0.1 | 2026-07-17 | SSRG | Initial public trajectory-admission contract. |
| 0.2 | 2026-09-23 | SSRG | Clarified that candidate admission does not authorize or release external effects. |
