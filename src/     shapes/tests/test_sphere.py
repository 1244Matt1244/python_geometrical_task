# src/shapes/tests/test_sphere.py
def test_sphere_volume():
    sphere = Sphere(3)
    assert sphere.volume() == (4/3) * math.pi * 3**3

def test_negative_radius():
    with pytest.raises(ValueError):
        Sphere(-2)
