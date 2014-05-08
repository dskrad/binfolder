#!/usr/bin/env python
# copyright DSK 2012
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)
# ok, that *args is pointless, just do this
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

print_two("David","K")
print_two_again("David","Shoja")
