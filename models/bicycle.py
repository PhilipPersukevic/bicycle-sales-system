from abc import ABC, abstractmethod

class Bicycle(ABC):
    def __init__(self, year, model, color, frame_size, wheel_size, number_of_gears, price):
        self._year = year
        self._model = model
        self._color = color
        self._frame_size = frame_size
        self._wheel_size = wheel_size
        self._number_of_gears = number_of_gears
        self._price = price

    @property
    def year(self): return self._year
    @property
    def model(self): return self._model
    @property
    def color(self): return self._color
    @property
    def frame_size(self): return self._frame_size
    @property
    def wheel_size(self): return self._wheel_size
    @property
    def number_of_gears(self): return self._number_of_gears
    @property
    def price(self): return self._price

    @abstractmethod
    def display_info(self):
        pass