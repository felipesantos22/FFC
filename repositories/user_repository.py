from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from models.user_model import User


class UserRepository:

    def create(self, db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def find_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

    def find_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def update_user(self, db: Session, user: User, user_name: str, email: str, password: str):
        user.user_name = user_name
        user.email = email
        user.password = password
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        db.delete(user)
        db.commit()
        return user
