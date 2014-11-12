from capitals import capitals_dict
import random

state = ''
capital = ''

game = 1

state = random.choice(capitals_dict.keys())
capital = capitals_dict[state]

capital = capital.lower()

print "The state is {}".format(state)
answer = raw_input("What is its capital? ")
answer = answer.lower()

while game == 1:
	if answer == capital:
		game = 0
		print "YAY"
	elif answer == "exit":
		# Return formatting
		capital = capitals_dict[state]
		print "The answer was {}".format(state)
		print "Goodbye."

print "Correct!"