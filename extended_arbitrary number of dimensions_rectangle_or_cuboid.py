import numpy as np
from scipy.spatial import distance
import re
import sys

def load_points(filename):
    with open(filename, 'r') as f:
        points = []
        for line in f:
            # Use regex to find numbers in the string
            numbers = re.findall(r"[-+]?\d*\.?\d+", line)
            # Convert the numbers to float and append to the list
            points.append([float(num) for num in numbers])
    return points

def is_hyperrectangle(points):
    if len(points) != 2 ** (len(points[0]) - 1):
        return False
    distances = [distance.euclidean(points[i], points[(i+1)%len(points)]) for i in range(len(points))]
    return len(set(distances)) == len(points[0])

def is_inside_hyperrectangle(points, X):
    A = np.array(points[0])
    vectors = [np.array(points[i]) - A for i in range(1, len(points))]
    try:
        coefficients = np.linalg.solve(np.array(vectors).T, np.array(X) - A)
        return all(0 <= ci <= 1 for ci in coefficients)
    except np.linalg.LinAlgError:
        return False

def calculate_hyperdiagonal(points):
    dimensions = len(points[0])
    # Calculate the lengths of the sides
    side_lengths = [max(point[i] for point in points) - min(point[i] for point in points) for i in range(dimensions)]
    # Calculate the diagonal as the square root of the sum of the squares of the side lengths
    return np.sqrt(sum(length**2 for length in side_lengths))

def main():
    # Set the path to the files using raw string literals
    path = r'C:\\Users\\korisnik\\Desktop\\Red Cat\\'

    # Load the points and X from the files
    points2D = load_points(r"C:\\Users\\korisnik\\Desktop\\Red Cat\\"+ 'points2D.txt')
    X2D = load_points(r"C:\\Users\\korisnik\\Desktop\\Red Cat\\" + 'x2D.txt')[0]
    points3D = load_points(r"C:\\Users\\korisnik\\Desktop\\Red Cat\\" + 'points3D.txt')
    X3D = load_points(r"C:\\Users\\korisnik\\Desktop\\Red Cat\\" + 'x3D.txt')[0]

    # Check if the points can form a hyperrectangle and if X is inside it
    if len(points2D[0]) == 2:
        if not is_hyperrectangle(points2D):
            print("Točke ne mogu biti vrhovi pravokutnika.")
            sys.exit()
        print("Točka X se nalazi unutar pravokutnika." if is_inside_hyperrectangle(points2D, X2D) else "Točka X se ne nalazi unutar pravokutnika.")
        print("Dijagonala lika je:", calculate_hyperdiagonal(points2D))
    elif len(points3D[0]) == 3:
        if not is_hyperrectangle(points3D):
            print("Točke ne mogu biti vrhovi kvadra.")
            return
        print("Točka X se nalazi unutar kvadra." if is_inside_hyperrectangle(points3D, X3D) else "Točka X se ne nalazi unutar kvadra.")
        print("Prostorna dijagonala je:", calculate_hyperdiagonal(points3D))

if __name__ == "__main__":
    main()
