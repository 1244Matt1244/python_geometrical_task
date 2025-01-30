import click
from shapes import Circle, Rectangle, Sphere

@click.group()
def cli():
    """Geometric Calculator - CLI Interface"""
    pass

@cli.command()
@click.option('--radius', type=float, required=True, help='Circle radius')
def circle(radius):
    try:
        c = Circle(radius)
        click.echo(f"Area: {c.area():.2f}")
        click.echo(f"Circumference: {c.perimeter():.2f}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.option('--radius', type=float, required=True, help='Sphere radius')
def sphere(radius):
    try:
        s = Sphere(radius)
        click.echo(f"Surface Area: {s.area():.2f}")
        click.echo(f"Volume: {s.volume():.2f}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)

if __name__ == '__main__':
    cli()
