# linkReaper-cli - Release 0.1
A python cli tool for finding dead links in html files and 
websites. Completed as part of DPS909 open-source course for
Seneca College.

## Functionalities and Features

linkReaper searches through html files stored locally and those pulled
from the web and determines whether any of the links in file are dead. It collects the link's response and then displays 
the status code and the corresponding link with a short description
of the result. These are color coded for the user's convenience and for easy identification of dead links.

### Optional Features

* Looks through a webpage for dead links given the url
* Colorized output
    * Red for bad urls
    * Green for good urls
    * Yellow for any urls with abnormal/unknown behaviour
* Option to check if http links work as https when looking through both local files and web pages
    * all http links found will have their scheme changed to https and will output the result
* Optimized to search only through the headers rather than full bodies
    * Doesn't download the full page when looking for a response
   
 ## Usage
 Make sure that python is installed on your machine first then execute the following commands on your terminal:
  
  > git clone https://github.com/rubyAnneB/linkReaper-cli.git

  > cd linkReaper-cli/linkReaper

  > pip install .

## Libraries
* Click
* Colorama
* urllib3

