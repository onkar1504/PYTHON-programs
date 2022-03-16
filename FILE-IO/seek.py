def main():

    name = input("enter the file name that you want to open:")

    fd = open(name,"rb")

    print("current offset is",fd.tell())

    # data = fd.read(2)   #read fist 2 charcter from file
    # print("data is",data)

    print("current offset is",fd.tell())

    # fd.seek(3) #beginign pasun  

    data = fd.read(5)

    fd.seek(3,1)

    print("current offset is",fd.tell())

    data =fd.read()
    
    print(data)

if __name__ == "__main__":
    main()


#0 begining
#1 current
#2 end



