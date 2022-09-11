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