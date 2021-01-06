# A .txt file needs to be created in the same directory as this app. The name provided to the app needs to match the name of the .txt file created in the directory 

import os.path

InsertFile = input("Paste text document name here -> ") #replace with name of text file if needed
OpenFile = InsertFile + ".txt" #adds .txt for the user
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
    

    
