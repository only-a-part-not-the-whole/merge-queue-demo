from shop.pricing import apply_discount


def bulk_price(unit_price: float, qty: int) -> float:
    """10% off orders of 10 or more items."""
    total = unit_price * qty
    return apply_discount(total, 10) if qty >= 10 else round(total, 2)
