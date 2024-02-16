from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.db.connection import Base


class AuditLogModel(Base):
    """Represents an audit log entry.

    Args:
        id (int): The unique identifier of the audit log entry.
        user_id (int, optional): The ID of the user associated with the activity.
        activity_type (str): The type of activity performed.
        bearer_token (str, optional): The bearer token used for authentication.
        ip_address (str, optional): The IP address of the user.
        path (str): The path of the activity.
        timestamp (datetime, optional): The timestamp of the activity. Defaults to the current datetime.

    Attributes:
        __tablename__ (str): The name of the database table.
    """
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    activity_type = Column(String, nullable=False)
    bearer_token = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    path = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now())
