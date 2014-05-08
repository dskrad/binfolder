#!/usr/bin/env ruby

require "open-uri"
puts "Content-type: text/calendar; charset=utf-8"
puts "Content-Disposition: inline; filename=calendar.ics"
puts ""
#puts "<html><head></head><body>"
#puts "it works!!"
url = "http://yale.medhub.com/functions/listeners/listener_calendar_sync.mh?_ics=a2c535f11a1ee31a0a675ff1cc8b7544"
puts open(url).read.gsub!(/\r/,"\r\n")
#puts "</body></html>"
