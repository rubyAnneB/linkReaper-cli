# linkReaper-cli - Release 0.1
A Python cli tool for finding dead links in html files and 
websites. Completed as part of DPS909 open-source course for
Seneca College.

## Functionalities and Features

linkReaper searches through html files stored locally and those pulled
from the web and determines whether any of the links in file are dead. It collects the link's response and then displays 
the status code and the corresponding link with a short description
of the result. These are color coded for the user's convenience and for easy identification of dead links.
   ![output](Assets/linkread-output.png)

### Optional Features

* Looks through a webpage for dead links given the url
* Colourized output
    * Red for bad urls
    * Green for good urls
    * Yellow for any urls with abnormal/unknown behaviour
* Option to check if http links work as https when looking through both local files and web pages
    * all http links found will have their scheme changed to https and will output the result
* Optimized to search only through the headers rather than full bodies
    * Doesn't download the full page when looking for a response
 
### Installation
 Make sure that [Python](https://www.python.org/) is installed on your machine first then execute the following commands on your terminal:
 
 Copy the code into your machine
  
    git clone https://github.com/rubyAnneB/linkReaper-cli.git
 Move to the linkReaper directory
  
    cd linkReaper-cli/linkReaper

This command will install the program along with its dependencies    
    
    pip install .

## Usage

This program has two main capabilities:
1. Find broken links in local html files
2. Find broken links in a website given the url

Entering the program name with no arguments will show the help page.

#### Local files
Command:
Look through local file

    linkreaper readfile [file path]

Check if the http links work with the https scheme

    linkreaper readfile -s [file path]
    
    
#### Website
Command:
Look through a webpage

    linkreaper readwebsite [website url]

Check if the http links work with the https scheme

    linkreaper readwebsite -s [website url]    
## Dependencies
* [Click](https://click.palletsprojects.com/en/7.x/) - Package for making cli tools    
* [Colorama](https://pypi.org/project/colorama/) - Required for colour on Windows
* [urllib3](https://urllib3.readthedocs.io/en/latest/) - Used to manage connections and make requests


