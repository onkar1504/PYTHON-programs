# parrallel programming (multiprocessing)

from ast import arg
from concurrent.futures import process
import os 
import multiprocessing

def fun(X):
    print("PID of fun  is:",os.getpid())
    print("PPID OF FUN:",os.getppid())
    print("inside fun")  

    for i in range(X):
        print("fun:",i)  

def gun(X):
    print("PID of gun is:",os.getpid())

    print("PPID OF GUN:",os.getppid())
    print("inside gun")

    for i in range(X):
        print("gun:",i) 

def main():

    No=5
    print("PID of main(parent) is:",os.getpid())  #parent 

    #process execution
    process1=multiprocessing.Process(target=fun,args=(No,))  #child
    process2=multiprocessing.Process(target=gun,args=(No,))  #child

    #use to start process
    process1.start()
    process2.start()

    process1.join()
    process2.join()


    print("end of main ")

if __name__ =="__main__":
    main()