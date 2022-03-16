# parrallel programming (multithreading)

import os 
import threading
from unicodedata import name

def fun(X):
    print("PID of fun  is:",os.getpid())   #pid 1000
    print("PPID OF FUN:",os.getppid())    #ppid 3300
    print("thread name of fun :",threading.current_thread().name)
    print("inside fun")  

    for i in range(X):
        print("fun:",i)  

def gun(X):
    
    print("PID of gun is:",os.getpid())        #1000
    print("PPID OF GUN:",os.getppid())          #3300
    print("thread name of gun :",threading.current_thread().name)
    print("inside gun")

    for i in range(X):
        print("gun:",i) 

def main():        

    No=5
    print("PID of main(parent) is:",os.getpid())  #parent  #pid 1000
    print("thread name of main is",threading.currentThread().name)
    #process execution
    thread1=threading.Thread(target=fun,args=(No,),name='fun thread')  #child
    thread2=threading.Thread(target=gun,args=(No,),name='gun thread')  #child

    #use to start process
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("end of main ")

if __name__ =="__main__":
    main()