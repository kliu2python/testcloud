from fastapi import APIRouter
import httpx
import os

router = APIRouter()

LLM_API_BASE = os.getenv("LLM_API_BASE")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")

@router.post("/analyze")
async def analyze(req: dict):
    prompt = req.get("prompt", "")

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {"Authorization": f"Bearer {LLM_API_KEY}"}

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{LLM_API_BASE}/chat/completions",
            json=payload,
            headers=headers
        )

    return res.json()
