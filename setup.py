from setuptools import setup, find_packages

setup(
    name="your_project_name",  # Replace with your actual project name
    version="0.1.0",
    description="A short description of your project",  # Optional but recommended
    author="Your Name",  # Optional: specify the author
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        # Add your runtime dependencies here, for example:
        # "numpy>=1.23",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2",
            "pytest-cov>=4.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "sphinx>=7.0"  # Documentation tool; remove if not needed
        ]
    },
    python_requires=">=3.8, <3.13",  # Specify the Python versions your project supports
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",  # Update if using a different license
        "Operating System :: OS Independent",
    ],
)
