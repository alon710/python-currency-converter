import os
from typing import Union

from fastapi import FastAPI

from currency_helper import base_get_request

app = FastAPI()


@app.get("/currencies")
def currencies():
    return base_get_request(path="/v1/currencies").json()


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
