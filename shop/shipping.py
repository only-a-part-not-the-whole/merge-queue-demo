def shipping_cost(subtotal: float) -> float:
    """Free shipping over £50, otherwise a flat £4.99."""
    return 0.0 if subtotal >= 50 else 4.99
