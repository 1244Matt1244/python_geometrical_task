import click
from .circle import Circle
from .sphere import Sphere

@click.group()
def cli():
    """Geometric Shapes Calculator"""
    pass

@click.command()
def main():
    """CLI for geometric calculations"""
    click.echo("Hello from shapes CLI!")
@click.option("--radius", type=float, required=True, help="Circle radius")
def circle_area(radius):
    """Calculate circle area"""
    try:
        circle = Circle(radius)
        click.echo(f"Area: {circle.area():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")

@cli.command()
@click.option("--radius", type=float, required=True, help="Sphere radius")
def sphere_volume(radius):
    """Calculate sphere volume"""
    try:
        sphere = Sphere(radius)
        click.echo(f"Volume: {sphere.volume():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")

if __name__ == "__main__":
    cli()
