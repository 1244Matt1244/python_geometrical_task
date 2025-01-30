import math
from abc import ABC, abstractmethod

class BaseShape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Base3DShape(BaseShape):
    @abstractmethod
    def volume(self) -> float:
        pass
