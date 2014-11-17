import argparse
import csv
import os
import sys

# create a parser to handle command-line arguments
parser = argparse.ArgumentParser()
#store input file name
parser.add_argument('-i', action='store')
#store output file name
parser.add_argument('-o', action='store')
#store number of rows
parser.add_argument('-r', action='store')

args = parser.parse_args()

total_rows = 0
rows = 0

# check to see if rows is an integer
try:
	rows = int(args.r)
except ValueError:
	# error handle and quit if does not eixst
	print "You didn't input an integer"
	sys.exit(0)

# check to see if input exists
try: 
	with open(args.i) as file:
		pass
except IOError:
	# error handle and quit if does not exist
	print "Your input file does not exist"
	sys.exit(0)

# count total number of rows
with open(args.i) as input:
	total_rows = sum(1 for row in input)-1

if total_rows <= rows:
	print "The split number is more than or equal to the size of the CSV to split"
	sys.exit(0)




print args.i
print args.o
print args.r