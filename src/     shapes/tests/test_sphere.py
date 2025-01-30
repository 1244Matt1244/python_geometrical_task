# tests/test_sphere.py
def test_sphere_volume():
    assert Sphere(3).volume() == (4/3) * math.pi * 3**3

def test_invalid_sphere_radius():
    with pytest.raises(ValueError):
        Sphere(-1)
