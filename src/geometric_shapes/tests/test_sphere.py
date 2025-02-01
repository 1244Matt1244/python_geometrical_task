import pytest
from geometric_shapes.circle import Circle
from shapes.exceptions import InvalidDimensionError

def test_valid_sphere():
    s = Sphere(3)
    assert s.surface_area() == pytest.approx(113.097, rel=1e-3)
    assert s.volume() == pytest.approx(113.097, rel=1e-3)

def test_invalid_sphere():
    with pytest.raises(InvalidDimensionError):
        Sphere(0)
