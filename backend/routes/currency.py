import os
from urllib.parse import urljoin

import requests
from cachetools import TTLCache
from fastapi import APIRouter, HTTPException

from .cache import cache

router = APIRouter(
    prefix="/currency",
    tags=["currency"],
)


def base_get_request(path: str, url_params: dict = None) -> requests.Response:
    base_url = os.getenv("BASE_URL_CURRENCY")
    headers = {"apikey": os.getenv("API_KEY")}

    endpoint_url = urljoin(base_url, path)
    response = requests.get(url=endpoint_url, headers=headers, params=url_params)
    if response.ok:
        return response.json()

    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/list")
def get_currencies():
    if "currencies" not in cache:
        cache["currencies"] = base_get_request(path="/v1/currencies")["data"]
    return cache["currencies"]


@router.get("/{currency_code}")
def get_currency(currency_code: str):
    currencies = get_currencies()
    if currency_code in currencies:
        if currency_code not in cache:
            cache[currency_code] = currencies[currency_code]
        return cache[currency_code]
    raise HTTPException(status_code=400, detail="Currency does not exist")


@router.get("/exchange_rate")
def get_exchange_rate(base_currency: str, target_currency: str):
    res = base_get_request(
        path="/v1/latest",
        url_params={"base_currency": base_currency, "currencies": [target_currency]},
    )
    value = res["data"][target_currency]
    return {
        "base_currency": base_currency,
        "target_currency": target_currency,
        "value": value,
        "explanation": f"1 {base_currency} is equal to {value} {target_currency}.",
    }


@router.get("/convert")
def convert(base_currency: str, target_currency: str, amount: float) -> dict:
    exchange_rate = get_exchange_rate(
        base_currency=base_currency, target_currency=target_currency
    )
    value = amount * exchange_rate["value"]
    return {
        "base_currency": base_currency,
        "target_currency": target_currency,
        "value": value,
        "amount": amount,
        "explanation": f"{amount} {base_currency} is equal to {value} {target_currency}.",
    }
