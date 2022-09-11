"""
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a 
function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""
def chop(t):
    del t[0], t[-1]
    return None

def middle(t):
    return t[1:-1]

letters = ['b', 'a', 's', 's', 'o'] 
chop(letters)
print(letters)

middle(letters)
print(letters)
print(middle(letters), letters)

"""
Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the 
program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

Answer: The last line can causa another index-out-of-range error because we haven't guaranteed that there are more words after "From: "
"""
fhand = open('08-EX-2-fail.txt')
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) < 3 : continue
    print(words[2])
fhand.close()

"""
Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the or 
logical operator with a single if statement.
"""
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue
    print(words[2])
fhand.close()