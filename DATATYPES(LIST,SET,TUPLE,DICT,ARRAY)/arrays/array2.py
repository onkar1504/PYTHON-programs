import array as ARR

def main():

    print("demonstration of array in python")
    
    data = ARR.array('i',[10,20,30,40,50])    

    print(data)

    print("length  of array:",len(data))
    print("type  of array:",type(data))

    print(data[0])
    print(data[1])

    print("data from array")

    for i in range(len(data)):
        print(data[i])

    print("second for loop")
    for no in data:
        print(no,end="\t")
    

if __name__ == "__main__":
    main()