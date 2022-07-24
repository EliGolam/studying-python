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


# 06 STRINGS
s1 = "Apple"
printStringBackwards_1(s1)




