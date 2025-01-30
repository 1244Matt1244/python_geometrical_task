import math

# Function to check if three points form a rectangle
def is_rectangle(points):
    if len(points) != 3:
        return False  # Must have exactly 3 points

    A, B, C = points
    AB = (B[0] - A[0], B[1] - A[1])  # Vector AB
    BC = (C[0] - B[0], C[1] - B[1])  # Vector BC

    # Perpendicular check using dot product: AB ⋅ BC == 0
    return AB[0] * BC[0] + AB[1] * BC[1] == 0

# Function to check if four points form a cuboid
def is_cuboid(points):
    if len(points) != 4:
        return False  # Must have exactly 4 points

    A, B, C, D = points
    vectors = [(B[i] - A[i], C[i] - A[i], D[i] - A[i]) for i in range(3)]  # Create vectors AB, AC, AD

    # Check if vectors are perpendicular (dot product should be 0)
    return all(sum(a * b for a, b in zip(vectors[i], vectors[j])) == 0 for i in range(3) for j in range(i + 1, 3))

# Function to check if a point is inside a rectangle
def is_inside_rectangle(rectangle, point):
    x, y = point
    x1, y1, x2, y2 = rectangle
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

# Function to check if a point is inside a cuboid
def is_inside_cuboid(cuboid, point):
    x, y, z = point
    x1, y1, z1, x2, y2, z2 = cuboid
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(z1, z2) <= z <= max(z1, z2)

# Function to calculate the diagonal of a rectangle or cuboid
def calculate_diagonal(points):
    return math.dist(points[0], points[-1])

# Validate input data
def validate_input(points, expected_dimensions):
    """Checks if all points have the correct number of dimensions."""
    for point in points:
        if len(point) != expected_dimensions:
            print(f"❌ Error: All points must have {expected_dimensions} dimensions. Found {len(point)}.")
            return False
    return True

# Test cases
tests = [
    {
        "shape": "rectangle",
        "points": [(0, 0), (5, 0), (0, 5)],
        "x": (2, 2),
        "expected": True
    },
    {
        "shape": "rectangle",
        "points": [(0, 0), (5, 0), (0, 5)],
        "x": (6, 6),
        "expected": False
    },
    {
        "shape": "cuboid",
        "points": [(0, 0, 0), (5, 0, 0), (0, 3, 0), (0, 0, 1)],
        "x": (2, 1, 0.5),
        "expected": True
    },
    {
        "shape": "cuboid",
        "points": [(0, 0, 0), (5, 0, 0), (0, 3, 0), (0, 0, 1)],
        "x": (6, 4, 2),
        "expected": False
    }
]

# Run tests
for test in tests:
    if test["shape"] == "rectangle":
        if not validate_input(test["points"], 2):
            continue
        if not is_rectangle(test["points"]):
            print(f"❌ Points do NOT form a rectangle.")
            continue
        is_inside = is_inside_rectangle((*test["points"][0], *test["points"][1]), test["x"])
        diagonal = calculate_diagonal(test["points"])

    elif test["shape"] == "cuboid":
        if not validate_input(test["points"], 3):
            continue
        if not is_cuboid(test["points"]):
            print(f"❌ Points do NOT form a cuboid.")
            continue
        is_inside = is_inside_cuboid((*test["points"][0], *test["points"][1]), test["x"])
        diagonal = calculate_diagonal(test["points"])

    print(f"Test Expected: {test['expected']}, Got: {is_inside}")
    print(f"Diagonal Length: {round(diagonal, 2)}")
