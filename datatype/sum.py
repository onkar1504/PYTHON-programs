############################
def addition(value1,value2):

    ans=0;
    ans=value1+value2;
    return ans;
#############################
def main():

    no1=0;
    no2=0;
    ret =0
    
    print("enter first number");
    no1=int(input());

    print("enter second number");
    no2=int(input());

    ret =addition(no1,no2)

    print("addition of two no is",ret)

#############################
if __name__ == " __main__":
    main()

#############################