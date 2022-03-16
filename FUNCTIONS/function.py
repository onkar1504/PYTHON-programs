def arithmatic(value1 ,value2):
    add=value1+value2;
    sub=value1-value2;
    div=value1/value2;
    mul=value1*value2;
    return add,sub,div,mul;

def main():
    print("enter 1 no");
    no1= int(input())

    print("enter 2 no");
    no2= int(input())

    ret1,ret2,ret3 ,ret4=arithmatic(no1 ,no2)

    print("addition is",ret1);
    print("sub is:",ret2);
    print("div is:",ret3);
    print("mul is:",ret4);


if __name__ == "__main__":
    main()