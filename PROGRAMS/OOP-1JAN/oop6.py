#instace method works acceesing

class Demo:
    A=10  #class variable

    def __init__(self):
        print("inside constructor")
        self.B=20         #instace variavle
    
    def fun_instace(self): #instace method
        print("inside instace method")
        print(self.B)
        print(self.A)
        print(Demo.A)  #this is the coorect way to access class variable

    @classmethod
    def fun_class(cls):  #class method
        print("inside class method")
        print(cls.A)
        print(Demo.A)
        # print(cls.B)    error yenar instace can access in class method


    @staticmethod       #static method
    def fun_static():
        print("inside static method")
        
    def __del__(self):  #destructor
        print("inside destructor")


def main():
    
    obj=Demo()    #object creation
    obj.fun_instace()   

    Demo.fun_class()  #calling class method
   

if __name__ == "__main__":
    main()

