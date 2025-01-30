import numpy as np

def is_rectangle(points):
    """
    Checks if four given points form a rectangle.
    
    Parameters:
        points (list of np.array): Four 2D points representing the rectangle.

    Returns:
        bool: True if the points form a rectangle, otherwise False.
    """
    if len(points) != 4:
        return False  # Must have exactly 4 points

    AB = np.subtract(points[1], points[0])
    BC = np.subtract(points[2], points[1])
    CD = np.subtract(points[3], points[2])
    DA = np.subtract(points[0], points[3])

    # Check perpendicularity: Dot product of adjacent vectors should be zero
    return (
        np.dot(AB, BC) == 0 and 
        np.dot(BC, CD) == 0 and 
        np.dot(CD, DA) == 0 and 
        np.dot(DA, AB) == 0
    )

def is_inside(points, X):
    """
    Determines whether a given point X is inside the rectangle.

    Parameters:
        points (list of np.array): Rectangle vertices.
        X (np.array): The point to check.

    Returns:
        bool: True if X is inside the rectangle, otherwise False.
    """
    AB = np.subtract(points[1], points[0])
    BC = np.subtract(points[2], points[1])
    AX = np.subtract(X, points[0])

    return (
        0 <= np.dot(AB, AX) <= np.dot(AB, AB) and
        0 <= np.dot(BC, AX) <= np.dot(BC, BC)
    )

def calculate_diagonal(points):
    """
    Computes the diagonal length of the rectangle.

    Parameters:
        points (list of np.array): Rectangle vertices.

    Returns:
        float: The diagonal length.
    """
    return np.linalg.norm(points[2] - points[0])  # Distance from (0,0) to (5,5)

def main():
    """
    Main function that initializes rectangle points, checks conditions,
    and prints results.
    """
    points = [
        np.array([0.0, 0.0]), 
        np.array([0.0, 5.0]), 
        np.array([5.0, 5.0]), 
        np.array([5.0, 0.0])
    ]
    X = np.array([2.0, 2.0])

    if not is_rectangle(points):
        print("❌ The points do NOT form a rectangle.")
        return

    print("✅ The points form a rectangle.")
    print(f"🔹 Point {X} {'is' if is_inside(points, X) else 'is NOT'} inside the rectangle.")
    print(f"📏 The diagonal length of the rectangle is: {calculate_diagonal(points):.2f}")

if __name__ == '__main__':
    main()
