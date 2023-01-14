import os
from urllib.parse import urljoin

import requests
from cachetools import TTLCache
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/country",
    tags=["country"],
)
cache = TTLCache(maxsize=1024, ttl=600)


def base_get_request(path: str, params: dict = None) -> requests.Response:
    base_url = os.getenv("BASE_URL_COUNTRY")
    endpoint_url = urljoin(base_url, path)
    response = requests.get(endpoint_url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/")
def get_country(country_name: str):
    if not country_name in cache:
            cache[country_name] = base_get_request(path=country_name)[0]["currencies"]
    return cache[country_name]
