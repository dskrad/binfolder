from urllib2 import urlopen

key = "MDAxNzgzOTYyMDEyMTUwMDkyMDM1ZWUwYw001"
url = "http://api.npr.org/query?apiKey="
params = "&numResults=3&action=Or&requiredAssets=audio&format=podcast"
url += key + params
npr_id = "2" # raw_input("Enter comma-separated NPR IDs or leave blank for none.")
#search_string =  raw_input("Enter your search string or leave blank for none.")
if (npr_id):
  #raw_input("Hit Enter to print your podcast.")
  if npr_id:
    url += "&id=" + npr_id
  #if search_string:
  #  url += "&searchTerm=" + search_string
  response = urlopen(url)
  output = response.read()
  print output #.decode("utf-8")
else: print "You must enter an NPR ID, a search term, or both."
