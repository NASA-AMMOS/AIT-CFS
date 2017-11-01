from setuptools import setup, find_packages

import os

setup(
    name         = 'bliss-cfs',
    version      = '0.1.0',
    packages     = find_packages(exclude=['tests']),
    author       = 'BLISS-cFS Development Team',
    author_email = 'bliss@jpl.nasa.gov',

    namespace_packages = ['bliss'],
    install_requires   = ['bliss-core>=0.26.1'],
    dependency_links = [
       'https://bliss.jpl.nasa.gov/pypi/simple/bliss-core/'
    ],
)
