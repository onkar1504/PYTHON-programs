from functools import reduce


def main():

    data=[5,7,6,8,4]

    print("original data:",data)

    #filter(function_name,list)
    
    newdata = list(filter( lambda no : (no%2==0),data))
    print("data after filter:",newdata)

    #map(function_name,list)
    incrementdata = list(map(lambda no :(no+2),newdata))
    print("data after map",incrementdata)

    #reduce(function_name,list)
    ret = reduce(lambda a , b : a + b,incrementdata)
    print("data after reduce additon is:",ret)


if __name__ == "__main__":
    main()