from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.runners import start_job_on_runner
from services.metrics import test_jobs_total, test_jobs_running

router = APIRouter()

class TestStartRequest(BaseModel):
  image: str = "fortigate-test:latest"
  env: dict | None = None
  cmd: list[str] | None = None

@router.post("/start")
async def start_test(req: TestStartRequest):
    try:
        test_jobs_running.inc()
        result = await start_job_on_runner(req.image, req.env, req.cmd)
        test_jobs_running.dec()
        return {"status": "started", **result}
    except Exception as e:
        test_jobs_total.labels("error", req.image).inc()
        raise HTTPException(status_code=500, detail=str(e))