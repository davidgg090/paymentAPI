import uuid
from typing import List

from fastapi import HTTPException

from src.db.models.customer import Customer as CustomerModel
from src.db.models.merchant import Merchant as MerchantModel
from src.db.models.transaction import Transaction as TransactionModel

from src.db.schemas.transaction import Transaction, TransactionCreate, TransactionUpdate
from src.db.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from src.db.schemas.merchant import Merchant, MerchantCreate, MerchantUpdate
from src.db.connection import SessionLocal
from src.utils.bank import BankUtils


# CREATE

## CUSTOMER

def create_customer(db: SessionLocal, customer: CustomerCreate) -> Customer:
    """Creates a new customer in the database.

    Args:
        db (Session): The database session.
        customer (CustomerCreate): The customer to create.

    Returns:
        Customer: The customer created in the database.
    """
    try:
        db_customer = CustomerModel(**customer.dict())
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()


## MERCHANT

def create_merchant(db: SessionLocal, merchant: MerchantCreate) -> Merchant:
    """Creates a new merchant in the database.

    Args:
        db (Session): The database session.
        merchant (MerchantCreate): The merchant to create.

    Returns:
        Merchant: The merchant created in the database.
    """
    try:
        db_merchant = MerchantModel(**merchant.dict())
        db.add(db_merchant)
        db.commit()
        db.refresh(db_merchant)
        return db_merchant
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()


## TRANSACTION

def create_transaction(db: SessionLocal, transaction: TransactionCreate) -> TransactionModel:
    """Crea una nueva transacción en la base de datos.

    Args:
        db (Session): La sesión de la base de datos.
        transaction (TransactionCreate): La transacción a crear.

    Returns:
        TransactionModel: La transacción creada en la base de datos.
    """
    try:
        transaction_data = transaction.dict()
        transaction_data['token'] = str(uuid.uuid4())
        transaction_data['state'] = 'pending'
        db_transaction = TransactionModel(**transaction_data)

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        return db_transaction
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()


# RETRIEVE


## CUSTOMER

def get_customer(db: SessionLocal, customer_id: int) -> Customer:
    """Retrieves a customer from the database.

    Args:
        db (Session): The database session.
        customer_id (int): The ID of the customer to retrieve.

    Returns:
        Customer: The customer retrieved from the database.
    """
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()


def get_customers(db: SessionLocal, skip: int = 0, limit: int = 10) -> List[Customer]:
    """Retrieves all customers from the database.

    Args:
        db (Session): The database session.
        skip (int): The number of records to skip.
        limit (int): The number of records to retrieve.

    Returns:
        List[Customer]: The list of customers retrieved from the database.
    """
    return db.query(CustomerModel).offset(skip).limit(limit).all()


## MERCHANT

def get_merchant_by_id(db: SessionLocal, merchant_id: int) -> Merchant:
    """Retrieves a merchant from the database.

    Args:
        db (Session): The database session.
        merchant_id (int): The ID of the merchant to retrieve.

    Returns:
        Merchant: The merchant retrieved from the database.
    """
    return db.query(MerchantModel).filter(MerchantModel.id == merchant_id).first()


def get_merchants(db: SessionLocal, skip: int = 0, limit: int = 10) -> List[Merchant]:
    """Retrieves all merchants from the database.

    Args:
        db (Session): The database session.
        skip (int): The number of records to skip.
        limit (int): The number of records to retrieve.

    Returns:
        List[Merchant]: The list of merchants retrieved from the database.
    """
    return db.query(MerchantModel).offset(skip).limit(limit).all()


## TRANSACTION

def get_transaction_by_id(db: SessionLocal, transaction_id: int) -> Transaction:
    """Retrieves a transaction from the database.

    Args:
        db (Session): The database session.
        transaction_id (int): The ID of the transaction to retrieve.

    Returns:
        Transaction: The transaction retrieved from the database.
    """
    return db.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()


def get_transaction_by_token(db: SessionLocal, token: str) -> Transaction:
    """Retrieves a transaction from the database by token.

    Args:
        db (Session): The database session.
        token (str): The token of the transaction to retrieve.

    Returns:
        Transaction: The transaction retrieved from the database.
    """
    return db.query(TransactionModel).filter(TransactionModel.token == token).first()


def get_transactions_by_merchant_id(db: SessionLocal, merchant_id: int) -> List[Transaction]:
    """Retrieves all transactions associated with a merchant.

    Args:
        db (Session): The database session.
        merchant_id (int): The ID of the merchant.

    Returns:
        List[Transaction]: The list of transactions associated with the merchant.
    """
    return db.query(TransactionModel).filter(TransactionModel.merchant_id == merchant_id).all()


def get_transactions_by_customer_id(db: SessionLocal, customer_id: int) -> List[Transaction]:
    """Retrieves all transactions associated with a customer.

    Args:
        db (Session): The database session.
        customer_id (int): The ID of the customer.

    Returns:
        List[Transaction]: The list of transactions associated with the customer.
    """
    return db.query(TransactionModel).filter(TransactionModel.customer_id == customer_id).all()


# UPDATE

## CUSTOMER

def update_customer(db: SessionLocal, customer: Customer, customer_update: CustomerUpdate) -> Customer:
    """Updates a customer in the database.

    Args:
        db (Session): The database session.
        customer (Customer): The customer to update.
        customer_update (CustomerUpdate): The updated customer data.

    Returns:
        Customer: The updated customer.
    """
    customer_update_dict = {k: v for k, v in customer_update.dict().items() if v is not None}

    for field, value in customer_update_dict.items():
        if hasattr(customer, field):
            setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer


## MERCHANT

def update_merchant(db: SessionLocal, merchant: Merchant, merchant_update: MerchantUpdate) -> Merchant:
    """Updates a merchant in the database.

    Args:
        db (Session): The database session.
        merchant (Merchant): The merchant to update.
        merchant_update (MerchantUpdate): The updated merchant data.

    Returns:
        Merchant: The updated merchant.
    """
    merchant_update_dict = {k: v for k, v in merchant_update.dict().items() if v is not None}
    for field, value in merchant_update_dict.items():
        setattr(merchant, field, value)
    db.commit()
    db.refresh(merchant)
    return merchant


## TRANSACTION
def update_transaction(db: SessionLocal, transaction: Transaction,
                       transaction_update: TransactionUpdate) -> Transaction:
    """Updates a transaction in the database.

    Args:
        db (Session): The database session.
        transaction (Transaction): The transaction to update.
        transaction_update (TransactionUpdate): The updated transaction data.

    Returns:
        Transaction: The updated transaction.
    """
    transaction_update_dict = {k: v for k, v in transaction_update.dict().items() if v is not None}
    for field, value in transaction_update_dict.items():
        setattr(transaction, field, value)
    db.commit()
    db.refresh(transaction)
    return transaction


# CUSTOM OPERATIONS

def customer_validation(customer: Customer):
    """Validates a customer.

    Args:
        customer (Customer): The customer to be validated.

    Raises:
        HTTPException: If the customer is not found, not active, or does not have a credit card.
    """
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if not customer.is_active:
        raise HTTPException(status_code=400, detail="Customer is not active")
    if not customer.hash_credit_card:
        raise HTTPException(status_code=400, detail="Customer does not have a credit card")


def merchant_validation(merchant: Merchant):
    """Validates a merchant.

    Args:
        merchant (Merchant): The merchant to be validated.

    Raises:
        HTTPException: If the merchant is not found or not active.
    """
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")
    if not merchant.is_active:
        raise HTTPException(status_code=400, detail="Merchant is not active")


def process_transaction(db: SessionLocal, transaction_token: str, type: str) -> Transaction:
    """
    Process a transaction.

    Args:
        db: The database session.
        transaction_token: The token of the transaction.
        type: The type of the transaction.

    Returns:
        The processed transaction.

    Raises:
        HTTPException: If the transaction is not found, the customer is not found or not active,
            the merchant is not found or not active, or the credit card is invalid.
    """
    transaction = db.query(TransactionModel).filter(TransactionModel.token == transaction_token).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found.")
    if transaction.state != 'pending':
        raise HTTPException(status_code=400, detail="Transaction already processed.")

    customer = get_customer(db, transaction.customer_id)
    merchant = get_merchant_by_id(db, transaction.merchant_id)

    if not customer or not customer.is_active:
        transaction.state = 'failed'
        raise HTTPException(status_code=400, detail="Customer not found or not active.")
    elif not merchant or not merchant.is_active:
        transaction.state = 'failed'
        raise HTTPException(status_code=400, detail="Merchant not found or not active.")
    else:
        if BankUtils.verify_hash_credit_card(transaction.hash_credit_card, customer.hash_credit_card):
            if type == 'capture':
                transaction.state = 'success'
                merchant.amount_account += transaction.amount
            elif type == 'refund':
                transaction.state = 'refunded'
                merchant.amount_account -= transaction.amount
        else:
            raise HTTPException(status_code=400, detail="Invalid credit card.")
    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e

    try:
        db.add(merchant)
        db.commit()
        db.refresh(merchant)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
    finally:
        db.close()
    return transaction
