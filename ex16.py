#!/usr/bin/env python
# copyright DSK 2012
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

print "Opening the file..."
f = open(filename, 'w')

print "Truncating the file. Goodbye!"
f.truncate()

print "Now I'm goint to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

f.write(line1)
f.write("\n")
f.write(line2)
f.write("\n")
f.write(line3)
f.write("\n")

print "And finally, we close it."
f.close()
