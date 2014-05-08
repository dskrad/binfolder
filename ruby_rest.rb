require "rubygems"
require "rest-client"
require "crack"

rem_url = "http://maps.googleapis.com/maps/api/geocode/xml?address=1400+Broadway,+New+York,+NY&sensor=false"

response = RestClient.get(rem_url)
puts response.code
#=> 200

#puts res.body
#=> <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
#=> "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#=> <html lang="en" dir="ltr" class="client-nojs" xmlns="http://www.w3.org/1999/xhtml">
#=> <head> ...
parsed_res = Crack::XML.parse(response)

status = parsed_res["GeocodeResponse"]["status"]
lat = parsed_res["GeocodeResponse"]["result"]["geometry"]["location"]["lat"]
lng = parsed_res["GeocodeResponse"]["result"]["geometry"]["location"]["lng"]

puts "Status:\t#{status}"
puts "Lat:\t#{lat}"
puts "Long:\t#{lng}"