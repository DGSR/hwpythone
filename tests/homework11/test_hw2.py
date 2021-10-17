from homework11.hw2 import Order


def morning_discount(order):
    return int(order.price * 0.25)


def elder_discount(order):
    return int(order.price * 0.8 + 10)


def test_Order():
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)
    assert order_1.final_price() == 75
    assert order_2.final_price() == 10
