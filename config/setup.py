from setuptools import setup, find_packages

setup(
    name="geometric_shapes",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["numpy>=1.21.0", "matplotlib>=3.5.0"],
    entry_points={"console_scripts": ["geoshapes=shapes.cli:main"]},
)
