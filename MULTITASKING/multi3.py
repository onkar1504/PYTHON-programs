# parrallel programming

import os 
import multiprocessing

def fun(X):
    print("PID of fun  is:",os.getpid())
    print("inside fun")  

    for i in range(X):
        print("fun:",i)  

def gun(X):
    print("PID of gun is:",os.getpid())
    print("inside gun")

    for i in range(X):
        print("gun:",i) 

def main():
    print("PID of main(parent) is:",os.getpid())
    fun(5)
    gun(10)

if __name__ =="__main__":
    main()