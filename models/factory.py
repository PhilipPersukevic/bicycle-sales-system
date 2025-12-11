from models.bicycle_types import (
    DownhillBike, Ebike, EnduroBike,
    TrailBike, XCBike, GravelBike
)

class BicycleFactory:
    @staticmethod
    def create_bicycle(bike_type, year, model, color, frame_size, wheel_size, number_of_gears, price):
        bike_type = bike_type.lower()

        types = {
            "downhill": DownhillBike,
            "ebike": Ebike,
            "enduro": EnduroBike,
            "trail": TrailBike,
            "xc": XCBike,
            "gravel": GravelBike
        }

        if bike_type not in types:
            raise ValueError("Unknown bicycle type.")

        return types[bike_type](year, model, color, frame_size, wheel_size, number_of_gears, price)
