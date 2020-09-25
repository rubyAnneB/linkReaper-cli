# Name: linkReaper
# Version: 0.1
# Author: Ruby Anne Bautista
# Description: A cli tool for finding dead links in local files given
# file path and searches through web pages for dead links given url

import click
import re
import urllib3


@click.group()
def main():
    pass


@main.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True))
@click.option('--s', '-s', is_flag=True, help='change the http link schemes into https and output results')
def readfile(filepath, s):
    """Read from a local file and parse through the file for links"""
    with open(filepath, 'r') as file:
        urls = collect_links(file.read(), s)

    retrieve_codes(urls)


@main.command()
@click.argument('url', default="")
@click.option('--s', '-s', is_flag=True, help='change the http link schemes into https and output results')
def weblink(url, s):
    """Input a url to check page for dead links"""
    try:
        pool = urllib3.PoolManager()
        # retrieve the html data from the given url
        res = pool.request('GET', url)
    except:
        click.echo("Url entered is not valid. Please input a different url.")
    else:
        urls = collect_links(res.data.decode('utf-8'), s)
        retrieve_codes(urls)


def retrieve_codes(links):
    """retrieves the http codes returned by the links"""
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
            # irregular responses
            click.echo(click.style("Irregular - Code        : " + str(response.status) + " " + link, fg='yellow'))


def collect_links(raw_data, secure):
    """parses through the raw data to find links and removes duplicates, if secure is true, parses through for http
    and turns them into https """
    urls = []
    unique_urls = []

    if secure: # if the user utilises the -s option
        urls_raw = re.findall(r'http?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        # get rid of duplicate links
        [urls.append(link) for link in urls_raw if link not in urls]

        for link in urls:
            # changes the scheme of the links from http to https
            unique_urls.append(re.sub("http", "https", link))

    else:
        urls_raw = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        # get rid of duplicate links
        [unique_urls.append(link) for link in urls_raw if link not in unique_urls]

    return unique_urls


if __name__ == '__main__':
    main()
