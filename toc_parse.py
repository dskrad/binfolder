#!/usr/bin/env python
# copyright DSK 2012
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('parse.html','r'))
for li in soup.find_all('li'):
    for a in li.find_all('a'):
      a.insert(2, a.parent.text)
      a.parent.contents[0].replace_with('')

fout = open('parsed.html','w')
fout.write(str(soup))
fout.close()
