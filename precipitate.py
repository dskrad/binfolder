#!/usr/bin/env python
# copyright DSK 2012
import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/ec260856a11d5e86/geolookup/forecast/q/CT/New_Britain.json')
parsed_json = json.loads(f.read())
f.close()
location = parsed_json['location']['city']
date = parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['pretty']
forecast = []
for i in range(4):
  forecast.append(parsed_json['forecast']['simpleforecast']['forecastday'][i])

print "Snowfall forecast for %s," % (location)
print date
for i in range(4):
  print "%s:  \t%s inches" % (forecast[i]['date']['weekday'], forecast[i]['snow_allday']['in'])
