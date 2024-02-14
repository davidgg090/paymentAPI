from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from src.db.connection import Base


class Merchant(Base):
    """Represents a merchant.

    Args:
        id (int): The unique identifier of the merchant.
        name (str): The name of the merchant.
        email (str): The email address of the merchant.
        is_active (bool, optional): Indicates if the merchant is active.
        authentication_key (str): The authentication key of the merchant.
        amount_account (int): The amount in the merchant's account.
        created_at (datetime): The timestamp when the merchant was created.
        updated_at (datetime): The timestamp when the merchant was last updated.
    """
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    amount_account = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)