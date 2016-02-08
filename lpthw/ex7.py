# Aight so we gotta comment shit again
print "Mary had a little lamb."
# this formatter throws a string in directly. beautiful
print "Its fleece was white as %s." % 'snow'
# try doing this without getting the song stuck in your head
print "And everywhere that Mary went."
# rememebr that concatenate thing from earlier? this is another example of
# an operation done on a string. This multiplies the string by ten and 
# prints the shit out of it
print "." * 10 # what'd that do?

# okay I'm not gonna comment on all of these lines, but there's something
# important to learn here Vi/Vim wise. Yanking. From what I've read, it seems
# that yanking in Vi will delete the line, but here in Vim it seems to have
# just copied it. I then used the p command to pasted the line (after the 
# current line. Good shit.
end1 = "S"
end2 = "p"
end3 = "a"
end4 = "c"
end5 = "e"
end6 = "B"
end7 = "u"
end8 = "r"
end9 = "g"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5, 
# So that comma was cool right? That added a space at the end of the line
# and also didn't start a new line, even with another print function.
print end6 + end7 + end8 + end9
# ALSO when you edited this to make it say "Space Burg" you used 
# the command d$ to delete till the end of the line. It was AWESOME!!!
