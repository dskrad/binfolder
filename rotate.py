#!/usr/bin/env python
# copyright DSK 2013

# Insert standard boilerplate that calls main()
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def shift(word):
  for i in word:
    x = alph.index(i.lower())
    if x < 13:
      print alph[x+13],
    else:
      print alph[x-13],

shift("jbeq")
