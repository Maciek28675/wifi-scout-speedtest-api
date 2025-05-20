from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import speedtest

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(speedtest.router)
@app.get("/")
async def root():
    return {"message": "Welcome to wifi scout speedtest api"}