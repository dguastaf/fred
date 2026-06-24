from fastapi import FastAPI

from app.routers import calendar

app = FastAPI(title="Fred", version="0.1.0")

app.include_router(calendar.router, prefix="/calendar", tags=["calendar"])


@app.get("/health")
async def health():
    return {"status": "ok"}
