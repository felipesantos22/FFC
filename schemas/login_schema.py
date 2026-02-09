from pydantic import BaseModel, field_validator


class LoginRequest(BaseModel):
    email: str
    password: str

    # @field_validator("email")
    # @classmethod
    # def email_not_empty(cls, value: str):
    #     if not value or not value.strip():
    #         raise ValueError("All fields must be filled")
    #     return value
    #
    # @field_validator("password")
    # @classmethod
    # def password_not_empty(cls, value: str):
    #     if not value or not value.strip():
    #         raise ValueError("All fields must be filled")
    #     return value
