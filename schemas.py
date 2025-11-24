from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    admin: Optional[bool] = False
    active: Optional[bool] = True

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float

class OrderListResponse(BaseModel):
    orders: list[Order]

