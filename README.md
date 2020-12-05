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
* Option to only output only good, only bad and all links
    * good option will only output links with 200 response code
    * bad option will output anything else
    * all option is default and will output all
* Option to have the outputs in json format
    * This works with the good,bad and all output options
 
## Usage

This program has two main capabilities:
1. Find broken links in local html files
2. Find broken links in a website given the url

Entering the program name with no arguments will show the help page.

#### Local files
##### options
**-s , --s**  
Checks if http links works as https 

**-bad, --b**  
Outputs only the links that don't have a successful response

**-good, --g**  
Outputs only the links that have a successful response

**-all, --a**  
The default, outputs all the links

**-json, --j**  
Outputs the results as a json array. This options works with the '-good', '-all', and '-bad' options.


Command:  
Look through local file

    linkreaper readfile [file path]

Check if the http links work with the https scheme

    linkreaper readfile -s [file path]
    
Have all the good links outputted in json format

    linkreaper readfile --g --j [filepath]   
#### Website
Command:  
Look through a webpage

    linkreaper readwebsite [website url]

Check if the http links work with the https scheme

    linkreaper readwebsite -s [website url]
    
Have all the http links that don't work as https outputted as json
    
    linkreaper readwebsite -s --b --j [website url]    

## Coverage

    pip install coverage

for code coverage

## releases
This project has been released on [pypi](https://pypi.org/project/linkreaper/).
To install execute the following command in your terminal.

   Pip is wonderful. Getting all my dependencies for my project was so simple with pip.  And now, it seems I'll be making my own application available for installation through pip. I was pretty excited. I've had problems with packaging my programs so that they can be used without having to run it from the source code. It's been a struggle, particularly with java. However, this week, I was able to do it with linkreaper, this made me very happy.

Python programs can be put on [PyPi](https://pypi.org/) so that they can be installed through pip. It's truly wonderful. The whole process of packing up [linkreaper](https://github.com/rubyAnneB/linkReaper-cli) was fairly straightforward and painless. I had to make a couple of changes to my directories however, they were fairly minor. One of these was moving my [setup.py](http://setup.py) from inside the linkreaper directory to the root directory which in hindsight, I should have done from the beginning.  I didn't realise setup.py had this role for packaging programs. I'm quite thankful that the [Click](http://click.palletsprojects.com/en/7.x/) tutorial that I looked at had a setup.py included. It also made development easier in general since I had to just "pip install ." in the directory rather than having to install every single dependency separately. 

I had to make a couple of changes to my [setup.py](http://setup.py) beyond moving it to the root directory. I added a couple more details such as my name as well as some classifiers. 

```python
"""Setup file detailing dependencies"""
from setuptools import setup

setup(
    name="linkreaper",
    author="rubyAnneB",
    author_email="bautisruby643@gmail.com",
    version="0.0.4",
    install_requires=["Click", "Colorama", "urllib3", "certifi"],
    py_modules=["linkreaper"],
    entry_points={
        "console_scripts": [
            "linkreaper= linkreaper:main",
        ]
    },
    description="checks for deadlinks in an html file or from a website. "
                "Done as part of DPS 909- Seneca College",
    package_dir={"": "src"},
    url="https://github.com/rubyAnneB/linkReaper-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
```

I also had to include the License to my project. Previously, I just had the little indicator on the side of the repo's view that showed what license the project was under. This time, a [LISCENSE.md](http://liscense.md) file was added to the repository. 

After setup was complete and a license file created, I then had to generate the distribution packages that were then going to be uploaded and installed through pip. This was very simple to do and consisted of two commands

```bash
python3 -m pip install --user --upgrade setuptools wheel 
# This installs setuptools and wheel
python3 setup.py sdist bdist_wheel
#This generates the distribution archives
```

 

After running these two commands, the distribution archives were created and it was time to upload them in PyPI.  Well, before that, it was actually time to put it into TestPyPi; always wise to test before hand. TestPyPI allows you to trial run your release without having to put it on the actual repository. 

To put my linkreaper into TestPyPI, I had to first create an account and token. With these under my belt, I then executed the following commands: 

```bash
python3 -m pip install --user --upgrade twine
# installs twine to be able to upload your packages
python3 -m twine upload --repository testpypi dist/*
#uploads in testpypi
```

Yay!! It uploaded linkreaper into [TestPyPi](https://test.pypi.org/project/linkreaper/). I was pretty excited to see it uploaded. To see if everything worked correctly, I created a new virtual environment to run the program in. Once created, I ran the following command in the virtual environment to see if it was successful

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-linkreaper

```

It installed correctly was running, however, it was giving me warnings that weren't being shown previously. This worried me. After writing that [patch](https://github.com/rubyAnneB/linkReaper-cli/commit/003f84df4e2e10246ca14f158062182845a2bd8d), I then had to figure out how to release the newer version. Luckily, StackOverflow had such a question that I was able to [consult](https://stackoverflow.com/questions/53122766/best-workflow-and-practices-for-releasing-a-new-python-package-version-on-github). After testing once again that everything was working just fine, I then prepared for release into PyPI. This was basically the same process as TestPyPI only it's into different repositories.  Now, I can say that I've published a package into [TestPyPI](https://pypi.org/project/linkreaper/#description). A bit more testing later and I can say that I was satisfied with it. I felt quite accomplished after I'd done this. 

Now all users have to do is run the following command to get linkreaper rather than having to clone my repo. 

```bash
pip install linkreaper
```

The ease of use and simplicity is really quite nice. I can almost forget the agony of creating jar files.


## Dependencies
* [Click](https://click.palletsprojects.com/en/7.x/) - Package for making cli tools    
* [Colorama](https://pypi.org/project/colorama/) - Required for colour on Windows
* [urllib3](https://urllib3.readthedocs.io/en/latest/) - Used to manage connections and make requests
* [certifi](https://pypi.org/project/certifi/) - Validating certificates
