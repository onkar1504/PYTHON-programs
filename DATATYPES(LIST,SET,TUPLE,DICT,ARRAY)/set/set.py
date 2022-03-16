data ={10,20,30,40}
mylist=[10,20,30,40]

print("datatype",type(data))
print("length of data",len(data))
print("data from set:",data)

print("data from lsit:",mylist)

#accesiing element from set

# print(data[0])      error

print("*****data traveersal using loop********")

for no in  data:
    print(no,end=" ")
    print()




data1={10,20,30,40,10}          #duplicate element allow but stored only onced
print("new set is",data1)

data2={10,20,20.5,"hello",True}  #set is hetrogenous 
print("set is heterogenous:",data2)

