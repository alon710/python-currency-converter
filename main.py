import os
from typing import Union

from fastapi import FastAPI

from currency_helper import base_get_request

app = FastAPI()


@app.get("/currencies")
def get_currencies():
    return base_get_request(path="/v1/currencies").json()["data"]


@app.get("/currency/{currency}")
def get_currency(currency):
    currencies = get_currencies()
    if currency in currencies:
        return currencies[currency]


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
