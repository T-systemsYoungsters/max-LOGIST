#Aufgabenblatt1
print("Dieses Programm multipliziert ihre eingegebenen Zahlen.")
zahl1=float(input("Bitte geben Sie ihre erste Zahl an: "))
zahl2=float(input("Bitte geben Sie ihre zweite Zahl an: "))
x=zahl1*zahl2
print("Das Ergebnis ist:",x)

#Aufgabenblatt2
print("Dieser Rechner berrechnet Ihnen die Temperatur von Grad Celsius in Kelvin und Fahrenheit um.")
gradc=float(input("Bitte geben Sie die Temperatur in Grad Clesius an: "))
gradf=(9*gradc)/5+32
print("Grad Fahrenheit:",gradf)
gradk=gradc+273.15
print("Kelvin:",gradk)

#Aufgabenblatt3
#1.Programmieraufgabe
print("Dieses Programm prüft, ob die von Ihnen angegebene Zahl gerade oder ungerade ist.")
zahl=int(input("Bitte geben Sie hier ihre zu prüfende Zahl an: "))
if 0<zahl<=100:
   rest=zahl%2
   if rest==0:
       print("Ihre Zahl ist gerade.")
   else:
       print("Ihre Zahl ist ungerade.")
else:
   print("Ihre Zahl lag nicht im Zahlenraum von 1 bis 100.")
#2.Programmieraufgabe
print("Dieses Programm berechnet Ihre Zinsen.")
einzahlung=float(input("Bitte geben Sie an, wie viel Geld Sie eingezahlt haben: "))
zinssatz=float(input("Bitte geben Sie den Zinssatz an (Bsp.: 2.5% Zinsen = 1.025): "))
jahre=int(input("Bitte geben Sie die Dauer in Jahren an: "))
jahre1=jahre
for i in range (jahre):
   einzahlung = einzahlung * zinssatz
   jahre = jahre - 1
print("Ihr Kontostand nach",jahre1, "Jahren beträgt:",einzahlung)
#3.Programmieraufgabe
print("Dieses Programm gibt Ihnen den Durchschnitt und das Maximum ihrer Zahlen aus.")
zahl1=int(input("Bitte geben sie Ihre erste Zahl an: "))
zahl2=int(input("Bitte geben sie Ihre zweite Zahl an: "))
zahl3=int(input("Bitte geben sie Ihre dritte Zahl an: "))
zahl4=int(input("Bitte geben sie Ihre vierte Zahl an: "))
zahl5=int(input("Bitte geben sie Ihre fünfte Zahl an: "))
if zahl1>=0 and zahl2>=0 and zahl3>=0 and zahl4>=0 and zahl5>=0:
   durchschnitt=(zahl1+zahl2+zahl3+zahl4+zahl5)/5
   print("Der Durchschnitt Ihrer Zahlen beträgt:",durchschnitt)
   zahlen=[zahl1, zahl2, zahl3, zahl4, zahl5]
   maximum=max(zahlen)
   print("Die größte Zahl, die Sie eingegeben haben ist:",maximum)
else:
   print("Sie haben eine negative Zahl eingegeben.")