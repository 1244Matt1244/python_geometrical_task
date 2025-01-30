import click
from .circle import Circle
from .sphere import Sphere

@click.group()
def main():
    """Geometric Shapes Calculator (Circle/Sphere)"""
    pass

@main.command()
@click.option("--radius", type=float, required=True, help="Circle radius")
def circle_area(radius):
    try:
        circle = Circle(radius)
        click.echo(f"Circle area: {circle.area():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")

@main.command()
@click.option("--radius", type=float, required=True, help="Sphere radius")
def sphere_volume(radius):
    try:
        sphere = Sphere(radius)
        click.echo(f"Sphere volume: {sphere.volume():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")

if __name__ == "__main__":
    main()
