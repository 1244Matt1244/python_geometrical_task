import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from shapes.circle import Circle  # ✅ Correct import

class TestCircle:
    def test_valid_circle(self):
        c = Circle(5)
        assert round(c.area(), 2) == 78.54
        assert round(c.perimeter(), 2) == 31.42
        
    def test_invalid_radius(self):
        with pytest.raises(ValueError):
            Circle(-1)
            
    def test_zero_radius(self):
        with pytest.raises(ValueError):
            Circle(0)
