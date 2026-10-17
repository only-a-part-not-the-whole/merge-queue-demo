from shop.pricing import add_tax, apply_discount


def checkout_total(prices: list[float], discount_percent: float = 0) -> float:
    """Sum the basket, apply a discount, then add tax."""
    subtotal = apply_discount(sum(prices), discount_percent)
    return add_tax(subtotal)
