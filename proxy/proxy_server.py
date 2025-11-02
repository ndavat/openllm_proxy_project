from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx, os

app = FastAPI(title="OpenAI-Compatible Proxy for OpenLLM")

TARGET_API = os.getenv("TARGET_API", "http://localhost:3000")
API_KEY = os.getenv("API_KEY", "local-key-123")

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    auth = request.headers.get("authorization", "")
    if auth != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return await call_next(request)

@app.post("/v1/chat/completions")
async def completions(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    prompt = " ".join([m["content"] for m in messages])
    payload = {"prompt": prompt, "max_new_tokens": 512}

    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TARGET_API}/generate", json=payload)
        data = resp.json()

    return JSONResponse({
        "id": "chatcmpl-local",
        "object": "chat.completion",
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": data.get("text", "")},
            "finish_reason": "stop"
        }]
    })
