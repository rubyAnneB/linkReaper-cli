from setuptools import setup

setup(
    name='linkReaper',
    version='1.0',
    install_requires=['Click', 'Colorama', 'urllib3'],
    py_modules=['linkReaper'],
    entry_points={
        'console_scripts': [
            'linkreap= linkReaper:main',

        ]
    }
)
