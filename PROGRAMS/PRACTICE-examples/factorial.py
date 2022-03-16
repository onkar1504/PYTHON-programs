def fact(num):

    factorial =1
    if num <0 :
        print("factorial not exits negative number ")
    elif num == 0:
        print("fact of  0 is 1")

    else:
        for i in range(1,num +1):
            factorial  = factorial *i
        print("factiorial of",num,"is",factorial)

def main():

    num = int(input("enter the num"))
    fact(num)
    
if __name__ =="__main__":
    main()
