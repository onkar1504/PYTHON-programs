def Addition(no1,no2):          #function defination
    ans=0;
    ans = no1+no2
    return ans

def main():

    print("enter first no")
    value1=int(input())

    print("enter second no")
    value2=int(input())

    #positional arguments
    ret =Addition(value2,value2)   #functiona call

    print("additon is:",ret)

if __name__ == "__main__":
    main()