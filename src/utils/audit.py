import logging
from fastapi import Request
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from src.db.connection import SessionLocal
from src.db.models.audit_log import AuditLogModel
from src.db.models.token import Token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def audit_log_middleware(request: Request, call_next):
    db: Session = next(get_db())
    response = await call_next(request)

    user_id = None

    activity_type = request.method
    bearer_token = request.headers.get("Authorization", None)
    if bearer_token:
        bearer_token = bearer_token.split(" ")[1]
        user_id = db.query(Token).filter(Token.access_token == bearer_token).first().user_id

    client_ip = request.client.host
    x_forwarded_for = request.headers.get("x-forwarded-for")

    ip_address = x_forwarded_for or client_ip

    path = request.url.path

    try:
        audit_log = AuditLogModel(
            user_id=user_id,
            activity_type=activity_type,
            bearer_token=bearer_token,
            ip_address=ip_address,
            path=path,
            timestamp=datetime.now(timezone.utc)
        )
        db.add(audit_log)
        db.commit()
    except Exception as e:
        logger.error(f"Error creating audit log: {e}")
        db.rollback()
    finally:
        db.close()

    return response
