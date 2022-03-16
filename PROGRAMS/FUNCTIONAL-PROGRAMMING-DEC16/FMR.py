from functools import reduce 

def checkEven(no):
    return (no %2 == 0)

def increment(no):
    return no+2

def addition(a,b):
    return a + b

def main():

    data=[5,7,6,8,4]

    print("original data:",data)

    #filter(function_name,list)
    newdata = list(filter(checkEven,data))
    print("data after filter:",newdata)

    #map(function_name,list)
    incrementdata = list(map(increment,newdata))
    print("data after map",incrementdata)

    #reduce(function_name,list)
    ret = reduce(addition,incrementdata)
    print("data after reduce additon is:",ret)


if __name__ == "__main__":
    main()