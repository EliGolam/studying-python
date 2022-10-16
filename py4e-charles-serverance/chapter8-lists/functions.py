from typing import List


def chop(array: list):
  array.pop(0) # remove first element
  array.pop(-1) # remove last element
  return None

def middle(array: list): 
  newArr = array.copy()
  chop(newArr)
  return newArr