#!/usr/bin/env ruby

require 'nokogiri'
require 'fileutils'

parsed = Nokogiri::HTML(open(ARGV[0]))

# for each img tag, check mimetype of src file and add
# appropriate extension. also, change src to point to 
# the new file
parsed.css("img").each do |img|
  i_file = img["src"]
  mime = `file -b --mime-type #{i_file}`
  if mime =~ /jpeg/  
    FileUtils.mv(i_file, i_file + ".jpg", :verbose => true)
    img["src"] = i_file + ".jpg"
  elsif mime =~ /gif/
    FileUtils.mv(i_file, i_file + ".gif", :verbose => true)
    img["src"] = i_file + ".gif"
  end
  # puts img["src"]
end

# write the output to file
File.open("fixed_imgs.htm", "w") { |x| x.write(parsed) }
