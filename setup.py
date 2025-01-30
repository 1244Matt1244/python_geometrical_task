[metadata]
name = geometric_shapes
version = 0.3
author = Your Name
author_email = your.email@example.com
description = Advanced geometric shape calculations

[options]
package_dir =
    = src
packages = find:
install_requires =
    numpy>=1.21
    matplotlib>=3.5
    click>=8.1
python_requires = >=3.8

[options.extras_require]
dev =
    pytest>=7.2
    pytest-cov>=4.0
    flake8>=6.0
    mypy>=1.0

[options.entry_points]
console_scripts =
    geoshapes = shapes.cli:main
