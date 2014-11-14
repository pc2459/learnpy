import os
import glob

# this script should delete any JPGs under 2KB

imgpath = "/Users/Fo/Dropbox/LearnPython/repo/images/little pics"

for current, sub, files in os.walk(imgpath):
	for file in files:
		size = os.path.getsize(os.path.join(current,file))
		print "Working with {} of size {}".format(file, size)
		# check to see if they are JPGs
		if file.lower().endswith(".jpg"):
			# check if they are smaller than 2KB
			if os.path.getsize(os.path.join(current,file)) < 2000:
				os.remove(os.path.join(current,file))
			else:
				print "we do nothing; it's too big"
		else:
			print "we do nothing; not a jpg"
