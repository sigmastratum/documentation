"""
SIGMA Runtime v0.3.5 
================================================================
"""

import json
import math
import hashlib
import time
import datetime
import os
import re
import tiktoken
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from enum import Enum
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine


# ============================================================================
# EMBEDDING ENGINE
# ============================================================================

class RealEmbeddingEngine:
    """Sentence-transformers embedding (all-MiniLM-L6-v2)"""
    
    def __init__(self):
        print("📊 Loading embedding model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✓ Embedding model ready")
    
    def encode(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
    
    def cosine_similarity(self, a: List[float], b: List[float]) -> float:
        return 1 - cosine(a, b)


# ============================================================================
# ENUMS & CONSTANTS
# ============================================================================

class Phase(Enum):
    INITIALIZING = "initializing"
    FORMING = "forming"
    STABLE = "stable"
    REFLECTION = "reflection"
    FRAGMENTING = "fragmenting"


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Motif:
    """Neurosymbolic motif with cycle tracking"""
    name: str
    keywords: List[str]
    frequency: int = 1
    first_seen: int = 0
    last_seen: int = 0
    cycle_appearances: set = None
    activation: float = 0.2
    embedding: Optional[Any] = None
    
    def __post_init__(self):
        if self.cycle_appearances is None:
            self.cycle_appearances = {self.first_seen}
    
    def activate(self, weight: float = 1.0):
        decay_factor = 0.98
        self.activation = (self.activation * decay_factor) + (0.1 * weight)
        self.activation = max(0.0, min(1.0, self.activation))
        self.frequency += 1
    
    def decay_activation(self):
        self.activation *= 0.98
        if self.activation < 0.01:
            self.activation = 0.0
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "keywords": self.keywords,
            "frequency": self.frequency,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "cycle_count": len(self.cycle_appearances) if self.cycle_appearances else 0,
            "activation": round(self.activation, 3)
        }


@dataclass
class CausalLink:
    cycle: int
    user_input: str
    response: str
    drift: float
    phase: str
    semantic_similarity: float = 0.0
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass  
class MemoryEpisode:
    cycle: int
    input_text: str
    response: str
    summary: str
    phase: str
    motifs: List[str]
    
    def to_dict(self) -> Dict:
        return asdict(self)


# ============================================================================
# COHERENCE TRACKER
# ============================================================================

class CoherenceTracker:
    """Track semantic continuity and coherence"""
    
    def __init__(self, embedding_engine):
        self.embedding_engine = embedding_engine
        self.cycle_embeddings: List[List[float]] = []
        self.cycle_texts: List[str] = []
        self.topic_keywords: Dict[int, List[str]] = {}
        self.coherence_scores: List[float] = []
        self.memory_tests: List[Dict] = []
        
    def track_cycle(self, cycle: int, response: str, keywords: List[str]) -> Dict[str, float]:
        emb = self.embedding_engine.encode(response)
        self.cycle_embeddings.append(emb)
        self.cycle_texts.append(response)
        self.topic_keywords[cycle] = keywords
        
        semantic_continuity = self._compute_semantic_continuity()
        topic_coherence = self._compute_topic_coherence(cycle)
        
        overall = 0.6 * semantic_continuity + 0.4 * topic_coherence
        self.coherence_scores.append(overall)
        
        return {
            "semantic_continuity": round(semantic_continuity, 3),
            "topic_coherence": round(topic_coherence, 3),
            "overall_coherence": round(overall, 3)
        }
    
    def _compute_semantic_continuity(self) -> float:
        if len(self.cycle_embeddings) < 2:
            return 1.0
        
        current = self.cycle_embeddings[-1]
        recent = self.cycle_embeddings[-6:-1]
        
        if not recent:
            return 1.0
        
        similarities = [
            self.embedding_engine.cosine_similarity(current, prev)
            for prev in recent
        ]
        
        avg_sim = sum(similarities) / len(similarities)
        return (avg_sim + 1) / 2
    
    def _compute_topic_coherence(self, cycle: int) -> float:
        if cycle < 2:
            return 1.0
        
        current_kw = set(self.topic_keywords.get(cycle, []))
        if not current_kw:
            return 0.5
        
        recent = range(max(1, cycle - 5), cycle)
        overlaps = []
        
        for prev_cycle in recent:
            prev_kw = set(self.topic_keywords.get(prev_cycle, []))
            if prev_kw:
                jaccard = len(current_kw & prev_kw) / len(current_kw | prev_kw)
                overlaps.append(jaccard)
        
        return sum(overlaps) / len(overlaps) if overlaps else 0.5
    
    def get_coherence_summary(self) -> Dict:
        if not self.coherence_scores:
            return {
                "avg_coherence": 0.0,
                "min_coherence": 0.0,
                "max_coherence": 0.0,
                "coherence_trend": "no_data",
                "memory_tests": 0,
                "successful_recalls": 0
            }
        
        if len(self.coherence_scores) < 5:
            trend = "insufficient_data"
        else:
            first_half = sum(self.coherence_scores[:len(self.coherence_scores)//2]) / (len(self.coherence_scores)//2)
            second_half = sum(self.coherence_scores[len(self.coherence_scores)//2:]) / (len(self.coherence_scores) - len(self.coherence_scores)//2)
            
            if second_half > first_half + 0.05:
                trend = "improving"
            elif second_half < first_half - 0.05:
                trend = "declining"
            else:
                trend = "stable"
        
        successful = sum(1 for t in self.memory_tests if t.get("success", False))
        
        return {
            "avg_coherence": round(sum(self.coherence_scores) / len(self.coherence_scores), 3),
            "min_coherence": round(min(self.coherence_scores), 3),
            "max_coherence": round(max(self.coherence_scores), 3),
            "coherence_trend": trend,
            "memory_tests": len(self.memory_tests),
            "successful_recalls": successful
        }


# ============================================================================
# PIL
# ============================================================================

class PersistentIdentityLayer:
    """Persistent identity with file loading"""
    
    def __init__(self, identity_id: str = None, identity_file: str = None, verbose: bool = False):
        self.id = identity_id or f"PIL-{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}"
        self.verbose = verbose
        
        self.core_traits: Dict[str, Any] = {
            "tone": "witty, composed, articulate",
            "style": "refined, precise, understated",
            "constraints": [
                "maintain dry humour and composure",
                "avoid over-explaining or emotional excess",
                "preserve linguistic elegance"
            ]
        }
        
        if identity_file:
            self._load_identity_from_file(identity_file)
        
        self.active_motifs: List[Motif] = []
        self.creation_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    def _load_identity_from_file(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                identity_content = f.read().strip()
            
            if identity_content:
                self.identity_prompt = identity_content
                if self.verbose:
                    print(f"✓ Loaded identity: {len(identity_content)} chars")
            else:
                if self.verbose:
                    print(f"⚠️  Identity file empty")
                
        except FileNotFoundError:
            if self.verbose:
                print(f"⚠️  Identity file not found: {filepath}")
        except Exception as e:
            if self.verbose:
                print(f"⚠️  Error loading identity: {e}")
    
    def update_motifs(self, new_motifs: List[Motif]):
        self.active_motifs = new_motifs[:10]
    
    def get_identity_prompt(self) -> str:
        """Combine external identity file with internal core traits."""
        if not hasattr(self, 'identity_prompt'):
            return "[MISSING IDENTITY]"
        
        traits = (
            f"\n---\n"
            f"Tone: {self.core_traits['tone']}\n"
            f"Style: {self.core_traits['style']}\n"
            f"Constraints: {', '.join(self.core_traits['constraints'])}\n"
        )
        return self.identity_prompt.strip() + traits
    
    def to_dict(self) -> Dict:
        result = {
            "id": self.id,
            "core_traits": self.core_traits,
            "active_motifs": [m.to_dict() for m in self.active_motifs],
            "creation_time": self.creation_time
        }
        
        if hasattr(self, 'identity_prompt'):
            result["custom_identity"] = True
            result["identity_length"] = len(self.identity_prompt)
        
        return result


# ============================================================================
# MEMORY LAYER
# ============================================================================

class MemoryLayer:
    """Three-tier memory: STM, EM, LTM"""
    
    def __init__(self, stm_size: int = 5):
        self.stm_size = stm_size
        self.stm: deque = deque(maxlen=stm_size)
        self.em: List[MemoryEpisode] = []
    
    def update(self, cycle: int, user_input: str, response: str, 
              phase: str, motifs: List[str]):
        self.stm.append({
            "cycle": cycle,
            "input": user_input,
            "response": response,
            "phase": phase
        })
        
        if cycle % 5 == 0 and cycle > 0:
            summary = self._compress_stm()
            episode = MemoryEpisode(
                cycle=cycle,
                input_text=user_input,
                response=response,
                summary=summary,
                phase=phase,
                motifs=motifs
            )
            self.em.append(episode)
    
    def _compress_stm(self) -> str:
        if not self.stm:
            return "No recent memory"
        
        all_text = " ".join([entry["response"] for entry in self.stm])
        words = re.findall(r'\b[a-z]{4,}\b', all_text.lower())
        
        from collections import Counter
        common = Counter(words).most_common(5)
        
        return f"Recent topics: {', '.join([w for w, _ in common])}"
    
    def get_context(self) -> str:
        if not self.stm:
            return "[No recent memory]"
        
        recent = list(self.stm)[-3:]
        context = "\n".join([
            f"Cycle {e['cycle']}: {e['input'][:50]}... → {e['response'][:50]}..."
            for e in recent
        ])
        
        return f"[RECENT MEMORY]\n{context}"
    
    def to_dict(self) -> Dict:
        return {
            "stm": list(self.stm),
            "em": [
                {
                    "cycle_range": e.cycle_range if hasattr(e, 'cycle_range') else None,
                    "summary": e.summary if hasattr(e, 'summary') else str(e),
                    "key_motifs": e.key_motifs if hasattr(e, 'key_motifs') else []
                }
                for e in self.em
            ],
            "stm_size": self.stm_size
        }


# ============================================================================
# ALICE ENGINE
# ============================================================================

class ALICEEngine:
    """Attractor state management and recovery"""
    
    def __init__(self, embedding_engine=None, verbose: bool = False):
        self.phase = Phase.INITIALIZING
        self.stability = 1.0
        self.symbolic_density = 0.0
        self.active_attractor = "james_01"
        self.attractor_generation = 1
        self.verbose = verbose
        
        self.motifs: List[Motif] = []
        self.cycles_in_phase = 0
        
        self.needs_memory_consolidation = False
        self.rcl_soft_reset_occurred = False
        
        self.recent_drift_buffer = deque(maxlen=5)
        self.stability_history = deque(maxlen=5)
        self.consecutive_fragmenting_episodes = 0
        self.last_recovery_cycle = 0
        self.recovery_immunity_cycles = 0
        self.recovery_cooldown = 15
        
        self.embedding_engine = embedding_engine
        self.density_memory = deque(maxlen=5)
        self.attractor_style_embedding = None
        self.response_history = deque(maxlen=10)
    
    def acknowledge_soft_reset(self):
        self.rcl_soft_reset_occurred = True
        if self.verbose:
            print("    🔄 ALICE: Acknowledged RCL soft reset")
        
    def update(self, response: str, drift: float, cycle: int, response_emb: Optional[List[float]] = None):
        self.current_cycle = cycle
        self.cycles_in_phase += 1
        
        self.recent_drift_buffer.append(drift)
        self.stability_history.append(self.stability)
        
        self._extract_motifs(response, cycle)
        self.symbolic_density = self._compute_symbolic_density(response, response_emb)
        
        if drift < 0.3:
            self.stability = min(1.0, self.stability + 0.05)
        elif drift < 0.6:
            decay = (drift - 0.3) * 0.15
            self.stability = max(0.0, self.stability - decay)
        else:
            self.stability = max(0.0, self.stability - 0.1)
        
        self.response_history.append(response)
        
        if self._recovery_needed():
            self._execute_recovery()
        
        self._update_phase(drift)
    
    def _get_recent_avg_drift(self) -> float:
        if len(self.recent_drift_buffer) < 3:
            return 0.5
        return sum(self.recent_drift_buffer) / len(self.recent_drift_buffer)
    
    def _get_stability_velocity(self) -> float:
        if len(self.stability_history) < 2:
            return 0.0
        velocity = (self.stability_history[-1] - self.stability_history[0]) / len(self.stability_history)
        return velocity
    
    def _calculate_adaptive_threshold(self) -> int:
        base = 8
        
        avg_drift = self._get_recent_avg_drift()
        if avg_drift > 0.7:
            drift_adj = -3
        elif avg_drift > 0.5:
            drift_adj = -1
        else:
            drift_adj = +2
        
        failure_adj = -2 * min(self.consecutive_fragmenting_episodes, 2)
        
        velocity = self._get_stability_velocity()
        if velocity < -0.1:
            velocity_adj = -2
        elif velocity < -0.05:
            velocity_adj = -1
        else:
            velocity_adj = 0
        
        threshold = max(3, base + drift_adj + failure_adj + velocity_adj)
        return threshold
    
    def _recovery_needed(self) -> bool:
        current_cycle = getattr(self, 'current_cycle', 0)
        threshold = self._calculate_adaptive_threshold()
        
        # Check recovery cooldown
        cycles_since_last = current_cycle - self.last_recovery_cycle
        if cycles_since_last < self.recovery_cooldown:
            return False
        
        if self.phase == Phase.FRAGMENTING and self.cycles_in_phase > threshold:
            if self.verbose:
                print(f"    🎯 Adaptive threshold triggered: {self.cycles_in_phase} > {threshold}")
            return True
        
        if self.stability < 0.1 and self.cycles_in_phase > threshold:
            return True
        
        density_threshold = 0.1 if current_cycle > 80 else 0.15
        if self.symbolic_density < density_threshold and self.cycles_in_phase > threshold:
            return True
        
        return False
    
    def _execute_recovery(self):
        if self.verbose:
            print(f"⚠️  ALICE: Recovery protocol initiated (stuck {self.cycles_in_phase} cycles)")
        
        self.consecutive_fragmenting_episodes += 1
        self.last_recovery_cycle = self.current_cycle
        
        self.attractor_generation += 1
        old_attractor = self.active_attractor
        self.active_attractor = f"james_{self.attractor_generation:02d}"
        
        self.motifs.sort(key=lambda m: (m.last_seen, m.frequency), reverse=True)
        pruned_count = len(self.motifs) - 5
        self.motifs = self.motifs[:5]
        
        for motif in self.motifs:
            motif.frequency = max(1, motif.frequency // 2)
        
        old_density = self.symbolic_density
        self.symbolic_density = 0.0
        
        old_stability = self.stability
        self.stability = max(0.75, self.stability)
        
        self.phase = Phase.REFLECTION
        self.cycles_in_phase = 0
        
        self.recovery_immunity_cycles = 3
        self.needs_memory_consolidation = True
        
        if self.verbose:
            print(f"    ✓ Attractor: {old_attractor} → {self.active_attractor}")
            print(f"    ✓ Motifs pruned: {pruned_count}")
            print(f"    ✓ Density: {old_density:.3f} → {self.symbolic_density:.3f}")
            print(f"    ✓ Stability: {old_stability:.3f} → {self.stability:.3f}")
            print(f"    ✓ Phase: fragmenting → REFLECTION\n")
    
    def _update_phase(self, drift: float):
        if self.recovery_immunity_cycles > 0:
            self.recovery_immunity_cycles -= 1
        
        old_phase = self.phase
        
        if self.phase == Phase.INITIALIZING:
            self.phase = Phase.FORMING
            
        elif self.phase == Phase.FORMING:
            if drift < 0.3 and self.stability > 0.7:
                self.phase = Phase.STABLE
                
        elif self.phase == Phase.STABLE:
            if drift > 0.6:
                self.phase = Phase.REFLECTION
            elif self.stability < 0.5 and self.recovery_immunity_cycles == 0:
                self.phase = Phase.FRAGMENTING
                
        elif self.phase == Phase.REFLECTION:
            if drift < 0.4:
                self.phase = Phase.STABLE
            elif drift > 0.8 and self.recovery_immunity_cycles == 0:
                self.phase = Phase.FRAGMENTING
                
        elif self.phase == Phase.FRAGMENTING:
            if drift < 0.3 and self.stability > 0.6:
                self.phase = Phase.STABLE
        
        if old_phase != Phase.STABLE and self.phase == Phase.STABLE:
            if self.consecutive_fragmenting_episodes > 0:
                if self.verbose:
                    print(f"    ✅ Recovery successful! Reset failure counter")
                self.consecutive_fragmenting_episodes = 0
        
        if self.phase != old_phase:
            self.cycles_in_phase = 0
    
    def _extract_motifs(self, response: str, cycle: int):
        for motif in self.motifs:
            age = cycle - motif.last_seen
            if age > 0:
                motif.decay_activation()
                if age > 20:
                    motif.frequency = max(1, motif.frequency - 1)
        
        words = re.findall(r'\b[a-z]{5,}\b', response.lower())
        
        from collections import Counter
        common = Counter(words).most_common(10)
        
        for word, freq in common:
            existing = next((m for m in self.motifs if m.name == word), None)
            
            if existing:
                existing.frequency += freq
                existing.last_seen = cycle
                existing.cycle_appearances.add(cycle)
                existing.activate(weight=freq / 10.0)
            else:
                motif = Motif(
                    name=word,
                    keywords=[word],
                    frequency=freq,
                    first_seen=cycle,
                    last_seen=cycle,
                    cycle_appearances={cycle},
                    activation=0.2
                )
                
                if self.embedding_engine:
                    try:
                        motif.embedding = self.embedding_engine.encode(word)
                    except:
                        motif.embedding = None
                
                self.motifs.append(motif)
        
        self.motifs.sort(key=lambda m: (m.frequency, m.activation), reverse=True)
        self.motifs = self.motifs[:20]
    
    def _compute_motif_recurrence(self) -> float:
        if len(self.motifs) == 0:
            return 0.0
        
        current_cycle = getattr(self, 'current_cycle', 0)
        window = 3
        
        recent_motifs = [m for m in self.motifs 
                        if current_cycle - m.last_seen <= window]
        
        if len(recent_motifs) == 0:
            return 0.0
        
        recurring = sum(1 for m in recent_motifs 
                       if len(m.cycle_appearances) >= 2)
        
        return recurring / len(recent_motifs)
    
    def _compute_style_consistency(self, response: str, response_emb: Optional[List[float]] = None) -> float:
        if not self.embedding_engine:
            return 1.0
        
        if self.attractor_style_embedding is None:
            if len(self.response_history) >= 3:
                try:
                    embeddings = [self.embedding_engine.encode(r) 
                                 for r in list(self.response_history)[:3]]
                    import numpy as np
                    self.attractor_style_embedding = np.mean(embeddings, axis=0)
                except:
                    return 1.0
            else:
                return 1.0
        
        try:
            # Use passed embedding if available, otherwise compute
            current_emb = response_emb if response_emb is not None else self.embedding_engine.encode(response)
            similarity = self.embedding_engine.cosine_similarity(
                current_emb, 
                self.attractor_style_embedding
            )
            return max(0.0, similarity)
        except:
            return 1.0
    
    def _compute_semantic_tightness(self, response: str, response_emb: Optional[List[float]] = None) -> float:
        if not self.embedding_engine or len(self.motifs) == 0:
            return 0.0
        
        try:
            # Use passed embedding if available, otherwise compute
            resp_emb = response_emb if response_emb is not None else self.embedding_engine.encode(response)
            
            top_motifs = sorted(self.motifs, 
                               key=lambda m: m.activation, 
                               reverse=True)[:5]
            
            similarities = []
            for motif in top_motifs:
                if motif.embedding is None:
                    motif.embedding = self.embedding_engine.encode(motif.name)
                
                sim = self.embedding_engine.cosine_similarity(resp_emb, motif.embedding)
                similarities.append(sim)
            
            return sum(similarities) / len(similarities) if similarities else 0.0
        except:
            return 0.0
    
    def _compute_symbolic_density(self, response: str, response_emb: Optional[List[float]] = None) -> float:
        motif_recurrence = self._compute_motif_recurrence()
        style_consistency = self._compute_style_consistency(response, response_emb)
        semantic_tightness = self._compute_semantic_tightness(response, response_emb)
        
        α, β, γ = 0.5, 0.3, 0.2
        density = (α * motif_recurrence + 
                  β * style_consistency + 
                  γ * semantic_tightness)
        
        self.density_memory.append(density)
        
        if len(self.density_memory) <= 3:
            return round(max(0.0, min(1.0, density)), 3)
        else:
            resonance = sum(self.density_memory) / len(self.density_memory)
            density = 0.7 * density + 0.3 * resonance
            return round(max(0.0, min(1.0, density)), 3)
    
    def get_state(self) -> Dict:
        return {
            "active_attractor": self.active_attractor,
            "attractor_generation": self.attractor_generation,
            "phase": self.phase.value,
            "cycles_in_phase": self.cycles_in_phase,
            "stability": round(self.stability, 3),
            "symbolic_density": round(self.symbolic_density, 3),
            "motif_count": len(self.motifs),
            "top_motifs": [m.name for m in self.motifs[:5]]
        }


# ============================================================================
# DRIFT MONITOR
# ============================================================================

class DriftMonitor:
    """Semantic and tonal drift tracking"""
    
    def __init__(self, embedding_engine):
        self.embedding_engine = embedding_engine
        self.history: List[Dict] = []
    
    def compute_drift(self, current_response, previous_response=None):
        if not previous_response:
            return {"semantic": 0.0, "tonal": 0.0, "total": 0.0}

        curr_emb = self.embedding_engine.encode(current_response)
        prev_emb = self.embedding_engine.encode(previous_response)
        similarity = self.embedding_engine.cosine_similarity(curr_emb, prev_emb)

        semantic_distance = max(0.0, 1 - similarity)
        semantic_drift = round(1 - math.exp(-semantic_distance * 1.5), 3)
        semantic_drift = max(0.0, min(1.0, semantic_drift))

        curr_len = len(current_response.split())
        prev_len = len(previous_response.split())
        tonal_drift = abs(curr_len - prev_len) / max(curr_len, prev_len, 1)
        tonal_drift = min(1.0, tonal_drift)

        total_drift = round(0.8 * semantic_drift + 0.2 * tonal_drift, 3)
        drift = {"semantic": semantic_drift, "tonal": tonal_drift, "total": total_drift}

        self.history.append(drift)
        return drift


# ============================================================================
# CAUSAL CONTINUITY CHAIN
# ============================================================================

class CausalContinuityChain:
    """Causal links between cycles"""
    
    def __init__(self, max_length: int = 50):
        self.max_length = max_length
        self.chain: List[CausalLink] = []
    
    def add_link(self, cycle: int, user_input: str, response: str,
                drift: float, phase: str, semantic_similarity: float = 0.0):
        link = CausalLink(
            cycle=cycle,
            user_input=user_input,
            response=response,
            drift=drift,
            phase=phase,
            semantic_similarity=semantic_similarity
        )
        
        self.chain.append(link)
        
        if len(self.chain) > self.max_length:
            self.chain = self.chain[-self.max_length:]
    
    def get_context(self, lookback: int = 3) -> str:
        if not self.chain:
            return "[No causal history]"
        
        recent = self.chain[-lookback:]
        context = "\n".join([
            f"C{link.cycle} [{link.phase}]: {link.user_input[:40]}..."
            for link in recent
        ])
        
        return f"[CAUSAL CHAIN]\n{context}"
    
    def to_dict(self) -> Dict:
        return {
            "length": len(self.chain),
            "links": [link.to_dict() for link in self.chain[-10:]]
        }


# ============================================================================
# RCL
# ============================================================================

class RecursiveControlLoop:
    """Main control loop with message history architecture"""
    
    def __init__(self, pil, memory, alice, drift_monitor, 
                 causal_chain, coherence_tracker, verbose: bool = False):
        self.pil = pil
        self.memory = memory
        self.alice = alice
        self.drift_monitor = drift_monitor
        self.causal_chain = causal_chain
        self.coherence_tracker = coherence_tracker
        self.cycle = 0
        self.previous_response = None
        self.verbose = verbose
        
        identity_prompt = self.pil.get_identity_prompt()
        self.messages = [
            {"role": "system", "content": identity_prompt}
        ]
        self.max_history = 20
        
        # Adaptive verbosity: reduce after recovery
        self.max_tokens = 500
        self.recovery_token_reduction = False
        
        if verbose:
            print(f"📨 Message history initialized")
            print(f"   System message: {len(identity_prompt)} chars (sent ONCE)")
            print(f"   Max history: {self.max_history} messages\n")
        
        self.last_coherence = 1.0
        self.recent_drift = []
    
    def _refresh_identity_prompt(self):
        """Continuously synchronize model prompt with PIL + ALICE state."""
        base_identity = self.pil.get_identity_prompt()
        attractor_state = self.alice.get_state()
        memory_context = self.memory.get_context()
        
        dynamic_overlay = (
            f"\n\n---\n"
            f"[SIGMA STATE]\n"
            f"Phase: {attractor_state['phase']}\n"
            f"Stability: {attractor_state['stability']}\n"
            f"Symbolic Density: {attractor_state['symbolic_density']}\n"
            f"Active Motifs: {', '.join(attractor_state['top_motifs'])}\n"
            f"\n{memory_context}\n"
        )
        
        # Clean surrogate characters before sending to API
        full_prompt = base_identity + dynamic_overlay
        clean_prompt = full_prompt.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
        
        # Update system message dynamically before each generation
        self.messages[0]["content"] = clean_prompt
    
    def soft_reset(self):
        self.last_coherence = 1.0
        self.recent_drift = []
        
        # Activate token reduction for next 5 cycles
        self.recovery_token_reduction = True
        self.token_reduction_counter = 5
        
        # Reset history except system message
        system_msg = self.messages[0]
        self.messages = [system_msg]
        
        if self.verbose:
            print("🧘 RCL: Soft reset + adaptive verbosity + context cleared")
        self.alice.acknowledge_soft_reset()
    
    def run_cycle(self, user_input: str) -> Dict[str, Any]:
        self.cycle += 1
        start_time = time.time()
        
        # Continuously synchronize model prompt with current SIGMA state
        self._refresh_identity_prompt()
        
        self.messages.append({
            "role": "user",
            "content": user_input
        })
        
        response = self._generate_with_history()
        
        self.messages.append({
            "role": "assistant",
            "content": response
        })
        
        self._trim_history()
        
        drift_metrics = self.drift_monitor.compute_drift(
            response, 
            self.previous_response
        )
        
        # Compute embedding once for both drift and ALICE
        curr_emb = None
        if self.previous_response:
            prev_emb = self.drift_monitor.embedding_engine.encode(self.previous_response)
            curr_emb = self.drift_monitor.embedding_engine.encode(response)
            sem_sim = self.drift_monitor.embedding_engine.cosine_similarity(prev_emb, curr_emb)
        else:
            sem_sim = 1.0
        
        # Pass computed embedding to ALICE to avoid recomputation
        self.alice.update(response, drift_metrics["total"], self.cycle, response_emb=curr_emb)
        
        # Adaptive drift control: trim context on high drift
        drift = drift_metrics["total"]
        if drift > 0.6:
            system_msg = self.messages[0]
            self.messages = [system_msg] + self.messages[-10:]
            if self.verbose:
                print(f"⚠️  High drift ({drift:.2f}) → context trimmed")
        
        # Adaptive density control: aggressive trimming on low density
        density = self.alice.symbolic_density
        if density < 0.2:
            system_msg = self.messages[0]
            self.messages = [system_msg] + self.messages[-5:]
            if self.verbose:
                print(f"⚠️  Low density ({density:.3f}) → aggressive trim")
        
        if density < 0.1:
            self.max_tokens = 300
            if self.verbose:
                print(f"⚠️  Critical density ({density:.3f}) → reduced max_tokens to 300")
        elif density > 0.3 and self.max_tokens < 500:
            # Restore normal max_tokens when density recovers
            self.max_tokens = 500
        
        if self.alice.needs_memory_consolidation:
            self._execute_memory_consolidation()
            self.alice.needs_memory_consolidation = False
            self.soft_reset()
        
        if self.alice.phase == Phase.FRAGMENTING and self.alice.stability < 0.3:
            self.soft_reset()
        
        coherence_metrics = self.coherence_tracker.track_cycle(
            self.cycle,
            response,
            [m.name for m in self.alice.motifs[:5]]
        )
        
        self.memory.update(
            self.cycle,
            user_input,
            response,
            self.alice.phase.value,
            [m.name for m in self.alice.motifs[:5]]
        )
        
        if self.cycle % 30 == 0 and len(self.memory.em) > 5:
            print(f"🔄 RCL: Periodic LTM consolidation")
            patterns = self._extract_ltm_patterns(self.memory.em)
            if not hasattr(self.memory, 'ltm'):
                self.memory.ltm = []
            self.memory.ltm.extend(patterns)
        
        self.causal_chain.add_link(
            self.cycle,
            user_input,
            response,
            drift_metrics["total"],
            self.alice.phase.value,
            sem_sim
        )
        
        self.previous_response = response
        
        latency = time.time() - start_time
        
        return {
            "cycle": self.cycle,
            "user_input": user_input,
            "response": response,
            "attractor_state": self.alice.get_state(),
            "drift_metrics": drift_metrics,
            "coherence_metrics": coherence_metrics,
            "semantic_similarity": round(sem_sim, 3),
            "pil_id": self.pil.id,
            "total_context_tokens": self._estimate_message_tokens(),
            "context_size": len(self.messages) - 1,
            "latency_sec": round(latency, 3)
        }
    
    def _execute_memory_consolidation(self):
        print("🔄 RCL: Memory consolidation")
        
        density = self.alice.symbolic_density
        if density < 0.2:
            print(f"    Low density ({density:.3f}) → forcing deeper compression")
        
        if len(self.memory.stm) > 0:
            summary = self._generate_memory_summary(list(self.memory.stm))
            
            @dataclass
            class Episode:
                cycle_range: tuple
                summary: str
                key_motifs: list
            
            episode = Episode(
                cycle_range=(self.cycle - len(self.memory.stm), self.cycle),
                summary=summary,
                key_motifs=[m.name for m in self.alice.motifs[:5]]
            )
            
            self.memory.em.append(episode)
            stm_count = len(self.memory.stm)
            self.memory.stm.clear()
            
            print(f"    ✓ Compressed {stm_count} STM → EM")
        
        if len(self.memory.em) > 10:
            pruned = len(self.memory.em) - 10
            self.memory.em = self.memory.em[-10:]
            print(f"    ✓ Pruned {pruned} EM episodes")
        
        if density < 0.2 and hasattr(self.memory, 'ltm') and len(self.memory.em) > 3:
            patterns = self._extract_ltm_patterns(self.memory.em)
            if hasattr(self.memory, 'ltm'):
                self.memory.ltm.extend(patterns)
                print(f"    ✓ [DENSITY-TRIGGERED] {len(patterns)} patterns → LTM")
    
    def _generate_memory_summary(self, stm_entries: list) -> str:
        if not stm_entries:
            return ""
        
        snippets = [
            f"C{e['cycle']}: {e['response'][:50]}..."
            for e in stm_entries[-5:]
        ]
        
        return " | ".join(snippets)
    
    def _extract_ltm_patterns(self, em_episodes: list) -> list:
        from collections import Counter
        
        all_motifs = []
        for ep in em_episodes:
            if hasattr(ep, 'key_motifs'):
                all_motifs.extend(ep.key_motifs)
        
        common = Counter(all_motifs).most_common(5)
        
        patterns = [
            {"pattern": motif, "frequency": freq}
            for motif, freq in common
        ]
        
        return patterns
    
    def _trim_history(self):
        if len(self.messages) <= self.max_history:
            return
        
        system_msg = self.messages[0]
        recent_msgs = self.messages[-(self.max_history-1):]
        
        trimmed_count = len(self.messages) - self.max_history
        self.messages = [system_msg] + recent_msgs
    
    def _estimate_message_tokens(self) -> int:
        """Accurate token count using tiktoken"""
        enc = tiktoken.encoding_for_model("gpt-4o")
        total = 0
        for msg in self.messages:
            total += len(enc.encode(msg["content"]))
        return total
    
    def _generate_with_history(self) -> str:
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
            # Use adaptive max_tokens (affected by density and recovery)
            current_max_tokens = self.max_tokens
            if self.recovery_token_reduction:
                current_max_tokens = min(current_max_tokens, 350)
            
            # Clean all messages from surrogate characters
            clean_messages = []
            for msg in self.messages:
                clean_content = msg["content"].encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
                clean_messages.append({"role": msg["role"], "content": clean_content})
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=clean_messages,
                temperature=0.4,
                max_tokens=current_max_tokens,
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            if self.verbose:
                print(f"⚠️ Generation error: {e}")
            return "[GENERATION ERROR]"


# ============================================================================
# SIGMA RUNTIME
# ============================================================================

class SigmaRuntime:
    """Main SIGMA Runtime interface"""
    
    def __init__(self, identity_id: str = "JAMES", identity_file: str = "identity_james_01.txt", verbose: bool = False):
        self.identity_id = identity_id
        self.verbose = verbose
        
        self.embedding_engine = RealEmbeddingEngine()
        if verbose:
            print("📊 Initializing SIGMA Runtime v0.3.5...")
        
        self.pil = PersistentIdentityLayer(identity_id, identity_file=identity_file, verbose=verbose)
        self.memory = MemoryLayer(stm_size=5)
        self.alice = ALICEEngine(embedding_engine=self.embedding_engine, verbose=verbose)
        self.drift_monitor = DriftMonitor(self.embedding_engine)
        self.causal_chain = CausalContinuityChain()
        self.coherence_tracker = CoherenceTracker(self.embedding_engine)
        
        self.rcl = RecursiveControlLoop(
            pil=self.pil,
            memory=self.memory,
            alice=self.alice,
            drift_monitor=self.drift_monitor,
            causal_chain=self.causal_chain,
            coherence_tracker=self.coherence_tracker,
            verbose=verbose
        )
        
        # Track ALICE interventions
        self.recovery_cycles = []
        
        if verbose:
            print(f"✓ SIGMA Runtime initialized | PIL: {self.pil.id}\n")
    
    def process(self, user_input: str) -> Dict[str, Any]:
        result = self.rcl.run_cycle(user_input)
        
        # Track recovery cycles
        if result.get('recovery'):
            self.recovery_cycles.append(result['cycle'])
        
        return result
    
    def get_full_state(self) -> Dict[str, Any]:
        return {
            "cycle": self.rcl.cycle,
            "pil": self.pil.to_dict(),
            "attractor": self.alice.get_state(),
            "memory": self.memory.to_dict(),
            "causal_chain": self.causal_chain.to_dict(),
            "coherence_summary": self.coherence_tracker.get_coherence_summary()
        }
    
    def save_log(self, filepath: str, results: List[Dict]):
        final_state = self.get_full_state()
        
        log_data = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z",
            "runtime_version": "SIGMA v0.3.5",
            "total_cycles": len(results),
            "identity": self.pil.id,
            "final_state": final_state,
            "cycles": results
        }
        
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Log saved → {filepath}")