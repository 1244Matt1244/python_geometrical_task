```markdown
# Python Geometrical Task 📐✨

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

A Python-based project designed to solve geometric problems involving rectangles, cuboids, and higher-dimensional shapes [[9]].

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Task Description](#task-description)
- [Examples](#examples)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Description

This repository contains Python scripts to perform geometric computations such as:
- Verifying if given points form a rectangle or cuboid.
- Checking if a point lies inside the formed shape.
- Calculating the diagonal length of the shape.

The implementation supports both 2D and 3D cases, with extensions for arbitrary dimensions.

---

## Features :star:

- **2D Rectangle Verification** 🟩: Check if four points form a rectangle.
- **Point Inclusion (2D)** 🔵: Determine if a point lies inside the rectangle.
- **Diagonal Calculation (2D)** ⬛: Compute the diagonal length of the rectangle.
- **3D Cuboid Verification** 🟦: Extend functionality to verify cuboid formation.
- **Point Inclusion (3D)** 🟪: Check if a point lies inside the cuboid.
- **Diagonal Calculation (3D)** 🟫: Compute the spatial diagonal of the cuboid.
- **Arbitrary Dimensions** 🔄: Support for higher-dimensional shapes.

---

## Task Description

### 1. 2D Rectangle Verification and Point Inclusion
- Input: Four points (A, B, C, X) in 2D space.
- Tasks:
  - Verify if A, B, and C form a rectangle.
  - If valid, check if point X lies inside the rectangle.
  - Calculate the diagonal of the rectangle.

### 2. 3D Cuboid Verification and Point Inclusion
- Input: Five points (A, B, C, D, X) in 3D space.
- Tasks:
  - Verify if A, B, C, and D form a cuboid.
  - If valid, check if point X lies inside the cuboid.
  - Calculate the spatial diagonal of the cuboid.

### 3. Arbitrary Dimensions
- Extend the above functionalities to handle n-dimensional spaces.

---

## Examples

### 2D Example
- **Input**: `0, 0`, `5, 0`, `0, 5`, `2, 2`
- **Output**: `True` (Point X is inside the rectangle.)

### 3D Example
- **Input**: `0, 0, 0`, `5, 0, 0`, `0, 3, 0`, `0, 0, 1`, `1, 1, 2`
- **Output**: `False` (Point X is outside the cuboid.)

---

## Repository Structure :file_folder:

| File/Directory         | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `.github/workflows`     | Contains GitHub Actions workflows for CI/CD processes [[1]].               |
| `__init__.py`           | Marks directories as Python packages [[5]].                                |
| `python.yml`            | Configuration file for Python environment setup [[7]].                     |
| `data`                  | Includes data files like `points2D.txt`, `points3D.txt`, etc.              |
| `docs`                  | Documentation written in markdown format [[4]].                            |
| `task.txt`              | Detailed task description.                                                 |
| `test_instruction.txt`  | Instructions for testing the scripts.                                      |
| `scripts`               | Python scripts such as `elementary_code_test0.py`, etc.                    |
| `src/geometric_shapes`  | Core functionality modules including `cuboid.py`, `visualization.py`, etc. |
| `.gitignore`            | Specifies intentionally untracked files [[5]].                             |
| `.pre-commit-config.yaml`| Pre-commit hook configurations [[8]].                                     |
| `README.md`             | This file provides an overview of the repository [[9]].                    |
| `pyproject.toml`        | Build system requirements and metadata [[5]].                              |
| `setup.py`              | Script for packaging and distributing the project [[5]].                   |

---

## Installation :wrench:

To use this repository, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/1244Matt1244/python_geometrical_task.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python_geometrical_task
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage :computer:

Run the scripts using Python:

```bash
python scripts/elementary_code_test0.py
```

For extended functionality:

```bash
python scripts/extended_rectangle_or_cuboid.py
```

Refer to `test_instruction.txt` for more details on running tests.

---

## Contributing :handshake:

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Open a pull request against the main repository.

Please ensure your code adheres to PEP 8 guidelines and includes appropriate tests.

---

## License :scroll:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Additional Notes

For more information on formatting the `README.md`, refer to GitHub's Markdown guide [[6]].

---

Thank you for visiting this repository! If you find it useful, please consider starring it. ★

---

 Icons made by [Simple Icons](https://simpleicons.org/) [[3]].
```
