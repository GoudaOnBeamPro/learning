from sys import argv

script, filename = argv

# First we open the file that was created in the normal excercise
textfile = open(filename)

#Next we print its contents
print textfile.read()

# Now we close the damn thing
textfile.close()
