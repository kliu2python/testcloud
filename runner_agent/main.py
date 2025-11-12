import os
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import docker
from prometheus_client import Counter, Gauge, generate_latest

app = FastAPI(title="TestCloud Runner Agent")

RUNNER_NAME = os.getenv("RUNNER_NAME", "runner-unknown")
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

client = docker.from_env()

# Prometheus metrics
jobs_total = Counter(
    "runner_jobs_total",
    "Total jobs handled by this runner",
    ["runner", "status", "image"]
)
jobs_running = Gauge(
    "runner_jobs_running",
    "Current running jobs on this runner",
    ["runner"]
)

class RunRequest(BaseModel):
    image: str
    env: dict | None = None
    cmd: list[str] | None = None

class RunResponse(BaseModel):
    container_id: str

@app.get("/health")
def health():
    return {"status": "ok", "runner": RUNNER_NAME}

@app.get("/metrics")
def metrics():
    return generate_latest()

@app.post("/internal/run", response_model=RunResponse)
def run_container(req: RunRequest):
    try:
        jobs_running.labels(RUNNER_NAME).inc()
        container = client.containers.run(
            req.image,
            command=req.cmd,
            environment=req.env,
            detach=True,
            auto_remove=True,
            name=f"job_{int(time.time())}_{os.urandom(3).hex()}"
        )
        jobs_total.labels(RUNNER_NAME, "started", req.image).inc()
        return RunResponse(container_id=container.short_id)
    except Exception as e:
        jobs_total.labels(RUNNER_NAME, "error", req.image).inc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        jobs_running.labels(RUNNER_NAME).dec()
