#!/usr/bin/env python
# copyright DSK 2013
from datetime import timedelta, datetime
wakeup, ninty_min = datetime(2014,1,1,6,5), timedelta(minutes=90)
print "For a wakeup time of %s" % wakeup.strftime("%H:%M")
print "Fall asleep at: "
for x in xrange(1,7):
  sleep = wakeup - (x * ninty_min)
  print "%s" % sleep.strftime("%I:%M %p")
