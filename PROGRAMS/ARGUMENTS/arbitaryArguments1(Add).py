def Adiition(*value):
    sum=0;

    for no in value:
        sum= sum+no;
    return sum

def main():

    ret=Adiition(10,20,30,40,50)
    print("addition is",ret)

    ret=Adiition(10,20,30)
    print("addition is",ret)

    ret=Adiition(10,20)
    print("addition is",ret)

    ret=Adiition()
    print("addition is",ret)

if __name__ == "__main__":
    main()