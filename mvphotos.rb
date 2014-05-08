#!/usr/bin/env ruby
#Copyright DSK 2013

require "fileutils"

input = ARGV[0]
output = ARGV[1]

Dir[input].each do |folder| 
  tomove = Dir.glob(File.join("**", folder, "**", "*.JPG"))
  tomove += Dir.glob(File.join("**", folder, "**", "*.MOV"))
  tomove += Dir.glob(File.join("**", folder, "**", "*.PNG"))
  tomove += Dir.glob(File.join("**", folder, "**", "*.AVI"))
  tomove.each do |x|
    FileUtils.mv(x, output, :verbose => true)
  end
end
