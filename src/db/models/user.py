from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.db.connection import Base


class User(Base):
    """Represents a user in the system.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Attributes:
        id (int): The unique identifier of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
