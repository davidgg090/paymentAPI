from pydantic import BaseModel, condecimal, Field
from typing import Optional
from datetime import datetime


class TransactionBase(BaseModel):
    """Base model for a transaction.

    Args:
        merchant_id (int): The ID of the merchant associated with the transaction.
        customer_id (int): The ID of the customer associated with the transaction.
        amount (Decimal): The amount of the transaction.
        currency (str): The currency of the transaction.
        state (str): The state of the transaction.
        hash_credit_card (str): The hash of the credit card used in the transaction.
    """
    merchant_id: int = Field(..., description="The ID of the merchant associated with the transaction.")
    customer_id: int = Field(..., description="The ID of the customer associated with the transaction.")
    amount: condecimal(max_digits=10, decimal_places=2) = Field(..., description="The amount of the transaction.")
    currency: str = Field(..., max_length=3, description="The currency of the transaction.")
    hash_credit_card: str = Field(..., description="The hash of the credit card used in the transaction.")



class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    """Represents an update request for a transaction.

    Args:
        merchant_id (int, optional): The updated ID of the merchant associated with the transaction.
        customer_id (int, optional): The updated ID of the customer associated with the transaction.
        amount (Decimal, optional): The updated amount of the transaction.
        currency (str, optional): The updated currency of the transaction.
        state (str, optional): The updated state of the transaction.
        hash_credit_card (str, optional): The updated hash of the credit card used in the transaction.
    """
    merchant_id: Optional[int] = Field(None, description="The ID of the merchant associated with the transaction.")
    customer_id: Optional[int] = Field(None, description="The ID of the customer associated with the transaction.")
    amount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(None,
                                                                          description="The amount of the transaction.")
    currency: Optional[str] = Field(None, max_length=3, description="The currency of the transaction.")
    state: Optional[str] = Field(None, description="The state of the transaction.")
    hash_credit_card: Optional[str] = Field(None, description="The hash of the credit card used in the transaction.")


class Transaction(BaseModel):
    """Represents a transaction.

    Args:
        id (int): The unique identifier of the transaction.
        merchant_id (int): The ID of the merchant associated with the transaction.
        customer_id (int): The ID of the customer associated with the transaction.
        amount (Decimal): The amount of the transaction.
        currency (str): The currency of the transaction.
        state (str): The state of the transaction.
        hash_credit_card (str): The hash of the credit card used in the transaction.
        created_at (datetime): The timestamp when the transaction was created.
        updated_at (datetime, optional): The timestamp when the transaction was last updated.

    Attributes:
        Config (class): Configuration options for the transaction schema.
    """
    id: int
    merchant_id: int
    customer_id: int
    amount: condecimal(max_digits=10, decimal_places=2)
    currency: str
    state: str
    hash_credit_card: str
    token: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
