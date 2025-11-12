from prometheus_client import Counter, Gauge

test_jobs_total = Counter(
    "test_jobs_total",
    "Total number of test jobs started",
    ["status", "image"]
)

test_jobs_running = Gauge(
    "test_jobs_running",
    "Current running test jobs",
)
