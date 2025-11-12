import itertools
import os
import httpx

# 可以将来改成从 DB / 配置表读取
RUNNERS = [
    {"name": "runner-node-1", "base_url": os.getenv("RUNNER1_URL", "http://runner-node-1:9000")},
    # 以后再加:
    # {"name": "runner-node-2", "base_url": "http://runner-node-2:9000"},
]

_cycle = itertools.cycle(RUNNERS)

async def pick_runner() -> dict:
    # TODO: 可以改成根据当前 load / 标签 选择
    return next(_cycle)

async def start_job_on_runner(image: str, env: dict | None = None, cmd: list[str] | None = None):
    runner = await pick_runner()
    async with httpx.AsyncClient(timeout=30) as client:
        res = await client.post(
            f"{runner['base_url']}/internal/run",
            json={"image": image, "env": env, "cmd": cmd},
        )
        res.raise_for_status()
        data = res.json()
        return {"runner": runner["name"], "container_id": data["container_id"]}
