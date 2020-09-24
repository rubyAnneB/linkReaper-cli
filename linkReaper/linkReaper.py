import click
import re
import urllib3
from urllib3 import request


@click.group()
def main():
    pass


@main.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True))
@click.option('--s', '-s', is_flag=True)
def readfile(filepath, s):
    """Read from a local file"""

    with open(filepath, 'r') as file:
        urls = collect_links(file.read(), s)

    retrieve_codes(urls)


@main.command()
@click.argument('url', default="")
@click.option('--s', '-s', is_flag=True)
def reqpage(url, s):
    """Input a url to check page for dead links"""
    try:
        pool = urllib3.PoolManager()
        res = pool.request('GET', url)
        # click.echo(res.data)
    except:
        click.echo("Url entered is not valid. Please input a different url.")
    else:
        urls = collect_links(res.data.decode('utf-8'), s)
        retrieve_codes(urls)


def retrieve_codes(links):
    # goes through the list of links and retrieves the htpp responses and displays them
    for link in links:
        try:
            pool = urllib3.PoolManager(num_pools=50)
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
            click.echo(click.style("Irregular - Code        : " + str(response.status) + " " + link, fg='yellow'))


def collect_links(raw_data, secure):
    urls = []
    unique_urls = []

    if secure:
        urls_raw = re.findall(r'http?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        [urls.append(x) for x in urls_raw if x not in urls]

        for link in urls:
            unique_urls.append(re.sub("http", "https", link))

    else:
        urls_raw = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        [unique_urls.append(x) for x in urls_raw if x not in unique_urls]

    return unique_urls


if __name__ == '__main__':
    main()
