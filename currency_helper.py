import os
from urllib.parse import urljoin

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
HEADERS = {"apikey": API_KEY}


def base_get_request(path: str, url_params: dict = None) -> requests.Response:
    endpoint_url = urljoin(BASE_URL, path)
    return requests.get(url=endpoint_url, headers=HEADERS)
