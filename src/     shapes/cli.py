import click
from .circle import Circle
from .sphere import Sphere


@click.group()
def main():
    """Geometric Shapes Calculator"""
    pass


@main.command()
@click.option("--radius", type=float, required=True)
def circle_area(radius):
    try:
        circle = Circle(radius)
        click.echo(f"Area: {circle.area():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")


@main.command()
@click.option("--radius", type=float, required=True)
def sphere_volume(radius):
    try:
        sphere = Sphere(radius)
        click.echo(f"Volume: {sphere.volume():.2f}")
    except ValueError as e:
        click.secho(f"Error: {str(e)}", fg="red")


if __name__ == "__main__":
    main()
