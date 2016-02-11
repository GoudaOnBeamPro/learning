# Grabs argv from the sys module
from sys import argv

# Assigns the script's name and the file stated after it in the command to argv
script, input_file = argv

# Creates a funtion that prints the entire contents of a file with read()
def print_all(f):
    # Prints the entire contents of the file
    print f.read()

# Creates a function that "rewinds" to the beginning of the file
def rewind(f):
    # Uses seek() to go back to the first byte in the file
    f.seek(0)

# Creates a function that prints the number of the line and the line of a file
def print_a_line(line_count, f):
    # Prints the number of line being read, then the line itself
    # Notice how current_line becomes line_count when passed here
    print line_count, f.readline(), # readline() also prints the \n
                                    # that's at the end of each line in the file
                                    # so I added the comma at the end to make it
                                    # less ugly. unlike this comment.

# Makes the variable current_file and assigns it the file object
current_file = open(input_file)

print "First let's print the whole file:\n"

# Calls the function print_all() with current_file as the arg to pass as f
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

# Calls the function rewind() with current_file as the arg to pass as f
rewind(current_file)

print "Let's print three lines:"

# Prints the first line in the file with readline()
current_line = 1
print_a_line(current_line, current_file)

# Adds one to the line count and prints that line the same way
current_line += 1 # Current_line is now 2. I was wondering when += would show up
print_a_line(current_line, current_file)

# Adds one again to the line count and prints that line
current_line += 1 # Current_line is now 3.
print_a_line(current_line, current_file)

# Always close the file for good measure, right Zed?
current_file.close()
