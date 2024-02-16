from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.connection import SessionLocal
from src.db.models.user import User
from src.db.schemas.merchant import Merchant, MerchantCreate, MerchantUpdate
from src.db.operations import (get_merchant_by_id,
                               create_merchant as create,
                               update_merchant as update,
                               get_merchants,
                               merchant_validation
                               )
from src.routes.auth import get_current_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/api/v1/merchant",
    tags=["merchants"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
        400: {"description": "Bad Request"}
    },
    dependencies=[Depends(get_db)],
)


@router.get("/", response_model=list[Merchant])
async def read_merchants(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Retrieve a list of merchants.

    Returns:
        List[Merchant]: A list of merchant objects.
    """
    return get_merchants(db)


@router.get("/{merchant_id}")
async def read_merchant(merchant_id: int, current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    """Retrieve a merchant by ID.

    Args:
        merchant_id (int): The ID of the merchant.
    Raises:
        HTTPException: If the merchant is not found or validation fails.

    Returns:
        Merchant: The merchant object.
    """
    merchant = get_merchant_by_id(db, merchant_id)
    validations = merchant_validation(merchant)
    if validations:
        raise HTTPException(status_code=400, detail=validations)

    return merchant


@router.post("/", response_model=Merchant)
async def create_merchant(merchant: MerchantCreate, current_user: User = Depends(get_current_user),
                          db: Session = Depends(get_db)):
    """Create a new merchant.

    Args:
        merchant (MerchantCreate): The merchant data.
    Raises:
        HTTPException: If validation fails.

    Returns:
        Merchant: The merchant object.
    """
    validations = merchant_validation(merchant)
    if validations:
        raise HTTPException(status_code=400, detail=validations)

    return create(db, merchant)


@router.put("/{merchant_id}", response_model=Merchant)
async def update_merchant(merchant_id: int, merchant: MerchantUpdate,
                          current_user: User = Depends(get_current_user),
                          db: Session = Depends(get_db)):
    """Update a merchant.

    Args:
        merchant_id (int): The ID of the merchant to be updated.
        merchant (MerchantUpdate): The updated merchant data.

    Returns:
        Merchant: The updated merchant object.
    """
    merchant_old = get_merchant_by_id(db, merchant_id)
    if not merchant_old:
        raise HTTPException(status_code=404, detail="Merchant not found")
    return update(db, merchant_old, merchant)
