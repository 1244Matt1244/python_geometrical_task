from setuptools import setup, find_packages

setup(
    name="geometric-shapes",
    version="0.4",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "geoshapes=shapes.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
