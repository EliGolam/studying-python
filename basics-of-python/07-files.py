# LEARING

"""
Open a file and count the number of lines
"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand :
    count += 1

print(f"Line Count: {count}")
fhand.close()

"""
Search through a file looking for specific instances
"""
fhand = open('mbox.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('From') :
        print(line)
fhand.close()

"""
Search for lines that contain a specific instance
"""
fhand = open('mbox-short.txt')
for line in fhand : 
    line = line.rstrip()
    # Skipping pattern
    if line.find('@uct.ac.za') == -1 : continue # Line not found
    print(line)
fhand.close()

"""
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
"""
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    print(line.upper())
fhand.close()

"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the 
total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
"""
string_search = 'X-DSPAM-Confidence: '
dspam_list = []
file_handle = open('mbox.txt')
for line in file_handle :
    if line.find(string_search) == -1 : continue
    line = line.rstrip()
    dspam_list.append(float(line.partition(string_search)[2]))
print(f"Average Spam Confidence: {sum(dspam_list) / len(dspam_list)}")
file_handle.close()

"""
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. 
"""