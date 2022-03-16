#function pass to another function

def fun(): # 0x100   
    print("inside fun")

def gun(func_name):  #0x200
    print("inside gun")

    func_name() # callling fun()  0x100

def main():

    gun(fun) #gun(0x100)

if __name__ =="__main__":
    main()