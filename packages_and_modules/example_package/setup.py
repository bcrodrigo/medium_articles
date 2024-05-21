"""
Script to create a custom package.

1. In your terminal you change to the directory containing the `setup.py` file. 

2. Activate the environment where we want to install the package

    > conda activate ENV_NAME

3. Install the package ionto the environment (don't forget the . at the end)

    (ENV_NAME) > pip install -e .

4. Double check that module is present in your environment

    (ENV_NAME) > conda list | grep example

"""

from setuptools import setup,find_packages

setup(
    name = 'src_package',
    version = '0.0.1',
    description = 'to demonstrate package installation',
    url = 'www.example.com',
    author = 'Me',
    packages = find_packages()
    )