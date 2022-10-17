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