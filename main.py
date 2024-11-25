import os, sys
filename = sys.argv([1])
executableCode = ""
file = open(filename, "r")
code = file.Read()
file.close()
file = open(filename, "w")
file.write(code)
file.close()
file = open(filename, "r")
codeLinesLen = len(file.ReadLines())
for i in range(0, codeLinesLen):
  codeLine = file.ReadLine(i)
  for j in range(0, len(codeLine)):
    codeLine[j]
if __name__ == "__main__":
  exec(executableCode)
