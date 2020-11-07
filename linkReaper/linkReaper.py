# Name: linkReaper
# Version: 0.1
# Author: Ruby Anne Bautista
# Description: A cli tool for finding dead links in local files given
# file path and searches through web pages for dead links given url

import click
import re
import urllib3
import json
from bs4 import BeautifulSoup

@click.group()
def main():
    pass


@main.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True))
@click.option('--s', '-s', is_flag=True, help='change the http link schemes into https and output results')
@click.option('--a', '-all', is_flag=True, default=True, help='Prints all the links and their status codes')
@click.option('--g', '-good', is_flag=True, help='Prints all the good links with 200 HTTP codes')
@click.option('--b', '-bad', is_flag=True, help='Prints all the bad links with anything other than a 200 HTTP code')
@click.option('--j', '-json', is_flag=True, help='Prints out links and their responses in json format')
@click.option('--ignore', help='Ignores links contained within a separate text file',
              type=click.Path(exists=True, readable=True))
def readfile(filepath, s, a, g, b, j, ignore):
    """Read from a local file and parse through the file for links"""
    try:
        with open(filepath, 'r') as file:
            urls = collect_links(file.read(), s)

        if ignore:
            with open(ignore, 'r') as ignore_file:
                urls_to_ignore = collect_links(ignore_file.read(), s)
                # remove blacklisted urls
                urls = list(set(urls) ^ set(urls_to_ignore))

    except PermissionError:
        click.echo("Invalid path- permission denied")

    else:
        # if the user inputted both g and b, all the links will be displayed and 'a' will override both options
        if b and g:
            b = False
            g = False

        if j:
            output_json(urls, g, b)
        else:
            output_codes(urls, g, b)


@main.command()
@click.argument('url', default="")
@click.option('--s', '-s', is_flag=True, help='change the http link schemes into https and output results')
@click.option('--a', '-all', is_flag=True, default=True, help='Prints all the links and their status codes')
@click.option('--g', '-good', is_flag=True, help='Prints all the good links with 200 HTTP codes')
@click.option('--b', '-bad', is_flag=True, help='Prints all the bad links with anything other than a 200 HTTP code')
@click.option('--j', '-json', is_flag=True, help='Prints out links and their responses in json format')
def readwebsite(url, s, a, g, b, j):
    """Input a url to check page for dead links"""
    res = getwebsiteresponse(url)

    if res is None:
        click.echo("Url entered is not valid. Please input a different url.")
    else:

        urls = collect_links(res.data.decode('ISO-8859-1'), s)

        # if the user inputted both g and b, all the links will be displayed and 'a' will override both options
        if b and g:
            b = False
            g = False

        if j:
            output_json(urls, g, b)
        else:
            output_codes(urls, g, b)


@main.command()
@click.argument('apiurl', default="")
def readtelescope(apiurl):
    try:
        pool = urllib3.PoolManager()
        # retrieve the html data from the given url
        res = pool.request('GET', apiurl, timeout=5.0)
    except:
        click.echo("Url entered is not valid. Please input a different url.")
    else:

        posts = json.loads(res.data.decode('ISO-8859-1'))
        click.echo(res.data.decode('ISO-8859-1'))
        urls = collect_links(posts, api=True, baseurl=apiurl)

        for url in urls:
            click.echo(click.style("Post Link: " + url, fg='magenta'))
            res = getwebsiteresponse(url)
            posturls = collect_links(res.data.decode('ISO-8859-1'))
            click.echo(res.data.decode('ISO-8859-1'))
            output_codes(posturls)


def getwebsiteresponse(url):

    try:
        pool = urllib3.PoolManager()
        # retrieve the html data from the given url
        res = pool.request('GET', url, timeout=5.0)
    except:
        res = None

    return res


def output_codes(links, good_links=False, bad_links=False):
    """retrieves the http codes returned by the links"""
    for link in links:

        try:
            pool = urllib3.PoolManager(num_pools=50)
            response = pool.request('HEAD', link, timeout=5.0)

            if 300 > response.status <= 200 and not bad_links:
                # successful responses
                click.echo(click.style("GOOD      - Successful  : " + str(response.status) + " " + link, fg='green'))

            elif 400 > response.status <= 300 and not good_links:
                # redirection message
                click.echo(click.style("BAD       - Redirect    : " + str(response.status) + " " + link, fg='red'))

            elif 500 > response.status <= 400 and not good_links:
                # client error responses
                click.echo(click.style("BAD       - Server Error: " + str(response.status) + " " + link, fg='red'))

            elif 600 > response.status <= 500 and not good_links:
                # server error response
                click.echo(click.style("BAD       - Client Error: " + str(response.status) + " " + link, fg='red'))

            else:
                click.echo(click.style("Unknown " + str(response.status) + " " + link, fg='red'))

        except Exception:
            # irregular responses- may return 200 but behaviour is irregular
            if not good_links:
                click.echo(click.style("Irregular link          : " + link, fg='yellow'))


def output_json(links, good_links=False, bad_links=False):
    """Goes through a list of links, retrieves the response code and outputs the results in a json array with the url
    and corresponding code user has the option to display only certain types of links based on if the results were
    bad or good """
    json_responses = []

    click.echo("Retrieving website responses...")
    # added progress bar to show the progress through each link
    with click.progressbar(links) as bar:
        for link in bar:
            website_response = {
                "url": link,
                "status": ""
            }
            try:
                pool = urllib3.PoolManager(num_pools=50)
                response = pool.request('HEAD', link, timeout=5.0)

                website_response["status"] = response.status

            except Exception:
                website_response["status"] = "irregular"

            # determine whether to add the response to the list depending on the options the user inputted
            if website_response["status"] != "irregular" and 300 > website_response["status"] <= 200 and not bad_links:
                json_responses.append(website_response)
            elif (website_response["status"] == "irregular" or website_response["status"] > 300) and not good_links:
                json_responses.append(website_response)

    click.echo(json_responses)


def collect_links(raw_data, secure=False, api=False, baseurl=""):
    """parses through the raw data to find links and removes duplicates, if secure is true, parses through for http
    and turns them into https """

    unique_urls = []

    if secure:  # if the user utilises the -s option

        urls_raw = re.findall(r'http?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        # get rid of duplicate links
        urls_raw = list(dict.fromkeys(urls_raw))

        for link in urls_raw:
            # changes the scheme of the links from http to https
            unique_urls.append(re.sub("http", "https", link))
    elif api:
        for postId in raw_data:
            unique_urls.append(baseurl + "/" + postId['id'])
    else:
        urls_raw = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', raw_data)
        # get rid of duplicate links
        [unique_urls.append(link) for link in urls_raw if link not in unique_urls]

    return unique_urls


if __name__ == '__main__':
    main()
