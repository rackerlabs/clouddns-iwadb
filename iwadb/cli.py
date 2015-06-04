import click


@click.group()
def main():
    pass


@main.command(help='Get a value by key')
@click.argument('key')
def get(key):
    pass


@main.command(help='Set a value')
@click.argument('key')
@click.argument('value', type=click.File('rb'), default='-')
@click.option('--text', '-t')
def set(key, value, text):
    pass


@main.command(help='Remove a value by key')
@click.argument('key')
def rm(key):
    pass


@main.command(help='Query an index')
@click.argument('query')
def query(query):
    pass


@main.command(help='Create an index')
@click.argument('index')
def index(index):
    pass
