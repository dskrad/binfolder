# open/close file

f_ile = File.open("file.txt","w")
f_ile.write("hello world")
f_ile.close

# open file block method

File.open("file.txt","w") do |x|
  x.write("hello file")
end

# read file block method

content = File.open("file.txt","r") do |x|
  x.read
end

# Append to a file

File.open(File.expand_path("~/file.txt"), "a") do |f|
  f << "hello append"
end

# For each line perform action

def load_file(file)
  comics = {}
  File.foreach(file) do |line|
    name, url = line.split(': ')
    comics[name] = url.strip
  end
  comics
end

comics = load_file("comics.txt")

# Directory and fileutils

# List files in directory

Dir.entries('/')
Dir['/*.txt']

# Copy a file

require "fileutils"

FileUtils.cp('/comics.txt', File.expand_path('~/comics.txt'))

# directory globbing

## count the files in my Downloads directory:

puts Dir.glob('Downloads/*').length   #=> 382

## count all files in my Downloads directory and in sub-directories

puts Dir.glob('Downloads/**/*').length #=> 308858

## list just PDF files, either with .pdf or .PDF extensions:

puts Dir.glob('Downloads/*.{pdf,PDF}').join(",\n")   


# download and write to file

require "open-uri"

kittens = open("http://placekitten.com/")
response_status = kittens.status
response_body = kittens.read[559,441]

puts response_status
puts response_body

kittenpic = open("http://placekitten.com/200/300")

File.open("kittens.jpg", "w") { |f| f.write(kittenpic) }

# parsing XML

require "open-uri"
require "rexml/document"

file = File.open("pets.txt")
doc = REXML::Document.new file
file.close

doc.elements.each("pets/pet/name") do |element|
  puts element
end