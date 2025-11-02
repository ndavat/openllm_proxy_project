# OpenLLM Proxy Project 🧠🚀

This repository lets you **run your own Claude-like local LLM agent** using **Mistral 7B** via [OpenLLM](https://github.com/bentoml/OpenLLM) and access it through an **OpenAI-compatible REST API**.

Perfect for integrating with VS Code extensions (like RooCode, KiloCode, or Copilot-style tools), and testable inside **GitHub Codespaces** or **Google Cloud GPU**.

---

## 🧩 Architecture Overview

```
VS Code Extension / REST Client
          │
          ▼
┌─────────────────────────────┐
│  proxy_server.py (FastAPI) │  ← exposes /v1/chat/completions
└─────────────────────────────┘
          │
          ▼
┌─────────────────────────────┐
│   OpenLLM (Mistral 7B)     │  ← runs the local LLM model
└─────────────────────────────┘
```

---

## 🚀 Quick Start (Codespaces or Local GPU)

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/openllm-proxy-project.git
cd openllm-proxy-project
```

### 2️⃣ Build & Run Containers
```bash
docker-compose up --build
```

This will:
- Build and start OpenLLM with Mistral 7B
- Start the FastAPI proxy server on port 8080

---

## 💬 API Usage

Your local model acts like OpenAI’s API!

```bash
curl http://localhost:8080/v1/chat/completions   -H "Authorization: Bearer local-key-123"   -H "Content-Type: application/json"   -d '{"messages":[{"role":"user","content":"Explain async await in C#"}]}'
```

Example Response:
```json
{
  "id": "chatcmpl-local",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {"role": "assistant", "content": "Async/await allows..."},
      "finish_reason": "stop"
    }
  ]
}
```

---

## ⚙️ Files Included

| File | Description |
|------|--------------|
| `Dockerfile` | Builds OpenLLM container for Mistral 7B |
| `docker-compose.yml` | Orchestrates OpenLLM + proxy |
| `proxy/Dockerfile` | Lightweight image for FastAPI proxy |
| `proxy/proxy_server.py` | API gateway mimicking OpenAI format |
| `README.md` | This file |

---

## 🧠 Tech Stack
- [OpenLLM](https://github.com/bentoml/OpenLLM)
- [Mistral 7B Instruct v0.2](https://huggingface.co/mistralai/mistral-7b-instruct-v0.2)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ☁️ Optional: Google Cloud Deployment

If using Google Cloud Vertex AI or Compute Engine:

1. Create a GPU VM (A100 or T4)
2. Clone this repo
3. Run `docker-compose up --build`
4. Expose `8080` using Cloud Run or `ngrok` to access your private API

---

## 🔐 API Key Security

Change the proxy key in `docker-compose.yml`:

```yaml
environment:
  - API_KEY=your-secure-key-here
```

Then use it in clients:
```bash
-H "Authorization: Bearer your-secure-key-here"
```

---

## 📦 License

This project uses **open-source components**. Mistral 7B is licensed under the Apache 2.0 License.

---

## ❤️ Credits

- [Mistral AI](https://mistral.ai/)
- [BentoML / OpenLLM](https://github.com/bentoml/OpenLLM)
- Built by **you** — for open, transparent coding AI!

