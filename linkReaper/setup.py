from setuptools import setup

setup(
    name="linkreaper",
    version="0.1",
    install_requires=["Click", "Colorama", "urllib3", "black", "pylint"],
    py_modules=["linkReaper"],
    entry_points={
        "console_scripts": [
            "linkreaper= linkReaper:main",
        ]
    },
)
