from urllib import request
from urllib.parse import urlparse
import click
import re


#
# @click.command()
# @click.argument('filename', default="", type=click.Path(exists=True), help='file path to check')
# @click.option('--s', default="", help='if you want to check if the http schemes work with https-requires a filename')

@click.group()
def main():
    pass


@main.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True))
# @click.argument('text', default="", type=click.Path(exists=True), help='file path to html file')
def readfile(filepath):
    """Read from a local file"""

    with open(filepath, 'r') as file:
        contents = file.read()
        regex = '<a href=["\' ]http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(regex, contents)
        # parse through to find urls


@main.command()
# @click.argument('name')
@click.argument('name', type=click.Path(exists=True))
def reqpage(name):
    """Go to given url"""
    click.echo("go to web page")
    click.echo(name)


if __name__ == '__main__':
    main()
