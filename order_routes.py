from http import HTTPStatus
from fastapi import APIRouter, Depends

from dependencies import catch_session
from schemas import OrderListResponse, OrderSchema
from sqlalchemy.orm import Session
from models import Order

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get(
  "/", 
  status_code=HTTPStatus.OK,
  response_model=OrderListResponse
)
async def list_orders():
    """List all orders."""
    return {"orders": []}

@order_router.post("/register_order", status_code=HTTPStatus.CREATED)
async def register_order(
    order: OrderSchema,
    session: Session = Depends(catch_session)
):
    """Register a new order."""
    new_order = Order(
        user=order.user
    )
    session.add(new_order)
    session.commit() 
    return {"message": "Order registered successfully", "order_id": new_order.id}