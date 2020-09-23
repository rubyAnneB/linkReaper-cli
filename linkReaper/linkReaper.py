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
        regex = 'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', file.read())
        urls = list(dict.fromkeys(urls))


        for link in urls:
            resp = request.urlopen(link)
            if resp.code == 200:
                click.echo(click.style("GOOD " + str(resp.code) + " " + link, fg='green'))

            if resp.code == 403:
                click.echo(click.style("BAD " + str(resp.code) + " " + link, fg='red'))


@main.command()
# @click.argument('name')
@click.argument('name', type=click.Path(exists=True))
def reqpage(name):
    """Go to given url"""
    click.echo("go to web page")
    click.echo(name)


if __name__ == '__main__':
    main()
