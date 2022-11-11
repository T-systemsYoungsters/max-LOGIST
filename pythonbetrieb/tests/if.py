temperatur = float (input("Bitte geben sie an, wie warm es gerade bei Ihnen ist: "))
# nach einem if/else/elif Statement immer mit Doppelpunkt beenden -> der Pc liest immer Zeile für Zeile -> wenn if bereits zutrifft kann man danach nicht mehr spezifischer werden
if temperatur >= 20:
    print("Es ist warm")
elif temperatur <= 10:
    print("Es ist kalt")
else:
    print("Es ist nicht warm")
