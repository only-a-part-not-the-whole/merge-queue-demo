from shop.formatting import format_price


def receipt_line(name: str, qty: int, unit_price: float) -> str:
    """Render one receipt line, e.g. "2 x Tea  £5.00"."""
    return f"{qty} x {name}  {format_price(qty * unit_price)}"
