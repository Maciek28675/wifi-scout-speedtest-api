from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse

import os
from enum import Enum

router = APIRouter(
    prefix="/speedtest",
    tags=["SpeedTest"],
    responses={404: {"description": "Not found"}},
)

class FileSize(int, Enum):
    mini = 1
    small = 10
    large = 25


@router.get(
    "/download/{file_size_mb}",
    summary="Download a file from the server",
    description="This endpoint is used for testing download speed of a file with given size."
)
async def download(file_size_mb: FileSize):

    file_path = f'app/static/files/{file_size_mb.value}MB.bin'

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File size {file_size_mb.value} not available")
    
    headers = {
        "Content-Disposition": f"attachment; filename=download_{file_size_mb}MB.bin",
        "Content-Length": str(file_size_mb * 1000 * 1000),
        "Cache-Control": "no-cache"
    }

    return FileResponse(file_path, media_type="application/octet-stream", headers=headers)


@router.post(
    "/upload/{file_size_mb}",
    summary="Upload a file to the server",
    description="This endpoint is used for testing upload speed of a file with given size"
)
async def upload(file_size_mb: FileSize, request: Request):
    expected_bytes = file_size_mb.value * 1000 * 1000
    received_bytes = 0
    
    content_length = request.headers.get("Content-Length")

    if content_length is None:
        raise HTTPException(411, "Content-Length header is required.")
    
    async for chunk in request.stream():
        received_bytes += len(chunk)

    if received_bytes != expected_bytes:
        raise HTTPException(422, f"Received {received_bytes} bytes but {expected_bytes} bytes were expected")
    
    return JSONResponse(status_code=200, content=f"Received bytes: {received_bytes}")


@router.get("/ping", summary="Test ping")
async def ping():
    return JSONResponse(status_code=200, content="OK!")