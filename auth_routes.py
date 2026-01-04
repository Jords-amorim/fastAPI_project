from models import User
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException

from dependencies import catch_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/", status_code=HTTPStatus.OK)
async def authentication():
    """Default route authentication."""
    return {"message": "Authentication successful"}


@auth_router.post("/register_user")
async def register_user(
    user: UserSchema, 
    session: Session = Depends(catch_session)
):
    """Register a new user."""
    usuario = session.query(User).filter(User.email == user.email).first()
    if usuario:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="User already exists")
    else:
        hashed_password = bcrypt_context.hash(user.password)
        new_user = User(
            name=user.name, 
            email=user.email, 
            password=hashed_password, 
            admin=user.admin, 
            active=user.active
        )
        session.add(new_user)
        session.commit() 
    return {"message": "User registered successfully", "user_email": new_user.email}