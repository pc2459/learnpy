"""
Write a script that will take three required command line arguments - input_file,
output_file, and the row_limit. From those arguments, split the input CSV into
multiple files based on the row_limit argument.

Arguments:
1. -i: input file name
2. -o: output file name
3. -r: row limit to split

Default settings:
1. output_path is the current directory
2. headers are displayed on each split file
3. the default delimiter is a comma
"""

from __future__ import division

import argparse
import csv
import os
import math
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

##########################

#find out the number of CSVs needed
segments = math.ceil(total_rows/rows)
print segments

#open the input and begin to read 
input = open(args.i, "r") 
reader = csv.reader(input)

#store the header
header = reader.next()

# create an list to store header + N rows 
templist = []

current = 1


while current <= segments:

	#add rows to the templist
	for i in range(rows):

		try: 
			line = reader.next()
			templist.append(line)
		except StopIteration:
			pass
		
		print "Added to list"

	#now write the templist to an output
	with open(args.o+str(current)+".csv", "wb") as output:
		writer = csv.writer(output)
		for line in templist:
			writer.writerow(line)
			print "Wrote to output"
	templist = []
	current += 1
	print "incremented current"



input.close()






print args.i
print args.o
print args.r