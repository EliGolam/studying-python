"""
Exercise 1: Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None. Then write a function 
called middle that takes a list and returns a new list that contains all but 
the first and last elements.
"""

from functions import middle


array = [1, 2, 3, 4, 5]

print(f"Modified array: {middle(array)} | Original array {array}")