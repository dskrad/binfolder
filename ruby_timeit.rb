#!/usr/bin/env ruby

def timeit blockname, &block
  starting = Time.now
  block.call
  duration = Time.now - starting
  puts "#{blockname}: #{duration.to_s} seconds"
end

timeit "Count to 1 million" do
  num = 0
  1000000.times do
    num += 1
  end
end
