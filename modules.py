#!/usr/bin/python
#copyright DSK 2012

def Head():
  print "Content-Type: text/html";     # HTML is following
  print                               # blank line, end of headers
  print "<html>"
  print "<head>"
  print "<title>Module Listing</title>"
  print "</head>"
  print "<body>"
  return

def Foot():
  print "</body>"
  print "</html>"
  return

def Modules():
  try:
    print help('modules')
    return
  except:
    print 'Error'
    return

Head()
print '<pre>'
Modules()
print '</pre>'
Foot()