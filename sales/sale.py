class Sale:
    def __init__(self, bicycle, quantity):
        self.bicycle = bicycle
        self.quantity = quantity

    def total_price(self):
        return self.bicycle.price * self.quantity