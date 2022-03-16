# //Write a program which accept one number from user and print that number of
# //even numbers on screen.
# //Input : 7
# //Output: 2 4 6 8 10 12 14 


def even(noo):
   for num in range(2,noo*2+1):
       
       if num%2==0:
           print(num)

def main():


    no=int(input("enter the no"))

    ret = even(no)

    print(ret)

if __name__ == "__main__":

    main()