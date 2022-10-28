# 1.
# for a in range(10):
#     print("Max")
# print("done")
# 2.
# for a in range(20):
#     print("Red")
#     print("Gold")
# 3.
# for c in range(2,101,2):
#     print(c)
# 4.
# g=10
# while g>=0:
#     print(g)
#     g=g-1
# print("Blast off!")
# 5.
# in der 7. Zeile muss man statt dem x -> total eingeben, in der 6. Zeile muss man statt dem i ein x eingesetzt werden, in der 5. Zeile muss man auch die eingegebene Zahl als integer definieren
# 6.
# import random
# zahl=random.randrange(0,10)
# print(zahl+1)
# 7. 
# import random
# neuezahl=random.random()*9+1
# print(neuezahl)
# 8.
# total=0
# zero=0
# positiv=0
# negativ=0
# for e in range(7):
#     number=int(input("Bitte geben sie eine Zahl ein: "))
#     total=total+number
#     if number > 0:
#         positiv=positiv+1
#     elif number==0:
#         zero=zero+1
#     else:
#         negativ=negativ+1
# print("Ihr Ergebnis ist:",total)
# print("Sie haben:",positiv,"positive Zahlen,",zero,"Nullen,",negativ,"negative Zahlen angegeben.")
# 9.
# import random
# head=0
# tail=0
# for a in range (50):
#     number=random.randrange(0,2)
#     if number==1:
#         head=head+1
#     else:
#         tail=tail+1
# print("Es wurde",head,"mal Kopf und",tail,"mal Zahl geworfen.")
# 10.
# import random
# print("1 = Schere")
# print("2 = Stein")
# print("3 = Papier")
# userinput=int(input("Was wählen sie?"))
# number=random.randrange(0,3)
# if number==0:
#     print("Das System hat Schere gewählt")
# elif number==1:
#     print("Das System hat Stein gewählt")
# else:
#     print("Das System hat Papier gewählt")
# if userinput==number+1:
#     print("Unendschieden")
# elif userinput == 1 and number==2:
#     print("Du hast gewonnen!")
# elif userinput==2 and number==0:
#     print("Du hast gewonnen!")
# elif userinput==3 and number==1:
#     print("Du hast gewonnen!")
# else:
#     print("Das System hat gewonnen!")