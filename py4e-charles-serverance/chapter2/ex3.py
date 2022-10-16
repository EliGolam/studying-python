"""
Exercise 3 : Write a program to prompt the user for hours and rate per hour to compute gross pay.
"""

# Function
def calcWage (hours: float, rate: float):
  return round(hours * rate, 2)

def takeUserInput (prompt: str):
  isValidInput = False
  value = 0

  while not isValidInput:
    try:
      value = float(input(f"Enter {prompt}: "))
      isValidInput = True
    except ValueError: 
      print(f"Please input a number.")

  return value


# Code
userHours = takeUserInput('hours')
userRate = takeUserInput('rate')


print(f"Your wage is: $ {calcWage(userHours, userRate)}")