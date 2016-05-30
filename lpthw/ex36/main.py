# This is the main (and possibly only??) file for my little python game.
# Here's hoping this turns out well!
from sys import exit

def courtyard():
    print "You arrive at a grand courtyard filled with beautiful fountains"
    print "and lush gardens. To the north is the large entrance to the"
    print "castle, to the east is what appears to be an abandoned market,"
    print "and to the west the largest fountain in the area, and is the"
    print "fountain that seems to be running. What do you do?"

    next = raw_input("> ")

    if "north" in next:
        castle_gate()
    elif "east" in next:
        market()
    elif "west" in next:
        fountain()
    elif "south" in next:
        print "You are already at the south end of the courtyard."
        exit(0)
    else:
        print "Please say 'go north/east/west/south' or something."
        print "The game isn't THAT hard..."
        exit(0)

def castle_gate():
    print "This is a placeholder for castle_gate()"
    exit(0)

def market():
    print "This is a placeholder for market()"
    exit(0)

def fountain():
    print "This is a placeholder for fountain()"
    exit(0)

if __name__ == '__main__':
    courtyard()
