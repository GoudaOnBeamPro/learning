#i = 0
#numbers = []

#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)
#
#    i += 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i
#
#
#print "The numbers: "
#
#for num in numbers:
#    print num

#Study Drills
print "What's the limit of the list?"
a = raw_input("> ")

def list_numbers(a):
    """This function might add numbers to a list?"""
    i = 0
    numbers = []

    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

    return

list_numbers(a)
