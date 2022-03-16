#method overloading

class demo:

    def __init__(self) :
        self.i=0;
        self.j=0;

    def Add(self,a):
        print("inside add with one parameter")

    def Add(self,a,b):
         print("inside add with two parameter")

def main():

    obj = demo()
    # obj.Add(11)
    obj.Add(11,12)

if __name__ == "__main__":
    main()


        