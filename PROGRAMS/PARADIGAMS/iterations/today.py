data = [ 11, 21,51,101]

print("data using while loop")

i=0;

#while(i<4)

while(i<len(data)):
    print(data[i])
    i=i+1

print("data using for loop")
#for i in range (4)
#for i in (0,1,2,3)
for i in range(len(data)):
    print(data[i])