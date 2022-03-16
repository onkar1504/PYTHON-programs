# parrallel programming (multithreading)

import os 
import threading

def fun(X):
    print("PID of fun  is:",os.getpid())   #pid 1000
    print("PPID OF FUN:",os.getppid())    #ppid 3300
    print("inside fun")  

    for i in range(X):
        print("fun:",i)  

def gun(X):
    
    print("PID of gun is:",os.getpid())        #1000
    print("PPID OF GUN:",os.getppid())          #3300
    print("inside gun")

    for i in range(X):
        print("gun:",i) 

def main():        

    No=5
    print("PID of main(parent) is:",os.getpid())  #parent  #pid 1000

    #process execution
    thread1=threading.Thread(target=fun,args=(No,))  #child
    thread2=threading.Thread(target=gun,args=(No,))  #child

    #use to start process
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("end of main ")

if __name__ =="__main__":
    main()