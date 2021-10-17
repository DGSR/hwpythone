from typing import Callable


class Order:
    """
    class calculates final price with 2 parameters
    price and discount function, which should return integer
    """
    def __init__(self, price: int, discount_func: Callable):
        self.price = price
        self.discount = discount_func

    def final_price(self) -> int:
        return self.price - self.discount(self)
