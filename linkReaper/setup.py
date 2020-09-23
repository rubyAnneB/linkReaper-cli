from setuptools import setup

setup(
    name = 'linkReaper',
    version = '0.1' ,
    install_requires = ['Click', 'Colorama'],
    py_modules = ['linkReaper'],
    entry_points={
        'console_scripts': [
            'reap= linkReaper:main',

        ]
    }
)