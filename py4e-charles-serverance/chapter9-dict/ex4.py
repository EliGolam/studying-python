"""
Exercise 4: Add code to the above program to figure out who has the 
most messages in the file. After all the data has been read and the 
dictionary has been created, look through the dictionary using a 
maximum loop (see Chapter 5: Maximum and minimum loops) to find who 
has the most messages and print how many messages the person has.
"""

from functions import openFile
import sys

import ex3


fhandle = openFile(ex3.FILE_PATH, ex3.FILE_FORMAT)
