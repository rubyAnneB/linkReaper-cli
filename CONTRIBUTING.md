Thank you for taking interest in this little project. These are some instructions to help you set up linkreaper on your machine.

### Installation
 Make sure that [Python](https://www.python.org/) is installed on your machine first then execute the following commands on your terminal:
 
 Copy the code into your machine
  
    git clone https://github.com/rubyAnneB/linkReaper-cli.git
 Move to the linkReaper directory
  
    cd linkReaper-cli/linkReaper

This command will install the program along with its dependencies    
    
    pip install .



Please use [Black](https://pypi.org/project/black/) for formatting the code. It will be installed automatically with the rest of the dependencies.

To format the code, go to the directory with the code and run

    black .

This will format everything in the directory.


This project uses Pylint to analyze the code it is installed with the rest of the dependencies. 
To use it, run the following command:

    pylint linkreaper.py

ide settings for pycharm is also available [here](settings.zip)

### Testing 

This project uses unitttest. At the moment, all tests are located [here](tests/test.py) in the tests directory. In the future, this project may move to using to 
using pyTest as can be seen [here](tests/test_.py). Also keep in mind that the [library](https://click.palletsprojects.com/en/7.x/) used in constructing this application
has its own [testing capabilities](https://click.palletsprojects.com/en/7.x/testing/?highlight=test) that can be used to test the commands.
A sample can be found in this [file](tests/test_.py). 

To test coverage use [coverage](https://coverage.readthedocs.io/en/coverage-5.3/).        


## Dependencies for development
* [Black](https://pypi.org/project/black/) - For source code formatting
* [Pylint](http://pylint.pycqa.org/en/latest/user_guide/installation.html) - For code analysis
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.3/)
