import math
from .base_shape import BaseShape


class Sphere(BaseShape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3
