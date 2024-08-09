"""Provide a base response model."""

try:
    from pydantic.v1 import BaseModel  # type: ignore # pragma: no cover
except ImportError:
    from pydantic import BaseModel  # type: ignore # pragma: no cover


class BaseResponse(BaseModel):
    """Represent a base response."""

    disclaimer: str
    license: str


class BaseRatesResponse(BaseResponse):
    """Represent a base rates response."""

    timestamp: int
    base: str
    rates: dict[str, float]
