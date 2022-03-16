def fun(i):
  
    if(i<5):
        print("*")


        i=i+1
       
        fun(i)  #recursive  call
        print("*",end=" ")
        
def main():

    fun(0)

if __name__ == "__main__":

    main()