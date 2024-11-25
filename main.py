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
code = file.Read()
for i in range(0, )
if __name__ == "__main__":
  exec(executableCode)
