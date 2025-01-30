import math
from .base_shape import BaseShape2D

class Circle(BaseShape2D):
    """Represents a 2D circle with radius-based calculations"""
    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Calculate the circle's area"""
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        """Calculate the circle's circumference"""
        return 2 * math.pi * self.radius
