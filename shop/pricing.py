"""Tiny pricing module used to demo GitHub merge queues."""


def apply_discount(price: float, percent: float) -> float:
    """Return price reduced by percent (0-100)."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def add_vat(price: float, rate: float = 0.2) -> float:
    """Return price with VAT added at the given rate."""
    return round(price * (1 + rate), 2)
