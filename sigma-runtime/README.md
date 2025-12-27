# SIGMA Runtime

This repository contains the evolving runtime architecture of the SIGMA cognitive framework.  
Each subdirectory represents a distinct phase in the system’s architectural evolution — from the original Reference Implementation (RI) to the modular architectures (MA) supporting distributed cognition and external memory integration.

---

<h2>Structure</h2>

<table>
<thead>
<tr>
<th align="left" width="160">Folder</th>
<th align="left" width="220">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>SR-RI-01</b></td>
<td>Reference Implementation</td>
<td>Original SIGMA Runtime (v0.1). Frozen baseline defining the canonical runtime loop and attractor model.</td>
</tr>
<tr>
<td><b>SR-EI-03</b></td>
<td>Experimental Implementation</td>
<td>First fully benchmarked runtime (v0.3). Integrated ALICE, RCL, and PIL subsystems. Demonstrated long-context stability and identity adherence over 110 cycles.</td>
</tr>
<tr>
<td><b>SR-EI-037</b></td>
<td>Experimental Implementation</td>
<td>Final publicly released build under CC BY-NC 4.0.  
Validated recursive coherence and attractor persistence on GPT-5.2.  
Serves as the last open reference implementation.</td>
</tr>
<tr>
<td><b>SR-EI-04 +</b></td>
<td>Proprietary Reference Builds</td>
<td>Closed research versions introducing Adaptive Phase Regulation, SCR metrics, and AEGIDA-2 safety.  
Maintained internally by the Sigma Stratum Research Group.</td>
</tr>
<tr>
<td><b>SR-MA-05 +</b></td>
<td>Modular Architecture</td>
<td>Next-generation modular SIGMA runtime.  
Implements compositional agents, distributed symbolic-density tracking, and cross-runtime coherence layers.</td>
</tr>
</tbody>
</table>

---

## Roadmap

1. **SR-EI-03 – 037** — Validated runtime with stable attractor behavior and identity preservation (completed / public).  
2. **SR-EI-04 +** — Transition to adaptive-phase regulation and proprietary reference runtime (internal / closed).  
3. **SR-MA-05 +** — Develop modular runtime framework with cross-runtime coherence and agent composition layers.  
4. **Post-05** — Evaluate distributed symbolic-density tracking across multiple concurrent cognitive agents.
