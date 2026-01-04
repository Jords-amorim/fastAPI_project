from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    admin: Optional[bool] = False
    active: Optional[bool] = True

    class Config:
        # orm_mode = True
        from_attributes = True

class OrderSchema(BaseModel):
    user: int

    class Config:
        from_attributes = True

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    user: int

class OrderListResponse(BaseModel):
    orders: list[Order]

