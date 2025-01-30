from setuptools import setup, find_packages

setup(
    name="geometric_shapes",
    version="0.3",
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced geometric shape calculations",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        include=["shapes*", "shapes.3d*", "shapes.tests*"]
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
    },
    python_requires=">=3.8",
)
