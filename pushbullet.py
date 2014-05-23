#!/usr/bin/env python
from urllib import urlopen, urlencode
import sys, os
key = os.environ['PUSHBULLET_APIKEY']
device = os.environ['PUSHBULLET_IPHONE']
push_url = "https://%s:@api.pushbullet.com/api/pushes" % key

def note(*args):
  title, body = args[0], ""
  if len(args) == 2:
    body = args[1]
  params = urlencode({
    #"device_iden": device,
    "type": "note",
    "title": title,
    "body": body
    })
  urlopen(push_url, params)

def link(*args):
  title, url = args
  params = urlencode({
    #"device_iden": device,
    "type": "link",
    "title": title,
    "url": url
    })
  urlopen(push_url, params)

def main():
  ntype, args = sys.argv[1], sys.argv[2:]
  if ntype == "note":
    note(*args)
  if ntype == "link":
    link(*args)

if __name__ == "__main__":
  main()
