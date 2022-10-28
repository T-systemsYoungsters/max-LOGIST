# zufällige Zahl wird in 10er Schritten bis 100 generiert
import random
zahl=random.randrange(0,100,10)
print(zahl)
print("----------------")
# per choice kann man aus einer Liste zufällig einen wert auswählen
# liste=["stein","schere","papier"]
# wahl=random.choice(liste)
# print(wahl)
# print("----------------")
# zufällige zahl mit Kommarstellen, dessen bereich angepasst werden kann
# neuezahl=random.random()*10+1
# print(neuezahl)