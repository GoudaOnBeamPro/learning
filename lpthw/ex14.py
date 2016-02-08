from sys import argv

script, user_name, age = argv
prompt = '>>> '

if int(age) < 18: 
    quip = "You're quite the smart kid, huh?"
else:
    quip = "Sounds about right."

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r to liking me.
You live in %r. Not sure where that is.
And you have a %r computer. %s
""" % (likes, lives, computer, quip)
