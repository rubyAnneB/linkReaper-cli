"""Setup file detailing dependencies"""
from setuptools import setup

setup(
    name="linkreaper",
    version="1.3",
    install_requires=["Click", "Colorama", "urllib3", "black", "pylint"],
    py_modules=["linkReaper"],
    entry_points={
        "console_scripts": [
            "linkreaper= linkReaper:main",
        ]
    },
)
