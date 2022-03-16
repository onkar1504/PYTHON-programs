def outer():
    print("inside outer function")

    def inner():

        print("inside inner function")

    inner() #inner function asa call hoto

def main():

    outer()

if __name__ == "__main__":
    main()