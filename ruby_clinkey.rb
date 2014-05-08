require 'open-uri'


base_url = 'http://www.clinicalkey.com/'
suffix_url = ''
page_url = base_url + suffix_url

page_data = open(page_url).read

loc_file = open('result.html', 'w')
loc_file.write(page_data)
loc_file.close