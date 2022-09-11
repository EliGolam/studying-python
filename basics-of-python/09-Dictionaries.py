import sys
"""
Dictionary examples
"""
residence = dict()

residence = {'Ash': 'Australia'}
residence['Eli'] = 'Italy'
residence['Eli'] = 'Australia'
print(residence)

yunHee = dict()
yunHee['name'] = 'Yun-Hee'
yunHee['age'] = 21
yunHee['height'] = 171
yunHee['residence'] = 'Eusol'
yunHee['power'] = 'Electricity'

print(yunHee['name'])
print(yunHee)

"""
DICTIONARY AS COUNTER
"""
# Initialize the string to be parsed
string1 = 'This is a random string to be parsed in some way'
# Eliminate whitespace from the string given to make it easier to work with
parsedString1 = ''.join(string1.split()).lower()
# print(parsedString1)

# Initialize the dictionaries for counting
charsInString = dict()
charsInStringAlt = dict()
charsInStringGet = dict()

# METHOD 1: count each character one by one
for char in parsedString1: 
    if char in charsInString:
        charsInString[char] += 1
    else :
        charsInString[char] = 1

# METHOD 2: when a letter that is not in the dictionary is found, count all instances
# of it in the string
for char in parsedString1:
    if char not in charsInStringAlt:
        charsInStringAlt[char] = parsedString1.count(char)

# METHOD 3: using the get method
for char in parsedString1:
    charsInStringGet[char] = charsInStringGet.get(char, 0) + 1 # If the key is present, add 1 to its value, otherwise create the string.



# For both methods the .lower() method is used to account for upper and lower case

# Open the log file for the outputs
logFile = open('log-test.txt', 'w')

# Write for METHOD 1
logFile.write('\nMethod 1: CharsInString\n\n')

for character in charsInString:
    line = f'Number of "{character}": {charsInString[character]}\n'
    logFile.write(line)


# Write for METHOD 2
logFile.write('\nMethod 2: CharsInStringAlt\n\n')

for character in charsInStringAlt:
    line = f'Number of "{character}": {charsInStringAlt[character]}\n'
    logFile.write(line)


logFile.write('\nMethod 3: CharsInStringGet\n')
logFile.write(str(charsInStringGet) + '\n\n')

for element in charsInStringGet: 
    line = f'Number of "{element}": {charsInStringGet[element]}\n'
    logFile.write((line))

# Closing the log file
logFile.close()

"""
Looking trhough a file to find instances of specific words
"""
# Opening the file with a try-except statement
filePath = './txtfiles/romeo.txt'
try:
    romeo = open(filePath)
except:
    print('File cannot be found')
    sys.exit()

print('File opened')

# Initializing log file and dictionary
romeoLog = open('./txtfiles/romeoLog.txt', 'w')
romeoDict = dict()


# For loop iterating through the file
for line in romeo:
    line = line.rstrip().lower() # Remove newLine characters
    words = line.split() # Divide the line in a list of words
    # For loop to iterated through the words list
    for word in words:
        romeoDict[word] = romeoDict.get(word, 0) + 1 # Using the get method implementation to count the instances        
        
romeo.close()


# For loop to iterate through the dictionary created
for element in romeoDict:
    if romeoDict[element] == 1: 
        line = f'Word "{element}" is present once\n'
    else :
        line = f'Word "{element}" is present {romeoDict[element]} times\n'
    romeoLog.write(line) # Print the appropriate line with the word and word count


"""
Alphabeticall order the dictionary output
"""
romeoLog.write('\n\nAlphabetically ordered dictionary\n\n')

# Creating a list of keys through the keys() method
listKeys = list(romeoDict.keys())
print(listKeys)

# Sort the list alphabetically
listKeys.sort()

for key in listKeys: 
    if romeoDict[key] == 1: 
        line = f'{key}: appears once\n'
    else:
        line = f'{key}: appears {romeoDict[key]} times\n'
    romeoLog.write(line)

romeoLog.close()
