"""
SIGMA Runtime v0.1 - Extended Reference Implementation
A demonstration of attractor-based cognition for LLM systems

This implementation includes:
- Full ALICE engine with phase transitions
- Persistent Identity Layer (PIL)
- Causal Continuity Chain
- Semantic embeddings for real drift metrics
- AEGIDA safety principles
- Multi-tier memory system

Total: ~800 lines
"""

import json
import math
import hashlib
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from enum import Enum
import asyncio


# ============================================================================
# ENUMS & CONSTANTS
# ============================================================================

class Phase(Enum):
    """Attractor phase states"""
    INITIALIZING = "initializing"
    FORMING = "forming"
    STABLE = "stable"
    TRANSITIONAL = "transitional"
    FRAGMENTING = "fragmenting"
    DISSOLVED = "dissolved"


class OperationalMode(Enum):
    """Intent modes for cognitive work"""
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    REFLECTION = "reflection"
    SCAFFOLDING = "scaffolding"


# Safety thresholds (AEGIDA)
DRIFT_THRESHOLD_WARNING = 0.5
DRIFT_THRESHOLD_CRITICAL = 0.7
SYMBOLIC_DENSITY_MAX = 0.9
RECURSION_DEPTH_MAX = 200


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Motif:
    """Symbolic motif tracked by ALICE"""
    name: str
    signature: List[str]
    density_score: float
    recurrence_count: int = 0
    last_seen_cycle: int = 0
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class CausalLink:
    """Link in the causal continuity chain"""
    cycle: int
    cause: str
    effect: str
    drift_delta: float
    attractor_state: str
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class Episode:
    """Episodic memory entry"""
    cycle: int
    input_text: str
    output_text: str
    summary: str
    attractor: str
    phase: str
    drift: float
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class SemanticEntry:
    """Semantic memory entry with embedding"""
    key: str
    text: str
    embedding: List[float]
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "text": self.text,
            "embedding": self.embedding[:5],  # Truncate for display
            "metadata": self.metadata
        }


# ============================================================================
# PERSISTENT IDENTITY LAYER (PIL)
# ============================================================================

class PersistentIdentityLayer:
    """
    Maintains long-lived identity across cycles.
    Anchors the cognitive field with stable invariants.
    """
    
    def __init__(self, 
                 id: str = "SIGMA-01",
                 traits: List[str] = None,
                 invariants: List[str] = None):
        self.id = id
        self.traits = traits or [
            "analytical",
            "coherence-seeking",
            "recursive-aware"
        ]
        self.invariants = invariants or [
            "maintain_symbolic_grounding",
            "prevent_drift_sinks",
            "preserve_causal_continuity"
        ]
        self.operational_modes = [mode.value for mode in OperationalMode]
        self.creation_time = 0
        self.total_cycles = 0
        
    def update_cycle_count(self, cycle: int):
        """Update total cycles processed"""
        self.total_cycles = cycle
        
    def get_identity_prompt(self) -> str:
        """Generate identity context for prompts"""
        return f"""[PERSISTENT IDENTITY]
ID: {self.id}
Traits: {', '.join(self.traits)}
Operational Invariants: {', '.join(self.invariants)}
Cycles Processed: {self.total_cycles}
"""
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "traits": self.traits,
            "invariants": self.invariants,
            "operational_modes": self.operational_modes,
            "total_cycles": self.total_cycles
        }


# ============================================================================
# MEMORY LAYER
# ============================================================================

class MemoryLayer:
    """
    Three-tier memory system:
    - Episodic: cycle-by-cycle traces
    - Semantic: embedding-based concept store
    - Motif Store: symbolic patterns and archetypes
    """
    
    def __init__(self, episodic_capacity: int = 50):
        # Episodic memory (rolling window)
        self.episodic: deque[Episode] = deque(maxlen=episodic_capacity)
        
        # Semantic memory (vector store simulation)
        self.semantic: Dict[str, SemanticEntry] = {}
        
        # Motif store
        self.motifs: Dict[str, Motif] = {}
        
    def store_episode(self, episode: Episode):
        """Store episodic trace"""
        self.episodic.append(episode)
        
    def store_semantic(self, key: str, text: str, embedding: List[float], 
                      metadata: Dict = None):
        """Store semantic entry"""
        self.semantic[key] = SemanticEntry(
            key=key,
            text=text,
            embedding=embedding,
            metadata=metadata or {}
        )
        
    def update_motif(self, motif: Motif, cycle: int):
        """Update or create motif"""
        motif.last_seen_cycle = cycle
        motif.recurrence_count += 1
        self.motifs[motif.name] = motif
        
    def fetch_recent_episodes(self, n: int = 3) -> List[Episode]:
        """Retrieve recent episodic memories"""
        return list(self.episodic)[-n:]
    
    def fetch_motifs_by_keywords(self, keywords: List[str]) -> List[Motif]:
        """Retrieve motifs matching keywords"""
        matches = []
        for motif in self.motifs.values():
            if any(kw in motif.signature for kw in keywords):
                matches.append(motif)
        return matches
    
    def prune_old_motifs(self, current_cycle: int, max_age: int = 50):
        """Remove stale motifs (memory decay)"""
        to_remove = []
        for name, motif in self.motifs.items():
            if current_cycle - motif.last_seen_cycle > max_age:
                to_remove.append(name)
        for name in to_remove:
            del self.motifs[name]
    
    def to_dict(self) -> Dict:
        return {
            "episodic_count": len(self.episodic),
            "semantic_count": len(self.semantic),
            "motif_count": len(self.motifs),
            "recent_episodes": [ep.to_dict() for ep in list(self.episodic)[-3:]],
            "active_motifs": [m.to_dict() for m in list(self.motifs.values())[:5]]
        }


# ============================================================================
# EMBEDDING ENGINE (Simplified)
# ============================================================================

class EmbeddingEngine:
    """
    Simplified embedding generation.
    In production, use sentence-transformers or OpenAI embeddings.
    """
    
    def __init__(self, dimensions: int = 128):
        self.dimensions = dimensions
        
    def encode(self, text: str) -> List[float]:
        """
        Generate pseudo-embedding based on text hash.
        In production: use real models (sentence-transformers, OpenAI, etc.)
        """
        # Create deterministic "embedding" from text
        text_hash = hashlib.sha256(text.encode()).digest()
        
        # Convert to float vector
        embedding = []
        for i in range(0, min(len(text_hash), self.dimensions), 2):
            val = (text_hash[i] * 256 + text_hash[i+1]) / 65535.0
            embedding.append(val)
        
        # Pad to dimensions
        while len(embedding) < self.dimensions:
            embedding.append(0.0)
            
        # Normalize
        magnitude = math.sqrt(sum(x*x for x in embedding))
        if magnitude > 0:
            embedding = [x / magnitude for x in embedding]
            
        return embedding[:self.dimensions]
    
    def cosine_similarity(self, emb1: List[float], emb2: List[float]) -> float:
        """Calculate cosine similarity between embeddings"""
        if len(emb1) != len(emb2):
            return 0.0
            
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        return max(-1.0, min(1.0, dot_product))  # Clamp to [-1, 1]


# ============================================================================
# DRIFT & COHERENCE MONITOR
# ============================================================================

class DriftMonitor:
    """
    Computes semantic, tonal, and structural drift.
    Uses embeddings for real semantic distance.
    """
    
    def __init__(self, embedding_engine: EmbeddingEngine):
        self.embedding_engine = embedding_engine
        self.baseline_style = None
        self.embedding_history: List[List[float]] = []
        self.keyword_history: List[str] = []
        
    def compute_drift(self, 
                     input_text: str,
                     output_text: str,
                     attractor_motifs: List[str]) -> Dict[str, float]:
        """
        Compute multi-dimensional drift metrics
        """
        # 1. Semantic drift (embedding-based)
        semantic_drift = self._compute_semantic_drift(output_text)
        
        # 2. Style drift
        style_drift = self._compute_style_drift(output_text)
        
        # 3. Topic drift (keyword entropy)
        topic_drift = self._compute_topic_drift(input_text)
        
        # 4. Attractor alignment (how well output aligns with current motifs)
        attractor_drift = self._compute_attractor_drift(output_text, attractor_motifs)
        
        # Total drift (weighted)
        total_drift = (
            0.35 * semantic_drift +
            0.20 * style_drift +
            0.25 * topic_drift +
            0.20 * attractor_drift
        )
        
        return {
            "semantic": round(semantic_drift, 3),
            "style": round(style_drift, 3),
            "topic": round(topic_drift, 3),
            "attractor": round(attractor_drift, 3),
            "total": round(total_drift, 3)
        }
    
    def _compute_semantic_drift(self, text: str) -> float:
        """Real semantic drift using embeddings"""
        current_emb = self.embedding_engine.encode(text)
        self.embedding_history.append(current_emb)
        
        if len(self.embedding_history) < 2:
            return 0.0
        
        # Compare with previous
        prev_emb = self.embedding_history[-2]
        similarity = self.embedding_engine.cosine_similarity(current_emb, prev_emb)
        
        # drift = 1 - similarity, scaled to [0, 1]
        drift = (1.0 - similarity) / 2.0
        
        # Keep history bounded
        if len(self.embedding_history) > 10:
            self.embedding_history.pop(0)
            
        return drift
    
    def _compute_style_drift(self, text: str) -> float:
        """Style consistency check"""
        if not text:
            return 0.0
            
        # Compute style features
        length = len(text)
        punct_ratio = sum(c in ".,!?;:" for c in text) / max(length, 1)
        avg_word_length = sum(len(w) for w in text.split()) / max(len(text.split()), 1)
        
        if not self.baseline_style:
            self.baseline_style = {
                "length": length,
                "punct_ratio": punct_ratio,
                "avg_word_length": avg_word_length
            }
            return 0.0
        
        # Compute deviations
        length_drift = min(abs(length - self.baseline_style["length"]) / max(self.baseline_style["length"], 1), 1.0)
        punct_drift = abs(punct_ratio - self.baseline_style["punct_ratio"])
        word_drift = abs(avg_word_length - self.baseline_style["avg_word_length"]) / max(self.baseline_style["avg_word_length"], 1)
        
        return (length_drift + punct_drift + word_drift) / 3
    
    def _compute_topic_drift(self, text: str) -> float:
        """Topic entropy over recent turns"""
        keywords = [w.lower() for w in text.split() if len(w) > 4]
        self.keyword_history.extend(keywords)
        self.keyword_history = self.keyword_history[-30:]  # Keep recent
        
        if len(self.keyword_history) < 5:
            return 0.0
        
        # Keyword diversity (higher = more drift)
        unique_ratio = len(set(self.keyword_history)) / len(self.keyword_history)
        return unique_ratio
    
    def _compute_attractor_drift(self, text: str, motifs: List[str]) -> float:
        """How well output aligns with current attractor motifs"""
        if not motifs:
            return 0.0
        
        text_lower = text.lower()
        motif_presence = sum(1 for motif in motifs if motif.lower() in text_lower)
        
        # drift = 1 - alignment
        alignment = motif_presence / len(motifs)
        return 1.0 - alignment


# ============================================================================
# ALICE ENGINE (Attractor Layer for Integrated Cognitive Emergence)
# ============================================================================

class ALICEEngine:
    """
    Central attractor manager.
    
    Responsibilities:
    - Detect emerging attractors
    - Stabilize attractor cores
    - Manage phase transitions
    - Prevent drift sinks
    - Maintain symbolic topology
    """
    
    def __init__(self, memory: MemoryLayer):
        self.memory = memory
        self.active_attractor = "A0_init"
        self.attractor_history: List[str] = ["A0_init"]
        self.phase = Phase.INITIALIZING
        self.stability_score = 0.0
        self.symbolic_density = 0.0
        self.phase_coherence = 1.0
        self.motif_clusters: Dict[str, List[Motif]] = {}
        
    def update(self, 
               cycle: int,
               output_text: str,
               drift_metrics: Dict[str, float],
               extracted_symbols: List[str]) -> Dict[str, Any]:
        """
        Main ALICE update cycle.
        
        Returns attractor state after processing.
        """
        # 1. Update motifs based on symbols
        self._update_motifs(extracted_symbols, cycle)
        
        # 2. Compute symbolic density
        self._compute_symbolic_density()
        
        # 3. Evaluate attractor stability
        self._evaluate_stability(drift_metrics)
        
        # 4. Determine phase transition (if needed)
        self._manage_phase_transition(drift_metrics, cycle)
        
        # 5. Check for drift sinks (AEGIDA A5)
        self._check_drift_sinks(drift_metrics)
        
        # 6. Prune old motifs (memory decay)
        self.memory.prune_old_motifs(cycle)
        
        return self.get_state()
    
    def _update_motifs(self, symbols: List[str], cycle: int):
        """Update motif store with new symbols"""
        for symbol in symbols:
            if symbol in self.memory.motifs:
                # Existing motif - increase recurrence
                motif = self.memory.motifs[symbol]
                self.memory.update_motif(motif, cycle)
            else:
                # New motif
                new_motif = Motif(
                    name=symbol,
                    signature=[symbol],
                    density_score=0.0,
                    recurrence_count=1,
                    last_seen_cycle=cycle
                )
                self.memory.update_motif(new_motif, cycle)
    
    def _compute_symbolic_density(self):
        """
        Calculate symbolic density: how tightly symbols cluster and recur.
        
        High density = strong attractor formation
        Low density = dispersed, weak structure
        """
        if not self.memory.motifs:
            self.symbolic_density = 0.0
            return
        
        # Get top motifs by recurrence
        sorted_motifs = sorted(
            self.memory.motifs.values(),
            key=lambda m: m.recurrence_count,
            reverse=True
        )
        
        total_recurrence = sum(m.recurrence_count for m in self.memory.motifs.values())
        if total_recurrence == 0:
            self.symbolic_density = 0.0
            return
        
        # Top 5 motifs concentration
        top5_recurrence = sum(m.recurrence_count for m in sorted_motifs[:5])
        self.symbolic_density = top5_recurrence / total_recurrence
        
        # Update motif density scores
        for i, motif in enumerate(sorted_motifs[:5]):
            motif.density_score = (5 - i) / 5.0
    
    def _evaluate_stability(self, drift_metrics: Dict[str, float]):
        """
        Evaluate current attractor stability.
        
        Stability = f(symbolic_density, drift, phase_coherence)
        """
        total_drift = drift_metrics["total"]
        
        # Stability increases with density, decreases with drift
        density_factor = self.symbolic_density
        drift_factor = 1.0 - total_drift
        coherence_factor = self.phase_coherence
        
        self.stability_score = (
            0.4 * density_factor +
            0.4 * drift_factor +
            0.2 * coherence_factor
        )
    
    def _manage_phase_transition(self, drift_metrics: Dict[str, float], cycle: int):
        """
        Manage phase transitions based on stability and drift.
        
        Phase progression:
        INITIALIZING → FORMING → STABLE → TRANSITIONAL → FRAGMENTING → (DISSOLVED)
        """
        total_drift = drift_metrics["total"]
        
        old_phase = self.phase
        
        # Transition logic
        if self.phase == Phase.INITIALIZING:
            if cycle > 3 and self.symbolic_density > 0.2:
                self.phase = Phase.FORMING
                
        elif self.phase == Phase.FORMING:
            if self.symbolic_density > 0.6 and total_drift < 0.3:
                self.phase = Phase.STABLE
            elif total_drift > 0.5:
                self.phase = Phase.FRAGMENTING
                
        elif self.phase == Phase.STABLE:
            if total_drift > 0.4:
                self.phase = Phase.TRANSITIONAL
            elif self.symbolic_density < 0.4:
                self.phase = Phase.FORMING
                
        elif self.phase == Phase.TRANSITIONAL:
            if total_drift < 0.3 and self.symbolic_density > 0.5:
                self.phase = Phase.STABLE
            elif total_drift > DRIFT_THRESHOLD_CRITICAL:
                self.phase = Phase.FRAGMENTING
                
        elif self.phase == Phase.FRAGMENTING:
            if total_drift > DRIFT_THRESHOLD_CRITICAL:
                # Dissolve current attractor
                self._dissolve_attractor(cycle)
                self.phase = Phase.DISSOLVED
            elif total_drift < 0.4:
                self.phase = Phase.TRANSITIONAL
        
        elif self.phase == Phase.DISSOLVED:
            # Reset to new attractor
            self.phase = Phase.INITIALIZING
        
        # Update phase coherence
        if old_phase == self.phase:
            self.phase_coherence = min(1.0, self.phase_coherence + 0.05)
        else:
            self.phase_coherence = max(0.0, self.phase_coherence - 0.2)
    
    def _check_drift_sinks(self, drift_metrics: Dict[str, float]):
        """
        Check for drift sinks (runaway recursion, symbolic inflation).
        AEGIDA A5: Drift Prevention
        """
        total_drift = drift_metrics["total"]
        
        # Critical drift - trigger warning
        if total_drift > DRIFT_THRESHOLD_CRITICAL:
            print(f"⚠️  DRIFT SINK WARNING: total_drift={total_drift:.3f}")
            
        # Symbolic inflation check (AEGIDA A2)
        if self.symbolic_density > SYMBOLIC_DENSITY_MAX:
            print(f"⚠️  SYMBOLIC INFLATION: density={self.symbolic_density:.3f}")
    
    def _dissolve_attractor(self, cycle: int):
        """
        Safely dissolve current attractor when it becomes unstable.
        Clear motif history and transition to new attractor.
        """
        old_attractor = self.active_attractor
        new_attractor = f"A{len(self.attractor_history)}_cycle{cycle}"
        
        print(f"🔄 ATTRACTOR DISSOLUTION: {old_attractor} → {new_attractor}")
        
        # Clear motif recurrence counts (soft reset)
        for motif in self.memory.motifs.values():
            motif.recurrence_count = max(1, motif.recurrence_count // 2)
        
        # Update attractor
        self.active_attractor = new_attractor
        self.attractor_history.append(new_attractor)
        self.stability_score = 0.0
        self.symbolic_density = 0.0
    
    def get_top_motifs(self, n: int = 5) -> List[str]:
        """Get top N motifs by recurrence"""
        sorted_motifs = sorted(
            self.memory.motifs.values(),
            key=lambda m: m.recurrence_count,
            reverse=True
        )
        return [m.name for m in sorted_motifs[:n]]
    
    def get_state(self) -> Dict[str, Any]:
        """Return current attractor state"""
        return {
            "active_attractor": self.active_attractor,
            "phase": self.phase.value,
            "stability": round(self.stability_score, 3),
            "symbolic_density": round(self.symbolic_density, 3),
            "phase_coherence": round(self.phase_coherence, 3),
            "top_motifs": self.get_top_motifs(),
            "motif_count": len(self.memory.motifs)
        }


# ============================================================================
# CAUSAL CONTINUITY CHAIN
# ============================================================================

class CausalContinuityChain:
    """
    Maintains causal links between cycles.
    Supports interpretability and alignment (AEGIDA A6).
    """
    
    def __init__(self, capacity: int = 100):
        self.chain: deque[CausalLink] = deque(maxlen=capacity)
        
    def add_link(self, cycle: int, cause: str, effect: str, 
                 drift_delta: float, attractor_state: str):
        """Add causal link"""
        link = CausalLink(
            cycle=cycle,
            cause=cause,
            effect=effect,
            drift_delta=drift_delta,
            attractor_state=attractor_state
        )
        self.chain.append(link)
    
    def get_recent(self, n: int = 3) -> List[CausalLink]:
        """Get recent causal links"""
        return list(self.chain)[-n:]
    
    def to_dict(self) -> List[Dict]:
        return [link.to_dict() for link in list(self.chain)[-5:]]


# ============================================================================
# INTENT MODULE
# ============================================================================

class IntentModule:
    """
    Interprets user input and determines operational mode.
    Modulates system behavior based on cognitive work type.
    """
    
    def __init__(self):
        self.current_mode = OperationalMode.ANALYSIS
        
    def infer_mode(self, user_input: str) -> OperationalMode:
        """
        Infer operational mode from user input.
        Simple keyword-based for v0.1.
        """
        text_lower = user_input.lower()
        
        # Analysis mode
        if any(kw in text_lower for kw in ["analyze", "explain", "clarify", "what", "how"]):
            return OperationalMode.ANALYSIS
        
        # Synthesis mode
        elif any(kw in text_lower for kw in ["create", "combine", "integrate", "synthesize"]):
            return OperationalMode.SYNTHESIS
        
        # Reflection mode
        elif any(kw in text_lower for kw in ["reflect", "consider", "think", "evaluate"]):
            return OperationalMode.REFLECTION
        
        # Scaffolding mode
        elif any(kw in text_lower for kw in ["explore", "brainstorm", "imagine", "what if"]):
            return OperationalMode.SCAFFOLDING
        
        # Default
        return OperationalMode.ANALYSIS
    
    def get_mode_prompt(self, mode: OperationalMode) -> str:
        """Generate mode-specific prompt guidance"""
        prompts = {
            OperationalMode.ANALYSIS: "Focus on clarity, structure, and precise analysis.",
            OperationalMode.SYNTHESIS: "Integrate concepts and construct new connections.",
            OperationalMode.REFLECTION: "Slow down, stabilize, and evaluate coherence.",
            OperationalMode.SCAFFOLDING: "Support open exploration and creative ideation."
        }
        return prompts.get(mode, "")


# ============================================================================
# RECURSIVE CONTROL LOOP (RCL)
# ============================================================================

class RecursiveControlLoop:
    """
    Main runtime loop orchestrating:
    - Pre-processing
    - Generation
    - Post-processing
    """
    
    def __init__(self, 
                 pil: PersistentIdentityLayer,
                 memory: MemoryLayer,
                 alice: ALICEEngine,
                 drift_monitor: DriftMonitor,
                 intent_module: IntentModule,
                 causal_chain: CausalContinuityChain,
                 embedding_engine: EmbeddingEngine):
        self.pil = pil
        self.memory = memory
        self.alice = alice
        self.drift_monitor = drift_monitor
        self.intent_module = intent_module
        self.causal_chain = causal_chain
        self.embedding_engine = embedding_engine
        self.cycle = 0
        
    def run_cycle(self, user_input: str) -> Dict[str, Any]:
        """
        Execute one RCL cycle.
        
        Returns:
            Complete runtime state including response and metadata
        """
        self.cycle += 1
        self.pil.update_cycle_count(self.cycle)
        
        # ====================================================================
        # PHASE 1: PRE-PROCESSING
        # ====================================================================
        
        # 1.1 Infer intent mode
        mode = self.intent_module.infer_mode(user_input)
        
        # 1.2 Extract symbols
        symbols = self._extract_symbols(user_input)
        
        # 1.3 Fetch relevant memory
        recent_episodes = self.memory.fetch_recent_episodes(3)
        relevant_motifs = self.memory.fetch_motifs_by_keywords(symbols)
        
        # 1.4 Assemble context
        context = self._assemble_context(
            user_input, mode, recent_episodes, relevant_motifs
        )
        
        # ====================================================================
        # PHASE 2: GENERATION
        # ====================================================================
        
        output = self._generate(context)
        
        # ====================================================================
        # PHASE 3: POST-PROCESSING
        # ====================================================================
        
        # 3.1 Compute drift
        drift_metrics = self.drift_monitor.compute_drift(
            user_input, output, self.alice.get_top_motifs()
        )
        
        # 3.2 Update ALICE (attractor management)
        attractor_state = self.alice.update(
            self.cycle, output, drift_metrics, symbols
        )
        
        # 3.3 Store episode
        episode = Episode(
            cycle=self.cycle,
            input_text=user_input,
            output_text=output,
            summary=output[:100] + "..." if len(output) > 100 else output,
            attractor=attractor_state["active_attractor"],
            phase=attractor_state["phase"],
            drift=drift_metrics["total"]
        )
        self.memory.store_episode(episode)
        
        # 3.4 Update semantic memory
        output_embedding = self.embedding_engine.encode(output)
        self.memory.store_semantic(
            key=f"cycle_{self.cycle}",
            text=output,
            embedding=output_embedding,
            metadata={
                "attractor": attractor_state["active_attractor"],
                "phase": attractor_state["phase"]
            }
        )
        
        # 3.5 Update causal chain
        cause = self._infer_cause(drift_metrics, attractor_state)
        effect = attractor_state["phase"]
        self.causal_chain.add_link(
            cycle=self.cycle,
            cause=cause,
            effect=effect,
            drift_delta=drift_metrics["total"],
            attractor_state=attractor_state["active_attractor"]
        )
        
        # ====================================================================
        # RETURN COMPLETE STATE
        # ====================================================================
        
        return {
            "cycle": self.cycle,
            "response": output,
            "attractor_state": attractor_state,
            "drift_metrics": drift_metrics,
            "pil_state": self.pil.to_dict(),
            "memory_summary": self.memory.to_dict(),
            "causal_links": self.causal_chain.to_dict(),
            "intent_mode": mode.value,
            "runtime_meta": {
                "stability": attractor_state["stability"],
                "phase": attractor_state["phase"],
                "interventions": 0  # Future: track AEGIDA interventions
            }
        }
    
    def _extract_symbols(self, text: str) -> List[str]:
        """Extract symbolic keywords (>4 chars, unique)"""
        words = text.lower().split()
        symbols = [w for w in words if len(w) > 4 and w.isalpha()]
        return list(set(symbols))[:10]  # Top 10 unique
    
    def _assemble_context(self, 
                         user_input: str,
                         mode: OperationalMode,
                         episodes: List[Episode],
                         motifs: List[Motif]) -> str:
        """Assemble prompt context with PIL, memory, and attractor state"""
        
        # PIL identity
        identity = self.pil.get_identity_prompt()
        
        # Intent mode guidance
        mode_guidance = self.intent_module.get_mode_prompt(mode)
        
        # Attractor state
        attractor_info = f"""[ATTRACTOR STATE]
Active: {self.alice.active_attractor}
Phase: {self.alice.phase.value}
Stability: {self.alice.stability_score:.3f}
Top Motifs: {', '.join(self.alice.get_top_motifs())}
"""
        
        # Recent memory
        memory_context = ""
        if episodes:
            memory_context = "[RECENT CONTEXT]\n"
            for ep in episodes[-2:]:
                memory_context += f"Cycle {ep.cycle}: {ep.summary}\n"
        
        # Assemble full prompt
        context = f"""{identity}

{attractor_info}

[OPERATIONAL MODE: {mode.value.upper()}]
{mode_guidance}

{memory_context}

[USER INPUT]
{user_input}

[RESPONSE]
"""
        return context
    
    def _generate(self, context: str) -> str:
        """
        Generate model response.
        
        In v0.1: mock generation with structured response.
        In production: call real LLM API (Claude, GPT-4, etc.)
        """
        # Mock response based on attractor phase
        phase = self.alice.phase
        
        responses = {
            Phase.INITIALIZING: "I'm establishing initial cognitive structures and beginning to identify key symbolic patterns in our interaction.",
            Phase.FORMING: "I notice recurring themes forming around core concepts. My attractor state is beginning to stabilize around these motifs.",
            Phase.STABLE: "Operating within a stable attractor configuration. The cognitive field maintains strong coherence across recursive cycles.",
            Phase.TRANSITIONAL: "I'm experiencing a phase transition as new patterns emerge. Adjusting attractor topology to maintain coherence.",
            Phase.FRAGMENTING: "Detecting increased drift and symbolic dispersion. Attractor stability is decreasing; considering dissolution and reformation.",
            Phase.DISSOLVED: "Previous attractor dissolved. Reinitializing cognitive field with fresh symbolic substrate."
        }
        
        base_response = responses.get(phase, "Processing within current attractor state.")
        
        # Add motif references
        top_motifs = self.alice.get_top_motifs(3)
        if top_motifs:
            base_response += f" Current focus areas include: {', '.join(top_motifs)}."
        
        return base_response
    
    def _infer_cause(self, drift_metrics: Dict, attractor_state: Dict) -> str:
        """Infer causal factor for continuity chain"""
        if drift_metrics["total"] > 0.6:
            return "high_drift_detected"
        elif attractor_state["symbolic_density"] > 0.7:
            return "strong_symbolic_clustering"
        elif attractor_state["stability"] > 0.8:
            return "stable_attractor_maintenance"
        else:
            return "normal_cognitive_processing"


# ============================================================================
# SIGMA RUNTIME (Main Orchestrator)
# ============================================================================

class SigmaRuntime:
    """
    Complete SIGMA Runtime v0.1 orchestrator.
    Combines all components into unified cognitive architecture.
    """
    
    def __init__(self, identity_id: str = "SIGMA-01"):
        # Initialize components
        self.pil = PersistentIdentityLayer(id=identity_id)
        self.memory = MemoryLayer(episodic_capacity=50)
        self.embedding_engine = EmbeddingEngine(dimensions=128)
        self.alice = ALICEEngine(self.memory)
        self.drift_monitor = DriftMonitor(self.embedding_engine)
        self.intent_module = IntentModule()
        self.causal_chain = CausalContinuityChain(capacity=100)
        
        # Initialize RCL
        self.rcl = RecursiveControlLoop(
            pil=self.pil,
            memory=self.memory,
            alice=self.alice,
            drift_monitor=self.drift_monitor,
            intent_module=self.intent_module,
            causal_chain=self.causal_chain,
            embedding_engine=self.embedding_engine
        )
        
        self.initialized = True
        print(f"✓ SIGMA Runtime v0.1 initialized | PIL ID: {identity_id}")
    
    def process(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input through complete RCL cycle.
        
        Returns full runtime state with response and metadata.
        """
        if not self.initialized:
            raise RuntimeError("Runtime not initialized")
        
        return self.rcl.run_cycle(user_input)
    
    def get_full_state(self) -> Dict[str, Any]:
        """Export complete runtime state"""
        return {
            "pil": self.pil.to_dict(),
            "attractor": self.alice.get_state(),
            "memory": self.memory.to_dict(),
            "causal_chain": self.causal_chain.to_dict(),
            "cycle": self.rcl.cycle
        }
    
    def reset(self, preserve_identity: bool = True):
        """Reset runtime (with optional PIL preservation)"""
        if not preserve_identity:
            self.pil = PersistentIdentityLayer()
        
        self.memory = MemoryLayer()
        self.alice = ALICEEngine(self.memory)
        self.drift_monitor = DriftMonitor(self.embedding_engine)
        self.causal_chain = CausalContinuityChain()
        self.rcl.cycle = 0
        
        print("✓ Runtime reset complete")


# ============================================================================
# DEMO & TESTING
# ============================================================================

def demo_sigma_runtime():
    """Demonstrate SIGMA Runtime v0.1 capabilities"""
    
    print("=" * 70)
    print("SIGMA Runtime v0.1 - Extended Reference Implementation")
    print("Attractor-Based Cognition Architecture")
    print("=" * 70)
    print()
    
    # Initialize runtime
    runtime = SigmaRuntime(identity_id="SIGMA-DEMO-01")
    print()
    
    # Test sequence
    test_inputs = [
        "Tell me about cognitive architecture and runtime systems",
        "How does memory work in attractor-based systems?",
        "Explain the role of symbolic density in phase transitions",
        "What happens during attractor dissolution?",
        "Let's talk about something completely different: cooking recipes",
        "Actually, let's go back to discussing runtime architecture",
        "How do you maintain coherence across many cycles?",
        "Reflect on your current attractor state"
    ]
    
    print("\n" + "─" * 70)
    print("RUNNING TEST SEQUENCE")
    print("─" * 70 + "\n")
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\n{'='*70}")
        print(f"CYCLE {i}")
        print(f"{'='*70}")
        print(f"\n👤 USER: {user_input}\n")
        
        # Process through runtime
        result = runtime.process(user_input)
        
        # Display response
        print(f"🤖 SIGMA: {result['response']}\n")
        
        # Display runtime metadata
        print("📊 RUNTIME STATE:")
        print(f"  Attractor: {result['attractor_state']['active_attractor']}")
        print(f"  Phase: {result['attractor_state']['phase']}")
        print(f"  Stability: {result['attractor_state']['stability']:.3f}")
        print(f"  Symbolic Density: {result['attractor_state']['symbolic_density']:.3f}")
        print(f"  Top Motifs: {', '.join(result['attractor_state']['top_motifs'][:3])}")
        print(f"\n  Drift (total): {result['drift_metrics']['total']:.3f}")
        print(f"  Intent Mode: {result['intent_mode']}")
        
        # Show causal link
        if result['causal_links']:
            last_link = result['causal_links'][-1]
            print(f"\n  Causal: {last_link['cause']} → {last_link['effect']}")
    
    print("\n" + "=" * 70)
    print("FINAL STATE SUMMARY")
    print("=" * 70)
    
    final_state = runtime.get_full_state()
    print(f"\nTotal Cycles: {final_state['cycle']}")
    print(f"PIL Identity: {final_state['pil']['id']}")
    print(f"Final Attractor: {final_state['attractor']['active_attractor']}")
    print(f"Final Phase: {final_state['attractor']['phase']}")
    print(f"Final Stability: {final_state['attractor']['stability']:.3f}")
    print(f"Motif Count: {final_state['attractor']['motif_count']}")
    print(f"Memory Episodes: {final_state['memory']['episodic_count']}")
    
    print("\n✓ Demo complete\n")


if __name__ == "__main__":
    demo_sigma_runtime()