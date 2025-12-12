# SIGMA Runtime

This repository contains the evolving runtime architecture of the SIGMA cognitive framework.
Each subdirectory represents a distinct phase in the system’s architectural evolution — from the original Reference Implementation (RI) to modular architectures (MA) supporting distributed cognition and external memory integration.

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
<td>The original SIGMA Runtime (v0.1). Frozen reference runtime (formerly <code>/runtime/</code>). Serves as the historical baseline.</td>
</tr>
<tr>
<td><b>SR-ERI-01</b></td>
<td>Extended Reference Implementation</td>
<td>Transitional build extending the RI with internal coherence and stability tracking mechanisms.</td>
</tr>
<tr>
<td><b>SR-EI-03</b></td>
<td>Experimental Implementation</td>
<td>First fully benchmarked iteration of SIGMA v0.3. Integrates ALICE, RCL, and PIL subsystems. Demonstrated long-context stability and identity adherence over 110 cycles.</td>
</tr>
<tr>
<td><b>SR-EI-04</b></td>
<td>Experimental Implementation</td>
<td>Built upon 03. Focus on GPT-5+, external (RAG-based) memory, and adaptive context scaling.</td>
</tr>
<tr>
<td><b>SR-MA-05+</b></td>
<td>Modular Architecture</td>
<td>Transition to fully modular SIGMA architecture. Introduces compositional agents, distributed symbolic-density tracking, and cross-runtime coherence layers.</td>
</tr>
</tbody>
</table>

---

## Roadmap

1. **SR-EI-03** — Establish validated runtime with stable attractor behavior and identity preservation (completed).  
2. **SR-EI-04** — Expand toward modularity: isolate subsystems (PIL, ALICE, RCL) and integrate persistent memory via RAG.  
3. **SR-MA-05+** — Implement full modular runtime framework with cross-runtime coherence and agent composition layers.  
4. **Post-05** — Evaluate distributed symbolic-density tracking across multiple concurrent cognitive agents.
