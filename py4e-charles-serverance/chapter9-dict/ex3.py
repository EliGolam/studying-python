"""
Exercise 3: Write a program to read through a mail log, build a 
histogram using a dictionary to count how many messages have come 
from each email address, and print the dictionary.
"""

import sys
from functions import openFile


# FILE
FILE_PATH = '../data/'
FILE_FORMAT = '.txt'
LOG_FILE = 'ex3-log.md'

# VARIABLES
emailCountDict = {}


fhandle = openFile(FILE_PATH, FILE_FORMAT)
if (fhandle is None): sys.exit()

for line in fhandle: 
  if not line.startswith('From '): continue

  words = line.rstrip().lower().split()
  if len(words) < 2 or not '@' in words[1]: continue

  email = words[1]
  emailCountDict[email] = emailCountDict.get(email, 0) + 1

fhandle.close()



logFile = open(LOG_FILE, 'w')
print("Logging results")

line = "# Log: Email senders\n\n"
logFile.write(line)

for email in emailCountDict:
  emailCount = emailCountDict[email]
  line = f"* From **{email}**: "

  if emailCount == 1: 
    line += f"1 email\n"
  else:
    line += f"{emailCount} emails\n"

  logFile.write(line)

logFile.write("\n")

logFile.close()
print("Logging completed")