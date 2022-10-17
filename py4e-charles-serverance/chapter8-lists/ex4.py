"""
Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you determine that? 
How would you produce the list of all the words that Shakespeare used? Would you download 
all his work, read it and track all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, 
that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of 
unique words, which will contain the final result. Write a program to open the file romeo.txt 
and read it line by line. For each line, split the line into a list of words using the split 
function. For each word, check to see if the word is already in the list of unique words. 
If the word is not in the list of unique words, add it to the list. When the program completes, 
sort and print the list of unique words in alphabetical order.
"""

# imports
from cmath import log
import sys
from functions import openFile


# File Variables
DATA_PATH = "../data/"
FILE_FORMAT = ".txt"
LOG_FILE_PATH = "log-ex4.txt"

# Result variables
uniqueWords = []


# Code
fhandle = openFile(DATA_PATH, FILE_FORMAT)

for line in fhandle:
  line = line.rstrip().lower()
  if len(line) == 0: continue # Guard clause

  wordsInLine = line.split()
  for word in wordsInLine:
    if word in uniqueWords: continue # Guard clause
    uniqueWords.append(word)
# end FOR

fhandle.close()


logFile = open(LOG_FILE_PATH, 'w')

logFile.write("Unique Words found in the small excerpt by Shakespeare\n\n")

for word in sorted(uniqueWords):
  logMessage = f"{word}\n"
  logFile.write(logMessage)

print("Completed! Bye Bye")
logFile.close()


