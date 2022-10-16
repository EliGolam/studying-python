from fnmatch import translate
import sys
import string
from typing import List

"""
EX 1: 
Write a program that reads the words in words.txt and stores them as keys in a 
dictionary. It doesn’t matter what the values are. Then you can use the in operator 
as a fast way to check whether a string is in the dictionary.
"""

wordsUsed = dict()

words = open('words.txt')
for lineNumber, line in enumerate(words):
    line = line.rstrip()
    wordsInLine = line.split() 
    for pos, word in enumerate(wordsInLine):
        key = word
        value = f'Word {pos + 1} in line {lineNumber + 1}'
        wordsUsed[key] = value
words.close()

wordsToFind = ['humans', 'boring', 'sham', 'WOW', 'lust', 'tasks']

for word in wordsToFind : 
    if word in wordsUsed : 
        print(f'{word} found: It\'s {wordsUsed[word]}') 
    else : 
        print(f'{word} not found')

logFile = open('log-test.txt', 'w')
for word in wordsUsed :
    line = f'{word}: {wordsUsed[word]}\n'
    logFile.write(line)
logFile.close()


"""
EX 2: 
Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for 
lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).
"""

# Testing array and file
# testStr = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# testStr2 = 'Saturnus has been dancing in the sky because they have nothing else to do'
# testFile = 'mbox-short.txt'


# Initialize an array for the days of the week
daysWeek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

# Find the 'date' function
def findInstances (stringToSearch, instancesArr) :
    arr = stringToSearch.rstrip().lower().split() # rsrtip + split + lower to create standardized value

    elementFound = None

    for element in arr:
        if element not in instancesArr: continue
        elementFound = element
        break

    return elementFound


# Dictionary for counting the days
dictDays = dict()
lineRecognizer = 'From'


# Open the file
fileName = 'mbox.txt'
try: 
    fhandle = open(fileName)
except:
    print(f'File {fileName} not found')
    sys.exit()


# For loop to find the right line
for line in fhandle: 
    if not line.startswith(lineRecognizer): continue # Guard statement

    day = findInstances(line, daysWeek)
    if day is None: continue

    dictDays[day] = dictDays.get(day, 0) + 1

# END FOR loop through fhandle
fhandle.close()


# Open file Log
logEmailDays = open('./logFiles/log-email-days.txt', 'w')

logEmailDays.write('Calculate Email amount for each day of the week\n\n')

for day in daysWeek:
    if day not in dictDays: continue

    dayStandardized = day[0].upper() + day[1:]
    line = f'{dayStandardized}: {dictDays[day]} Emails\n' if dictDays[day] != 1 else f'{dayStandardized}: {dictDays[day]} Email\n'
    logEmailDays.write(line)
    
logEmailDays.close()
# close log file



"""
EXERCISE 3: 
Write a program to read through a mail log, build a histogram using a dictionary to count how many messages 
have come from each email address, and print the dictionary.
"""

### TEST
testLine = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
testFile = 'mbox-short.txt'

# testStr = testLine.rstrip().split()
# print(f'Test - Stripped and split - Array: {testStr}')


###############################################################################
### FUNCTIONS

def findEmailinLine(line: str):
    searchArr = line.rstrip().split()
    pos = 1
    email = findEmailinArray(searchArr, pos)

    return email

def findEmailinArray (arr: List[str], pos: int):
    email = arr[pos]
    return email

# print(f'Test findEmail: {findEmailinArray(testStr, 1)}')
# print(f'Test findEmail: {findEmailinLine(testLine)}')

def countEmailSender (fileName: str, lineFinder: str):
    # Initialize Counter as a dictionary
    countSender = dict()

    # Open the file
    try:
        fhandle = open(fileName)
    except:
        print(f'File {fileName} Not Found')
        return None
    
    # FOR LOOP through file: fhandle
    for line in fhandle:
        line = line.rstrip()
        if not line.startswith(lineFinder): continue # If the line doesn't match the format skip to next iteration

        # Line found
        email = findEmailinLine(line)
        # print(f'Found email: {email}')

        countSender[email] = countSender.get(email, 0) + 1

    # END FOR LOOP fhandle

    # Close file
    fhandle.close()

    return countSender

## countEmailSender(testFile, 'From')
## print(f"Test function countEmailSender: {countEmailSender(testFile, 'From')}")

def writeToFile(histogram: dict, fileName: str, alphabetical = 'No'):
    # Open the file to write
    try:
        fhandle = open(fileName, 'w')
    except:
        print(f'File {fileName} could not be found')
        return None

    keys = list(histogram.keys())
    if (alphabetical == 'alphabetical'): keys.sort()

    # FOR LOOP to write
    for key in keys:
        line = f'Sender: {key} ----- Number of emails: {histogram[key]}\n'
        fhandle.write(line)

    # END FOR LOOP to write

    # Close File
    fhandle.close()

    return None

###############################################################################
### EXERCISE SOLUTION
FILE = 'mbox.txt'
LOG_FILE = './logfiles-09-dictionaries/exercise3.txt'

emails = countEmailSender(FILE, 'From')
writeToFile(emails, LOG_FILE, 'alphabetical')