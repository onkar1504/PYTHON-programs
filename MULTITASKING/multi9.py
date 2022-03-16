# parallel 

import os
import multiprocessing

def square (no):
    print("PID is",os.getpid())
    return no*no

def main():

    data = [2,3,4,5]

    p =multiprocessing.Pool()

    result=list()

    result = p.map(square,data)


    print("result is",result)

    
if __name__ == "__main__":
    main()