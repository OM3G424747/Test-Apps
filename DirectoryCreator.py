import os.path

InsertFile = input("Paste text document name here -> ")
OpenFile = InsertFile + ".txt"
OpenFile = open(OpenFile)
for line in OpenFile:
    line = line.rstrip("\n")
    FileCheck = os.path.exists(line)
    if FileCheck == False:
        output = os.mkdir(line)
        print(FileCheck)
        print(line)
    else:
        print(FileCheck)
        print(line)
    

    