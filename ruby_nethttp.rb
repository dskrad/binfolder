#!/usr/bin/env ruby
#Copyright DSK 2013

require 'net/http'

Net::HTTP.start('www.ruby-lang.org', 80) do |http|
  puts http.get('/en/about/license.txt').body
end
puts ARGV[0..2]
