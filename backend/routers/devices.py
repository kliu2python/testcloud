from fastapi import APIRouter, HTTPException
import httpx
import os

router = APIRouter()

MCLOUD_API_BASE = os.getenv("MCLOUD_API_BASE")
MCLOUD_TOKEN = os.getenv("MCLOUD_TOKEN")

@router.get("/list")
async def list_devices():
    headers = {"Authorization": f"Bearer {MCLOUD_TOKEN}"}
    url = f"{MCLOUD_API_BASE}/devices"

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            res = await client.get(url, headers=headers)
            res.raise_for_status()
            return {"devices": res.json()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MCloud error: {e}")
