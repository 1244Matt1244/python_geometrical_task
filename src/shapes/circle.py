import math
from .base_shape import GeometricShape

class Circle(GeometricShape):
    def __init__(self, radius: float):
        self.radius = radius
        super().__init__("Circle")
        
    def _validate_positive_values(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
            
    def area(self) -> float:
        return math.pi * self.radius ** 2
        
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
        
    def circumference(self) -> float:
        return self.perimeter()
