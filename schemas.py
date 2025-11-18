from pydantic import BaseModel


class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float

class OrderListResponse(BaseModel):
    orders: list[Order]

