#!/usr/bin/env python
import os, json
from subprocess import check_output
from pushbullet import note

fp = "/media/backup/Dropbox/Apps/PlainText 2/puff.json"
mp3_path = "/symserv/audio/"
args = ["youtube-dl","-x", "-t", "--audio-format=mp3"]
with open(fp) as fo:
  js = json.load(fo)
print js
if js['state'] == 0:
  args.append(js['id'])
  os.chdir(mp3_path)
  result = check_output(args)
  for f in os.listdir("."):
    if js['id'] in f:
      note("youtube-dl", result)
      url = "http://d-k.mooo.com/Roku/Audio/" + f
      title, descr = "-".join(f.split("-")[:-1]), ""
      js['title'] = title
      result = check_output(["puff.py", url, title, descr])
      note("Puff.py", result)
  js['state'] = 1
  with open(fp,"w") as fw:
    json.dump(js, fw, separators=(",\n", ": "))
