import math
from ..base_shape import GeometricShape

class Sphere(GeometricShape):
    def __init__(self, radius: float):
        self.radius = radius
        super().__init__("Sphere")
        
    def _validate_positive_values(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
            
    def area(self) -> float:  # Missing 3D surface area
            raise NotImplementedError
        
    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3
        
    def perimeter(self) -> float:
        raise NotImplementedError("Sphere does not have perimeter")
