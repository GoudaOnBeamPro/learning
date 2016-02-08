from sys import argv

script, my_file = argv

print "We're now going to print your lovely file."

target = open(my_file)

print target.read() + 'We have now printed your lovely file. Thank you.'

target.close()
