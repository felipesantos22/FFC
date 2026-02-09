from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.user_repository import UserRepository
from models.user_model import User
from schemas.user_schema import UserCreate, UserUpdate
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, db: Session, user_create: UserCreate) -> User:
        data = user_create.model_dump()
        data["password"] = password_hash.hash(data["password"])
        user = User(**data)
        return self.repository.create(db, user)

    def list_users(self, db: Session):
        return self.repository.find_all(db)

    def list_user_by_id(self, db: Session, user_id: int):
        return self.repository.find_by_id(db, user_id)

    def update_user(self, db: Session, user_id: int, user_update: UserUpdate):
        user = self.repository.find_by_id(db, user_id)
        return self.repository.update_user(db, user, user_update.user_name, user_update.email, user_update.password)

    def delete_user(self, db: Session, user_id: int):
        return self.repository.delete_user(db, user_id)

