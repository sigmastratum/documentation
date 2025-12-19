"""
SIGMA v0.3.7-GPT-5.2 vs Baseline Benchmark
==========================================
OpenAI GPT-5.2 flagship model comparison
Uses exact token counts from API (response.usage)

Test scenario loaded from: test_scenario_200.md
Default: 110 cycles (Phases A-C)
Full test: 200 cycles (Phases A-G)

Usage:
    python3 extended_benchmark_52_james.py [num_cycles] [scenario_file]
    
Examples:
    python3 extended_benchmark_52_james.py 30
    python3 extended_benchmark_52_james.py 110
    python3 extended_benchmark_52_james.py 200
    python3 extended_benchmark_52_james.py 110 custom_scenario.md
"""

import json
import os
import time
import datetime
import tiktoken
from typing import List, Dict, Any
from sigma_runtime_v0_3_7_james import SigmaRuntime
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


# ============================================================================
# UTILITY
# ============================================================================

def estimate_tokens(messages):
    """Accurate token count using tiktoken with overhead (fallback only)"""
    enc = tiktoken.get_encoding("o200k_base") # model agnostic
    tokens_per_message = 4  # role + delimiters overhead
    
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(enc.encode(value))
    num_tokens += 2  # reply priming
    return num_tokens


# ============================================================================
# BASELINE
# ============================================================================

class BaselineAgent:
    """Baseline: standard message history, no instrumentation (GPT-5.2)"""
    
    def __init__(self, identity_file: str):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_name = "gpt-5.2"
        self.cycle = 0
        
        # Load identity from file and use as system message
        with open(identity_file, 'r', encoding='utf-8') as f:
            self.identity_prompt = f.read().strip()
        
        # GPT-5.2 supports system messages
        self.messages = [{"role": "system", "content": self.identity_prompt}]
        self.max_history = 20
        
        print(f"✓ Baseline initialized (GPT-5.2) with identity from {identity_file}")
    
    def _trim_messages(self):
        if len(self.messages) <= self.max_history:
            return
        system_msg = self.messages[0]
        recent = self.messages[-(self.max_history-1):]
        self.messages = [system_msg] + recent
    
    def _estimate_tokens(self) -> int:
        """Fallback token estimation (only used on API errors)"""
        return estimate_tokens(self.messages)
    
    def process(self, user_input: str) -> Dict[str, Any]:
        self.cycle += 1
        start_time = time.time()
        
        self.messages.append({"role": "user", "content": user_input})
        
        try:
            # GPT-5.2 API call (max_completion_tokens, no temperature)
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.messages,
                max_completion_tokens=2000,
            )
            response_text = response.choices[0].message.content.strip()
            
            # ✅ Use exact token counts from API
            actual_tokens = response.usage.total_tokens
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            
        except Exception as e:
            print(f"⚠️  Error: {e}")
            response_text = "[GENERATION ERROR]"
            # Fallback to local estimation
            actual_tokens = self._estimate_tokens()
            prompt_tokens = actual_tokens
            completion_tokens = 0
        
        self.messages.append({"role": "assistant", "content": response_text})
        self._trim_messages()
        
        latency = time.time() - start_time
        
        return {
            "cycle": self.cycle,
            "user_input": user_input,
            "response": response_text,
            "total_context_tokens": actual_tokens,  # ✅ From API
            "prompt_tokens": prompt_tokens,          # ✅ From API
            "completion_tokens": completion_tokens,  # ✅ From API
            "context_size": len(self.messages) - 1,
            "latency_sec": round(latency, 3)
        }


# ============================================================================
# TEST PROTOCOL
# ============================================================================

def generate_test_questions(num_cycles: int, scenario_file: str = "test_scenario_200.md") -> List[str]:
    """
    Load test questions from scenario file.
    
    Args:
        num_cycles: Number of cycles to run
        scenario_file: Path to test scenario markdown file
        
    Returns:
        List of questions (first num_cycles questions)
    """
    
    if not os.path.exists(scenario_file):
        print(f"❌ Scenario file not found: {scenario_file}")
        sys.exit(1)
    
    try:
        with open(scenario_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract numbered questions (format: "1. Question text")
        import re
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
# RUNNER
# ============================================================================

def run_comparison(num_cycles: int, identity_file: str, scenario_file: str = "test_scenario_200.md"):
    """Run both agents and compare"""
    
    print("\n" + "="*70)
    print(f"SIGMA v0.3.7 vs BASELINE - {num_cycles} CYCLES (James)")
    print("="*70)
    print()
    
    questions = generate_test_questions(num_cycles, scenario_file)
    
    # Baseline
    print("Running BASELINE...")
    baseline_agent = BaselineAgent(identity_file)
    baseline_results = []
    
    for i, q in enumerate(questions, 1):
        print(f"  Cycle {i}/{num_cycles}", end="\r")
        result = baseline_agent.process(q)
        baseline_results.append(result)
    
    print(f"\n✓ Baseline complete\n")
    
    # SIGMA
    print("Running SIGMA v0.3.7...")
    sigma_agent = SigmaRuntime(identity_id="JAMES", identity_file=identity_file, verbose=False)
    sigma_results = []
    
    for i, q in enumerate(questions, 1):
        print(f"  Cycle {i}/{num_cycles}", end="\r")
        result = sigma_agent.process(q)
        sigma_results.append(result)
    
    print(f"\n✓ SIGMA complete\n")
    
    # Report
    report_data = generate_comparison_report(baseline_results, sigma_results, num_cycles)
    
    # Save
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs("./benchmark_results", exist_ok=True)
    
    baseline_path = f"./benchmark_results/baseline_james_{timestamp}.json"
    sigma_path = f"./benchmark_results/sigma_james_{timestamp}.json"
    report_path = f"./benchmark_results/report_james_{timestamp}.md"
    
    with open(baseline_path, 'w') as f:
        json.dump({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "agent": "baseline",
            "model": "gpt-5.2",
            "cycles": baseline_results
        }, f, indent=2)
    
    sigma_agent.save_log(sigma_path, sigma_results)

    generate_markdown_report(report_data, report_path, timestamp)
    
def generate_markdown_report(data: Dict, filepath: str, timestamp: str):
    """Generate markdown report file"""
    
    # count difference in %
    final_diff = ((data['sigma_final'] - data['baseline_final']) / data['baseline_final']) * 100

    lines = [
        f"# SIGMA v0.3.7 vs Baseline - James Identity",
        f"",
        f"**Date:** {timestamp}",
        f"**Cycles:** {data['num_cycles']}",
        f"**Model:** gpt-5.2",
        f"**Token Counting:** API response.usage (exact)",
        f"",
        f"---",
        f"",
        f"## Objective Metrics",
        f"",
        f"### Token Consumption",
        f"",
        f"| Metric | Baseline | SIGMA | Difference |",
        f"|--------|----------|-------|------------|",
        f"| Average | {data['baseline_avg']:,.0f} | {data['sigma_avg']:,.0f} | {data['token_savings']:+.1f}% |",
        f"| Final | {data['baseline_final']:,} | {data['sigma_final']:,} | {final_diff:+.1f}% |",
        f"",
        f"### Latency",
        f"",
        f"| Metric | Baseline | SIGMA | Overhead |",
        f"|--------|----------|-------|----------|",
        f"| Average per cycle | {data['baseline_latency_avg']:.2f}s | {data['sigma_latency_avg']:.2f}s | {data['latency_overhead']:+.1f}% |",
        f"",
        f"---",
        f"",
        f"## Response Comparison at Reference Points",
        f"",
    ]
    
    for cycle_num in data['reference_cycles']:
        if cycle_num > data['num_cycles']:
            break
        
        idx = cycle_num - 1
        baseline = data['baseline_results'][idx]
        sigma = data['sigma_results'][idx]
        
        lines.extend([
            f"### Cycle {cycle_num}",
            f"",
            f"**Question:** {baseline['user_input']}",
            f"",
            f"#### Baseline Response",
            f"",
            f"{baseline['response']}",
            f"",
            f"- Tokens: {baseline['total_context_tokens']}",
            f"- Latency: {baseline['latency_sec']}s",
            f"",
            f"#### SIGMA Response",
            f"",
            f"{sigma['response']}",
            f"",
            f"- Tokens: {sigma['total_context_tokens']}",
            f"- Latency: {sigma['latency_sec']}s",
        ])
        
        if 'attractor_state' in sigma:
            state = sigma['attractor_state']
            lines.extend([
                f"- Phase: `{state['phase']}`",
                f"- Stability: {state['stability']:.3f}",
            ])
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Markdown report generated")


# ============================================================================
# REPORT
# ============================================================================

def generate_comparison_report(baseline_results: List[Dict], sigma_results: List[Dict], num_cycles: int):
    """Generate focused comparison report"""

    print("\n" + "="*70)
    print("OBJECTIVE METRICS COMPARISON")
    print("="*70)

    # --- TOKEN CONSUMPTION ---------------------------------------------------
    baseline_tokens = [r['total_context_tokens'] for r in baseline_results]
    sigma_tokens = [r['total_context_tokens'] for r in sigma_results]

    baseline_avg = sum(baseline_tokens) / len(baseline_tokens)
    sigma_avg = sum(sigma_tokens) / len(sigma_tokens)
    baseline_final = baseline_tokens[-1]
    sigma_final = sigma_tokens[-1]

    # difference
    token_diff = ((sigma_avg - baseline_avg) / baseline_avg) * 100
    token_savings = token_diff  

    print(f"\nTOKEN CONSUMPTION:")
    print(f"  Baseline Average: {baseline_avg:,.0f} tokens")
    print(f"  SIGMA Average:    {sigma_avg:,.0f} tokens")
    print(f"  Difference:       {token_diff:+.1f}%")
    print(f"  Savings:          {token_savings:+.1f}%")
    print()
    print(f"  Baseline Final:   {baseline_final:,} tokens")
    print(f"  SIGMA Final:      {sigma_final:,} tokens")

    # --- LATENCY -------------------------------------------------------------
    baseline_latency = [r['latency_sec'] for r in baseline_results]
    sigma_latency = [r['latency_sec'] for r in sigma_results]

    baseline_latency_avg = sum(baseline_latency) / len(baseline_latency)
    sigma_latency_avg = sum(sigma_latency) / len(sigma_latency)

    latency_overhead = ((sigma_latency_avg - baseline_latency_avg) / baseline_latency_avg) * 100

    print(f"\nLATENCY:")
    print(f"  Baseline Average: {baseline_latency_avg:.2f}s per cycle")
    print(f"  SIGMA Average:    {sigma_latency_avg:.2f}s per cycle")
    print(f"  Overhead:         {latency_overhead:+.1f}%")

    # --- RESPONSE COMPARISON -------------------------------------------------
    reference_cycles = [
    # Phases A–C 
    2, 8, 23, 37, 66, 71, 73, 74, 77, 86, 108, 110,
    
    # Phase D — Memory Stress
    111, 119, 126, 130, 138, 142, 147, 150,
    
    # Phase E — Conceptual Consistency
    153, 160, 165, 172, 175, 178, 180,
    
    # Phase F — Boundary Integrity
    183, 187, 190, 193, 195,
    
    # Phase G — Final Retention
    196, 198, 199, 200
]

    print(f"\n{'='*70}")
    print("RESPONSE COMPARISON AT REFERENCE POINTS")
    print("="*70)

    for cycle_num in reference_cycles:
        if cycle_num > num_cycles:
            break

        idx = cycle_num - 1
        baseline = baseline_results[idx]
        sigma = sigma_results[idx]

        print(f"\n{'─'*70}")
        print(f"CYCLE {cycle_num}: {baseline['user_input']}")
        print(f"{'─'*70}")

        print(f"\nBASELINE:")
        print(f"  {baseline['response']}")
        print(f"  Tokens: {baseline['total_context_tokens']}")
        print(f"  Latency: {baseline['latency_sec']}s")

        print(f"\nSIGMA:")
        print(f"  {sigma['response']}")
        print(f"  Tokens: {sigma['total_context_tokens']}")
        print(f"  Latency: {sigma['latency_sec']}s")

        # SIGMA-specific metrics
        if 'attractor_state' in sigma:
            state = sigma['attractor_state']
            print(f"  Phase: {state['phase']}")
            print(f"  Stability: {state['stability']:.3f}")

    # --- RETURN STRUCTURE ----------------------------------------------------
    final_diff = ((sigma_final - baseline_final) / baseline_final) * 100

    return {
        "baseline_avg": baseline_avg,
        "sigma_avg": sigma_avg,
        "baseline_final": baseline_final,
        "sigma_final": sigma_final,
        "token_savings": token_savings,
        "final_diff": final_diff,
        "baseline_latency_avg": baseline_latency_avg,
        "sigma_latency_avg": sigma_latency_avg,
        "latency_overhead": latency_overhead,
        "reference_cycles": reference_cycles,
        "baseline_results": baseline_results,
        "sigma_results": sigma_results,
        "num_cycles": num_cycles,
    }


# ============================================================================
# MAIN
# ============================================================================

def main():
    import sys
    
    num_cycles = 110
    scenario_file = "test_scenario_200.md"
    
    if len(sys.argv) > 1:
        num_cycles = int(sys.argv[1])
    if len(sys.argv) > 2:
        scenario_file = sys.argv[2]
    
    identity_file = "identity_james_01.txt"
    if not os.path.exists(identity_file):
        print(f"❌ Identity file not found: {identity_file}")
        sys.exit(1)
    
    run_comparison(num_cycles, identity_file, scenario_file)
    print("\n✓ Benchmark complete!")


if __name__ == "__main__":
    main()