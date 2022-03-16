# import itertools
# import array as ar


# def ParallelSums(arr):
    
#     combs = set(itertools.combinations(arr,len(arr)/2))
    
#     for a in combs:
#         a_sum = sum(a)
#         b = arr[:]
#         for i in a:
#             b.remove(i)
#         b_sum = sum(b)
#         if a_sum == b_sum:
#             ans = compose(list(a),b)
#             return ans
#     return -1
    
# def compose(a,b):
#     a.sort()
#     b.sort()
#     if a[0] <= b[0]:
#         return ','.join(str(x) for x in a + b)
#     else:        
#         return ','.join(str(x) for x in b + a)

# def sortInWave(arr, n):
     
#     #sort the array
#     arr.sort()
    
#     # Swap adjacent elements
#     for i in range(0,n-1,2):
#         arr[i], arr[i+1] = arr[i+1], arr[i]
 
# # Driver program
# arr = [1,2,1,5]
# sortInWave(arr, len(arr))
# for i in range(0,len(arr)):
#     print (arr[i],end=" ")

# def twoSum(arr, s):
#     for num in arr:
#         dif = s - num
#         try:
#             if arr.index(dif):
#                 arr.remove(dif)
#                 arr.remove(num)
#                 yield num, dif
#         except ValueError:
#             pass


# arr = [3, 5, 2, -4, 8, 1,11]
# for num1, num2 in twoSum(arr, 4):
#     print(num1, num2)

# import datetime

# time_1 = datetime.strptime('05:00:00',"%H:%M:%S")
# time_2 = datetime.strptime('10:00:00',"%H:%M:%S")

# time_interval = time_2 - time_1
# print(time_interval)


def turn_minutes(time):
  result = time[:-2].split(":") 
  result = [int(result[0]), int(result[1])] if time[-2:] == "AM" else [int(result[0])+12, int(result[1])]
  result[0] = result[0] if (result[0]!=12 and result[0]!=24) else result[0]-12
  return result[0] * 60 + result[1]

def MostFreeTime(strArr): 
  times_list = []
  for time in strArr:
    times_list.append([turn_minutes(i) for i in time.split("-")])
  times_list.sort()
  most_free =  0
  for i in range(len(times_list)-1):
      if times_list[i+1][0] - times_list[i][1] > most_free:
          most_free =  times_list[i+1][0] - times_list[i][1]
  return "%02d:%02d" %(most_free/60, most_free%60) 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
strArr = "12:15pM-02:00PM","09:00am-10:00am","10:30am-12:00am"

print(MostFreeTime(strArr()) )    