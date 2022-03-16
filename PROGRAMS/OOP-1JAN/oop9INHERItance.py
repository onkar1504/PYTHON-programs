class Base:

    def __init__(self):
        print("inside base constructor")
        self.A=10

    def fun(self):
        print("Base fun ")

########################################
class Derived(Base): 

    def __init__(self):
        print("inside derived constructor")

        Base.__init__(self)  #calling  base class 

        # super().__init__()   #this also use for calling base class

        self.B=20

    def gun(self):
        print("derived gun")

def main():
    
    dobj= Derived()
    dobj.fun()

    print(dobj.A) 

if __name__ == "__main__":
    main()