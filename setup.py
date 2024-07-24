#! /usr/bin/env python

from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

setup_args = generate_distutils_setup(
    packages=["mindrove_package"], package_dir={"": "src"}
)

setup(**setup_args)
