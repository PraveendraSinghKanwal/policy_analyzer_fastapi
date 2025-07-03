from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger

async def handle_upload_errors(request: Request, exc: HTTPException):
    logger.error(f"Error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail}) 