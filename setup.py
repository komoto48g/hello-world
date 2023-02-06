#! python3
# -*- coding: utf-8 -*-
"""setup file

Run the build process by entering:

>>> python setup.py bdist_egg

If everything works well, you should find a subdirectory named 'dist'
"""
from setuptools import setup
from mylib import __version__, __author__


setup(
    name = "mylib",
    version = __version__,
    author = __author__,
    author_email = "komoto@jeol.co.jp",
    description = "Hello world sample program",
    
    ## Description of the package in the distribution
    package_dir = {
        '' : "." # root packages is `.`, i.e., the package is in ./
    },
    
    ## Packing all modules in mwx package
    packages = [
        "mylib",
    ],
    
    ## This is necessary for egg distribution to include readme files
    package_data={
        'mylib' : ['README.md'],
    },
    include_package_data=True,
)
