data = {"A":10,"B":20,"C":30,"D":40,"D":50, 51:"D"}

print("data is");
print("type of data is",type(data));
print("length of data is",len(data));

# print("data of 0",data[0]);  we canot access with index

print(data["A"])

print("******iterating in dict*********")
for keys in data:
    
    print(keys,data[keys])
