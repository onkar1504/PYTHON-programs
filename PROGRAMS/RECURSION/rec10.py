def fun():
    i=0   #local variable

    if(i<5):
        print(i)

        i=i+1

        fun()  #recursive  call
        
def main():

    fun()

if __name__ == "__main__":

    main()