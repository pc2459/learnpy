# CSV

import csv
import os

path = "/Users/Fo/Dropbox/LearnPython/repo"

# rb = "read binary", necessary in Python 2.x for CSV
# stick to r in P3
with open(os.path.join(path,"wonka.csv"),"rb") as file:
	reader = csv.reader(file)
	for row in reader:
		print row

print "-----"

with open(os.path.join(path,"pastimes.csv"),"rb") as file,open(os.path.join(path,"categorized pastimes.csv"),"wb") as outfile:

	reader = csv.reader(file)
	writer = csv.writer(outfile)

	next(reader) #skip the header
	writer.writerow(["Name","Favourite Pastime","Type of Pastime"])

	for row in reader:
		if row[1].lower().find("fighting") != -1:
			row.append("Combat")
		else:
			row.append("Other")
		writer.writerow(row)