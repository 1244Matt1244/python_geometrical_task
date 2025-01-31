from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Your dependencies here
    ],
    extras_require={
        "dev": [
            "pytest",
            "pre-commit",
            "mypy",
            "sphinx"
        ]
    },
    python_requires=">=3.8, <3.13"  # Adjust this to the minimum and maximum Python version you want to support
)
