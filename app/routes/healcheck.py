from fastapi import APIRouter
from fastapi.responses import JSONResponse

healcheck_router = APIRouter()

@healcheck_router.get("/", tags=["Health Check"])
def healcheck():
    return JSONResponse(status_code=200, content="OK")
