#Encapsulation-> class = characteristics(variables) + behaviours(function)

#class defination
class arithematic:
    
    def __init__(self,a,b) :  #constructor
       print("inside init(constructor)")
       self.no1=a;          #characteristics  instance variable
       self.no2=b;          #characteristics

    def addition(self):        #Behaviour  #instance method
        ans = self.no1+self.no2
        return ans

def main():
    print("enter first no")
    x=int(input())

    print("enter second number")
    y=int(input())

    obj = arithematic(x,y)  # object creation of class arithemetic

    ret = obj.addition()

    print("addition is:",ret)

if __name__ == "__main__":
    main()