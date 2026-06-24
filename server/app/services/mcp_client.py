from app.config import settings

MCP_SERVER_URL = settings.mcp_server_url


async def send_to_mcp(payload: dict) -> dict:
    raise NotImplementedError("MCP client integration not yet implemented")
