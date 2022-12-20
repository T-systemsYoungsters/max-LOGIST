# def maxi(n1,n2):
#     if n1>n2:
#         return n1
#     elif n1<n2:
#         return n2
    
# def mini(n1,n2):
#     if n1<n2:
#         return n1
#     elif n1>n2:
#         return n2

# a=int(input("1. Number: "))
# b=int(input("2. Number: "))
# if a!=b:
#     print("The max is: ",maxi(a,b))
#     print("The min is: ",mini(a,b))
# else:
#     print("Your numbers are equal.")

def maxi(testlist):
    max=testlist[0]
    for i in range(len(testlist)):
        if max<testlist[i]:
            max=testlist[i]
    return max
    
def mini(testlist):
    min=testlist[0]
    for i in range(len(testlist)):
        if min>testlist[i]:
            min=testlist[i]
    return min

liste=[]
x=int(input("Wie viele Zahlen möchten sie prüfen? "))
for i in range(x):
    liste.append(int(input("Number: ")))
print(liste)
a=maxi(liste)
b=mini(liste)
if a!=b:
    print("The max is: ",a)
    print("The min is: ",b)
else:
    print("The numbers are equal.")