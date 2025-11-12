from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.runners import start_job_on_runner
from main import test_jobs_total

router = APIRouter()

class TestStartRequest(BaseModel):
  image: str = "fortigate-test:latest"
  env: dict | None = None
  cmd: list[str] | None = None

@router.post("/start")
async def start_test(req: TestStartRequest):
    try:
        result = await start_job_on_runner(req.image, req.env, req.cmd)
        test_jobs_total.labels("started", req.image).inc()
        return {"status": "started", **result}
    except Exception as e:
        test_jobs_total.labels("error", req.image).inc()
        raise HTTPException(status_code=500, detail=str(e))