print("enter number of elements")

size=int(input())

data ={0}

for i in range(size):
    print("enter element no:",i+1)
    no=int(input())
    data.add(no)
    
print("data from set:",data)

print("enter data to search")
value = int(input())

if value in data:
    print("element is theere")

else:
    print("there is no such elemnt")