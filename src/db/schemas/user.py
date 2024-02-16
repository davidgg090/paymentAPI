from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    """Base schema for a user.

    Args:
        username (str): The username of the user.
    """
    username: str


class UserCreate(UserBase):
    """Schema for creating a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    """
    password: str


class UserResponse(UserBase):
    """Schema for a user response.

    Attributes:
        id (int): The unique identifier of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (Optional[datetime], optional): The timestamp when the user was last updated.
            Defaults to None.

    Config:
        orm_mode (bool): Enables ORM mode for the schema.
    """
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    """Schema for updating a user.

    Attributes:
        username (Optional[str], optional): The updated username of the user.
            Defaults to None.
        password (Optional[str], optional): The updated password of the user.
            Defaults to None.

    Config:
        orm_mode (bool): Enables ORM mode for the schema.
    """
    username: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
