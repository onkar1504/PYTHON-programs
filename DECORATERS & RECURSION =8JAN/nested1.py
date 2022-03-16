def outer(): #0x100
    print("inside outer function")

    def inner(): #0x200

        print("inside inner function")

    return inner  # return 0x200  hascode denar fkt
    # return inner()

def main():

    fun_name=outer()  #call outer

    fun_name()        #call inner 
    #inner()

    print(type(fun_name()))

if __name__ == "__main__":
    main()