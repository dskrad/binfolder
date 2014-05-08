#!/usr/bin/env python
# copyright DSK 2012
from subprocess import Popen, PIPE

f = Popen(["airport", "-I"],stdout=PIPE) # call command and pipe stdout
result = f.communicate()[0] # tuple (stdout,stderr) is retrieved via communicate, so [0] is just stdout

if "SSID: DavesAPE" in result:
  print "Connected to DavesAPE"
elif "visitor-hh" in result:
  print "Connected to visitor-hh"
else:
  print "Not connected!!"
