import httpx

from app.config import settings


async def list_events(calendar_id: str = "primary") -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.google_calendar_api_base_url}/calendars/{calendar_id}/events"
        )
        response.raise_for_status()
        return response.json()


async def create_event(calendar_id: str, event_data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.google_calendar_api_base_url}/calendars/{calendar_id}/events",
            json=event_data,
        )
        response.raise_for_status()
        return response.json()
