from fastapi import FastAPI

from currency_helper import base_get_request

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/currencies")
def currencies():
    res = base_get_request(path="/v1/currencies")
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
