"""
This file was created to print an ascii text art heart using loops.
This file also outputs a txt file called "HeartPrint" that as a copy of the ascii heart
"""



Print_Left_Blank = " "
Print_Center_Blank = " "
Print_Heart = "X"
Blank_Length = 10
Heart_Lenght = 6
output = open("HeartPrint.txt","w")

for pos in range (1,6):
    print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}")
    output.write(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}\n")
    Blank_Length = Blank_Length -2
    Heart_Lenght = Heart_Lenght +3
    if Heart_Lenght == 18:
        for pos in range (1,3):
            print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}")
            output.write(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}\n")

Heart_Lenght = 42
Blank_Length = 0

for pos in range(1,11):
    Blank_Length = Blank_Length +2
    Heart_Lenght = Heart_Lenght -4
    print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}")
    output.write(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}\n")

output.close()
