from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TokenBase(BaseModel):
    """Base schema for a token.

    Attributes:
        access_token (str): The access token value.
        token_type (str): The type of the token.
    """
    access_token: str
    token_type: str


class TokenResponse(TokenBase):
    """Schema for a token response.

    Attributes:
        created_at (datetime): The timestamp when the token was created.
        updated_at (Optional[datetime], optional): The timestamp when the token was last updated.
            Defaults to None.

    Config:
        orm_mode (bool): Enables ORM mode for the schema.
    """
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
