#Encapsulation-> class = characteristics(variables) + behaviours(function)

#class defination
class arithematic:
    
    def __init__(self,a,b) :  #constructor
       print("inside init(constructor)")
       self.no1=a;          #characteristics
       self.no2=b;          #characteristics

    def addition(self):        #Behaviour
        ans = self.no1+self.no2
        return ans

def main():

    obj1 = arithematic(10,20)  # object creation of class arithemetic
    ret = obj1.addition()  #addition(obj1)  addition(0*100)
    print("addition is:",ret)

    obj2=arithematic(22,22)
    ret=obj2.addition()     #addition(obj2)  addition(0*200)
    print("addition is",ret)

if __name__ == "__main__":
    main()