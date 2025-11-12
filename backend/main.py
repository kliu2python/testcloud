from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import generate_latest
from services.metrics import test_jobs_total, test_jobs_running

from routers import dashboard, devices, tests, files, ai_analysis

app = FastAPI(title="TestCloud Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(devices.router, prefix="/api/devices", tags=["devices"])
app.include_router(tests.router, prefix="/api/tests", tags=["tests"])
app.include_router(files.router, prefix="/api/files", tags=["files"])
app.include_router(ai_analysis.router, prefix="/api/ai", tags=["ai"])

@app.get("/")
def root():
    return {"status": "ok", "service": "testcloud-backend"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
