import array as ARR

def main():

    print("***********demonstration of array in python*************")
    
    data = ARR.array('f',[10.1,20.2,30.3,40.4,50.5])    

    print(data)

    print("length  of array:",len(data))
    print("type  of array:",type(data))

    print("*******initializing data from array********")           
    print(data[0])
    print(data[1])

    print("*******data from array********")

    for i in range(len(data)):
        print(data[i])

    print("********second for loop***********")
    for no in data:
        print(no,end="\t")

    print("typecode of array is:",data.typecode)
    

if __name__ == "__main__":
    main()