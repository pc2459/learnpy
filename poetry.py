import random


# Create vocabularies for the poem to come from...
nouns = ["mariner","marinade","marina","marinara"]
verbs = ["tarried","tarred","terrified","turned"]
adjectives = ["fair","furry","fine","fluid"]
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
while(noun2==noun1)
	noun2 = random.choice(nouns)
noun3 = random.choice(nouns)
while(noun2==noun3)
	noun3 = random.choice(nouns)

# Assign the adjectives

adjective1 = random.choice(adjectives)
adjective2 = random.choice(adjectives)
while(adjective2==adjective1)
	adjective2 = random.choice(adjectives)
adjective3 = random.choice(adjectives)
while(adjective3==adjective1)
	adjective3 = random.choice(adjectives)
