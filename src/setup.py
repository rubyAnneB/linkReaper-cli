"""Setup file detailing dependencies"""
from setuptools import setup

setup(
    name="linkreaper",
    version="1.3",
    install_requires=["Click", "Colorama", "urllib3"],
    py_modules=["linkreaper"],
    entry_points={
        "console_scripts": [
            "linkreaper= linkreaper:main",
        ]
    },

)
