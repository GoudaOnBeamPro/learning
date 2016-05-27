#i = 0
#numbers = []
#
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

#Study Drill Part 1
#print "What's the limit of the list?"
#a = int(raw_input("> "))
#
#def list_numbers(a):
#    """This function might add numbers to a list?"""
#    i = 0
#    numbers = []
#
#    while i < a:
#        print "At the top i is %d" % i
#        numbers.append(i)
#
#        i += 1
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % i
#
#    print "The numbers: "
#
#    for num in numbers:
#        print num
#
#    return
#
#list_numbers(a)

#Study Drill Part 2
print "What's the limit of the list?"
a = int(raw_input("> "))

print "What is the desired increment?"
n = int(raw_input("> "))

def list_numbers():
    """This function might add numbers to a list?"""
    i = 0
    numbers = []

    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)

        i += n
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

    return

list_numbers()
