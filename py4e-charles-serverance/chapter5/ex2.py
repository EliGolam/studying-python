"""
Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the 
maximum and minimum of the numbers instead of the average.
"""

from functools import reduce
from typing import List
from ex1 import getArrayOfNum


# Functions
def analyseNumbers(nums: List[float]): 
  results = {}

  results['total'] = reduce(lambda sum, currentVal: sum + currentVal, nums, 0)
  results['count'] = len(nums)
  results['max'] = max(nums)
  results['min'] = min(nums)
  results['array'] = nums.copy()

  return results;

# CODE

results = analyseNumbers(getArrayOfNum())

print(f"From the array: {results['array']}\nMax: {results['max']}\nMin: {results['min']}")