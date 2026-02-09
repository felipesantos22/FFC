from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20),nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

