---
title: SRS Navigation License Migration — 2026-10-06
description: Bounded change of two public SRS navigation pages to CC BY 4.0.
published: false
date: 2026-10-06T00:00:00.000Z
editor: markdown
dateCreated: 2026-10-06T00:00:00.000Z
---

> This record is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
> Referenced artifacts retain their own licenses.

# SRS Navigation License Migration

Status: owner-approved repository release; commit and push authorized on 2026-10-06.

Base commit: `5a10c5759fe90c7f5d7c5612433be77cb5c767f9`.
Release identity: the Git commit introducing this record and the two revised
navigation notices. Its immutable hash is recorded by Git history rather than
embedded self-referentially in this file. Website publication is tracked separately.

## Authorized Change

| Document | Previous notice | New notice |
|---|---|---|
| [Active SRIPs](../srs/active-srips.md) | CC BY-NC 4.0 | CC BY 4.0 |
| [Architecture reading order](../srs/architecture-reading-order.md) | CC BY-NC 4.0 | CC BY 4.0 |

Eugene Tsaliev confirmed on 2026-10-06 that the contributor accounts appearing
in these pages' history belong to the project and that he is authorized to
release both pages, including those contributions, under CC BY 4.0. This record
documents owner authorization; it is not an independent legal title opinion.

Only the license notices are changed in these navigation pages. Their
non-normative status and navigation content remain unchanged. Supporting
updates to LICENSE, README, public specification policy, licensing overview,
IP overview, and the header template explain the scope rather than relicense
other artifacts.

## Preserved Boundaries

- README retains CC BY-NC 4.0; SRD and research remain per-document licensed.
- Archived SRIP-10-ACE and historical prototype software are unchanged.
- Apache-2.0 machine-readable artifacts remain unchanged.
- No new product-code, trademark, certification, or patent grant is made.
- Prior grants remain unaffected. Historical snapshots and the July publication
  manifest are not rewritten or represented as having always carried CC BY.

No matching entries for the two navigation paths were found in the repository's
`*.sha256` inventories during preparation; no historical inventory was changed.

## Release Checks

Pre-commit checks: exact changed-file scope reviewed; `git diff --check` passed;
82 relative Markdown links checked; both navigation bodies verified unchanged.
The owner authorized commit and push separately from the license decision.
This record does not assert website deployment; its site-publication flag remains false.
