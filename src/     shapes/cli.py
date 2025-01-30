@click.group()
def main():
    """Geometric Shapes Calculator"""
    pass


@main.command()  # Add blank line after function
@click.option("--radius", type=float, required=True)
def circle_area(radius):
    ...


@main.command()  # Add blank line after function
@click.option("--radius", type=float, required=True)
def sphere_volume(radius):
    ...


if __name__ == "__main__":  # Add 2 blank lines before this
    main()
