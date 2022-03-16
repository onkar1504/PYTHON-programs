def fun(i=0):  #using default argument
  
    if(i<5):
        print(i)

        i=i+1

        fun(i)  #recursive  call
        
def main():

    fun()

if __name__ == "__main__":

    main()



