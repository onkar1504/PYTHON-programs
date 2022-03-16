from audioop import mul
import os
import multiprocessing

def square (no):
    print("PID is",os.getpid())
    return no*no

def main():

    data = [2,3,4,5]

    result=list()

    for i in range(len(data)):
        result.append(square(data[i]))

    print("result is",result)

    

if __name__ == "__main__":
    main()