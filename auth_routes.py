from http import HTTPStatus
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/", status_code=HTTPStatus.OK)
async def authentication():
    """Default route authentication."""
    return {"message": "Authentication successful"}


