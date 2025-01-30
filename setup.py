from setuptools import setup, find_packages

setup(
    name="shapes",
    version="0.3",
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced geometric shape calculations",
    long_description=open("README.md").read(),  # Add if you have a README
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
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
            "mypy>=1.0",
            "black>=23.3"  # Consider adding if using formatting
        ]
    },
    entry_points={
        "console_scripts": ["geoshapes=shapes.cli:main"]  # Fixed path
    },
    python_requires=">=3.8",
    classifiers=[  # Add relevant classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/yourusername/geometric-shapes",  # Add if applicable
)
