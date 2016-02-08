# Prints the string. Notice the comma at the end of the line. That's there
# to prevent it from starting a new line for raw_input().
print "How old are you?",
# Functions are love. Functions are life.
age = raw_input('> ')
print "How tall are you?",
# Notice how an input like 5' 8" will be printed as '5\' 8"'
height = raw_input('> ')
print "How much do you weigh?",
weight = raw_input('> ')

# When you typed this the first time, you put a $ (dollar sign) for the 
# second formatter and it threw you an error. Don't mess it up again, slick.
print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight)

# YO!! All data from raw_input() is converted to a string!
# Keep that in mind namsayin ;)
