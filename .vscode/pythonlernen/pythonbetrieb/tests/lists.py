# int(3)
# int(-3)
# float(3.32234)
# float(-3.243)
# str("Hello")
# bool(True)
# bool(False)
# list([1,2,3,4,5])
# tuple((1,2,3,4,5))
x=[3,4,6,3,7,8,4,2] #-> die Stellen werden von 0 bis 7 nummeriert
print(x) # -> um liste anzuzeigen
print(x[4]) # -> printed das 5. Element der Liste
print(x[2],x[5]) # -> um mehrere Zahlen aus der Liste anzuzeigen
x[3]=103 # -> ersetzt die 3. Zahl der Liste 
print(x)
x[-1]=200 # -> ersetzt das letzte Element der Liste 
print(x)
x[-2]=100 # -> ersetzt das vorletzte Element der Liste 
print(x)
y=(3,4) # -> kann auch als eine Liste verwendet werden
print(y)
print(y[1]) # -> man kann auch bestimmte Werte anzeigen lassen
# y[0]=3 -> Werte der Liste y können aber nicht ersetzt werden -> Liste die nicht verändert werden kann
