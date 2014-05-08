#!/usr/bin/env python
import os
from subprocess import check_output
from pushbullet import note

puffer_path = "/media/backup/Dropbox/Apps/PlainText 2/Puffer.txt"
mp3_path = "/symserv/audio/"
args = ["youtube-dl","-x", "-t", "--audio-format=mp3"]

if os.path.exists(puffer_path):
  ytid = open(puffer_path, 'r').read().strip()
  args.append(ytid)
  os.chdir(mp3_path)
  result = check_output(args)
  for f in os.listdir("."):
    if ytid in f:
      note("yt-puffer", result)
      url = "http://d-k.mooo.com/Roku/Audio/" + f
      title, descr = "-".join(f.split("-")[:-1]), ""
      result = check_output(["puff.py", url, title, descr])
      note("Puff.py", result)
  with open(puffer_path, 'w') as fn:
    fn.close()
