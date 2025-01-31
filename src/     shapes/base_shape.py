from abc import ABC, abstractmethod

class BaseShape2D(ABC):
    @abstractmethod
    def area(self) -> float: ...
    
    @abstractmethod
    def perimeter(self) -> float: ...

class BaseShape3D(ABC):
    @abstractmethod
    def surface_area(self) -> float: ...
    
    @abstractmethod
    def volume(self) -> float: ...
