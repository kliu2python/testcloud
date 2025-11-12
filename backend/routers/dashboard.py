from fastapi import APIRouter

router = APIRouter()

# Fake VM Data (Future: PostgreSQL)
fake_vms = [
    {
        "name": "FGT-VM-7.0.12",
        "platform": "FortiGate",
        "version": "7.0.12",
        "priority": "P1",
        "result": "Pass",
        "failures": 0
    },
    {
        "name": "FAC-VM-6.5.3",
        "platform": "FortiAuthenticator",
        "version": "6.5.3",
        "priority": "P2",
        "result": "Fail",
        "failures": 3
    }
]

@router.get("/vms")
async def vms():
    return {"vms": fake_vms}
