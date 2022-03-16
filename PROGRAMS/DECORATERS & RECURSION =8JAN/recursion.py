def display():
    print("inside for loop")

    for i in range(4):
        print("marvellous")

def displayX():
    print("while loop")
    i=0
    while(i<4):
        print("marvellous")

        i=i+1

def main():
    display()
    displayX()

if __name__ =="__main__":
    main()