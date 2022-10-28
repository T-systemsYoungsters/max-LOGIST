# int(3)
# int(-3)
# float(3.32234)
# float(-3.243)
# str("Hello")
# bool(True)
# bool(False)
# list([1,2,3,4,5])
# tuple((1,2,3,4,5))
# x=[3,4,6,3,7,8,4,2] #-> die Stellen werden von 0 bis 7 nummeriert
# print(x) # -> um liste anzuzeigen
# print(x[4]) # -> printed das 5. Element der Liste
# print(x[2],x[5]) # -> um mehrere Zahlen aus der Liste anzuzeigen
# x[3]=103 # -> ersetzt die 3. Zahl der Liste 
# print(x)
# x[-1]=200 # -> ersetzt das letzte Element der Liste 
# print(x)
# x[-2]=100 # -> ersetzt das vorletzte Element der Liste 
# print(x)
# y=(3,4) # -> kann auch als eine Liste verwendet werden
# print(y)
# print(y[1]) # -> man kann auch bestimmte Werte anzeigen lassen
# y[0]=3 -> Werte der Liste y können aber nicht ersetzt werden -> Liste die nicht verändert werden kann
# z=[101,20,10,50,60]
# for item in z:
#     print(item)
# for i in range(len(z)):
#     print(z[i])
# a=[2,4,5,6]
# a.append(10) # -> um Zahlen zu ergänzen
# print(a)
# a=a+[13] # -> um Zahlen zu ergänzen
# print(a)
# b=[]
# for i in range(5):
#     user=input("was wollen sie hinzufügen? ") # -> Liste mit user eingeaben füllen
#     b=b+[user]
#     print(b)
# c=[0]*10 # -> erstellt liste mit 10 nullen
# print(c)
# d = [5,76,8,5,3,3,56,5,23]
# sum = 0 # -> sollte 0 sein da es der startwert ist
# for i in range(len(d)): # -> addiert einzeln die werte
#     sum= sum+d[i]
# print(sum)
# Copy of the array to sum
# -> anderer weg zu addieren:
# e = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# sum = 0
# for item in e:
#     sum =sum+ item
# print(sum)
# Copy of the array to modify
# f = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# for i in range(len(f)): # -> verdoppeln der werte in der liste
#     f[i] = f[i] * 2
# print(f)
# g = "This is a sample string"
# print("g=", g)
# print("g[1]=", g[1]) # -> zeigt 2. buchstaben
# print("g[:6]=", g[:6]) # -> zeigt buchstaben von 0-5 
# print("g[6:9]=", g[6:9]) # -> zeigt buchstaben von 6-8
# h="Hi"
# i="There"
# j="!"
# print(h + i + j)
# print(3 * h)
# print((h * 2) + (i * 2))
# Verschlüsselung
# text = "This is a test. ABC abc"
# for c in text:
#     x = ord(c) # -> verwandelt Zeichen in ihre Ordnungszahlen
#     x = x + 1 # -> verändert die ordnungszahl
#     c2 = chr(x) # -> verwandelt ordnungs zahl in die neuen zeichen
#     print(c2, end="")