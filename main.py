from fastapi import FastAPI, Query

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


@app.get("/exchange_rate")
def get_exchange_rate(base_currency: str, target_currency: str):
    return base_get_request(
        path="/v1/latest",
        url_params={"base_currency": base_currency, "currencies": [target_currency]},
    ).json()["data"]


@app.get("/convert")
def convert(
    query: str = Query(None, base_currency="ILS", amount=0, target_currency="USD")
) -> float:
    pass


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
