from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.connection import SessionLocal
from src.db.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from src.db.operations import (get_customer,
                               create_customer as create,
                               update_customer as update,
                               get_customers,
                               customer_validation
                               )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/api/v1/customer",
    tags=["customers"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
        400: {"description": "Bad Request"}
    },
    dependencies=[Depends(get_db)],
)


@router.get("/", response_model=list[Customer])
async def read_customers(db: Session = Depends(get_db)):
    """Retrieve a list of customers.

    Returns:
        List[Customer]: A list of customer objects.
    """
    return get_customers(db)


@router.get("/{customer_id}")
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    """Retrieve a customer by ID.

    Args:
        customer_id (int): The ID of the customer.
    Raises:
        HTTPException: If the customer is not found or validation fails.

    Returns:
        Customer: The customer object.
    """
    customer = get_customer(db, customer_id)
    validations = customer_validation(customer)
    if validations:
        raise HTTPException(status_code=400, detail=validations)
    return customer


@router.put("/{customer_id}")
async def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    """Update a customer.

    Args:
        customer_id (int): The ID of the customer to be updated.
        customer (CustomerUpdate): The updated customer data.

    Returns:
        Customer: The updated customer object.
    """
    customer_old = get_customer(db, customer_id)
    if not customer_old:
        raise HTTPException(status_code=404, detail="Customer not found")
    return update(db, customer_old, customer)


@router.post("/")
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a new customer.

    Args:
        customer (CustomerCreate): The customer data for creation.

    Returns:
        Customer: The created customer object.
    """
    return create(db, customer)
