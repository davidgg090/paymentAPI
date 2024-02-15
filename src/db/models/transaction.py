from sqlalchemy import DateTime, Column, String, Integer, ForeignKey, Numeric
from datetime import datetime

from sqlalchemy.orm import relationship

from src.db.connection import Base


class Transaction(Base):
    """Represents a transaction.

    Args:
        id (str): The unique identifier of the transaction.
        merchant_id (int): The ID of the merchant associated with the transaction.
        customer_id (int): The ID of the customer associated with the transaction.
        amount (Decimal): The amount of the transaction.
        currency (str): The currency of the transaction.
        state (str): The state of the transaction.
        hash_credit_card (str): The hash of the credit card used in the transaction.
        created_at (datetime): The timestamp when the transaction was created.
        updated_at (datetime): The timestamp when the transaction was last updated.

    Attributes:
        merchant (Merchant): The merchant associated with the transaction.
        customer (Customer): The customer associated with the transaction.
    """
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    merchant_id = Column(Integer, ForeignKey('merchants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), nullable=False)
    state = Column(String, nullable=False, default='pending')
    hash_credit_card = Column(String, nullable=False)
    token = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    merchant = relationship("Merchant")
    customer = relationship("Customer")
