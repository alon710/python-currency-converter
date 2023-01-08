from fastapi import FastAPI, HTTPException

from currency_helper import base_get_request

app = FastAPI()


@app.get("/currencies")
def get_currencies():
    return base_get_request(path="/v1/currencies")["data"]


@app.get("/currency/{currency}")
def get_currency(currency: str):
    currencies = get_currencies()
    if currency in currencies:
        return currencies[currency]
    raise HTTPException(status_code=400, detail="Currency does not exist")


@app.get("/exchange_rate")
def get_exchange_rate(base_currency: str, target_currency: str):
    return base_get_request(
        path="/v1/latest",
        url_params={"base_currency": base_currency, "currencies": [target_currency]},
    )["data"]


@app.get("/convert/")
def convert(base_currency: str, target_currency: str, amount: float) -> dict:
    exchange_rate = get_exchange_rate(
        base_currency=base_currency, target_currency=target_currency
    )
    return {
        "base_currency": base_currency,
        "target_currency": target_currency,
        "value": amount * exchange_rate[target_currency],
        "amount": amount,
    }


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
