import pytest
from geometric_shapes.circle import Circle
from shapes.exceptions import InvalidDimensionError

def test_valid_circle():
    c = Circle(5)
    assert c.area() == pytest.approx(78.54, rel=1e-2)
    assert c.perimeter() == pytest.approx(31.4159, rel=1e-4)

def test_invalid_circle():
    with pytest.raises(InvalidDimensionError):
        Circle(-2)
