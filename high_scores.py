import csv
import os

# read the scores into a dictionary
# replace existing scores with higher scores

# create dictionary
scores = {}

path = "/Users/Fo/Dropbox/LearnPython/repo"

# open the file
with open(os.path.join(path,"scores.csv"),"rb") as file:
	# create a CSV reader
	reader = csv.reader(file)
	for name,score in reader:
		#convert scores to int
		score = int(score) 
		# add if new
		if name not in scores.keys():
			scores[name] = score
		# append higher score if not
		else:
			if scores[name] < score:
				scores[name] = score

for key in sorted(scores):
	print key, scores[key]

