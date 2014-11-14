import csv
import os

# read the scores into a dictionary
# replace existing scores with higher scores

# create dictionary
scores = {}

path = "/Users/Fo/Dropbox/LearnPython/repo"

# open the file
with open(os.path.join(path,"scores.csv"),rb) as file:
	# create a CSV reader
	reader = csv.reader(file)
	for row in reader:
		# add if new
		if row[0] not in scores.keys():
			scores[row[0]] = row[1]
		# append higher score if not
		else:
			if scores[row[0]] < row[1]:
				scores[row[0]] = row[1]

print scores

