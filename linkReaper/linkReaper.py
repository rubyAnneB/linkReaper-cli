from urllib3 import request
import click
import re
import urllib3


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

    # TODO: get support for HTTP to HTTPS

    with open(filepath, 'r') as file:
        urls = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', file.read())
        r = []
        [r.append(x) for x in urls if x not in r]
        retrieve_codes(r)


def retrieve_codes(links):
    # goes through the list of links and retrieves the htpp responses and displays them
    for link in links:

        try:
            pool = urllib3.PoolManager()
            response = pool.request('HEAD', link)
            if 300 > response.status <= 200:
                # successful responses
                click.echo(click.style("GOOD      - Successful  : " + str(response.status) + " " + link, fg='green'))
            elif 400 > response.status <= 300:
                # redirection message
                click.echo(click.style("BAD       - Redirect    : " + str(response.status) + " " + link, fg='red'))
            elif 500 > response.status <= 400:
                # client error responses
                click.echo(click.style("BAD       - Client Error: " + str(response.status) + " " + link, fg='red'))
            elif 600 > response.status <= 500:
                # server error response
                click.echo(click.style("BAD       - Server Error: " + str(response.status) + " " + link, fg='red'))
            else:
                click.echo(click.style("Unknown " + str(response.status) + " " + link, fg='red'))

        except Exception:
            click.echo(click.style("Irregular -  Code       :" + str(response.status) + " " + link, fg='yellow'))


@main.command()
# @click.argument('name')
@click.argument('name', type=click.Path(exists=True))
def reqpage(name):
    """Go to given url"""
    click.echo("go to web page")
    click.echo(name)


if __name__ == '__main__':
    main()
