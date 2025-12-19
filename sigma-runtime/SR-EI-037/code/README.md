# SIGMA Runtime v0.3.7

Cognitive Attractor Architecture for LLM Identity Stabilization

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. Run Tests

**Interactive mode:**
```bash
python3 sigma_test_runner_52_james.py terminal
```

**Benchmark (30/110/200 cycles):**
```bash
python3 extended_benchmark_52_james.py 110
```

**Test scenario:**
```bash
python3 sigma_test_runner_52_james.py scenario 110
```

---

## Files

| File | Purpose |
|------|---------|
| `sigma_runtime_v0_3_7_james.py` | Core SIGMA Runtime engine |
| `extended_benchmark_52_james.py` | Baseline vs SIGMA comparison |
| `sigma_test_runner_52_james.py` | Interactive testing tool |
| `test_scenario_200.md` | 200-cycle test protocol |
| `identity_james_01.txt` | Identity profile (James) |

---

## Usage Examples

### Run 110-cycle benchmark:
```bash
python3 extended_benchmark_52_james.py 110
```

**Output:**  
`./benchmark_results/sigma_james_YYYYMMDD-HHMMSS.md`  
`./benchmark_results/baseline_james_YYYYMMDD-HHMMSS.md`  
`./benchmark_report_james_YYYYMMDD-HHMMSS.md`

### Interactive terminal:
```bash
python3 sigma_test_runner_52_james.py terminal
```

**Commands:**
- Type questions normally
- `state` - show SIGMA internal state
- `exit` - quit and save session

### Custom test scenario:
```bash
python3 sigma_test_runner_52_james.py scenario 30
```

---

## Requirements

- Python 3.10+
- OpenAI API key (GPT-5.2 recommended)
- ~2GB RAM for embedding model

---

## Results

**Benchmark output:** `./benchmark_results/report_james_*.md`  
**Test logs:** `./test_results/test_*.json`  

---

## Quick Tips

✅ Start with 30 cycles to test setup  
✅ Use 110 cycles for standard validation  
✅ Use 200 cycles for comprehensive testing **(memory testing blocks is not supporing in this version)**  
✅ Check `./benchark_results/` for raw data and reports  
✅ Terminal mode is NOT saving sessions on exit

---

**Documentation:** See `SIGMA_Runtime_0_3_7_CVR.md`  
**Support:** Check test scenario comments in `test_scenario_200.md`
