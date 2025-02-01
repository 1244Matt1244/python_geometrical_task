import math
from .exceptions import InvalidDimensionError

class Sphere:
    """Sphere implementation with surface area and volume calculations"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidDimensionError("Radius must be positive")
        self.radius = radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius**2

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius**3
