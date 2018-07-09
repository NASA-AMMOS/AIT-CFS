from setuptools import setup, find_packages

import os

setup(
    name         = 'ait-cfs',
    version      = '1.0.0',
    packages     = find_packages(exclude=['tests']),
    author       = 'ait-cFS Development Team',
    author_email = 'ait@jpl.nasa.gov',

    namespace_packages = ['ait'],
    install_requires   = [
        'ait-core==1.1.0',
        'ait-gui==1.0.0',
    ],
)
