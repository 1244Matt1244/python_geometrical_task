import numpy as np

def is_rectangle(points):
    AB = np.subtract(points[1], points[0])
    BC = np.subtract(points[2], points[1])
    return np.dot(AB, BC) == 0

def is_inside(points, X):
    AB = np.subtract(points[1], points[0])
    BC = np.subtract(points[2], points[1])
    AX = np.subtract(X, points[0])
    return 0 <= np.dot(AB, AX) <= np.dot(AB, AB) and 0 <= np.dot(BC, AX) <= np.dot(BC, BC)

def calculate_diagonal(points):
    AB = np.subtract(points[1], points[0])
    BC = np.subtract(points[2], points[1])
    return np.sqrt(np.dot(AB, AB) + np.dot(BC, BC))

def main():
    points = [np.array([0.0, 0.0]), np.array([0.0, 5.0]), np.array([5.0, 5.0]), np.array([5.0, 0.0])]
    X = np.array([2.0, 2.0])
    if not is_rectangle(points):
        print('The points do not form a rectangle.')
        return
    print('The points form a rectangle.')
    print('Point', X, 'is inside the rectangle.' if is_inside(points, X) else 'is not inside the rectangle.')
    print('The diagonal of the rectangle is', calculate_diagonal(points))

if __name__ == '__main__':
    main()
