#!/usr/bin/env python
# Takes markdown formatted file and converts all '# ' to none
# all '* ' to \t (tab), 4 spaces to tab, and line endings to DOS
# The result is an outline file suitable for Powerpoint

# Import sys and regular expressions
import sys
import re

filein = sys.argv[1]
f = open(filein, 'r')
fileout = f.name[:-4] + '.ppt'
d = open(fileout, 'w')

def main():
  text = f.read() # read entire input file
  result = re.sub(r'# ',r'',text) # sub headings
  result = re.sub(r'\* ','\t',result) # sub bullets
  result = re.sub('\n','\r\n',result) # sub LF(Unix) for CRLF(DOS)
  result = re.sub('^    ', '\t', result, flags=re.MULTILINE) # convert 4 spaces to tabs
  d.write(result) # write output to filename.ppt
  return

if __name__ == '__main__':
  main()
