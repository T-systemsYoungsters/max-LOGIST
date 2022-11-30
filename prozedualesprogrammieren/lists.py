# Aufgabenblatt 5
# 1.a=2
# 1.b=3,2,7,9
# 1.c=3

#Bubble
import random
list = []
for i in range(10):
    list.append(random.randrange(-100,100))
print("unsorted")
for i in range(len(list)-1):
    for j in range(0, len(list) - i - 1):
      if list[j] > list[j + 1]:
        # temp = list[j]
        # list[j] = list[j+1]
        # list[j+1] = temp
        list[j],list[j+1]=list[j+1],list[j]
print("sorted")
print(list)