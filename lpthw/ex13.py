from sys import argv

script, name, age, height, weight = argv

# These print out what was unpacked by argv
print "The scrpit is called:", script
print "Your name is:", name
print "Your age is:", age
print "Your height is:", height
print "Your weight is:", weight

# Here I've made a fun little test to try out if statements and using
# raw_input() with argv

# Asks for the name that was passed to argv
w = raw_input('What is your name? ')
# Tests to see if it matches what was unpacked by argv. If it is, the next
# line of code executes. If not, the code under else: executes.
if w == name:
    print "That's correct! Your name is %s." % name
    else:
    print "I'm afraid that's incorrect. Your name is actually %s." % name

# Same as before. This should be self explanatory
x = raw_input('What is your age? ')

if x == age:
    print "That's correct! You are %s." % age
    else:
    print "I'm afraid that's incorrect. Your age is actually %s." % age

y = raw_input('What is your height (in inches)? ')

if y == height:
    print "That's correct! You are %s inches tall." % height
    else:
    print "I'm afraid that's incorrect. Your height is actually %s." \
          % height
z = raw_input('What is your weight (in lbs.)? ')

if z == weight:
    print "That's correct! You weigh %s lbs." % weight
    else:
    print "I'm afraid that's incorrect. Your weight is actually %s." \
          % weight
