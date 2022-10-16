"""
Exercise 1: Write a program to read through a file and print the contents of the file 
(line by line) all in upper case. Executing the program will look as follows:
"""

fileName = '../data/mbox-short.txt'

try:
  fhand = open(fileName)
except: 
  print(f"File {fileName} not found")

for line in fhand: 
  line = line.rstrip().upper()
  print(line)

