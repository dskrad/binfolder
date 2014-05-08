#!/usr/bin/env python
# copyright DSK 2012
from os import popen
from sys import argv
for arg in argv[1:]:
  outfile = arg[:-4] + '.m4a'
  popen('ffmpeg -i '+arg+' -vn -acodec copy -absf aac_adtstoasc '+outfile)
