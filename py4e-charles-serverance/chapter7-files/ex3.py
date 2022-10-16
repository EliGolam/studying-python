"""
 Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. 
 Modify the program that prompts the user for the file name so that it prints a funny message when the user types in 
 the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist
 """

import sys

 # File variables
DATA_PATH = '../data/'
FILE_FORMAT = '.txt'
logFileName = 'log.txt'
findModule = 'X-DSPAM-Confidence:'

# Results Variables
countLines = 0
writtenLines = 0

fileNameInp = input("Input file name: ").lower()


if fileNameInp.find('.txt') == -1:
  fileNameInp += FILE_FORMAT

# Open File
try: 
  fhandle = open(DATA_PATH + fileNameInp)
except FileNotFoundError: 
  if(fileNameInp == 'na na boo boo.txt'):
    print("NA NA BOO BOO TO YOU - You have been punk'd")
  
  else:
    print(f"File Cannot be found: ({DATA_PATH + fileNameInp})")
    sys.exit()
  

for line in fhandle: 
  countLines += 1
  if line.strip() == '': continue
  writtenLines += 1

# Close File
fhandle.close()

log = f"There are {countLines} in {fileNameInp}.\nThe number of non-empty lines is: {writtenLines}"
print(log)