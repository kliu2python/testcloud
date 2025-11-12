from fastapi import APIRouter, UploadFile
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/list")
async def list_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}

@router.post("/upload")
async def upload_file(file: UploadFile):
    dest = os.path.join(UPLOAD_DIR, file.filename)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"uploaded": file.filename}
