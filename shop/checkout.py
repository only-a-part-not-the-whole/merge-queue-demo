from shop.pricing import add_vat, apply_discount


def checkout_total(prices: list[float], discount_percent: float = 0) -> float:
    """Sum the basket, apply a discount, then add VAT."""
    subtotal = apply_discount(sum(prices), discount_percent)
    return add_vat(subtotal)
