from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator
from email_validator import validate_email, EmailNotValidError


class Customer(BaseModel):
    """Represents a customer.

    Args:
        id (int): The unique identifier of the customer.
        name (str): The name of the customer.
        email (EmailStr): The email address of the customer.
        address (str, optional): The address of the customer.
        hash_credit_card (str): The hash of the customer's credit card.
        is_active (bool, optional): Indicates if the customer is active.
        created_at (datetime): The timestamp when the customer was created.
        updated_at (datetime): The timestamp when the customer was last updated.

    Methods:
        validate_email(value): Validates the format of the email address.

    Attributes:
        Config (class): Configuration options for the customer schema.
    """
    id: int
    name: str
    email: EmailStr = EmailStr(...)  # Ensure valid email format
    address: Optional[str] = None
    hash_credit_card: str  # Consider security best practices for storing sensitive data
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    @field_validator("email")
    def validate_email(cls, value):
        """Validates the format of the email address.

        Args:
            value (str): The email address to be validated.

        Raises:
            ValueError: If the email address is invalid.

        Returns:
            str: The normalized email address.
        """
        try:
            emailinfo = validate_email(value, check_deliverability=False)
            email = emailinfo.normalized
            return email
        except EmailNotValidError as e:
            print(str(e))
            raise ValueError("Invalid email format") from e

    class Config:
        orm_mode = True


class CreateCustomer(Customer):
    """Represents a customer creation request.

    Args:
        name (str): The name of the customer.
        email (EmailStr): The email address of the customer.
        address (str, optional): The address of the customer.

    Attributes:
        Config (class): Configuration options for the customer creation schema.
    """
    name: str
    email: EmailStr
    address: Optional[str] = None

    class Config:
        orm_mode = True


class UpdateCustomer(Customer):
    """Represents a customer update request.

    Args:
        name (str, optional): The updated name of the customer.
        email (EmailStr, optional): The updated email address of the customer.
        address (str, optional): The updated address of the customer.
        is_active (bool, optional): The updated active status of the customer.

    Attributes:
        Config (class): Configuration options for the customer update schema.
    """
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True
