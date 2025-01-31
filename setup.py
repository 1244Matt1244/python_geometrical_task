from setuptools import setup, find_packages

setup(
    name="geometric-shapes",
    version="1.0.2",
    description="Python package for calculating geometric properties",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["click>=8.1.0"],
    extras_require={"test": ["pytest>=7.0.0"]},
    entry_points={"console_scripts": ["geoshapes=shapes.cli:main"]},
    python_requires=">=3.8",
)
