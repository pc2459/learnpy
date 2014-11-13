# create an empty circle of cats 
cat_list = {}

# append like 10 cats to a dictionary 
for i in range (0,10):
	cat_list[i] = "off"

i = 1

for cat in cat_list:
	# if you visit the cat on round N 
	if cat % i == 0: 
		# do the binary action of taking a hat on or off
		if cat_list[cat] == "off":
			cat_list[cat] = "on"
		else:
			cat_list[cat] = "off"
	# increment the way you go around the rounds
	i += 1

# print out results of cats with hats
for cat in cat_list:
	if cat_list[cat] == "on":
		print cat
