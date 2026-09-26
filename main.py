import os
import sys
import time
import json
import requests

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def run_qwengram_inference(prompt, system_prompt="You are Qwengram-0.8B, an ultra-fast LLM enhanced with n-gram memory transfer. Keep answers brief (1-2 sentences).", model_name="qwengram-0.8b"):
    """
    Directly query the local Qwengram-0.8B model via Ollama API without local mock fallbacks.
    """
    ollama_url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9
        }
    }
    
    start_time = time.time()
    try:
        response = requests.post(ollama_url, json=payload, timeout=10)
        elapsed_time = round((time.time() - start_time) * 1000, 2)
        if response.status_code == 200:
            data = response.json()
            eval_count = data.get("eval_count", 40)
            tokens_per_sec = round((eval_count / max(elapsed_time / 1000.0, 0.001)), 2)
            return {
                "status": "success",
                "prompt": prompt,
                "output": data.get("response", "").strip(),
                "eval_count": eval_count,
                "duration_ms": elapsed_time,
                "tokens_per_sec": tokens_per_sec
            }
        else:
            raise RuntimeError(f"Ollama server returned status code {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            "Could not connect to Ollama at http://localhost:11434. "
            "Please ensure Ollama is running (`ollama serve`) and the model is created (`ollama create qwengram-0.8b -f Modelfile`)."
        ) from e


def main():
    print("=" * 60)
    print(" 🧠 Qwengram-0.8B: 5 Brief Test Benchmarks")
    print("=" * 60)
    
    test_prompts = [
        "Explain N-Gram memory in 1 short sentence.",
        "Why is Qwengram-0.8B ideal for mobile edge devices?",
        "Summarize the benefit of 5.05% lower validation perplexity.",
        "Give a 1-line Python code snippet to read a text file.",
        "What is the main advantage of local GGUF models?"
    ]
    
    results = []
    for idx, prompt in enumerate(test_prompts, 1):
        print(f"\n[+] Test {idx}/5: '{prompt}'")
        try:
            res = run_qwengram_inference(prompt)
            results.append(res)
            print(f"    - Output: {res['output']}")
            print(f"    - Time: {res['duration_ms']} ms | Speed: {res['tokens_per_sec']} t/s")
        except Exception as err:
            print(f"    [!] Test failed: {err}")
            sys.exit(1)
            
    # Calculate performance averages
    avg_duration = round(sum(r['duration_ms'] for r in results) / len(results), 2)
    avg_speed = round(sum(r['tokens_per_sec'] for r in results) / len(results), 2)
    
    # Save output report focused strictly on outputs and generation times
    os.makedirs("outputs", exist_ok=True)
    output_file_path = os.path.join("outputs", "outputs.md")
    
    markdown_lines = [
        "# 🧠 Qwengram 0.8B Test Performance Report",
        "",
        "## ⚡ Speed & Latency Summary",
        "| Metric | Value |",
        "| :--- | :--- |",
        f"| **Total Prompts Executed** | {len(results)} |",
        f"| **Average Response Time** | {avg_duration} ms |",
        f"| **Average Generation Speed** | {avg_speed} tokens/sec |",
        "",
        "## 🎯 5 Brief Test Outputs",
        ""
    ]
    
    for idx, r in enumerate(results, 1):
        markdown_lines.extend([
            f"### Test {idx}: {r['prompt']}",
            f"- **Model Output:** {r['output']}",
            f"- **Generation Time:** `{r['duration_ms']} ms` | **Speed:** `{r['tokens_per_sec']} tokens/sec`",
            ""
        ])
        
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))
        
    print(f"\n[+] Output report successfully written to: {output_file_path}")


if __name__ == "__main__":
    main()
