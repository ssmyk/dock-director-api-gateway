from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/manager", tags=["container"])


@router.get("/")
async def main():
    return JSONResponse({"result": "SUCCESS"})
