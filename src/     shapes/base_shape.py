from abc import ABC, abstractmethod
import math

class BaseShape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class BaseShape3D(ABC):
    @abstractmethod
    def surface_area(self) -> float:
        pass
    
    @abstractmethod
    def volume(self) -> float:
        pass
