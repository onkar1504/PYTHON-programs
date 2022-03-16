#abstrction in python

class Demo:
    
    def __init__(self):
        self.A=10

        self.__B=20   #private variable of class Abstarction achive here

    def fun_instace(self):
        print("inside fun")
        print(self.A)
        print(self.__B)

def main():

    obj=Demo()

    print(obj.A)

    # print(obj.__B)  error cant access

    obj.fun_instace()


if __name__ == "__main__":
    main()


#A is public variable

#B is private variable