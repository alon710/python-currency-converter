from dotenv import load_dotenv

load_dotenv()


from backend.routes.currency import router
from fastapi.testclient import TestClient

client = TestClient(router)


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
