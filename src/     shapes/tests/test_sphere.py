import pytest
from shapes.sphere import Sphere

def test_sphere_surface_area():
    assert pytest.approx(Sphere(3).surface_area(), rel=1e-3) == 113.097

def test_sphere_volume():
    assert pytest.approx(Sphere(3).volume(), rel=1e-3) == 113.097
