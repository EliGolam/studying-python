"""
Exercise 2: Write a program that categorizes each mail message by which 
day of the week the commit was done. To do this look for lines that start 
with “From”, then look for the third word and keep a running count of each 
of the days of the week. At the end of the program print out the contents 
of your dictionary (order does not matter).Exercise 2: Write a program that 
categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with “From”, then look for the third 
word and keep a running count of each of the days of the week. At the end of 
the program print out the contents of your dictionary (order does not matter).
"""

import sys
from functions import openFile



# FILE
FILE_PATH = '../data/'
FILE_FORMAT = '.txt'
LOG_FILE = 'ex2-log.txt'

# Counter
emailCountDict = {}

fhandle = openFile(FILE_PATH, FILE_FORMAT)
if (fhandle is None): sys.exit()


for line in fhandle:
  if not line.startswith('From '): continue # Guard clause

  words = line.rstrip().lower().split()
  if len(words) < 3: continue

  day = words[2]
  emailCountDict[day] = emailCountDict.get(day, 0) + 1
# End FOR loop

fhandle.close()

print(emailCountDict)


