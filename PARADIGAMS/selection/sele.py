def maximum(value1,value2):
    #logic
    if(value1 > value2):
        return value1
    else:
        return value2


def main():
    print("enter first number");
    no1=int(input())  

    print("enter second number");
    no2=int(input())

    ret = maximum(no1,no2)

    print("maximunn no is",ret)

if __name__ == "__main":
    main()