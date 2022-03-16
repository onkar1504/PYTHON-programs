class Demo:

    A=10        #class variable

    def __init__(self):
        self.B=30        #instace variable

    def fun(self):
        print("inside instace method")   

    @classmethod
    def gun(cls):           #class method
        print("inside class method")
        

def main():
    print("value of class variable",Demo.A)
    Demo.gun()
    
    obj1 =Demo()
    print("value of instace variable",obj1.B)
    obj1.fun()

if __name__ == "__main__":
    main()