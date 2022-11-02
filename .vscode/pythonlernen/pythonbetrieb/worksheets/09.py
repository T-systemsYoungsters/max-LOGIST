# Block 1
# 1.
# 1,2,3,4,5
# 2.
# 0,1,2,3,4
# 3.
# 5
# 4.
# 25
# 5.
# 00,01,02,03,04,10,11,12,13,14,...,44
# 6.
# *,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
# 7.
# *****,*****,*****,*****
# 8.
# *************************
# 9.
# i wurde auch als variable verwendet
# 10.
# 5
# 11.
# random 5 stellige binär-Zahl, bye wenn man nicht y schreibt
# 12.
# 3
# 13.
# 4,3
# 14.
# 4,3
# 15.
# 4,4
# 16.
# x=10, x=11, x=10
# 17.
# f start, g start, h, g end, h ,f end
# 18.
# x= 10, foo has been called, x= 10
# 19.
# main 1, a 1, a 2, main 1, main 5, b 5, b 6, main 5, main 5, c 5, c 102, main 5
# 
# Block 2
# 1.
# Klammer bei return müssen weggelassen werden
# 2.
# x wird nicht vergrößert, da x nicht zum vergrößern aufgegriffen wird. Das heißt man muss vor dem increase noch -> x= schreiben
# 3.
# Klammer hinter print_hello wurde vergessen
# 4.
# durch die eckigen Klammern denkt Python an eine Liste und nicht an die direkte Zahl 10
# 5.
# es werden nirgendswo die Zahlen addiert. Um sie zu addieren muss man zu erst sum=0 setzen, dann sum += i statt nur =. Außerdem darf return nur einmal getabbt sein
# 6.
# um das P auch umzudrehen muss man i+1 in der eckigen Klammer rechnen
# 7.
# if immer mit doppel==, um auf eine Buchstabeneingabe zu prüfen muss man ""setzen, 
# 
# Block 3
# 1.
# def hello():
#     print("Hello World")
# 2.
# hello()
# 3.
# def hello(name):
#     print("Hello",name)
# 4.
# hello("Bob")
# 5.
# def multiply(x,y):
#     print(x*y)
# 6.
# multiply(13,235)
# 7.
# def phrases(phrase,count):
# for i in range(count):
#     print(phrase)
# 8.
# phrases("Hello,5")
# 9.
# def square(x):
#     return(x*x)
# 10.
# print(square(5))
# 11.
# def centrifugal(m,r,v):
#     return m*((v**2)/r)
# 12.
# print(centrfugal(12,15,4))
# 13.
# def numbers(numberlist):
#     for item in numberlist:
#         print(item)