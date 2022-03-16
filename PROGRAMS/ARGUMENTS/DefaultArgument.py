#default arguments

def Area(radius,PI=3.14):          #function defination
   ans=0;
   ans = PI*radius*radius
   return ans

def main():

    print("enter radius of circle")
    value = float(input())

    ret =0.0

    ret=Area(value,7.10);         #poistional and default argument

    # ret=Area(PI=7.10,radius=value)   #keyword and default argument

    print("area of circle:",ret)

  

if __name__ == "__main__":
    main()