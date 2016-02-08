midinitial = 'A.'
name = 'Jared %s Manning' % midinitial
age = 23 # not a lie
height = 68 # inches
weight = 170 # lbs... not a lie
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try ot get it exactly right
print "If I add %d, %d, and %d I get %r." % (
        age, height, weight, age + height + weight)
