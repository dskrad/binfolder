#!/usr/bin/env python
# copyright DSK 2013

import os
from sys import argv

for arg in argv[1:]:
  st = ("HandBrakeCLI -i {} -Z Normal -o {}").format(arg, arg[:-3]+"mp4")
  print st
  os.system(st)
