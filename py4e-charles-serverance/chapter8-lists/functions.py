from typing import List


def chop(array: list):
  array.pop(0) # remove first element
  array.pop(-1) # remove last element
  return None

def middle(array: list): 
  newArr = array.copy()
  chop(newArr)
  return newArr

def openFile(folderPath: str, fileFormat: str):
  import sys

  isNotValidInput = True

  while isNotValidInput: 
    fileNameInp = input("Select File name: ").lower()
    if(fileNameInp.find(fileFormat) == -1): 
      fileNameInp += fileFormat

    filePath = folderPath + fileNameInp

    try:
      fhandle = open(filePath)
      isNotValidInput = False
    except FileNotFoundError as error: 
      errorMessage = f"File not found: {fileNameInp}\n{str(error)}"
      print(errorMessage)

      userInp = input("Do you want to try again? [y/n] - ").lower()

      if userInp == 'n': 
        print("Oki! Bye bye!")
        sys.exit()
  # End WHILE
  return fhandle



def getNumberInput():
  nums = []

  isDone = False

  while not isDone: 
    newNum = input("Type a number to add to array or 'done' if you want to stop: ")

    if (newNum.lower().strip() == 'done'):
      isDone = True
    elif (newNum.isnumeric()):
      nums.append(int(newNum))
    else: 
      print("That was not a number")
  # End WHILE

  return nums


def getArrayInfo(array: list, property: str): 
  property = property.lower()

  if (property == 'max'):
    return max(array)
  elif (property == 'min'): 
    return min(array)
  elif (property == 'length'): 
    return len(array)
  elif (property == 'average'): 
    return round(sum(array) / len(array), 2)
  else: 
    print("Not valid property")
    return None