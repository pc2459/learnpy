# TUPLES  ()
# -- immutable

a_tuple = ("not", "changeable")
print a_tuple

# brackets are optional

coordinates = 4.2, 9.2
print coordinates

# DICTIONARIES

birthdays = {}
birthdays["Luke Skywalker"] = "5/24/19"
birthdays["Obi-Wan Kenobi"] = "3/11/57"
birthdays["Darth Vader"] = "4/1/41"
print birthdays

if "Yoda" in birthdays:
	print "Yep"
else:
	birthdays["Yoda"] = "Unknown"
print birthdays

for name in birthdays:
	print name, birthdays[name]

del(birthdays["Darth Vader"])
print birthdays


# I/O

""" 
Files have to be 
1. Open()'d (W = write (new), A = append, R = read)
2. Closed'd
"""

# Using while not EOF type method

poem = open("poem.txt","r")

line = poem.readline()
while line != "":
	print line, #comma to kill /n
	line = poem.readline()
poem.close()

# Using WITH method

with open("poem.txt","r") as poem:
	for line in poem.readlines():
		print line,

poem = open("poem.txt","a")

poem.writelines("\nHAHAHAHA ADDED A LINE")

with open("poem.txt","r") as poem:
	for line in poem.readlines():
		print line,


# FILE STRUCTURES

import os

pathname = "/Users/Fo/Dropbox/LearnPython/repo/io"
input2 = os.path.join(pathname,"test.txt")

with open(input2,"r") as input2file:
	for line in input2file.readlines():
		print line,

# EXERCISE: PRINT ALL IMAGE FILES IN THE IMAGE FOLDER
print " "
imgpath = "/Users/Fo/Dropbox/LearnPython/repo/images"

# get list of all files and folders in images
filesfolders = os.listdir(imgpath)

# print all files
for file in filesfolders:
	if os.path.isfile(os.path.join(imgpath,file)):
		print os.path.join(imgpath,file)

# using glob.glob, which returns a list of files that
# match a path and can be used to match wildcards

import glob
print "ONLY PNGS: "
possible_pngs = os.path.join(imgpath,"*.png")
for file in glob.glob(possible_pngs):
	print os.path.join(imgpath,file)



# WALK
print "WALKING AND RENAMING: "
for current, sub, files in os.walk(imgpath):
	for file in files:
		# Rename any PNGs to JPGs
		if file.lower().endswith(".png"):
			oldname =  os.path.join(current,file)
			newname = oldname[0:len(oldname)-4]+".jpg"
			os.rename(oldname,newname)

print "ONLY JPGS: "
possible_jpgs = os.path.join(imgpath,"*.jpg")
for file in glob.glob(possible_jpgs):
	if os.path.exists(os.path.join(imgpath,file)):
		print os.path.join(imgpath,file)


# 

