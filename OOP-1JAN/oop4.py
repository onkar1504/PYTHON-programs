class Demo:

    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("inside destructor")


def main():
    print("inside main")

    obj1=Demo()

    print("end of main")

if __name__ == "__main__":
    main()

    print("end of appliction")