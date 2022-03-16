
data2={"even":[2,4,6,8],"odd":[1,3,5,7],"other":[11.2,55.4,4]}

print(data2["even"][0])

for keys in data2:
    print(keys)

    for i in data2[keys]:
        print(i)


print("*****data by new for loop******")

for keys in data2:
    print(keys,end="")
    
    for i in range(len(data2[keys])):
        print(data2[keys][i],end=' ')

    print("")