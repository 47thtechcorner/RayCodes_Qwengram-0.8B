<div align="center">
  <a href="https://youtu.be/15bFPswd3AA">
    <img src="https://img.youtube.com/vi/15bFPswd3AA/0.jpg" alt="Qwen 3.8 Memory Hack: This 0.8B AI Steals a 51B Brain Locally! (Qwengram Setup)">
  </a>
  <h3>📺 <a href="https://youtu.be/15bFPswd3AA">Watch the full tutorial on YouTube</a></h3>
</div>

# 🧠 Qwengram 0.8B N-Gram Memory LLM

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Model Size](https://img.shields.io/badge/Model--Size-0.8B--Parameters-green.svg)](https://huggingface.co/Ninnix96/Qwengram-0.8B)
[![GGUF Format](https://img.shields.io/badge/GGUF-Q8__0--1.06GB-orange.svg)](https://huggingface.co/Ninnix96/Qwengram-0.8B)
[![Perplexity](https://img.shields.io/badge/Validation-5.05%25--Lower--Perplexity-purple.svg)](https://reddit.com/r/LocalLLaMA)

Qwengram 0.8B transfers recall memory patterns from Qwen3.8 Flash-Next into a lightweight 0.8B base model, lowering text generation errors by 5.05%. This repository provides an end-to-end Python engine to execute local prompts and automatically save dynamic reports.

---

## ⚡ 3-Step Execution Workflow

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Text prompt or file query | Qwengram 0.8B N-Gram recall processing | Dynamic output written to `outputs/outputs.md` |

---

## 🛠️ Quick Setup & Installation

Run this single PowerShell command to install required libraries and download the GGUF model checkpoint:

```powershell
pip install requests urllib3 huggingface_hub; hf download Ninnix96/Qwengram-0.8B QwenGram-0.8B-Q8_0.gguf --local-dir models/
```

### ⚙️ Register Model in Ollama (Optional)

To serve Qwengram 0.8B locally via Ollama, create the local model image:

```powershell
ollama create qwengram-0.8b -f Modelfile
```

---

## 🚀 How to Run

Execute the main application script:

```powershell
python main.py
```

The model will process your prompt and output performance metrics directly into `outputs/outputs.md`.

---

## 📂 Repository Layout

```
Qwengram-0.8B/
├── Modelfile
├── requirements.txt
├── main.py
└── README.md
```

---

## 🎯 5 Real-World Use Cases

1. **Offline Edge Devices**: Run smart voice or text agents on Raspberry Pi, single-board hardware, or laptops without internet.
2. **Instant Text Summarization**: Condense long documents and tech articles into clean bullet points with zero delay.
3. **Terminal Auto-Completion**: Predict CLI commands and developer shell scripts on low-power devices.
4. **Local File Extraction**: Parse sensitive JSON, CSV, or text files locally without sending data to public clouds.
5. **Lightweight NPC Dialogue**: Generate non-player character responses in local game projects without slowing GPU graphics.

---

## 🔮 5 Planned Future Features

1. **Quantization Variants**: Add support for Q4_K_M and FP16 model variants inside `models/`.
2. **Interactive CLI Loop**: Add an interactive chat interface for real-time terminal conversation.
3. **Multi-Model Benchmark**: Compare token speed and memory usage across multiple small LLMs dynamically.
4. **Local Web Dashboard**: Build a lightweight browser viewer for viewing real-time memory hit stats.
5. **Context Window Expansion**: Support extended 8k context lengths for large log analysis.

---

## 🔑 Keywords & Search Tags

`Qwengram 0.8B`, `Qwen 3.5 0.8B`, `N-Gram Memory Transfer`, `Ollama GGUF Setup`, `Local LLM Edge Execution`, `Tiny LLM Benchmark`, `Offline AI Model`, `Raspberry Pi AI Engine`
