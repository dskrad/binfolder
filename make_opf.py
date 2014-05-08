#!/usr/bin/env python
# copyright DSK 2012
from bs4 import BeautifulSoup
import sys

tocfile = BeautifulSoup(open(sys.argv[1]))
opffile = BeautifulSoup('','xml')
for item in tocfile.find_all('a'):
  link = item['href']
  args = {'href': link, 'id': link[:-4], 'media-type': "application/xhtml+xml"}
  nt = opffile.new_tag('item', **args)
  opffile.append(nt)
  opffile.append("\n")
outf = open('index.opf','w')
outf.write(str(opffile))
outf.close()
