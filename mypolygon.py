#!/usr/bin/env python
# copyright DSK 2012
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

for i in range(4):
  fd(bob,100)
  lt(bob)

wait_for_user()
