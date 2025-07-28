"""Fetch rates from openexchangerates with aiohttp."""

from .client import Client
from .exceptions import (
    OpenExchangeRatesAuthError,
    OpenExchangeRatesClientError,
    OpenExchangeRatesError,
)
from .model import Latest

__all__ = [
    "Client",
    "Latest",
    "OpenExchangeRatesAuthError",
    "OpenExchangeRatesClientError",
    "OpenExchangeRatesError",
]
__version__ = "1.0.0-rc.1"
