from capitals import capitals_dict
import random

state = ''
capital = ''

game = 1

state = random.choice(capitals_dict.keys())
capital = capitals_dict[state]

capital = capital.lower()

print "The state is {}".format(state)

while game == 1:
	answer = raw_input("What is its capital? ")
	answer = answer.lower()
	if answer == capital:
		game = 0
		print "YAY"
	elif answer == "exit":
		# Return formatting
		capital = capitals_dict[state]
		print "The answer was {}".format(capital)
		print "Goodbye."

print "Correct!"