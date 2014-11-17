import argparse
import csv
import os
import sys

parser = argparse.ArgumentParser()
#store input file name
parser.add_argument('-i', action='store')
#store output file name
parser.add_argument('-o', action='store')
#store number of rows
parser.add_argument('-r', action='store')

args = parser.parse_args()

# check to see if input exists
try: 
	with open(args.i) as f:
		pass
except IOError:
	print "Your input file does not exist"
	sys.exit(0)

# check to see if rows is an integer

try:
	rows = int(args.r)
except ValueError:
	print "You didn't input an integer"
	sys.exit(0)



print args.i
print args.o
print args.r