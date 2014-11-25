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

# STILL NOT QUITE GETTING WITH THE PROGRAM BUT BETTER

"""SO IF YOU GIT INIT IN THE FOLDER, THEN IN TERMINAL SET THE REMOTE DEETS,
THEN YOU'RE PRETTY MUCH GOOD TO GO USING SUBLIME SIDEBARGIT IF YOU SET 
GIT CONFIG --GLOBAL PUSH.DEFAULT MATCHING TO MAKE SURE IT ??? OVERWRITES FILES
 ON THE REMOTE END????

STEP 1: INSTALL GIT
STEP 2: SET YOUR USERNAME AND EMAIL
STEP 3: GET A GITHUB ACCOUNT
STEP 4: GET YOUR SSH SET UP 
STEP 5: GET A REMOTE REPO SET UP
STEP 6: GET A LOCAL REPO SET UP
STEP 7: GIT INIT IN YOUR LOCAL REPO
STEP 8: REMOTE ADD YOUR REMOTE REPO (I MEAN THIS SOUNDS OBVIOUS BUT NO)
STEP 9: ADD YOUR FILES
STEP 10: COMMIT YO CHANGES
STEP 11: PROFIT WHEN YOU PUSH
STEP 12: IF IT BITCHES, --GLOBAL PUSH.DEFAULT MATCHING

 """

 # Integer division in Python 2, non-integer division in Python 3
 # To correct in Pythong 2: from __future__ import division


# FUNCTIONS

def square(number):
    """Here is a docstring explaining that this returns a 
    square of a number."""
    sqr = number ** 2
    return sqr

input = 5
output = square(input)

print output


def cube(number):
    """Returns the cubed form of a number"""
    cube = number ** 3
    return cube

input2 = 10
output2 = cube(input2)
print output2

def multiply(first,second):
    """Returns the product of two numbers"""
    product = first * second
    return product

output3 = multiply(2,5)
print output3

for i in range(0,4):
    if i == 2:
        continue
    print i
print "Finished with i =", str(i)



from random import randint

print randint(1,6)

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
throw = 0
for i in range (0,10000):
    throw = randint(1,6) 
    if throw == 1:
        ones += 1
    elif throw == 2:
        twos += 1
    elif throw == 3:
        threes += 1
    elif throw == 4:
        fours += 1
    elif throw == 5:
        fives += 1
    elif throw == 6:
        sixes += 1
print (6*sixes+5*fives+4*fours+3*threes+2*twos+1*ones)/10000
print ones,twos,threes,fours,fives,sixes


# LISTS

desserts = ["ice cream", "cookies"]
print desserts

desserts.sort()
print desserts

print desserts.index("ice cream")

food = desserts[:]
food.extend(["broccoli","turnips"])
print food, desserts

food.remove("cookies")
print food
print food[0:2]


def twixtwenty(list):
    for i in list:
        if 1 < i < 20:
            print i

list1 = [2, 4, 8, 16, 32, 64]

twixtwenty(list1)


def enrollment_stats(list):
    enrollment = []
    tuition = []
    for i,j,k in list:
        enrollment.append(j)
        tuition.append(k)
    return enrollment
    return tuition

def mean(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum / len(list)
    return mean




