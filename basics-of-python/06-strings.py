# Exercise 1: 
## Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
## printing each letter on a separate line, except backwards. 

### Solution 1: with the while loop we can initiate the index at len(str) - 1 and make each step be -1

def printStringBackwards_1 (s: str) : 
    index = len(s) - 1
    while index >= 0 :
        print(s[index])
        # step
        index -= 1
    return None

### Solution 2: with a FOR loop we can include the steps within FOR with a definite loop
def printStringBackwards_2 (s: str) :
    for i in range(len(s), 0, -1) :
        print(s[i-1])
    return None

# Exercise 2: 
## Write a function that slices a string with between the parameters given
def sliceIt (s: str, m: int, n: int) :
    return s[m:n]

# Exercise 3: 
## Write a function that accepts a string and a letter as arguments and counts how many times that letter appears in the string
def countLetters (word: str, letter: str) : 
    count = 0
    if len(letter) == 0 :
        print(f"You must input a character to search in the word {word}")
    elif len(letter) > 1:
        print(f"{letter} is not a character")
    else: 
        for l in word: 
            if l == letter :
                count += 1
    return count

# 06 STRINGS
s1 = "Apple"
printStringBackwards_1(s1)
printStringBackwards_2(s1)

s2 = "Windy"
print(sliceIt(s2, 1, 4))

s3 = "bananana"
letter = "a"
print(f"There are {countLetters(s3, letter)} times the letter {letter} in {s3}")
print(f"We can also verify this with the built-in Python method for strings: {s3.count('a')}")

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
host = data[data.find('@')+1 : data.find(' ', data.find('@'))]
print(f"The host of the email is {host}")




