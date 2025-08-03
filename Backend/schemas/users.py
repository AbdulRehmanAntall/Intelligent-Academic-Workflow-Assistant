from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Shared properties for User
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, description="Username must be between 3 and 30 characters")
    email: EmailStr = Field(..., description="Must be a valid email address")
    bio: Optional[str] = Field(default="", max_length=300, description="Optional short user bio")
    profile_picture: Optional[str] = Field(default="default.jpg", description="Path or URL to the profile picture")


# Properties to receive on user creation
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100, description="Password must be 6-100 characters long")


# Properties to return to client
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# Properties stored in DB (e.g. for internal use)
class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True
