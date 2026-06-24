from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    google_calendar_api_base_url: str = "https://www.googleapis.com/calendar/v3"
    mcp_server_url: str = "http://localhost:3000"

    model_config = {"env_prefix": "FRED_"}


settings = Settings()
