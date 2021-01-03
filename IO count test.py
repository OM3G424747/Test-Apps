"""
a simple practice scripts to that writes 1 to a 100 on a txt file
after every number it prints a space for formating 
after every mutiple of 10, it creates a new line 
"""

output = open("testoutput.txt","w")

for i in range(100):
    i = i + 1
    if i%10 == 0:
      output.write(str(i))
      output.write("\n")
    else:
        output.write(str(i))
        output.write(" ")
    print(i)

output.close()
