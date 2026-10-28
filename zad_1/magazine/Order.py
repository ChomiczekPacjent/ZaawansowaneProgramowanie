from magazine import utils


class Order:
    def __init__(self, products: list) -> None:
        self.products = products

    def total(self) -> float:
        return utils.calculate_total(
            [product.price for product in self.products])

    def __str__(self) -> str:
        return (f'Zamówienie ({len(self.products)} produkty), '
                f'razem {utils.format_price(self.total())}')
