#!/usr/bin/python
# import regular expressions
import re
import sys

# Open file
f = open(sys.argv[1], 'r')

# findall() in file; returns a list of found strings

strings = re.findall(r'\# ', f.read())

# Print results
for string in strings:
  print string

"""
Repetition

Things get more interesting when you use + and * to specify repetition in the
pattern

+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
* -- 0 or more occurrences of the pattern to its left
? -- match 0 or 1 occurrences of the pattern to its left; also used to modify . and + to make them nongreedy

Leftmost & Largest

First the search finds the leftmost match for the pattern, and second it tries
to use up as much of the string as possible -- i.e. + and * go as far as
possible (the + and * are said to be "greedy").
"""
