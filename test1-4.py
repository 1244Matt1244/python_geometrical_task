import math

# Function to check if points form a rectangle
def is_rectangle(points):
    x1, y1, x2, y2 = points
    return x1 != x2 and y1 != y2

# Function to check if points form a cuboid
def is_cuboid(points):
    x1, y1, z1, x2, y2, z2 = points
    return x1 != x2 and y1 != y2 and z1 != z2

# Function to check if a point is inside a rectangle
def is_inside_rectangle(rectangle, point):
    x, y = point
    x1, y1, x2, y2 = rectangle
    return x1 <= x <= x2 and y1 <= y <= y2

# Function to calculate the diagonal of a rectangle
def rectangle_diagonal(rectangle):
    x1, y1, x2, y2 = rectangle
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to check if a point is inside a cuboid
def is_inside_cuboid(cuboid, point):
    x, y, z = point
    x1, y1, z1, x2, y2, z2 = cuboid
    return x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2

# Function to calculate the space diagonal of a cuboid
def cuboid_diagonal(cuboid):
    x1, y1, z1, x2, y2, z2 = cuboid
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Test cases
tests = [
    {
        "shape": "rectangle",
        "points": [(0, 0), (5, 5)],
        "x": (2, 2),
        "expected": "Points form a rectangle. Point X is inside the rectangle. The diagonal of the shape is 7.07."
    },
    {
        "shape": "rectangle",
        "points": [(0, 0), (5, 5)],
        "x": (6, 6),
        "expected": "Points form a rectangle. Point X is not inside the rectangle. The diagonal of the shape is 7.07."
    },
    {
        "shape": "cuboid",
        "points": [(0, 0, 0), (5, 3, 1)],
        "x": (2, 1, 0.5),
        "expected": "Points form a cuboid. Point X is inside the cuboid. The space diagonal is 5.92."
    },
    {
        "shape": "cuboid",
        "points": [(0, 0, 0), (5, 3, 1)],
        "x": (6, 4, 2),
        "expected": "Points form a cuboid. Point X is not inside the cuboid. The space diagonal is 5.92."
    }
]

# Run tests
for test in tests:
    if test["shape"] == "rectangle":
        rectangle = (*test["points"][0], *test["points"][1])
        if not is_rectangle(rectangle):
            print(f"Points do not form a rectangle.")
            continue
        is_inside = is_inside_rectangle(rectangle, test["x"])
        diagonal = rectangle_diagonal(rectangle)
    elif test["shape"] == "cuboid":
        cuboid = (*test["points"][0], *test["points"][1])
        if not is_cuboid(cuboid):
            print(f"Points do not form a cuboid.")
            continue
        is_inside = is_inside_cuboid(cuboid, test["x"])
        diagonal = cuboid_diagonal(cuboid)
    print(f"Test: {test['expected']}")
    print(f"Result: {'Points form a ' + test['shape'] + '. Point X is inside the ' + test['shape'] + '.' if is_inside else 'Points form a ' + test['shape'] + '. Point X is not inside the ' + test['shape'] + '.'} The diagonal of the shape is {round(diagonal, 2)}.")

