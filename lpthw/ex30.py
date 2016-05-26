people = 30
cars = 40
buses = 55


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

# Study Drills

if (buses > cars and cars > people):
    print "The buses out number us... DECEPTICONS!!"
elif (buses > cars and cars < people):
    print "This line won't print... just trust me. *peers through console*"
else:
    print "If this line actually prints, I'll go to bed. I dare you to try."
