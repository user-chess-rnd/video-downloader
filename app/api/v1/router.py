from fastapi import FastAPI
from app.api.v1.endpoints import downloads

app = FastAPI() 

app.include_router(downloads.router)

@app.get("/")
async def root():
    return {"OK"}