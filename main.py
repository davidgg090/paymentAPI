from fastapi import FastAPI
from src.routes.customer import router as customer_router

app = FastAPI()

app.include_router(customer_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
