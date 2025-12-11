from .bicycle import Bicycle

class DownhillBike(Bicycle):
    def display_info(self):
        return f"Downhill Bike - {self.model}, €{self.price}"

class Ebike(Bicycle):
    def display_info(self):
        return f"Ebike - {self.model}, €{self.price}"

class EnduroBike(Bicycle):
    def display_info(self):
        return f"Enduro Bike - {self.model}, €{self.price}"

class TrailBike(Bicycle):
    def display_info(self):
        return f"Trail Bike - {self.model}, €{self.price}"

class XCBike(Bicycle):
    def display_info(self):
        return f"XC Bike - {self.model}, €{self.price}"

class GravelBike(Bicycle):
    def display_info(self):
        return f"Gravel Bike - {self.model}, €{self.price}"