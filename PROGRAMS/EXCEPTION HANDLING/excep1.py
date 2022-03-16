def division(a,b):
    ans=0.0;

    try:
        ans = a/b    #ghatk ahe te try madhe liha

    except ZeroDivisionError:
        
        print("exception occured")

    return ans

def main():

    no1=int(input("enter first no:"))
    no2=int(input("enter second number:"))

    ret = division(no1,no2)
    print("division is:",ret)

if __name__ =="__main__":
    main()