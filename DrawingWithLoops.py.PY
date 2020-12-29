"""
This file was created to print an ascii text art heart using loops.
 ... For shits and giggles
"""
Print_Left_Blank = " "
Print_Center_Blank = " "
Print_Heart = "X"
Blank_Length = 10
Heart_Lenght = 3

for pos in range (1,7):
    print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}")
    Blank_Length = Blank_Length -2
    Heart_Lenght = Heart_Lenght +3
    if Heart_Lenght == 18:
        for pos in range (1,3):
            print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}{(Print_Center_Blank*Blank_Length)}{(Print_Heart*Heart_Lenght)}")

Heart_Lenght = 36
Blank_Length = 0

for pos in range(1,10):
    Blank_Length = Blank_Length +2
    Heart_Lenght = Heart_Lenght -4
    print(f"{(Print_Left_Blank)*Blank_Length}{(Print_Heart)*Heart_Lenght}")
