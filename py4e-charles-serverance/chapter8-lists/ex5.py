from functions import openFile

# File Variables
DATA_PATH = '../data/'
FILE_FORMAT = '.txt'
LOG_FILE = 'log-ex5.txt'

# Variables
lineDiscriminator = 'from'
emailSenders = []


fhandle = openFile(DATA_PATH, FILE_FORMAT)

for line in fhandle: 
  line = line.rstrip().lower()
  wordsInLine = line.split()
  
  if len(wordsInLine) < 2: continue # Guard clause to avoid empty string and out of bound error
  # print("DEBUG - wordsInLine:", wordsInLine)
  if wordsInLine[0] != lineDiscriminator: continue # Guard clause to skip the uninteresting lines
  
  emailSenders.append(wordsInLine[1])

print("emailSenders List created")
fhandle.close()


uniqueEmails = sorted([*set(emailSenders)]) # Use of the set to remove duplicates and the spread operator to turn it back into a list


logFile = open(LOG_FILE, 'w')

logFile.write(f"TOTAL EMAILS IN INBOX: {len(emailSenders)}\n\n")

for email in uniqueEmails:
  emailCount = emailSenders.count(email)
  if emailCount == 1:
    line = f"There is 1 email"
  else:
    line = f"There are {emailCount} emails"

  line += f" from {email}\n"
  logFile.write(line)


print("Files logged!")
logFile.close()