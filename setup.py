from setuptools import setup, find_packages

setup(
    name="geometric_shapes",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        include=["shapes*", "3d*", "tests*"]
    ),
    install_requires=[
        "numpy>=1.21",
        "matplotlib>=3.5",
        "click>=8.1"
    ],
    extras_require={
        "dev": [
            "pytest>=7.2",
            "pytest-cov>=4.0",
            "flake8>=6.0",
            "mypy>=1.0"
        ]
    },
    entry_points={
        "console_scripts": ["geoshapes=shapes.cli:main"]
    }
)
