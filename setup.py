#!/usr/bin/env python3

from setuptools import setup

setup(
    name='test_bioconda_build',
    version='1.0.3',
    description='packate for testing Cherri depencies',
    author='Teresa Mueller',
    author_email='muellert@informatik.uni-freiburg.de',
    url='https://github.com/teresa-m/test_bioconda_build',
    scripts=['test_conda_cherri/test_conda_cherri.py'],
    licence='GPL-3.0',
    zip_safe=False,
)
