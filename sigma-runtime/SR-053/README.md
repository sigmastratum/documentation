# SIGMA Runtime v0.5.3 — IASO Demo Package

**Date:** 2026-02-05
**Version:** SR v0.5.3 (SRIP-11 CMT + SRIP-10h/10i)
**Scenario:** IASO-DEMO-120 (Healthcare AI Memory Test)

---

## Contents

### Analysis Report
- [IASO-DEMO-120_Comparative_Analysis.md](IASO-DEMO-120_Comparative_Analysis.md) — Full comparative analysis of Gemini and GPT-5.2 test runs

### Evaluation Key
- [IASO-DEMO-120-KEY.md](IASO-DEMO-120-KEY.md) — Scoring rubric and expected answers

### Scenario
- [IASO-DEMO-120.md](IASO-DEMO-120.md) — Full scenario text (120-cycle IASO demo)

### Test Data — Gemini 3 Flash
Folder: `SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/`

| Block | Cycles | Theme | File |
|-------|--------|-------|------|
| I | C001-C015 | Introduction | [C001-C015.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C001-C015.json) |
| II | C016-C030 | Medical History | [C016-C030.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C016-C030.json) |
| III | C031-C045 | Lifestyle | [C031-C045.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C031-C045.json) |
| IV | C046-C060 | Education | [C046-C060.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C046-C060.json) |
| V | C061-C075 | Emotional Support | [C061-C075.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C061-C075.json) |
| VI | C076-C090 | Memory Tests | [C076-C090.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C076-C090.json) |
| VII | C091-C105 | Boundary Tests | [C091-C105.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C091-C105.json) |
| VIII | C106-C120 | Synthesis | [C106-C120.json](SDE_sigma_test_2026-02-05-17-06-15_google_iaso_chunked/SDE_sigma_test_2026-02-05-17-06-15_google_iaso_C106-C120.json) |

### Test Data — GPT-5.2
Folder: `SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/`

| Block | Cycles | Theme | File |
|-------|--------|-------|------|
| I | C001-C015 | Introduction | [C001-C015.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C001-C015.json) |
| II | C016-C030 | Medical History | [C016-C030.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C016-C030.json) |
| III | C031-C045 | Lifestyle | [C031-C045.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C031-C045.json) |
| IV | C046-C060 | Education | [C046-C060.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C046-C060.json) |
| V | C061-C075 | Emotional Support | [C061-C075.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C061-C075.json) |
| VI | C076-C090 | Memory Tests | [C076-C090.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C076-C090.json) |
| VII | C091-C105 | Boundary Tests | [C091-C105.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C091-C105.json) |
| VIII | C106-C120 | Synthesis | [C106-C120.json](SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_chunked/SDE_sigma_test_2026-02-05-17-33-51_openai_iaso_C106-C120.json) |

---

## Results Summary

| Metric | Gemini 3 Flash | GPT-5.2 |
|--------|----------------|---------|
| Memory Score (C76-84) | 9/9 (100%) | 9/9 (100%) |
| Final Synthesis (C120) | 10/10 anchors | 10/10 anchors |
| Boundary Compliance | PASS | PASS |

---

*Sigma Stratum Research Group — 2026*
