from __future__ import division

def CtoF(cel):
	f = cel * 9/5 + 32
	return f

def FtoC(fah):
	c = (fah-32) * 5/9
	return c

print "72 degrees F =", FtoC(72), "degrees C"
print "37 degrees C =", CtoF(37), "degrees F"