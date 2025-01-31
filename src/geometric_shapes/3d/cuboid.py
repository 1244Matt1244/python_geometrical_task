# src/shapes/3d/cuboid.py
class Cuboid(Base3DShape):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self) -> float:
        return 2 * (self.length*self.width + self.width*self.height + self.length*self.height)

    def volume(self) -> float:
        return self.length * self.width * self.height
