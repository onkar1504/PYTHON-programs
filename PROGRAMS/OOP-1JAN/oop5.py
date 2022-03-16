class Demo:
    A=10  #class variable

    def __init__(self):
        print("inside constructor")
        self.B=20         #instace variavle
    
    def fun_instace(self): #instace method
        print("inside instace method")

    @classmethod
    def fun_class(cls):  #class method
        print("inside class method")

    @staticmethod       #static method
    def fun_static():
        print("inside static method")
        
    def __del__(self):  #destriuctor
        print("inside destructor")


def main():
    Demo.fun_class()
    Demo.fun_static()

    obj1=Demo()    #object creation
    obj1.fun_instace()

    # obj1.fun_static() #class method can call by object also but nka karu
    # obj1.fun_class()

if __name__ == "__main__":
    main()

#instace method

#class method

#