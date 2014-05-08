#!/usr/bin/env python
# copyright DSK 2012
from bs4 import BeautifulSoup
import sys

fin = BeautifulSoup(open(sys.argv[1]),'xml')
fout = BeautifulSoup('','xml')

playOrder = 1

for item in fin.find_all('a'):
  src = item['href']
  title = item.string
  kwargs = {'id': src[:-4], 'playOrder': playOrder}
  stanza = BeautifulSoup('','xml')
  nt = stanza.new_tag('text')
  nt.string = title
  stanza.append(nt)
  stanza.find_all('text')[0].wrap(stanza.new_tag('navLabel')).wrap(stanza.new_tag('navPoint', **kwargs))
  kwargs = {'src': src}
  stanza.navLabel.insert_after(stanza.new_tag('content', **kwargs))
  fout.append(stanza.navPoint)
  playOrder += 1

foutput = open('ncx.ncx','w')
foutput.write(str(fout.prettify()))
foutput.close()
