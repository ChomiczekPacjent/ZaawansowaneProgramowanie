def format_price(price: float) -> str:
    return f'{price:.2f} zł'


def calculate_total(prices: list) -> float:
    return sum(prices)
