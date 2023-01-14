from dotenv import load_dotenv
from fastapi.testclient import TestClient

from backend.routes.currency import router

client = TestClient(router)

load_dotenv()


def test_currency_list_status_code():
    response = client.get("/currency/list")
    assert response.status_code == 200


def test_specific_currency_value():
    response = client.get("/currency/USD")
    assert response.status_code == 200
    assert response.json() == {
        "symbol": "$",
        "name": "US Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "USD",
        "name_plural": "US dollars",
    }
