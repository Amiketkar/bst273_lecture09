#!/usr/bin/env python

import argparse
"""
We could import sys modelue and write path to that file from file = sys.argv[1]
in this case it is better to use argparse module because we want to modify itself.
"""
parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read?",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------
args = parser.parse_args( )
print(args)
"""print(args.get(data_file))- on;y works with dictionary"""
print(args.data_file) # to check we are on correct files


#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
