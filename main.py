from fastapi import FastAPI
from src.routes.customer import router as customer_router
from src.routes.merchant import router as merchant_router
from src.routes.transaction import router as transaction_router
from src.routes.root import router as root_router

app = FastAPI()

app.include_router(root_router)
app.include_router(customer_router)
app.include_router(merchant_router)
app.include_router(transaction_router)




