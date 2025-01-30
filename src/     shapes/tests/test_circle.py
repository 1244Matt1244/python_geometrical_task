from shapes.circle import Circle  # Relative import works now
import pytest

def test_circle_area():
    assert Circle(5).area() == 3.141592653589793 * 25

def test_negative_radius():
    with pytest.raises(ValueError):
        Circle(-2)
