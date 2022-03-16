# def is_even(a):
#     if a%2==0:
#         return True

# lst=[20,2,1,30]

# result=(list(filter(is_even,lst)))
# print(result)

#output [20, 2, 30]     

# Now I will create my own function to do filter operation without taking the help of inbuilt filter() function in python.

def my_filter(is_even,list2):
    return is_even()

list2=[2,3,4,5,6,7,8,9,10,20]

list3=[]

def is_even():
    for i in list2:
        if i%2==0:
            list3.append(i)

        print(list3)

my_filter(is_even,list2)