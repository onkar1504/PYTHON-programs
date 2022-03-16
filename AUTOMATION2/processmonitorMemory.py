import psutil

def processdisplay():
    listprocess=list()

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    print(listprocess) 

def main():

    print("marvellous infosystem")
    print("process monitor")

    listprocess = processdisplay()

    for elem in listprocess:
        print(elem)


if __name__ == "___main__":
    main()


