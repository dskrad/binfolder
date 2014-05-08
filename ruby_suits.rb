#!/usr/bin/env ruby
#Copyright DSK 2013

require "uri"
require "cgi"
require "open-uri"
require "nokogiri"

@cgi = CGI.new("html4") # create CGI object

url = @cgi["v"]  # uri argument "v" 
ng_obj = Nokogiri::HTML(open(url))

# build list of vid_sites from iframes
vid_sites = []
ng_obj.css("iframe").each do |iframe|
  vid_sites << iframe["src"]
end

@links = []
vid_sites.each do |link|
  begin
    response = open(link).read
    # scan finds all matches in the string ending in mp4
    # [^etc] character class exclusion list,
    # +? non-greedy (stops at first .mp4)
    @links << response.scan(/http:\/\/[^&;"]+?\.mp4/s)
  rescue
    # puts "Error:\t#{link}"
  end
end

@body = "" # will hold html code for resulting page
@links.each do |vidsite|
  vidsite.each do |mp4link|
    @body << @cgi.a("#{mp4link}") {"#{mp4link}"} +
    @cgi.br + @cgi.br # add links and separate by BR tags
  end
end

@cgi.out {      # cgi generated html output
  @cgi.html {
    CGI.pretty( # pretty print html
      @cgi.head { @cgi.title{"Beaming..."} } +
      @cgi.body {
      """
      <div style='font-size:2.5em'>
      #{@body}
      </div>
      """
      }) 
  }
}
