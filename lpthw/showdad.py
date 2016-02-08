# When I made this, I was not comletely sure how to make functions, so when it
# doesn't understand the input, it just spits out a line saying it didn't 
# understand then moves on.
author = 'Zed A. Shaw'
book = 'Learn Python the Hard Way by %s' % author

print """
Hi dad! This is a little program I wrote
to show you some of the cool things I've
learned today while hammering away at the
book %s\n.
""" % book

print "\nI'm just going to ask you a few simple questions."
print "When answering a 'yes' or 'no' question, please"
print "use 'y' or 'n' for your response."
    
ready = raw_input('Are you ready? ')

if ready == 'y':
    print "\nGood! Let's get started.\n"
elif ready == 'n':
    print "\nAh, I see. Well, we're moving on anyways!\n"
else:
    print "\nI'm sorry, I didn't understand that... Moving on!\n"

name = raw_input('What is your name? ')

print "\nHello %s!\n" % name

day_going = raw_input("How is your day going? (say 1 for good, 2 for so-so, or 3 for bad) ")
strDayGoing = None

if day_going == '1':
    print "\nI'm glad you're having a good day.\n"
    strDayGoing = 'good'
elif day_going == '2':
    print "\nAw, cheer up ol' chum!\n"
    strDayGoing = 'so-so'
elif day_going == '3':
    print "\nI'm sorry to hear that... Moving on!\n"
    strDayGoing = 'bad'
else:
    print "\nI'm sorry, I didn't understand that... Moving on!\n"

fave_color = raw_input("What's your favorite color? ")

if fave_color.lower() == 'blue':
    print "\nI knew that already, dad. You're probably wearing",
    print "blue shirt too, right?\n"
else:
    print "\nThat... that can't be right! It's supposed to be blue!!\n"

lunch = raw_input('What did you have for lunch today? ')

print "\nMmmm! %s sounds delicious!\n" % lunch

print """
So let me get this straight...
Your name is %s.
You're having a %s day.
Your favorite color is %s.
And you had %s for lunch.
""" % (name, strDayGoing, fave_color, lunch)

correct = raw_input("Is all of that information correct? ")

if correct == 'y':
    print "\nGreat! Thanks for checking out all the stuff I learned today!",
    print "I'm now going to give you a brief tour of the script itself.\n"
elif correct == 'n':
    print "\nWelp, can't be my fault! I wrote this script perfectly!!\n"
else:
    print "\nSorry, I didn't get that. Oh well!\n"
