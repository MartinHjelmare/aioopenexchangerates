"""Provide a client for the Open Exchange Rates API."""
from __future__ import annotations

from types import TracebackType
from typing import Any, cast

from aiohttp import ClientSession

BASE_API_ENDPOINT = "https://openexchangerates.org/api/"


class Client:
    """Represent the client for the Open Exchange Rates API."""

    def __init__(self, api_key: str, session: ClientSession | None = None) -> None:
        """Initialize the client."""
        self.api_key = api_key
        self.session = session or ClientSession()

    async def get_latest(
        self, base: str = "USD", symbols: list[str] | None = None
    ) -> dict[str, float]:
        """Get the latest rates for the given base and symbols."""
        url = f"{BASE_API_ENDPOINT}latest.json"
        params = {"app_id": self.api_key, "base": base}
        if symbols:
            params["symbols"] = ",".join(symbols)
        response = await self.session.get(
            url,
            params=params,
        )
        data: dict[str, Any] = await response.json()
        return cast(dict[str, float], data["rates"])

    async def close(self) -> None:
        """Close the client."""
        await self.session.close()

    async def __aenter__(self) -> Client:
        """Enter the context manager."""
        return self

    async def __aexit__(
        self, exc_type: Exception, exc_value: str, traceback: TracebackType
    ) -> None:
        """Exit the context manager."""
        await self.close()
