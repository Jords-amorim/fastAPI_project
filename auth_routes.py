from models import User
from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends

from dependencies import catch_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/", status_code=HTTPStatus.OK)
async def authentication():
    """Default route authentication."""
    return {"message": "Authentication successful"}


@auth_router.post("/register_user")
async def register_user(email: str, name: str, password: str, session=Depends(catch_session)):
    """Register a new user."""
    usuario = session.query(User).filter(User.email == email).first()
    if usuario:
        return {"message": "User already exists"}
    else:
        hashed_password = bcrypt_context.hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        session.add(new_user)
        session.commit() 
    return {"message": "User registered successfully"}