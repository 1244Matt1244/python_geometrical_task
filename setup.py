from setuptools import setup, find_packages

setup(
    name="geometric-shapes",
    version="1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["click", "pytest"],
    entry_points={
        "console_scripts": [
            "geoshapes=shapes.cli:main"
        ]
    },
    python_requires=">=3.7",
)
