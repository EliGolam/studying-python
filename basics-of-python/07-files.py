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