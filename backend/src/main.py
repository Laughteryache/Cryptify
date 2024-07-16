from fastapi import FastAPI

from src.crypto.router import router as crypto_router

app = FastAPI(title="Cryptify")


app.include_router(crypto_router)