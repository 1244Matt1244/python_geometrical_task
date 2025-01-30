
import numpy as np
from scipy.spatial import distance
import re
import sys
import os

def load_points(filename):
    """
    Reads numerical points from a file.

    Parameters:
        filename (str): Path to the file.

    Returns:
        list of lists: Parsed numerical data as float values.
    """
    try:
        with open(filename, 'r') as f:
            points = []
            for line in f:
                numbers = re.findall(r"[-+]?\d*\.?\d+", line)
                if numbers:
                    points.append([float(num) for num in numbers])
        return points
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        sys.exit(1)

def is_hyperrectangle(points):
    """
    Checks if given points form a hyperrectangle.

    Parameters:
        points (list of lists): List of N-dimensional points.

    Returns:
        bool: True if the points form a hyperrectangle, otherwise False.
    """
    dimensions = len(points[0])
    expected_vertices = 2 ** (dimensions - 1)
    
    if len(points) != expected_vertices:
        return False
    
    unique_distances = set(distance.euclidean(points[i], points[(i+1) % len(points)]) for i in range(len(points)))
    return len(unique_distances) == dimensions

def is_inside_hyperrectangle(points, X):
    """
    Determines if a point X is inside a hyperrectangle.

    Parameters:
        points (list of lists): Hyperrectangle vertices.
        X (list): The point to check.

    Returns:
        bool: True if X is inside, otherwise False.
    """
    A = np.array(points[0])
    vectors = [np.array(points[i]) - A for i in range(1, len(points))]
    
    try:
        coefficients = np.linalg.solve(np.array(vectors).T, np.array(X) - A)
        return np.all((0 <= coefficients) & (coefficients <= 1))
    except np.linalg.LinAlgError:
        return False

def calculate_hyperdiagonal(points):
    """
    Computes the hyperdiagonal of a hyperrectangle.

    Parameters:
        points (list of lists): Hyperrectangle vertices.

    Returns:
        float: The length of the hyperdiagonal.
    """
    dimensions = len(points[0])
    side_lengths = [max(p[i] for p in points) - min(p[i] for p in points) for i in range(dimensions)]
    return np.linalg.norm(side_lengths)

def process_dimension(points, X, shape_name):
    """
    Processes and prints results for a given dimension.

    Parameters:
        points (list of lists): The set of points defining the shape.
        X (list): The point to check inside the shape.
        shape_name (str): Name of the shape (e.g., "rectangle", "cuboid").
    """
    if not is_hyperrectangle(points):
        print(f"❌ The given points do NOT form a valid {shape_name}.")
        sys.exit(1)

    inside_msg = "✅ The point is INSIDE the {shape_name}." if is_inside_hyperrectangle(points, X) else "❌ The point is OUTSIDE the {shape_name}."
    print(inside_msg.format(shape_name=shape_name.capitalize()))
    print(f"📏 The {shape_name} diagonal is: {calculate_hyperdiagonal(points):.2f}")

def get_file_path(prompt):
    """
    Prompts the user to enter a valid file path.

    Parameters:
        prompt (str): The message to display when asking for input.

    Returns:
        str: The validated file path.
    """
    while True:
        file_path = input(prompt).strip()
        if os.path.isfile(file_path):
            return file_path
        print("❌ Invalid file path. Please enter a valid path.")

def main():
    """
    Main function that loads points from files and determines if they form
    valid shapes, checks if a given point is inside, and calculates the diagonal.
    """
    # Option 1: Use command-line arguments if provided
    if len(sys.argv) == 5:
        points2D_path, X2D_path, points3D_path, X3D_path = sys.argv[1:5]
    else:
        # Option 2: Prompt user for file paths dynamically
        print("📂 Please enter the file paths:")
        points2D_path = get_file_path("➡️ Enter 2D points file path: ")
        X2D_path = get_file_path("➡️ Enter 2D X point file path: ")
        points3D_path = get_file_path("➡️ Enter 3D points file path: ")
        X3D_path = get_file_path("➡️ Enter 3D X point file path: ")

    # Load data
    points2D = load_points(points2D_path)
    X2D = load_points(X2D_path)[0]
    points3D = load_points(points3D_path)
    X3D = load_points(X3D_path)[0]

    # Process dimensions
    if len(points2D[0]) == 2:
        process_dimension(points2D, X2D, "rectangle")
    elif len(points3D[0]) == 3:
        process_dimension(points3D, X3D, "cuboid")

if __name__ == "__main__":
    main()
