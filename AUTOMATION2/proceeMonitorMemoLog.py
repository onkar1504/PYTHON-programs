from sys import *
import os
from time import time
import psutil


def processdisplay(Dir='marvellous'):
    listprocess=[]

    if not os.path.exists(Dir):
        try:
            os.mkdir(Dir)
        except:
            pass

    seprator = '-'* 50
    log_path= os.path.join(Dir,"marvellouslog%s.log"%(time.ctime()))
    f=open(log_path,"w")
    f.write(seprator+'\n')
    f.write("marvellous processor log:"+time.ctime()+"\n")
    f.write(seprator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for ele in listprocess:
        f.write("%s\n" %ele)

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        processdisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
