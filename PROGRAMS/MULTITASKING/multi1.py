import os 
def main():

    print("hello")
    print("PID of current process",os.getpid())
    print("PID of parent process",os.getppid()) #id fix rahto


if __name__ =="__main__":
    main()