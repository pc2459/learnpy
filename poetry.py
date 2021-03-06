import random


# Create vocabularies for the poem to come from...
nouns = ["mariner","marinade","marina","marinara"]
verbs = ["tarried","tarred","terrified","turned"]
adjectives = ["fair","furry","fine","fluid", "average"]
prepositions = ["upon","in","like","under","after"]
adverbs = ["swiftly","brightly","softly"]

# Create placeholders for the words
noun1 = ''
noun2 = ''
noun3 = ''
adjective1 = ''
adjective2 = ''
adjective3 = ''
verb1 = ''
verb2 = ''
verb3 = ''
prepo1 = ''
prepo2 = ''

# Assign the nouns, ensuring there are no repeats
noun1 = random.choice(nouns)
noun2 = random.choice(nouns)
while(noun2==noun1):
	noun2 = random.choice(nouns)
noun3 = random.choice(nouns)
while(noun2==noun3):
	noun3 = random.choice(nouns)

# Assign the adjectives

adjective1 = random.choice(adjectives)
adjective2 = random.choice(adjectives)
while(adjective2==adjective1):
	adjective2 = random.choice(adjectives)
adjective3 = random.choice(adjectives)
while(adjective3==adjective1):
	adjective3 = random.choice(adjectives)

verb1 = random.choice(adjectives)
verb2 = random.choice(adjectives)
while(verb2==verb1):
	verb2 = random.choice(adjectives)
verb3 = random.choice(adjectives)
while(verb3==verb1):
	verb3 = random.choice(adjectives)

adverb1 = random.choice(adverbs)

prepo1 = random.choice(prepositions)
prepo2 = random.choice(prepositions)
while (prepo2 == prepo1):
	prepo2 = random.choice(prepositions)


# Print poem
if adjective1[0] == 'a':
	print "An {} {}".format(adjective1,noun1)
else:
	print "A {} {}".format(adjective1,noun1)
print "A {} {} {} {} the {} ".format(adjective1,noun1,verb1,prepo1,adjective2)
print "  {}".format(noun2)
print "{}, the {} {}".format(adverb1,noun1,verb2)
print "the {} {} {} a {} {}".format(noun2,verb3,prepo2,adjective3,noun3)
