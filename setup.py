from setuptools import setup, find_packages

setup(
    name="geometric_shapes",
    version="1.0.2",
    description="Python package for calculating geometric properties",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "click>=8.1.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0"
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0"
        ]
    },
    entry_points={
        "console_scripts": ["geoshapes=shapes.cli:main"]
    },
    python_requires=">=3.7",  # Adjust this to the minimum Python version you want to support
)
