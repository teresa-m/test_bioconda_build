#!/usr/bin/env python3

import argparse
#import pandas as pd
import numpy as np
#import sklearn as sk
#from interlap import InterLap
#import eden.graph as eg
#import networkx as nx
#from ubergauss import tools
#import biofilm.algo.feature_selection as featsel
#import wget
#import subprocess




"""

~~~~~~~~~~~~~~~~~~~~~~~~~~
Check out available modes
~~~~~~~~~~~~~~~~~~~~~~~~~~

test_conda_cherry.py -h

__version__ = "1.0.4"

"""


def setup_argument_parser():
    """Setup argparse parser."""
    help_description = """
    Help description
    """
    p = argparse.ArgumentParser(description='',
                                     add_help=False,
                                     prog="test_conda_cherri.py",
                                     formatter_class=argparse.MetavarTypeHelpFormatter)
    p.add_argument("-h", "--help",
                   action="help",
                   help="Print help message")
    p.add_argument("-i", "--input", 
                   dest="input", 
                   type=str,
                   required=True,
                   help= "path to input file")
    
    return p 



if __name__ == '__main__':

    parser = setup_argument_parser()
    args = parser.parse_args()
    
    assert os.path.exists(args.input), "--in file \"%s\" not found" % (args.input)
