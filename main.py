import click

__version__ = "0.1.2"

@click.command("guten-tag")
def guten_tag():
    click.echo("guten tag")

@click.command("bonjour")
def bonjour():
    click.echo("bonjour monde")

@click.command("version")
def version():
    click.echo(__version__)

@click.command("hello")
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()
