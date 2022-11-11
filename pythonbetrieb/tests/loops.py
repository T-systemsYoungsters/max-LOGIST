# wiederholt genau 5 mal
for a in range(5):
    print(a+1)
print("----------------")
# wiederholt für den Wert von von/bis
for b in range(3,7):
    print(b)
print("----------------")
# wiederholt in 2er Schritten
for c in range(2,20,2):
    print(c)
print("----------------")
# zählt runter
for d in range(10,0,-1):
    print(d)
print("----------------")
# addiert alle 5 Zahlen die man eingibt
ergebnis=0
for e in range(2):
    neuezahl=int(input("Bitte geben sie eine Zahl ein: "))
    ergebnis=ergebnis+neuezahl
print("Ihr Ergebnis ist:",ergebnis)
print("----------------")
# zählt die anzahl der eingegebenen Nullen
ergebnis=0
for f in range(2):
    neuezahl=int(input("Bitte geben sie eine Zahl ein: "))
    if neuezahl==0:
        ergebnis=ergebnis+1
print("Sie haben",ergebnis,"Nullen eingegeben")
print("----------------")
# while loops:
# g ist eine Variable die einbezogen wird im Gegensatz zu for -> somit kann man bedingungen für g festlegen
g=0
while g<10:
    print(g)
    g=g+1
print("----------------")
# durch die Abfrage entscheidet der Nutzer wann die loop beendet wird
verlassen="nein"
print("Wenn sie die Eingabe nicht verlassen wollen schreiben sie \"nein\".")
while verlassen =="nein":
    verlassen=input("Wollen sie die Eingabe verlassen? ")
print("----------------")
# die loop kann durch 2 Abfragen enden
fertig=False
while fertig==False:
    verlassen=input("Wenn du verlassen willst dann schreibe\"ja\". ")
    if verlassen=="ja":
        fertig=True
    else:
        angriff=input("Wenn sie den Drachen angreifen wollen dann schreibe\"ja\". ")
        if angriff=="ja":
            print("Sie sind gestorben.")
            fertig=True
print("----------------")