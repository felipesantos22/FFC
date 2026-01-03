from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.user_repository import UserRepository
from models.user_model import User
from schemas.user_schema import UserCreate, UserUpdate


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, db: Session, user_create: UserCreate) -> User:
        user = User(**user_create.model_dump())
        return self.repository.create(db, user)

    def list_users(self, db: Session):
        return self.repository.find_all(db)

    def list_user_by_id(self, db: Session, user_id: int):
        return self.repository.find_by_id(db, user_id)

    def update_user(self, db: Session, user_id: int, user_update: UserUpdate):
        user = self.repository.find_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repository.update_user(db, user, user_update.user_name, user_update.email, user_update.password)

    def delete_user(self, db: Session, user_id: int):
        user = self.repository.find_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repository.delete_user(db, user)
