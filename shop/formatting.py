def format_price(price: float, currency: str = "£") -> str:
    """Render a price for display, e.g. £12.50."""
    return f"{currency}{price:,.2f}"
