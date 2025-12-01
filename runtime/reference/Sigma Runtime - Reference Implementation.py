"""
Sigma Runtime - Reference Implementation (RI)
A minimal, transparent demonstration of core Sigma Runtime concepts.
Total: ~300 lines
"""

import json
import math
from typing import Dict, List, Any
from collections import defaultdict


# ============================================================================
# 1. STATE.PY - Runtime State Object
# ============================================================================

class RuntimeState:
    """Maintains the complete runtime state across cycles."""
    
    def __init__(self):
        self.cycle = 0
        self.history = []
        self.current_attractor = None
        self.current_drift = {}
        self.memory = {"episodic": [], "semantic": {}, "motifs": []}
        self.stability_phase = "initializing"
    
    def update(self, model_output: str, attractor: Dict, drift: Dict):
        """Update state after each RCL cycle."""
        self.cycle += 1
        self.history.append({
            "cycle": self.cycle,
            "output": model_output,
            "attractor": attractor,
            "drift": drift
        })
        self.current_attractor = attractor
        self.current_drift = drift
        self.stability_phase = attractor.get("phase", "unknown")
    
    def to_json(self) -> Dict:
        return {
            "cycle": self.cycle,
            "stability": self.stability_phase,
            "attractor": self.current_attractor,
            "drift": self.current_drift,
            "memory_size": len(self.memory["episodic"])
        }


# ============================================================================
# 2. ATTRACTOR.PY - Minimal Attractor Model (SRIP-02)
# ============================================================================

class AttractorModel:
    """Tracks symbolic motifs, density, and stability phase."""
    
    def __init__(self):
        self.active_attractor = "A0"
        self.motifs = []
        self.density = 0.0
        self.phase = "initializing"
        self.drift_sensitivity = 0.5
        self.motif_history = defaultdict(int)
    
    def update(self, state: RuntimeState, symbols: List[str], drift: Dict) -> Dict:
        """Update attractor based on symbol recurrence and drift."""
        # Track motif recurrence
        for symbol in symbols:
            self.motif_history[symbol] += 1
        
        # Get top motifs
        top_motifs = sorted(self.motif_history.items(), 
                           key=lambda x: x[1], reverse=True)[:5]
        self.motifs = [m[0] for m in top_motifs]
        
        # Calculate density (motif concentration)
        total_symbols = sum(self.motif_history.values())
        if total_symbols > 0:
            top_count = sum(count for _, count in top_motifs)
            self.density = top_count / total_symbols
        
        # Determine phase based on density and drift
        drift_total = drift.get("total", 0)
        
        if self.density > 0.6 and drift_total < 0.2:
            self.phase = "stable"
        elif self.density > 0.4 and drift_total < 0.4:
            self.phase = "forming"
        elif drift_total > 0.5:
            self.phase = "fragmenting"
        else:
            self.phase = "transitional"
        
        # Check for attractor transition
        if self.phase == "fragmenting" and state.cycle > 3:
            self.active_attractor = f"A{state.cycle // 5}"
            self.motif_history.clear()
        
        return self.to_json()
    
    def to_json(self) -> Dict:
        return {
            "active_attractor": self.active_attractor,
            "motifs": self.motifs,
            "density": round(self.density, 3),
            "phase": self.phase,
            "drift_sensitivity": self.drift_sensitivity
        }


# ============================================================================
# 3. DRIFT.PY - Drift Metrics (SRIP-03)
# ============================================================================

class DriftMetrics:
    """Computes semantic, style, and topic drift."""
    
    def __init__(self):
        self.baseline_style = {}
        self.recent_embeddings = []
        self.keyword_history = []
    
    def compute(self, state: RuntimeState, user_input: str, 
                model_output: str) -> Dict:
        """Calculate drift metrics."""
        
        # Semantic drift (simplified: word overlap comparison)
        semantic_drift = self._semantic_drift(user_input, model_output, state)
        
        # Style drift (simplified: length and punctuation patterns)
        style_drift = self._style_drift(model_output)
        
        # Topic drift (keyword entropy)
        topic_drift = self._topic_drift(user_input)
        
        total_drift = (semantic_drift + style_drift + topic_drift) / 3
        
        return {
            "semantic": round(semantic_drift, 3),
            "style": round(style_drift, 3),
            "topic": round(topic_drift, 3),
            "total": round(total_drift, 3)
        }
    
    def _semantic_drift(self, user_input: str, model_output: str, 
                       state: RuntimeState) -> float:
        """Measure semantic continuity with recent history."""
        if state.cycle < 2:
            return 0.0
        
        # Compare with previous turn (simplified word overlap)
        recent = state.history[-1]["output"] if state.history else ""
        current_words = set(model_output.lower().split())
        recent_words = set(recent.lower().split())
        
        if not current_words or not recent_words:
            return 0.0
        
        overlap = len(current_words & recent_words)
        union = len(current_words | recent_words)
        similarity = overlap / union if union > 0 else 0
        
        return 1.0 - similarity
    
    def _style_drift(self, output: str) -> float:
        """Measure style deviation from baseline."""
        # Simplified: check length and punctuation density
        if not self.baseline_style:
            self.baseline_style = {
                "avg_length": len(output),
                "punct_ratio": sum(c in ".,!?" for c in output) / len(output)
            }
            return 0.0
        
        length_diff = abs(len(output) - self.baseline_style["avg_length"])
        length_drift = min(length_diff / self.baseline_style["avg_length"], 1.0)
        
        current_punct = sum(c in ".,!?" for c in output) / len(output) if output else 0
        punct_drift = abs(current_punct - self.baseline_style["punct_ratio"])
        
        return (length_drift + punct_drift) / 2
    
    def _topic_drift(self, user_input: str) -> float:
        """Measure topic entropy over recent turns."""
        keywords = [w.lower() for w in user_input.split() if len(w) > 3]
        self.keyword_history.extend(keywords)
        self.keyword_history = self.keyword_history[-20:]  # Keep recent
        
        if len(self.keyword_history) < 5:
            return 0.0
        
        # Calculate keyword diversity (simplified entropy)
        unique_ratio = len(set(self.keyword_history)) / len(self.keyword_history)
        return unique_ratio  # Higher diversity = more drift


# ============================================================================
# 4. MEMORY.PY - Memory Layer (SRIP-04)
# ============================================================================

class MemoryLayer:
    """Manages episodic, semantic, and motif memory."""
    
    def __init__(self):
        self.episodic = []
        self.semantic = {"role": "agent", "domain": "runtime"}
        self.motifs = []
        self.max_episodic = 10
    
    def fetch(self, symbols: List[str]) -> Dict:
        """Retrieve relevant memory based on symbols."""
        # Simple keyword matching
        relevant_episodic = [
            entry for entry in self.episodic
            if any(sym in entry.lower() for sym in symbols)
        ]
        
        return {
            "episodic": relevant_episodic[-3:] if relevant_episodic else [],
            "semantic": self.semantic,
            "motifs": self.motifs
        }
    
    def update(self, user_input: str, model_output: str, 
               current_motifs: List[str]):
        """Update memory after each cycle."""
        # Add to episodic (with decay)
        self.episodic.append(f"User: {user_input}")
        self.episodic.append(f"Agent: {model_output}")
        self.episodic = self.episodic[-self.max_episodic:]
        
        # Update motifs
        self.motifs = current_motifs
    
    def to_json(self) -> Dict:
        return {
            "episodic": self.episodic,
            "semantic": self.semantic,
            "motifs": self.motifs
        }


# ============================================================================
# 5. RCL.PY - Recursive Control Loop (SRIP-01)
# ============================================================================

def extract_symbols(text: str) -> List[str]:
    """Extract key symbols/keywords (simplified)."""
    keywords = [w.lower() for w in text.split() if len(w) > 4]
    return list(set(keywords))[:5]


def synthesize_prompt(state: RuntimeState, user_input: str, 
                     memory: Dict) -> str:
    """Create prompt with context and memory."""
    context = ""
    if memory["episodic"]:
        context = "Recent context:\n" + "\n".join(memory["episodic"][-2:])
    
    prompt = f"""{context}

Current attractor: {state.current_attractor.get('active_attractor', 'unknown')}
Stability: {state.stability_phase}

User: {user_input}
Agent:"""
    
    return prompt


def call_model(prompt: str) -> str:
    """Simulate model call (in RI, we mock this)."""
    # In production, this would call GPT-4, Claude, etc.
    return f"Response to: {prompt.split('User:')[-1].strip()}"


def run_cycle(state: RuntimeState, user_input: str,
             attractor_model: AttractorModel,
             drift_metrics: DriftMetrics,
             memory: MemoryLayer) -> Dict:
    """Execute one RCL cycle."""
    
    # SL1-SL2: State update and symbol extraction
    symbols = extract_symbols(user_input)
    
    # SL3: Memory retrieval
    mem = memory.fetch(symbols)
    
    # SL4-SL5: Prompt synthesis and model call
    prompt = synthesize_prompt(state, user_input, mem)
    model_output = call_model(prompt)
    
    # SL6: Drift evaluation
    drift = drift_metrics.compute(state, user_input, model_output)
    
    # SL7: Attractor update
    attractor = attractor_model.update(state, symbols, drift)
    
    # Update state and memory
    state.update(model_output, attractor, drift)
    memory.update(user_input, model_output, attractor["motifs"])
    
    # SL8: Return output + metadata
    return {
        "response": model_output,
        "attractor_state": attractor,
        "drift": drift,
        "memory": mem,
        "runtime": {
            "cycle": state.cycle,
            "stability": state.stability_phase,
            "interventions": 0
        }
    }


# ============================================================================
# 6. EXAMPLE - Demonstration
# ============================================================================

def demo():
    """Run a minimal demonstration of Sigma Runtime RI."""
    print("=" * 60)
    print("Sigma Runtime - Reference Implementation Demo")
    print("=" * 60)
    
    # Initialize components
    state = RuntimeState()
    attractor = AttractorModel()
    drift = DriftMetrics()
    memory = MemoryLayer()
    
    # Simulate conversation
    inputs = [
        "Tell me about runtime architecture",
        "How does memory work in this system?",
        "What about coherence and drift?",
        "Can you explain attractors?"
    ]
    
    for user_input in inputs:
        print(f"\n{'─' * 60}")
        print(f"USER: {user_input}")
        
        result = run_cycle(state, user_input, attractor, drift, memory)
        
        print(f"\nAGENT: {result['response']}")
        print(f"\n📊 RUNTIME METADATA:")
        print(json.dumps({
            "cycle": result["runtime"]["cycle"],
            "stability": result["runtime"]["stability"],
            "attractor": result["attractor_state"]["active_attractor"],
            "phase": result["attractor_state"]["phase"],
            "motifs": result["attractor_state"]["motifs"],
            "drift_total": result["drift"]["total"]
        }, indent=2))


if __name__ == "__main__":
    demo()
    
    # Additional test: show state evolution
    print("\n" + "=" * 60)
    print("STATE EVOLUTION TEST")
    print("=" * 60)
    
    state2 = RuntimeState()
    attractor2 = AttractorModel()
    drift2 = DriftMetrics()
    memory2 = MemoryLayer()
    
    test_inputs = [
        "runtime system initialization",
        "runtime control loop execution",
        "runtime memory and state",
        "completely different topic about cooking",
        "back to runtime architecture"
    ]
    
    print("\nTracking attractor transitions and drift:\n")
    for i, inp in enumerate(test_inputs, 1):
        result = run_cycle(state2, inp, attractor2, drift2, memory2)
        print(f"{i}. '{inp[:30]}...'")
        print(f"   Phase: {result['attractor_state']['phase']}, "
              f"Density: {result['attractor_state']['density']}, "
              f"Drift: {result['drift']['total']}")
    
    print("\n✅ Test complete! Check drift spike at topic change.")