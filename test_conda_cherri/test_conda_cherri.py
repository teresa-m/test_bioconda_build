#!/usr/bin/env python
import argparse
#import pandas as pd
import numpy as np
import sklearn as sk
from interlap import InterLap
import eden.graph as eg
import networkx as nx
from ubergauss import tools
import biofilm.algo.feature_selection as featsel
import wget
#import subprocess


__version__ = "1.0.3"

"""

~~~~~~~~~~~~~~~~~~~~~~~~~~
Check out available modes
~~~~~~~~~~~~~~~~~~~~~~~~~~

test_conda_cherry.py -h



"""


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-i", "--input", dest="input", help= "path to input file")
    args = parser.parse_args()

    #print('Hallo I am running!')
    input = args.input



if __name__ == '__main__':
    main()
