#named function
def Add(a,b):
    return a+b

#lambda function     
Addx = lambda a,b : a+b

def main():
    ret = Add(10,20)
    print("add is",ret)

    ret = Addx(10,20)
    #ret = 10+20
    print("add is",ret)

    print(type(Add))
    print(type(Addx))
    print(lambda a,b:a+b)

if __name__ == "__main__":

    main()