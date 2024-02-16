from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.db.connection import Base


class Token(Base):
    """Represents an access token in the system.

    Attributes:
        id (int): The unique identifier of the token.
        access_token (str): The access token value.
        token_type (str): The type of the token.
        created_at (datetime): The timestamp when the token was created.
        updated_at (datetime): The timestamp when the token was last updated.
        user_id (int): The foreign key referencing the associated user.
        customer (relationship): The relationship to the associated user.
    """
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    access_token = Column(String(255), nullable=False, unique=True)
    token_type = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    customer = relationship("User")
