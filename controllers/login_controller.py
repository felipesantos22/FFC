from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user_model import User
from schemas.login_schema import LoginRequest
from services.login_service import LoginService
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

router = APIRouter(prefix="/login", tags=["login"])
service = LoginService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    if not data.email or not data.email.strip():
        raise HTTPException(
            status_code=400,
            detail="All fields must be filled"
        )

    if not data.password or not data.password.strip():
        raise HTTPException(
            status_code=400,
            detail="PAll fields must be filled"
        )

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = service.create_access_token(
        payload={"sub": str(user.id)}
    )

    return {
        "token": token,
        "token_type": "bearer"
    }


@router.get("/role")
def verify_auth_token(role: str = Depends(service.verify_token)):
    return {
        "role": "admin",
        "token": role
    }
