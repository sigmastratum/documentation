import json
import pandas as pd
import datetime

# === Paths ===
sigma_path = "/home/metasys1/runtime/tests/sigma_test_20251204-101319.json"
baseline_path = "/home/metasys1/runtime/tests/baseline_20251204-103258.json"

# === Output file with timestamp ===
timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
summary_path = f"./summary_{timestamp}.csv"

# === Load JSON ===
def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["cycles"]

baseline = load_data(baseline_path)
sigma = load_data(sigma_path)

# === Compute per-run stats ===
def stats(data):
    latencies = [c["usage"]["latency_sec"] for c in data]
    total_tokens = [c["usage"]["total_tokens"] for c in data]
    input_tokens = [c["usage"]["input_tokens"] for c in data]
    output_tokens = [c["usage"]["output_tokens"] for c in data]
    return {
        "avg_latency": sum(latencies) / len(latencies),
        "max_latency": max(latencies),
        "total_latency": sum(latencies),
        "avg_total_tokens": sum(total_tokens) / len(total_tokens),
        "total_tokens": sum(total_tokens),
        "avg_input_tokens": sum(input_tokens) / len(input_tokens),
        "avg_output_tokens": sum(output_tokens) / len(output_tokens),
    }

b = stats(baseline)
s = stats(sigma)

# === Calculate improvements ===
def improve(baseline_val, sigma_val):
    try:
        return round((1 - sigma_val / baseline_val) * 100, 2)
    except ZeroDivisionError:
        return 0.0

data = [
    ["Avg Latency (s)", b["avg_latency"], s["avg_latency"], improve(b["avg_latency"], s["avg_latency"])],
    ["Max Latency (s)", b["max_latency"], s["max_latency"], improve(b["max_latency"], s["max_latency"])],
    ["Avg Total Tokens", b["avg_total_tokens"], s["avg_total_tokens"], improve(b["avg_total_tokens"], s["avg_total_tokens"])],
    ["Total Tokens", b["total_tokens"], s["total_tokens"], improve(b["total_tokens"], s["total_tokens"])],
    ["Avg Input Tokens", b["avg_input_tokens"], s["avg_input_tokens"], improve(b["avg_input_tokens"], s["avg_input_tokens"])],
    ["Avg Output Tokens", b["avg_output_tokens"], s["avg_output_tokens"], improve(b["avg_output_tokens"], s["avg_output_tokens"])],
]

# === Add cumulative efficiency ===
cum_latency_eff = improve(b["total_latency"], s["total_latency"])
cum_token_eff = improve(b["total_tokens"], s["total_tokens"])

data.append(["Cumulative Token Efficiency (%)", b["total_tokens"], s["total_tokens"], cum_token_eff])
data.append(["Cumulative Latency Efficiency (%)", b["total_latency"], s["total_latency"], cum_latency_eff])

# === Save CSV ===
df = pd.DataFrame(data, columns=["Metric", "Baseline", "SIGMA", "Δ Improvement (%)"])
df.to_csv(summary_path, index=False, encoding="utf-8")

print(df)
print(f"\n✅ Summary with cumulative metrics saved → {summary_path}\n")