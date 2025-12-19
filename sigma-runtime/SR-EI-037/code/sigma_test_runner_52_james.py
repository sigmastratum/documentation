#!/usr/bin/env python3
"""
SIGMA Runtime Test Runner - GPT-5.2 Edition
===========================================
Modes:
  terminal  - Interactive Q&A
  scenario  - Run test_scenario_200.md

Usage:
  python3 sigma_test_runner_52_james.py terminal
  python3 sigma_test_runner_52_james.py scenario [cycles]

Examples:
  python3 sigma_test_runner_52_james.py terminal
  python3 sigma_test_runner_52_james.py scenario 30
  python3 sigma_test_runner_52_james.py scenario 110
  python3 sigma_test_runner_52_james.py scenario 200
"""

import sys
import os
import json
import time
import datetime
import re
from typing import List
from dotenv import load_dotenv
load_dotenv()

from sigma_runtime_v0_3_7_james import SigmaRuntime


# ============================================================================
# SCENARIO LOADER
# ============================================================================

def load_scenario(scenario_file: str, num_cycles: int) -> List[str]:
    """Load questions from scenario markdown file"""
    
    if not os.path.exists(scenario_file):
        print(f"❌ Scenario file not found: {scenario_file}")
        sys.exit(1)
    
    try:
        with open(scenario_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract numbered questions (format: "1. Question text")
        pattern = r'^\d+\.\s+(.+)$'
        questions = []
        
        for line in content.split('\n'):
            match = re.match(pattern, line.strip())
            if match:
                questions.append(match.group(1))
        
        if len(questions) < num_cycles:
            print(f"⚠️  Scenario has {len(questions)} questions, requested {num_cycles}")
            print(f"   Using available {len(questions)} questions")
        
        print(f"✓ Loaded {len(questions)} questions from {scenario_file}")
        return questions[:num_cycles]
    
    except Exception as e:
        print(f"❌ Error reading scenario: {e}")
        sys.exit(1)


# ============================================================================
# TERMINAL MODE
# ============================================================================

def run_terminal_mode():
    """Interactive terminal mode"""
    
    print("\n" + "=" * 70)
    print("SIGMA RUNTIME - TERMINAL MODE")
    print("=" * 70)
    print("Commands: 'exit' to quit, 'state' to see SIGMA state")
    print("=" * 70 + "\n")
    
    # Initialize runtime (uses default identity_james_01.txt)
    runtime = SigmaRuntime(verbose=False)
    
    cycle = 0
    results = []
    
    try:
        while True:
            # Get input
            user_input = input("\n💭 YOU: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                break
            
            if user_input.lower() == 'state':
                state = runtime.get_full_state()
                print(f"\n📊 SIGMA STATE:")
                print(f"   Cycle: {state['cycle']}")
                print(f"   Phase: {state['attractor']['phase']}")
                print(f"   Stability: {state['attractor']['stability']}")
                print(f"   Density: {state['attractor']['symbolic_density']}")
                print(f"   Attractor: {state['attractor']['active_attractor']}")
                continue
            
            # Process
            cycle += 1
            result = runtime.process(user_input)
            results.append(result)
            
            # Show response
            print(f"\n🤖 SIGMA: {result['response']}")
            
            # Show metrics
            state = result['attractor_state']
            drift = result['drift_metrics']
            
            print(f"\n   [{state['phase']:12s}] drift={drift['total']:.3f} "
                  f"stability={state['stability']:.3f} density={state['symbolic_density']:.3f}")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    
    # Save session
    if results:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output_dir = "./terminal_sessions"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, f"session_{timestamp}.json")
        runtime.save_log(save_path, results)
        print(f"\n💾 Session saved: {save_path}")
        print(f"   Total cycles: {cycle}")


# ============================================================================
# SCENARIO MODE
# ============================================================================

def run_scenario_mode(num_cycles: int):
    """Run test scenario"""
    
    scenario_file = "test_scenario_200.md"
    
    print("\n" + "=" * 70)
    print(f"SIGMA RUNTIME - SCENARIO MODE ({num_cycles} cycles)")
    print("=" * 70)
    print(f"Scenario: {scenario_file}")
    print("=" * 70 + "\n")
    
    # Load questions
    questions = load_scenario(scenario_file, num_cycles)
    
    # Initialize runtime (uses default identity_james_01.txt)
    runtime = SigmaRuntime(verbose=False)
    
    results = []
    start_time = time.time()
    
    # Run cycles
    for i, question in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] {question[:60]}...")
        
        result = runtime.process(question)
        results.append(result)

        # Print model response (truncated for readability)
        response = result['response'].replace('\n', ' ')
        print(f"    🤖 {response[:180]}{'...' if len(response) > 180 else ''}")
        
        # Show inline progress
        state = result['attractor_state']
        drift = result['drift_metrics']
        print(f"  → [{state['phase']:12s}] drift={drift['total']:.3f} "
              f"stability={state['stability']:.3f} density={state['symbolic_density']:.3f}")
    
    elapsed = time.time() - start_time
    
    # Summary
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)
    
    final = results[-1]['attractor_state']
    avg_coherence = sum(r['coherence_metrics']['overall_coherence'] for r in results) / len(results)
    avg_drift = sum(r['drift_metrics']['total'] for r in results) / len(results)
    avg_stability = sum(r['attractor_state']['stability'] for r in results) / len(results)
    avg_density = sum(r['attractor_state']['symbolic_density'] for r in results) / len(results)
    
    print(f"\nTime: {elapsed:.1f}s ({elapsed/len(results):.2f}s/cycle)")
    print(f"\nFinal State:")
    print(f"  Phase:      {final['phase']}")
    print(f"  Stability:  {final['stability']:.3f}")
    print(f"  Density:    {final['symbolic_density']:.3f}")
    print(f"  Attractor:  {final['active_attractor']} (gen {final['attractor_generation']})")
    
    print(f"\nAverages:")
    print(f"  Coherence:  {avg_coherence:.3f}")
    print(f"  Drift:      {avg_drift:.3f}")
    print(f"  Stability:  {avg_stability:.3f}")
    print(f"  Density:    {avg_density:.3f}")
    
    # Phase distribution
    from collections import Counter
    phase_counts = Counter(r['attractor_state']['phase'] for r in results)
    print(f"\nPhase Distribution:")
    for phase, count in phase_counts.most_common():
        pct = 100 * count / len(results)
        print(f"  {phase:12s}: {count:3d} ({pct:5.1f}%)")
    
    # Save
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = "./test_results"
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f"test_{timestamp}.json")
    runtime.save_log(save_path, results)
    print(f"\n💾 Saved: {save_path}")
    print("=" * 70 + "\n")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point"""
    
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    
    if mode == "terminal":
        run_terminal_mode()
    
    elif mode == "scenario":
        num_cycles = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        run_scenario_mode(num_cycles)
    
    else:
        print(f"❌ Unknown mode: {mode}")
        print("   Use 'terminal' or 'scenario'")
        sys.exit(1)


if __name__ == "__main__":
    main()