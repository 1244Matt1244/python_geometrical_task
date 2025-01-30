import click
from .circle import Circle
from .sphere import Sphere
from .base_shape import BaseShape

@click.group()
def main():
    """Command-line interface for geometric shape calculations"""
    pass

@main.command()
@click.option("--radius", type=float, required=True, help="Radius of the circle")
def circle_area(radius):
    """Calculate area of a circle"""
    circle = Circle(radius)
    click.echo(f"Circle area: {circle.area()}")

@main.command()
@click.option("--radius", type=float, required=True, help="Radius of the sphere")
def sphere_volume(radius):
    """Calculate volume of a sphere"""
    sphere = Sphere(radius)
    click.echo(f"Sphere volume: {sphere.volume()}")

@main.command()
@click.option("--input-file", type=click.Path(exists=True), help="Input file with coordinates")
@click.option("--output-file", type=click.Path(), help="Output file for results")
def process_shapes(input_file, output_file):
    """Process shapes from input file and save to output file"""
    # Add your file processing logic here
    click.echo(f"Processing shapes from {input_file}")

if __name__ == "__main__":
    main()
