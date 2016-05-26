people = 20
cats = 3
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# Study Drill 4

if (cats > dogs and dogs == people):
    print "In this universe, there are more cats than both people and dogs."
if (cats < dogs and dogs == people):
    print "In this universe, there are more dogs than both cats and people."
