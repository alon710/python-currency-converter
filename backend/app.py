import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

if __name__ == "__main__":
    from routes import country, currency

    app = FastAPI()

    app.include_router(
        router=currency.router,
    )
    app.include_router(
        router=country.router,
    )

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
