# CSV

import csv
import os

path = "/Users/Fo/Dropbox/LearnPython/repo"

with open(os.path.join(path,"wonka.csv"),"rb") as file:
	reader = csv.reader(file):
	for row in reader:
		print row