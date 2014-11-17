import argparse
import csv
import os

parser = argparse.ArgumentParser()
#store input file name
parser.add_argument('-i', action='store')
#store output file name
parser.add_argument('-o', action='store')
#store number of rows
parser.add_argument('-r', action='store', type=int)

args = parser.parse_args()

print args.i
print args.o
print args.r