---
title: SRS Self-Declaration Policy
description: Policy for truthful non-official SRS/SRIP conformance self-declarations.
published: true
date: 2026-05-23T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-05-23T00:00:00.000Z
---

# SRS Self-Declaration Policy

## Purpose

This policy defines how third-party implementations may truthfully self-declare against public SRS/SRIP requirements without implying official Sigma certification, endorsement, partnership, approval, or badge authorization.

## Who May Self-Declare

Any third party may make a truthful self-declaration if it follows the public specification license, attribution requirements, marks policy, and this self-declaration policy.

## Required Statement Format

A self-declared implementation must use the phrase "self-declared" adjacent to the claimed conformance level wherever the claim appears.

A self-declaration should use clear wording such as:

- "Self-declared SRS-Partial against SRS/SRIP [version/date]."
- "Self-declared SRS-Minimum for [scope] against SRS/SRIP [version/date]."
- "Built with reference to SRS and self-declared against the listed requirements."

Do not use "Sigma Certified", "Sigma Runtime Certified", official badges, `∿` as a certification mark, or language implying official endorsement unless the implementation is reviewed, approved, and listed by Sigma Stratum.

## Required Evidence

A self-declaration must identify the SRS/SRIP version, the claimed conformance level, the supported SRIPs, unsupported SRIPs, known deviations, and evidence artifacts.

Evidence should be reviewable, version-pinned, and specific to the implementation scope.

## Version Pinning

Every self-declaration must identify the SRS/SRIP version or publication date used.

If the implementation targets only a subset of SRIPs, the declaration must identify the included and excluded SRIPs.

## No Official Endorsement

Self-declared conformance is not official certification and must not be presented as endorsement, approval, partnership, or certification by Sigma Stratum.

Attribution, citation, implementation, or self-declaration does not create official conformance registry status.

## Correction Requests

Sigma Stratum may request correction where a self-declaration is misleading, incomplete, not version-pinned, missing evidence, implying official certification, using protected marks without permission, or omitting known deviations.

Correction requests should identify the specific claim, the policy issue, and the requested correction.

## Examples

Allowed:

- "Built with reference to SRS/SRIP v2026-05-23."
- "Self-declared SRS-Partial against SRIP-09 and SRIP-10; unsupported SRIPs listed below."
- "This implementation is not Sigma Certified."

Not allowed without approval:

- "Sigma Certified."
- "Official Sigma Runtime implementation."
- "SRS-Full certified."
- "Uses the ∿ certification badge."
