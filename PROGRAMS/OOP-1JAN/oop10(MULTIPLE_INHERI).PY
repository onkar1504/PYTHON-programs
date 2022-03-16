class Base1:

    def __init__(self) :
        print("insdide Base1 constr")
        self.A=10

    def fun(self):
        print("inside fun of Base1")

class Base2:

    def __init__(self) :
        print("insdide Base2 constru")
        self.B=20

    def gun(self):
        print("inside gun of Base2")

class Derived(Base1,Base2):

    def __init__(self):
        self.C=30
        print("inside derived constru")
        
        Base1.__init__(self)
        Base2.__init__(self)

    def sun(self):
        print("inside sun of derived")

def main():

    dobj = Derived()
   
if __name__ == "__main__":
    main()