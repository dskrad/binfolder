#!/usr/bin/env python
import requests as R
import sys, os
key = os.environ['PUSHBULLET_APIKEY']
device = os.environ['PUSHBULLET_IPHONE']
url = "https://api.pushbullet.com/api/pushes"

def note(*args):
  title, body = args[0], ""
  if len(args) == 2:
    body = args[1]
  params = {
    #"device_iden": device,
    "type": "note",
    "title": title,
    "body": body}
  R.post(url, params, auth=(key,""))

def link(*args):
  title, url = args
  params = {
    #"device_iden": device,
    "type": "link",
    "title": title,
    "url": url}
  R.post(url, params, auth=(key,""))

def main():
  ntype, args = sys.argv[1], sys.argv[2:]
  if ntype == "note":
    note(*args)
  if ntype == "link":
    link(*args)

if __name__ == "__main__":
  main()
