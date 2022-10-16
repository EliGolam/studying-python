"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
"""

# File variables
DATA_PATH = '../data/'
fileNameInp = input("Input file name: ")
FILE_FORMAT = '.txt'
logFileName = 'log.txt'
findModule = 'X-DSPAM-Confidence:'

# Results Array
spamConfidenceArray = []


if fileNameInp.find(FILE_FORMAT) == -1:
  fileNameInp += FILE_FORMAT


# Open file
try: 
  fhandle = open(DATA_PATH + fileNameInp)
except FileNotFoundError:
  print(f"File not found: {DATA_PATH + fileNameInp}")

# Open Logs
logFile = open(logFileName, 'w')


for line in fhandle:
  line = line.rstrip()
  if line.find(findModule) == -1: continue # Guard clause

  logFile.write(f"{line}\n")
  spamConfidence = float(line.split(': ')[1])
  spamConfidenceArray.append(spamConfidence)

fhandle.close()

avgConfidence = sum(spamConfidenceArray) / len(spamConfidenceArray)
line = f"\n\nAverage {findModule} {round(avgConfidence, 4)}\n"
logFile.write(line)

logFile.close()
