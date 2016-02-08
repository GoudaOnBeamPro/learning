# This get s the argv function thing from the sys module
from sys import argv

# This unpacks argv into two variables
script, filename = argv

# This creates a variable called txt and the file name from argv is inserted
# The vriable is now a file object.
txt = open(filename)

# this orints the filename unpacked from argv
print "Here's your file %r:" % filename
# This is hwere shit gets crazy. This tells the txt file object to read itself
# and the result is printed (from the rint func, not by itself)
print txt.tell()

# print "Type the filename again:"
# this is where we do it again but take input from the raw_input func
# file_again = raw_input("> ")

# This opens the file in the variable, making it a file object
# txt_again = open(file_again)

# Prints it with the read func on itself. rememebr, the .read() doens't make
# it orint, the print func does
# print txt_again.read()
