"""
Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. Then you can use the in operator as a fast way to 
check whether a string is in the dictionary.
"""

import sys


DATA_PATH = '../data/'
FILE_NAME = 'words.txt'

LOG_FILE = 'ex1-log.txt'

# Open file
try:
  words = open(DATA_PATH + FILE_NAME)
except FileNotFoundError:
  print("File not found")
  sys.exit()

wordCounter = {}

for line in words:
  lineWords = line.rstrip().lower().split()
  for word in lineWords:
    wordCounter[word] = wordCounter.get(word, 0) + 1

words.close() 



log = open(LOG_FILE, 'w')

for word in wordCounter: 
  line = f"{word}: {wordCounter[word]}\n"
  log.write(line)

log.close()
