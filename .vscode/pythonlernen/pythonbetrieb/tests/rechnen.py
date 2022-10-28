# mit Komma abtrennen um mehrere Sachen zu schreiben
print("Die Lösung von 10+10 ist:", 10+10)
# immer \ verwenden wenn ich im Text sonderzeichen verwenden will, die normaler weise zum programmieren gebrauht werden
print("\"hallo was geht\"nichts und bei dir")
# \'	Single Quote
# \"	Double Quote
# \t	Tab
# \r	CR: Carriage Return (move to the left)
# \n	LF: Linefeed (move down)
print("This\nis\nmy\nsample.")
# Variabeln erstellen -> Variable muss immer auf der rechten Seite der Rechnung sein -> +,-,*,/,** -> Potenz
# -> Kommarzahlen immer mit Punkt dazwischen schreiben -> und Punkt vor Strich beachten -> Variabeln immer Richtig benennen um Übersicht zu behalten
x = 10
print("x =",x)
x = x + 1
print(x)
y = 9
z = y ** 0.5
print(z)
# mathematische Formeln importieren
from math import *
x = sin(0) + cos(0)
print(x)
# Rechnung mit Inputs -> um dem Pc zu sagen das Zahlen verwendet wurden, mit denen er rechnen kann muss man int vor dem Input verwenden / wenn man Stellen hinter dem Komma hat -> float
gefahrenekilometer = float (input("Geben sie bitte an wie viele Kilometer sie auf ihrer Tour gefahren sind:"))
verbrauchtesbenzin = float (input("Geben sie bitte an wie viele Liter Benzin sie auf ihrer Tour verbraucht haben:"))
verbrauch = gefahrenekilometer/verbrauchtesbenzin
print("Sie haben auf ihrer Tour durchschnittlich:",verbrauch,"Kilometer pro Liter zurück gelegt")