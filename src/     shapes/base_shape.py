from abc import ABC, abstractmethod
from typing import Tuple

class GeometricShape(ABC):
    def __init__(self, name: str):
        self.name = name
        self._validate_positive_values()
        
    @abstractmethod
    def _validate_positive_values(self):
        """Validate all shape parameters are positive"""
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @property
    def metadata(self) -> Tuple[str, dict]:
        return (self.name, {
            'area': self.area(),
            'perimeter': self.perimeter()

class BaseShape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter()")
        })
