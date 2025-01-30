from shapes.circle import Circle  # Relative import
import pytest

def test_valid_circle():
    c = Circle(5)
    assert c.area() == 3.141592653589793 * 5**2

def test_negative_radius():
    with pytest.raises(ValueError):
        Circle(-2)
