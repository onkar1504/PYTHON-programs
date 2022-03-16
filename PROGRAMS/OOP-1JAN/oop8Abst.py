#abstrction in python

class Demo:
    
    def __init__(self):
        self.A=10

        self.__B=20   #private variable of class, Abstarction achive here

    def fun(self):
        print("inside fun")
        print(self.A)
        print(self.__B)

        self.__gun()          #accesingg private method

    def __gun(self):   #private method of clsss 
        print("inside gun")


def main():

    obj=Demo()
    obj.fun()  

    # obj.__gun()   erorr 



if __name__ == "__main__":
    main()


#A is public variable

#B is private variable

#fun is public 

#gun is private