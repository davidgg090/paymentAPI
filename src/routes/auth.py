import os
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from starlette import status
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

from src.db.connection import SessionLocal
from src.db.schemas.user import UserResponse, UserCreate, UserUpdate
from src.db.schemas.token import TokenResponse
from src.db.models.user import User as UserModel, User
from src.db.models.token import Token as TokenModel

load_dotenv()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/api/v1",
    tags=["auth"],
    responses={
        201: {"description": "Created"},
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
        400: {"description": "Bad Request"}
    },
    dependencies=[Depends(get_db)],
)

SECRET_KEY = os.getenv("SECRET_KEY") or "thisisavery"  # change this to a more secure key
ALGORITHM = os.getenv("ALGORITHM") or "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 720  # 12 hours

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username: str, password: str, db: Session):
    """Authenticate a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        db (Session): The database session.

    Returns:
        Union[UserModel, bool]: The authenticated user if successful, False otherwise.
    """
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(data: dict):
    """Create an access token.

    Args:
        data (dict): The data to encode in the token.

    Returns:
        str: The access token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        return {"username": username, "id": user_id}
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e


@router.post("/auth", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user.

    Args:
        user (UserCreate): The user to create.
    Returns:
        UserResponse: The created user.
    """
    try:
        db_user = UserModel(
            username=user.username,
            password=bcrypt_context.hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.put("/auth/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate,
                      current_user: User = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    """Update a user.

    Args:
        user_id (int): The user id.
        user (UserUpdate): The user data to update.
    Returns:
        UserResponse: The updated user.
    """
    try:
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.username = user.username
        db_user.password = bcrypt_context.hash(user.password)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()


@router.get("/auth/me", response_model=UserResponse)
async def user_me(
        current_user: Annotated[dict, Depends(get_current_user)],
        db: Session = Depends(get_db)):
    if (
            user := db.query(UserModel)
                    .filter(UserModel.id == current_user["id"])
                    .first()
    ):
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/token", response_model=TokenResponse)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login to get an access token.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data.
    Returns:
        TokenResponse: The access token.
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": user.username, "id": user.id})
    try:
        db_token = TokenModel(
            access_token=token,
            token_type="bearer",
            user_id=user.id
        )
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
        return db_token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()
