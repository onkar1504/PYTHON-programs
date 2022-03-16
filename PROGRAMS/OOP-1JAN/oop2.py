class Demo:

    A=10  #class variable
    B=20   #class variable
    
    def __init__(self):
        self.C=30   #instance variable
        self.D =40  #instance variable


def main():

    print("value of A:",Demo.A)  #accessing class variable using class name
    print("value of B:",Demo.B)

    obj1 = Demo()
    obj2 =Demo()

    print("value of C from obj1:",obj1.C) #accessing instace variable using obj name
    print("value of C from obj2:",obj2.C)

    #we can change instace variable
    obj1.C=31
    print("value of C after changee",obj1.C)

if __name__ == "__main__":
    main()