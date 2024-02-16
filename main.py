from fastapi import FastAPI
from src.routes.customer import router as customer_router
from src.routes.merchant import router as merchant_router
from src.routes.transaction import router as transaction_router
from src.routes.auth import router as auth_router
from src.routes.root import router as root_router
from src.utils.audit import audit_log_middleware

app = FastAPI(
    title="Payment Gateway API",
    description="This is a simple payment gateway API.",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc"
)


app.middleware("http")(audit_log_middleware)

app.include_router(auth_router)
app.include_router(root_router)
app.include_router(customer_router)
app.include_router(merchant_router)
app.include_router(transaction_router)




