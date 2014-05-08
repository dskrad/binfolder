#!/usr/bin/env python
# copyright DSK 2012

def Cat(filename):
  try:
    f = open(filename)
    text = f.read()
    print '---', filename
    print text
  except IOError:
    print 'IO Error', filename

def main():
  args = sys.argv[1:]
  for arg in args:
    Cat(arg)

# This is the standard boilerplate that calls main()
if __name__ == '__main__':
  main()
