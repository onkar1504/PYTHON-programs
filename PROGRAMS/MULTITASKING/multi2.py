#serial prograamming

import os 

def fun():
    print("PID of fun  is:",os.getpid())
    print("inside fun")  

    for i in range(5):
        print("fun:",i)  

def gun():
    print("PID of gun is:",os.getpid())
    print("inside gun")

    for i in range(5):
        print("gun:",i) 

def main():
    print("PID of main is:",os.getpid())
    fun()
    gun()

if __name__ =="__main__":
    main()