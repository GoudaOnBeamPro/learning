# \t is for tabbing
tabby_cat = "\tI'm tabbed in."
# \n is for a new line
persian_cat = "I'm split\non a line."
# \\ escapes a backslash
backslash_cat = "I'm \\ a \\ cat."

# this is pretty self explantory
# To answer Dtudy Drills #3, I cannot immediately see why I would use
# single-quotes for this instead of double-quotes.
# Later in the cpater, Zed explains that it's just a style preference.
# I think I like the double-quotes better, but we'll see.
fat_cat = '''
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
'''

# now it's time to print that shit out baby
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Zed wants me to get really crazy right here... hold on to your butts!
#
# while (i<=10):
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i
#
# Yeah... that didn't look so pretty over SSH. 
