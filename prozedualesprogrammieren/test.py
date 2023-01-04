# x = 7
# y = 0
# liste = [1, 2, 3]
# def funktion1 (a, b):
#     x = a / 2
#     print (x)
# def funktion2(a, b):
#     x = 4
#     return x + a + b
# def funktion3(l):
#     l[0]= 0
# print (x)
# print (liste)
# y = funktion2(x, 7)
# funktion3 (liste)
# print (y)
# print (liste)
# z = funktion1 (y, 2)
# print(x)
zahlen = []
j = int(input("Wie viele Zahlen?: "))
for i in range(j):
    zahlen.append(int(input(f"Gönn {i+1}. Zahl: ")))
def maxi(zahlen):
    maximum = zahlen[0]
    for i in range (len(zahlen)-1):
        if maximum < zahlen[i+1]:
            maximum = zahlen[i+1]
    return maximum
def mini(zahlen):
    minimum = zahlen[0]
    for i in range (len(zahlen)-1):
        if minimum > zahlen[i+1]:
            minimum = zahlen[i+1]
    return minimum
print(f"Maximum: {maxi(zahlen)}")
print(f"Minimum: {mini(zahlen)}")