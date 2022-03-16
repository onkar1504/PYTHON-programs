#accepet  n no from user and addition of them

import marvellous

def main():
    size =0 
    i=0
    data=[]

    print("enter how many elements you want?");
    size=int(input())

    print("enter the elements");

    for i in range(size):

        data.append(int(input()))

    print("your enterd data is", data);
    
    ret = marvellous.addition(data)
    print("addition of elements is",ret)

if __name__ == "__main__":
        main()