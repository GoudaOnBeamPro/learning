formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        # The following line will print with double-quotes around it.
        # That's because of the single-quote used in the string. :)
        "But it didn't sing.",
        "So I said goodnight."
)

# After the study drills, see if you can do a formatter insert within another
# one. Should work.... right?
#
# Okay so on this last edit, I'm going to remove the commas. Hopefully the
# strings will print normally and without the spaces since I have the \n
# making new lines.
# OKAY SO it almost worked perfectly until the last line where the formatter
# was used. Let's try making it a string variable.
#
# OKAY SO that didn't work. Looks like using the comma in a print function does more that just add spaces. Reminds me of using parantheses.... say... Will
# that make it work??
#
# NOPE That didn't work either. Oh well. I've fixed it now. This is just here
# remember later. And also because I'm narcissistic and want to think I'll
# look back on these early days of learning programming.
#
# Dear diary,
#
#   Hey, it's me again. Apparently I didn't fix the last thing I commented
# about. I believe the problem might be that I'm still not using the commas
# to seperate the strings. Let's fix that and see what happens.
#
# With love,
# Jared Manning
#
# P.S. I also changed the string printed back to the formatter variable and 
# deleted the \n lines from the inner strings. That seems to have fixed all
# of my problems (even though the output is still ugly).
