from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class CustomerBase(BaseModel):
    """Base model for a customer.

    Args:
        name (str): The name of the customer.
        email (EmailStr): The email address of the customer.
        address (str, optional): The address of the customer.
        is_active (bool, optional): Indicates if the customer is active.
    """
    name: str = Field(..., description="The name of the customer.")
    email: EmailStr = Field(..., description="The email address of the customer.")
    address: Optional[str] = Field(None, description="The address of the customer.")
    is_active: Optional[bool] = Field(True, description="Indicates if the customer is active.")


class CustomerCreate(CustomerBase):
    """Represents a customer creation request.

    Args:
        hash_credit_card (str): The hash of the customer's credit card.

    Attributes:
        name (str): The name of the customer.
        email (EmailStr): The email address of the customer.
        address (str, optional): The address of the customer.
        is_active (bool, optional): Indicates if the customer is active.
    """
    hash_credit_card: str = Field(..., description="The hash of the customer's credit card.")


class CustomerUpdate(CustomerBase):
    """Represents a customer update request.

    Args:
        name (str, optional): The updated name of the customer.
        email (EmailStr, optional): The updated email address of the customer.
        address (str, optional): The updated address of the customer.
        is_active (bool, optional): The updated active status of the customer.
        hash_credit_card (str, optional): The updated hash of the customer's credit card.
    """
    name: Optional[str] = Field(None, description="The name of the customer.")
    email: Optional[EmailStr] = Field(None, description="The email address of the customer.")
    address: Optional[str] = Field(None, description="The address of the customer.")
    is_active: Optional[bool] = Field(None, description="Indicates if the customer is active.")
    hash_credit_card: Optional[str] = Field(None, description="The hash of the customer's credit card.")


class Customer(CustomerBase):
    """Represents a customer.

    Args:
        id (int): The unique identifier of the customer.
        created_at (datetime): The timestamp when the customer was created.
        updated_at (datetime, optional): The timestamp when the customer was last updated.

    Attributes:
        Config (class): Configuration options for the customer schema.
    """
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
