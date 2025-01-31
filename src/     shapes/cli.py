import click
from .circle import Circle
from .sphere import Sphere
from .exceptions import InvalidDimensionError

@click.group()
def main():
    """Geometric Shapes CLI Calculator"""
    pass

@main.command()
@click.option('--radius', type=float, required=True, help='Radius of the circle')
def circle_area(radius):
    """Calculate circle area"""
    try:
        c = Circle(radius)
        click.echo(f"Area: {c.area():.2f}")
    except InvalidDimensionError as e:
        click.secho(f"Error: {str(e)}", fg='red')

@main.command()
@click.option('--radius', type=float, required=True, help='Radius of the sphere')
def sphere_volume(radius):
    """Calculate sphere volume"""
    try:
        s = Sphere(radius)
        click.echo(f"Volume: {s.volume():.2f}")
    except InvalidDimensionError as e:
        click.secho(f"Error: {str(e)}", fg='red')
