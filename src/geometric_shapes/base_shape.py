from abc import ABC, abstractmethod

class BaseShape2D(ABC):
    """Abstract base class for 2D shapes"""
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class BaseShape3D(ABC):
    """Abstract base class for 3D shapes"""
    @abstractmethod
    def surface_area(self) -> float:
        pass
    
    @abstractmethod
    def volume(self) -> float:
        pass
