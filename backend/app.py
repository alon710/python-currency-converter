from fastapi import FastAPI
from routes import currency

app = FastAPI()

app.include_router(
    router=currency.router,
)


@app.get("/")
def index():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
