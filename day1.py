phrase = "Hello, world"
print phrase

# python is CaSe SenSiTive for variables

phrase2 = """earendil was a mariner who tarried in the avernin
he built a boat of timber felled in nimbrethil to journey in
her sails he wove of silver fair of silver were her lanterns made
her prow was fashioned like a swan and light upon her banners laid"""

print phrase2

# triple quotes for SUPER LONG STRINGS that also
# preserve       white  s p a   c e 

"""SUPER LONG COMMENT FROM HELL"""

# TRIPLE QUOTES for super long COMMENTS


# STRING FUNCTIONALITY

#### Length
string = "ned i-gwilith"
length = len(string)
print length

#### Concat
string2 = "i feel it in"
mashup = string + " " + string2
print mashup
# Or more easily, with commas to add spaces 
print string,string2

#### Substring
print string[0]
print string[0:3]
print string[:5] #from start to 5
print string[5:] #from 5 to end
print string[:] #either direction

# PYTHON STRINGS ARE IMMUTABLE; YOU HAVE TO REASSIGN

string3 = "earendil"
#string3[0] = "E" WILL throw an error
#string3 = "E" + string3[1:] instead

string4 = "EARENDIL"
string4 = string4.lower()
print string4

#user_input = raw_input("Say somming: ")
#print "Y'said: ", user_input

stringint = "12131414"
print stringint*4
stringint = int(stringint)
print stringint*4

flint = "9289"
print flint*4
flint = float(flint)
print flint*4

string5 = "whoobageong"
int1 = 2909204
str(int1)
print string5,int1


# Python 3 style print format
name = "Earendil"
trade = "mariner"
num_ships = "12"
print "{} was a {} who had {} ships".format(name, trade, num_ships)


# Search within strings

bigstring = "a tralala lalley here down in the valley your beards are a-wagging"
print bigstring.find("beards") #returns index location of search, otherwise -1


# TESTING GIT

# MAKING A CHANGE

# OMG I THINK THAT MAY HAVE WORKED

# ADDING VERSUS COMMITTING 