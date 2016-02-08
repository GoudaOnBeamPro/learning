# this is the setup of the joke. is uses a formatter to put the number 10
# inside of the string
# NOTICE how you were able to use a formatter in the variable declaration
# You figured that out yourself last lesson. Good job Jared. 12/23/2015 
x = "There are %d types of people." % 10
# this joke is getting old already
binary = "binary"
# this is another string variable. wheeeeeee
do_not = "don't"
# Here it is boys and girls. The punchline. Notice the formatter input in
# variab;es declaration again. Good shit.
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the setup
print x
# prints the punchline. notice how it's a new line!
print y

# notice how with the %r formatter, it will print the string x in single quotes
print "I said: %r." % x
# and notice here how you put the single quotes around it this time.
print "I also said: '%s'." % y

# boolean baby namsayin ayyyyy
hilarious = False
# okay so you accidentally hit F1 in Vim, and noticed that doing :q
# only made it close the current buffer (which was the help stuff from 
# hitting F1)
joke_evaluation = "Isn't that joke so funny?! %r"

# So this is cool. Here the variable is called and THEN the formatter is 
# put in. Neat huh?
print joke_evaluation % hilarious

# This is a comment above a
w = "This is the left side of... "
# line of sting variables that
e = "a string that has a right side."

# are concatenated in the print function.
print w + e
