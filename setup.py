"""Setup file detailing dependencies"""
from setuptools import setup

setup(
    name="linkreaper",
    author="rubyAnneB",
    author_email="bautisruby643@gmail.com",
    version="0.0.5",
    install_requires=["Click", "Colorama", "urllib3", "certifi"],
    py_modules=["linkreaper"],
    entry_points={
        "console_scripts": [
            "linkreaper= linkreaper:main",
        ]
    },
    long_description=long_description,  # pylint: disable=undefined-variable
    long_description_content_type="text/markdown",
    description="checks for deadlinks in an html file or from a website. "
    "Done as part of DPS 909- Seneca College",
    package_dir={"": "linkreaper"},
    url="https://github.com/rubyAnneB/linkReaper-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
