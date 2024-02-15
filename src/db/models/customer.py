from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, Boolean

from src.db.connection import Base


class Customer(Base):
    """Represents a customer.

    Args:
        id (int): The unique identifier of the customer.
        name (str): The name of the customer.
        email (str): The email address of the customer.
        address (str, optional): The address of the customer.
        is_active (bool, optional): Indicates if the customer is active.
        created_at (datetime): The timestamp when the customer was created.
        updated_at (datetime): The timestamp when the customer was last updated.
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    address = Column(String, nullable=True)
    hash_credit_card = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)




