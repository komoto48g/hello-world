#! python
# -*- coding: utf-8 -*-
"""setup file

Run the build process by entering 'python setup.py bdist_egg'.
If everything works well, you should find a subdirectory named 'dist'
"""
from setuptools import setup
from setuptools import find_packages
from mylibs import __version__, __author__


setup(
    name = "hello-world",
    version = __version__,
    author = __author__,
    author_email = "komoto@jeol.co.jp",
    description = "Love Gladys Knight & Pips",
    
    ## Description of the package in the distribution
    package_dir = {
        '' : "." # root packages is `.`, i.e., the package is in ./
    },
    
    ## Packing all modules in mwx package
    ## packages = [
    ##     "",
    ## ],
    packages = find_packages(),
    
    ## install_requires = [
    ##     'pillow',
    ##     'matplotlib',
    ##     'scipy==1.2.3',
    ##     'wxpython==4.0.7',
    ##     'opencv-python==3.4.5.20',
    ## ],
    
    ## This is necessary for egg distribution to include *.txt files
    package_data={
        '' : [
            'README.md',
        ],
    },
    include_package_data=True,
)
