from __future__ import division

user_input = raw_input("Give us a number to factorise: ")

user_input = int(user_input)
factor = 1

while factor <= user_input:
	if user_input % factor == 0:
		print "{} is a divisor of {}".format(factor, user_input)
	factor = factor + 1