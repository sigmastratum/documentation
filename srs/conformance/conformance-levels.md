---
title: SRS Conformance Levels
description: Public vocabulary for SRS-referenced, aligned, partial, minimum, full, and Sigma-certified conformance levels.
published: true
date: 2026-05-23T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-05-23T00:00:00.000Z
---

# SRS Conformance Levels

These levels define public conformance vocabulary for implementations that cite, align with, implement, self-declare against, or obtain official certification for the Sigma Runtime Standard.

## SRS-Referenced

### Definition

The implementation cites, discusses, or uses concepts from SRS/SRIP but does not claim technical conformance.

### Allowed public wording

- "Built with reference to the Sigma Runtime Standard."
- "Uses concepts described in SRS/SRIP."

### Disallowed wording

- "Sigma Certified."
- "Official Sigma Runtime implementation."
- "Fully SRS conformant."

### Evidence required

Attribution link and version reference.

### Who may claim it

Any third party following the attribution requirements.

### Sigma approval required?

No.

## SRS-Aligned

### Definition

The implementation intentionally follows selected public SRS/SRIP concepts or requirements but does not claim complete conformance.

### Allowed public wording

- "Aligned with selected SRS requirements."
- "Implements selected public SRS/SRIP concepts."

### Disallowed wording

- "Sigma Certified."
- "Fully SRS conformant."
- "Official Sigma Runtime compatible."

### Evidence required

SRS/SRIP version reference, supported requirement list, unsupported requirement list, and known deviation summary.

### Who may claim it

Any third party with public or reviewable evidence.

### Sigma approval required?

No for truthful self-declaration. Yes for official certification or badge use.

## SRS-Partial

### Definition

The implementation satisfies a documented subset of public SRS/SRIP normative requirements and identifies unsupported or incomplete areas.

### Allowed public wording

- "Self-declared SRS-Partial against [version]."
- "Partially implements the following SRS/SRIP requirements: [list]."

### Disallowed wording

- "Sigma Certified."
- "SRS-Full."
- "Officially approved by Sigma Stratum."

### Evidence required

Version-pinned requirement matrix, supported SRIPs, unsupported SRIPs, known deviations, and evidence artifacts.

### Who may claim it

Any third party following the self-declaration policy.

### Sigma approval required?

No for self-declaration. Yes for official certification or registry listing.

## SRS-Minimum

### Definition

The implementation satisfies the minimum required public SRS/SRIP requirements for a declared scope and version.

### Allowed public wording

- "Self-declared SRS-Minimum against [version]."
- "Meets the declared minimum SRS/SRIP requirement set for [scope]."

### Disallowed wording

- "Sigma Certified."
- "SRS-Full."
- "Official Sigma Runtime implementation."

### Evidence required

Version-pinned minimum requirement matrix, test evidence, unsupported SRIPs, known deviations, and implementation scope.

### Who may claim it

Any third party following the self-declaration policy with sufficient evidence.

### Sigma approval required?

No for self-declaration. Yes for official certification or badge use.

## SRS-Full

### Definition

The implementation claims complete coverage of applicable public SRS/SRIP normative requirements for a specified version and scope.

### Allowed public wording

- "Self-declared SRS-Full against [version] for [scope]."
- "Claims complete public SRS/SRIP coverage for [version] with evidence."

### Disallowed wording

- "Sigma Certified" unless officially certified.
- "Official Sigma Runtime implementation" unless approved and listed.
- "Certified SRS-Full" unless the certification registry lists that level.

### Evidence required

Complete version-pinned requirement matrix, supported SRIPs, unsupported SRIPs if excluded by scope, known deviations, test artifacts, implementation scope, and reproducible evidence references.

### Who may claim it

Any third party may make a truthful self-declaration with complete evidence. Official certification requires Sigma review.

### Sigma approval required?

No for self-declared wording. Yes for official certification, badge use, or registry listing.

## Sigma-Certified

### Definition

The implementation has completed an official Sigma certification review for a specified version, scope, and level.

### Allowed public wording

- "Sigma Certified for [level], [version], [scope]."
- "Listed in the official Sigma conformance registry."

### Disallowed wording

- Certification claims outside the listed version, scope, or level.
- Badge use outside the approved implementation.
- Enterprise certification claims without enterprise certification.

### Evidence required

Certification record, review scope, approved evidence artifacts, registry entry, and badge authorization where applicable.

### Who may claim it

Only implementations reviewed, approved, and listed by Sigma Stratum.

### Sigma approval required?

Yes.

## Sigma-Certified Enterprise

### Definition

The implementation has completed an official Sigma enterprise certification review covering enterprise deployment, support, governance, and operational requirements in addition to technical conformance.

### Allowed public wording

- "Sigma-Certified Enterprise for [version], [scope]."
- "Listed in the official Sigma conformance registry as Sigma-Certified Enterprise."

### Disallowed wording

- Enterprise certification claims without registry listing.
- Claims outside the certified deployment scope.
- Claims implying transferability to unrelated customers, deployments, or versions.

### Evidence required

Enterprise certification record, technical evidence, governance evidence, deployment scope, support or operational evidence, registry entry, and badge authorization where applicable.

### Who may claim it

Only implementations reviewed, approved, and listed by Sigma Stratum for enterprise certification.

### Sigma approval required?

Yes.
