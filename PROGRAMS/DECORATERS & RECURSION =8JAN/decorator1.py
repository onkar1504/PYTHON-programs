# def division(a,b):

#     ans =0.0
#     ans = a/b
#     return ans

# def smartdivion(fun_name):

#     def inner(a,b):
#         if a<b:
#             a,b = b,a

#         return fun_name(a,b)

#     return inner

# division = smartdivion(division)

# def main():

#     no1=int(input("enter first no:"));
#     no2=int(input("enter second number:"))

#     print("div is",division(no1,no2))

# if __name__ =="__main__":
#     main()



def division(a,b):

    ans =0
    ans = a -b
    return ans

def smartdivion(fun_name):

    def inner(a,b):
        if a<b:
            a,b = b,a

        return fun_name(a,b)

    return inner

division = smartdivion(division)

def main():

    no1=int(input("enter first no:"));
    no2=int(input("enter second number:"))

    print("div is",division(no1,no2))

if __name__ =="__main__":
    main()