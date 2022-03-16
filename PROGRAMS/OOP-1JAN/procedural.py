
def addition(a,b):

    ans=a+b;
    return ans

def main():

    print("enter first no");
    no1=int(input())

    print("enter second no");
    no2=int(input())
    
    result=addition(no1,no2)

    print("add is",result)
    
    
if __name__ == "__main__":
    main()