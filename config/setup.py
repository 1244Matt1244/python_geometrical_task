from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geometric_shapes",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for working with geometric shapes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21,<2.0",
        "matplotlib>=3.5,<4.0"
    ],
    extras_require={
        "dev": [
            "mypy>=0.991,<1.0",
            "flake8>=6.0,<7.0",
            "pytest>=7.2,<8.0",
            "pytest-cov>=4.0,<5.0"
        ]
    },
    entry_points={"console_scripts": ["geoshapes=shapes.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
