def printStringLoop(string: str, direction = 'forwards'):

  if direction == 'backwards': 
    # Backwards
    for char in string[::-1]:
      print(char)
  
  else: 
    # Forwards
    for char in string: 
      print(char)

  return None


def printWithWhile(string: str, direction = 'forwards'): 

  if direction == 'backwards': 
    # Backwars
    pos = len(string)

    while pos > 0: 
      pos -= 1
      print(string[pos])

  else: 
    # Forwards
    pos = 0

    while pos < len(string):
      print(string[pos])
      pos += 1

  return None


def countLetters(string: str, letter: str): 
  count = 0

  for char in string: 
    if char != letter: continue
    count += 1

  return count

def getDspamValue (string: str): 
  pos = string.find(':')

  try:
    return float(string[pos+1:])
  except ValueError: 
    return None
