import math
from .exceptions import InvalidDimensionError

class Circle:
    """Circle implementation with area and perimeter calculations"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidDimensionError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
