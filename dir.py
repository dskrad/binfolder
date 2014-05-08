#!/usr/bin/python
#copyright DSK 2012

import os

def Head():
  print "Content-Type: text/html";     # HTML is following
  print                               # blank line, end of headers
  print "<html>"
  print "<head>"
  print "<title>Dir Listing</title>"
  print "</head>"
  print "<body>"
  return

def Foot():
  print "</body>"
  print "</html>"
  return

def Dir(dir):
  path = os.listdir(dir)
  dirname = os.path.basename(dir)
  print "<h1>" + dirname + "</h1>"
  print "<ul>"
  for each in path:
    print "<li><a href='" + each + "'>" + each + "</a></li>"
  return

Head()
Dir('.')
Foot()
