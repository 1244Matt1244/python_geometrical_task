Task

Create a program that will accept 2D coordinates of points A, B, C, and X as input. The coordinates should be read from a file. The program should:

check if these three points can be vertices of a rectangle. If they cannot, the program must stop working in a controlled manner and inform the user about the error,
check whether point X is inside the rectangle ABC and inform the user about the result,
calculate the diagonal of the figure.

Addition

• depending on points A, B, and C, the program should recognize what type of rectangle it is (rectangle or cuboid) and dynamically determine which classes or functions will be called for its execution • expand the program to support the input of points A, B, C, D, and X, each of which has 3 dimensions. The program should check whether points A, B, C, and D can be vertices of a cuboid. Check if point X is inside the cuboid ABCD. Calculate the spatial diagonal. • make the program work with an arbitrary number of dimensions for all tasks from the previous task

Examples of input and output

Input: 0, 0 5, 0 0, 5 2, 2 Output: True

Input: 0, 0, 0 5, 0, 0 0, 3, 0 0, 0, 1 1, 1, 2 Output: False
