#!/usr/local/bin/python3

#read the lines from a file
fh = open('lines.txt');
for line in fh.readlines():
  print(line, end="");
