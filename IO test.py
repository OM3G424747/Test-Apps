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