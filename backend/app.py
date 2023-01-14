from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import country, currency

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=currency.router,
)
app.include_router(
    router=country.router,
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
