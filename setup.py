from setuptools import find_packages
from setuptools import setup

setup(
    name='test_bioconda_build',
    version='1.0.2',
    description='packate for testing Cherri depencies',
    author='Teresa Mueller',
    author_email='muellert@informatik.uni-freiburg.de',
    url='https://github.com/teresa-m/test_bioconda_build',
    #install_requires=[],
    #packages=find_packages(),
    scripts=['test_conda_cherri/test_conda_cherri.py'],
    #entry_points={
    #    'console_scripts'=[
    #        'test-cherri-cli = test_conda_cherri.test_conda_cherri:main'
    #    ],
    #},
)
