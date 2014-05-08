#!/usr/bin/env python
# copyright DSK 2013
import os
import sys
import hashlib

def hashfile(path, blocksize=65536):
  """md5hash of each file given the path"""
  afile = open(path, 'rb')
  hasher = hashlib.md5()
  hasher.update(afile.read(blocksize))
  #buf = afile.read(blocksize)
  #while len(buf) > 0:
  #  hasher.update(buf)
  #  buf = afile.read(blocksize)
  afile.close()
  return hasher.hexdigest()

def findDups(parentDir):
  """Dups in format {hash:[paths]}"""
  dups = {}
  for dirName, subDirs, fileList in os.walk(parentDir):
    # Modify the lists in place to exclude dot folders and files
    subDirs[:] = [d for d in subDirs if d[0] != "."]
    fileList = [f for f in fileList if f[0] != "."]
    print "Scanning %s" % dirName
    for fileName in fileList:
      # Get path of file
      path = os.path.join(dirName, fileName)
      # Exclude 0 byte files
      if os.path.getsize(path) > 0:
        # Calculate the hash
        file_hash = hashfile(path)
        # Add or append the path to the dict
        if file_hash in dups:
          dups[file_hash].append(path)
        else:
          dups[file_hash] = [path]
  return dups

def joinDicts(dict1,dict2):
  """for each item in dict2, add to list if exists in dict1 else add new key:[value] pair"""
  for key in dict2.keys():
    if key in dict1:
      dict1[key] = dict1[key] + dict2[key]
    else:
      dict1[key] = dict2[key]

def printResults(dict1):
  """Print resulting dictionary"""
  results = list(filter(lambda x: len(x) > 1, dict1.values()))
  if len(results) > 0:
    print "Duplicates found!!"
    print "Although the filenames may differ, the following are identical copies"
    print "------------------"
    for result in results:
      for i in result:
        print "  %s" % i
      print "------------------"
  else:
    print "No duplicates found :-)"


def main():
  """Takes folders as commandline arguments and finds
  all duplicates then prints the results"""
  if len(sys.argv) > 1:
    dups = {}
    dirs = sys.argv[1:]
    for i in dirs:
      if os.path.exists(i):
        joinDicts(dups, findDups(i))
      else:
        print "%s is not a valid path" % i
        sys.exit()
    printResults(dups)
  else:
    print "Usage: python find_dups.py folder or find_dups.py folder1 folder 2 etc."


if __name__ == '__main__':
  main()
