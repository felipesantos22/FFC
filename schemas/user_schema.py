from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    user_name: str
    email: str
    password: str

class UserDelete(BaseModel):
    user_name: str
    email: str
    password: str

