from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.connection import SessionLocal
from src.db.schemas.transaction import Transaction, TransactionCreate, TransactionUpdate
from src.db.operations import (get_transaction_by_id,
                               create_transaction as create,
                               update_transaction as update,
                               get_transaction_by_token
                               )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/api/v1/transaction",
    tags=["transactions"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
        400: {"description": "Bad Request"}
    },
    dependencies=[Depends(get_db)],
)


@router.get("/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """Retrieve a transaction by ID.

    Args:
        transaction_id (int): The ID of the transaction.
    Raises:
        HTTPException: If the transaction is not found.
    Returns:
        Transaction: The transaction object.
    """
    transaction = get_transaction_by_id(db, transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/token/{token}", response_model=Transaction)
async def read_transaction_by_token(token: str, db: Session = Depends(get_db)):
    """Retrieve a transaction by token.

    Args:
        token (str): The token of the transaction.
    Raises:
        HTTPException: If the transaction is not found.
    Returns:
        Transaction: The transaction object.
    """
    transaction = get_transaction_by_token(db, token)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.post("/", response_model=Transaction)
async def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    """Create a new transaction.

    Args:
        transaction (TransactionCreate): The transaction to create.
    Returns:
        Transaction: The transaction created.
    """
    return create(db, transaction)


@router.put("/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    """Update a transaction.

    Args:
        transaction_id (int): The ID of the transaction to update.
        transaction (TransactionUpdate): The transaction data.
    Raises:
        HTTPException: If the transaction is not found.
    Returns:
        Transaction: The updated transaction.
    """
    db_transaction = get_transaction_by_id(db, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return update(db, db_transaction, transaction)
