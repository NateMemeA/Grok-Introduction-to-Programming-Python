msg = input("Message? ")
length = len(msg)
output = ""
for i in range(0,length-1,3):
  output = output+(msg[i]+" ")
print(output.rstrip())
               
