from functools import reduce


def main():

    data=[5,7,6,8,4]

    print("original data:",data)

    #filter(function_name,list)
    
 
    # print("data after filter:",newdata)

    #map(function_name,list)
   
    # print("data after map",incrementdata)

    #reduce(function_name,list)

    print("data after reduce additon is:", reduce(lambda a , b : a + b,list(map(lambda no :(no+2),list(filter( lambda no : (no%2==0),data))))))


if __name__ == "__main__":
    main()