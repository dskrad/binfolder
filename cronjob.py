#!/usr/bin/env python
# copyright DSK 2012
import datetime

def main():
  """write time to log file"""
  t = datetime.datetime.now()
  d = open('/Users/david/bin/cronjob.log', 'a')
  d.write(str(t))
  d.write('\n')
  d.close()
  return
# Insert standard boilerplate that calls main()
if __name__ == '__main__':
  main()
