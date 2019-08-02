#!bin/bash/env python3
"""
Python script that works like the grep command
Searches a file with a given string and returns matching lines
Arguments: 
argv[1] the file to search
argv[2] the string used to search
returns the lines from that file that the string is found
"""
import sys

file = ''

try:
  file = sys.argv[1]
  string = sys.argv[2]
except exception as e:
  print(e)
for line in open (file):
    if string in line:
        print(line)
