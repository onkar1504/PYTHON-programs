def addition(value1,value2):
    ans=value1+value2
    return ans


def mul(value1,value2):
    ans=value1*value2
    return ans

def main():

    print("marvellous addition application")

    no1 = int(input("enter first no"))
    no2= int(input("enter first no"))

    ret = addition(no1,no2)

    print("addition is",ret)



    
def main2():

    print("marvellous addition application")

    no1 = int(input("enter first no"))
    no2= int(input("enter first no"))

    ret = mul(no1,no2)

    print("multip is",ret)

if __name__ =="__main__":

    main();


if __name__ =="__main2__":

    main2();