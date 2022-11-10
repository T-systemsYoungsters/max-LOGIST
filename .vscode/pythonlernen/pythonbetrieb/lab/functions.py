# 1.
# def min3(x,y,z):
#     if x<y and x<z:
#         return x
#     elif y<x and y<z:
#         return y
#     elif z<x and z<y:
#         return z
#     else:
#         return x
# print(min3(4, 7, 5))
# print(min3(4, 5, 5))
# print(min3(4, 4, 4))
# print(min3(-2, -6, -100))
# print(min3("Z", "B", "A"))
# 2.
# def box(x,y):
#     for i in range(y):
#         for i in range(x):
#             print("*",end='')
#         print()
# box(7,5)
# print()
# box(3,2)
# print()
# box(3,10)
# 3.
# def find(mylist, key):
#     for i in range(len(my_list)):
#         if key == my_list[i]:
#             print(key , "found at ",i+1)
# my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
# find(my_list, 12)
# find(my_list, 91)
# find(my_list, 80)
# 4. 
# import random
# def create_list(size):
#     my_list=[]
#     for i in range(size):
#         r=random.randrange(1,7)
#         my_list.append(r)
#     return my_list
# def count_list(list,number):
#     counted=0
#     for i in range(len(list)):
#         if number == list[i]:
#             counted+=1
#     return counted
# def average_list(list):
#     sum = 0
#     for i in range(len(list)): 
#         sum= sum+list[i]
#     average=sum/(i+1)
#     return average
# list=create_list(10000)
# count=count_list(list,1)
# print(count)
# count=count_list(list,2)
# print(count)
# count=count_list(list,3)
# print(count)
# count=count_list(list,4)
# print(count)
# count=count_list(list,5)
# print(count)
# count=count_list(list,6)
# print(count)
# avg=average_list(list)
# print(avg)