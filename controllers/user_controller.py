from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user_schema import UserCreate, UserUpdate, UserDelete, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
service = UserService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return service.repository.find_all(db)


@router.get("/{user_id}", response_model=UserResponse)
def list_users(user_id: int, db: Session = Depends(get_db)):
    return service.repository.find_by_id(db, user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user)

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User removed"}
