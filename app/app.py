from typing import Optional

from fastapi import FastAPI

from app.investing import get_crypto_portfolio


app = FastAPI()

@app.get("/")
def read_root():
    return {}

@app.get("/portfolio")
def get_portfolio_status():
    return get_crypto_portfolio()