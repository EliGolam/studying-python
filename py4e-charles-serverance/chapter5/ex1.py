"""
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
"""

from typing import List
from functools import reduce

# FUNCTIONS

def getArrayOfNum():
  userInput = ''
  numArr = []

  while userInput.lower() != 'done': 
    userInput = input("Enter a number: ")
    
    try:
      numArr.append(float(userInput))
    except ValueError:
      print("Please input a number")

  # End parent WHILE loop
  return numArr


def analyseNumArr(array: List[float]):
  results = {}

  results['total'] = reduce(lambda sum, value: sum + value, array, 0)
  results['count'] = len(array)
  results['average'] = round(results['total'] / results['count'], 2)

  return results

# END FUNCTIONS


# CODE
results = analyseNumArr(getArrayOfNum())

print(f"Total Sum: {results['total']}")
print(f"Total Count: {results['count']}")
print(f"Average: {results['average']}")