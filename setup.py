#from setuptools import find_packages
from setuptools import setup

setup(
    name='test_bioconda_build',
    verion='1.0.0',
    description='packate for testing Cherri depencies'
    author='Teresa Müller'
    author_email='muellert@informatik.uni-freiburg.de'
    url=''
    #install_requerments=[]
    #packages=finde_packages(),
    scripts=['test_bioconda_build.py'],
    #entry_points={
    #    'console_scripts'=[
    #        'test-cherri-cli = test_conda_cherri.main:main'
    #    ],
    #},
)
