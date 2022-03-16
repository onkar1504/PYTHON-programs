class base:

    def __init__(self) :

        self.i=10;
        self.j=20;

    def fun(self):
        print("inside basse fun")

    def gun(self):
        print("inside basse gun")

class derived(base):

    def __init__(self):

        self.a=11;
        self.b=21;

    def fun(self):
        print("inside derived fun")

    def sun(self):
        print("derived sun")

def main():

    bobj = base()



    dobj=derived()

if __name__ == "__main__":
    main()



        