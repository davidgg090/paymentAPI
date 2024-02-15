from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class MerchantBase(BaseModel):
    """Base model for a merchant.

    Args:
        name (str): The name of the merchant.
        email (EmailStr): The email address of the merchant.
        is_active (bool, optional): Indicates if the merchant is active.
        amount_account (int): The amount in the merchant's account.

    Attributes:
        Config (class): Configuration options for the merchant schema.
    """
    name: str = Field(..., description="The name of the merchant.")
    email: EmailStr = Field(..., description="The email address of the merchant.")
    is_active: Optional[bool] = Field(True, description="Indicates if the merchant is active.")
    amount_account: int = Field(..., description="The amount in the merchant's account.", ge=0)


class MerchantCreate(MerchantBase):
    """Represents a merchant creation request.

    Args:
        authentication_key (str): The authentication key of the merchant.

    Attributes:
        name (str): The name of the merchant.
        email (EmailStr): The email address of the merchant.
        is_active (bool, optional): Indicates if the merchant is active.
        amount_account (int): The amount in the merchant's account.

    """
    authentication_key: str = Field(..., description="The authentication key of the merchant.")


class MerchantUpdate(BaseModel):
    """Represents a merchant update request.

    Args:
        name (str, optional): The updated name of the merchant.
        email (EmailStr, optional): The updated email address of the merchant.
        is_active (bool, optional): The updated active status of the merchant.
        amount_account (int, optional): The updated amount in the merchant's account.

    Attributes:
        Config (class): Configuration options for the merchant update schema.
    """
    name: Optional[str] = Field(None, description="The name of the merchant.")
    email: Optional[EmailStr] = Field(None, description="The email address of the merchant.")
    is_active: Optional[bool] = Field(None, description="Indicates if the merchant is active.")
    amount_account: Optional[int] = Field(None, description="The amount in the merchant's account.", ge=0)
    authentication_key: Optional[str] = Field(None, description="The authentication key of the merchant.")


class Merchant(MerchantBase):
    """Represents a merchant.

    Args:
        id (int): The unique identifier of the merchant.
        created_at (datetime): The timestamp when the merchant was created.
        updated_at (datetime, optional): The timestamp when the merchant was last updated.

    Attributes:
        Config (class): Configuration options for the merchant schema.
    """
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
