from urllib import request
from urllib.parse import urlparse
import click
import re


@click.command()
@click.option('--url', default="", help='web url to check')
def main(url):
    click.echo(click.style('hello world', fg='green'))


if __name__ == '__main__':
    main()
