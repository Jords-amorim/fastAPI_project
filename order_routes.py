from http import HTTPStatus
from fastapi import APIRouter

from schemas import OrderListResponse

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get(
  "/", 
  status_code=HTTPStatus.OK,
  response_model=OrderListResponse
)
async def list_orders():
    """List all orders."""
    return {"orders": []}