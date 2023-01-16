def openFile(path: str, format: str):
  fileNameInp = input("Enter file name: ").strip().lower()

  if format not in fileNameInp:
    fileNameInp += format

  # OPEN FILE
  try:
    fhandle = open(path + fileNameInp)
    print("DEBUG - File Successfully opened")
  except FileNotFoundError:
    print("ERROR: File not found")
    return None

  return fhandle