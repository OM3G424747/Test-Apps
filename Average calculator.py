print("Welcome! This calculator is used to determine the average of values entered by you!")

reloop = True
while reloop == True:
  number = (int(input("How many values would you like to calculate?\n")))
  blank_list = []
  for total in range(0, number): 
    total += 1
    numP = (float(input(f"Enter value number {total} that you'd like to calcluate\n")))
    blank_list.append(numP)
    print(sum(blank_list) / len(blank_list))
  redo = (input("Are you ready to terminate the calculator? \n"))
  if redo == "Yes" or redo == "Y" or redo == "y" or redo == "yes":
    reloop = False
  else:
    print("Restarting Loop ... ")
    reloop = True
  
