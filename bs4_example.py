#!/usr/bin/env python

# example of web scraping
# extracting table data from yahoo finance
# the find_all statement finds a known item in the table
# then the .parent.parent (etc.) finds the whole table
# the series of list comprehensions parses the text from
# each cell of the table

from bs4 import BeautifulSoup as BS
from urllib import urlopen

soup= BS(urlopen("http://finance.yahoo.com/q/op?s=AAPL+Options")) result = soup.find(text="AAPL131116C00220000")
# result is a list with one item, hence the [0] in the following list comprehension
opt_table = [ x for x in result.parent.parent.parent.parent ]
# this is "inception"! a list comp within a list comp!!
table_data = [ [x.text for x in y.children ] for y in opt_table ]
# print resulting tablized list
for i in table_data:
  print i
