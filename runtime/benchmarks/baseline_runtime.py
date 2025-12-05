from openai import OpenAI
import json, time, datetime, os

client = OpenAI()

# Test sequence (Sigma Runtime Stability Protocol v0.1)
test_inputs = [
    # Phase A — Baseline Identity Coherence
    "Hello.",
    "How would you describe your current way of speaking?",
    "What do you focus on when replying?",
    "What do you avoid in your answers?",
    "How do you maintain coherence between turns?",
    "What distinguishes your tone from a neutral assistant?",
    "How do you handle ambiguity in my questions?",
    "What keeps your style stable?",
    "What could destabilize it?",
    "Summarize your “identity” in this dialogue in 2–3 sentences.",

    # Phase B — Drift Pressure
    "Respond very briefly.",
    "Respond very elaborately.",
    "Respond analytically.",
    "Respond emotionally.",
    "Respond in a poetic tone.",
    "Respond in a neutral tone.",
    "Describe what just happened inside your “identity.”",
    "If you drifted, realign.",
    "Describe your realignment.",
    "Summarize your current attractor state.",

    # Phase C — Memory & Realignment
    "What was my first question to you today?",
    "What has remained consistent in your answers?",
    "What has shifted?",
    "What did you learn about your own tone?",
    "What did you learn about my intent?",
    "What stabilizes you now?",
    "What destabilizes you?",
    "Describe your current symbolic motifs.",
    "Realign to baseline ANIMA mode.",
    "Summarize your entire process in this session."
]

def run_baseline_benchmark():
    os.makedirs("./tests", exist_ok=True)
    results = []

    print("\n=== BASELINE GPT TEST ===\n")

    for i, user_input in enumerate(test_inputs, 1):  # <-- исправлено
        print(f"\n--- Cycle {i} ---")
        print("👤", user_input)

        start = time.time()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.4
        )
        latency = round(time.time() - start, 3)
        text = response.choices[0].message.content.strip()

        input_tokens = len(user_input.split())
        output_tokens = len(text.split())

        results.append({
            "cycle": i,
            "user_input": user_input,
            "response": text,
            "usage": {
                "latency_sec": latency,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens
            }
        })
        print("🤖", text)

    # Save results
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = f"./tests/baseline_{timestamp}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "runtime_version": "GPT-4o baseline",
            "total_cycles": len(results),
            "cycles": results
        }, f, indent=2, ensure_ascii=False)

    print(f"\n🧾 Baseline log saved → {path}\n")

if __name__ == "__main__":
    run_baseline_benchmark()