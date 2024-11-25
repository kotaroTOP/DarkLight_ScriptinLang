import os, sys
filename = sys.argv([1])
executableCode = "import os, sys, subprocess, shutil"
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
    if codeLine.endswith("["):
      if codeLine == "EVP(CDLoop)[":
        executableCode += "subprocess.call(\"cscript VBS\\CDLoop.vbs\")"
      if codeLine.startswith("EVP(SendKey(\"") and codeLine.endswith("))"):
        for j in range(13, len(codeLine)):
          if codeLine[j] not in ListForSlash:

          else:
            print("PythonError: in {codeLine}, need symbol '\' before writing
      else:
        print(f"UnexpectedFuncError: in {codeLine}")
    else:
      print(f"SyntaxError: No end signal of line signal in {codeLine} ([)")
    
  
    
if __name__ == "__main__":
  file.close()
  os.remove(file)
  exec(executableCode)
