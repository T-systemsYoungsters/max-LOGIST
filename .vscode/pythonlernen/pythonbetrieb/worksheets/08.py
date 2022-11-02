# 1.
# der Code funktioniert nicht, da der x-Wert des Rechtecks in jedem loop zurückgesetzt wird
# 2.
# rectx -> x-Wert des Rechtecks/recty -> y-Wert des Rechtecks/rectchangex -> Veränderung des x-Wertes pro loop/rectchangey -> Veränderung des y-Wertes pro loop
# 3.
# 400-20-rectchangey
# 4.
# wenn man den y-Wert des Rechtecks einfach nur umkehrt teleoprtiert sich das Rechteck nur weg. Um die Bewegung umzukehren muss man rectchangey * -1 nehmen
# 5.
# der Schüler könnte das vereinfachen, indem er eine varable einbaut, die in jeder Koordinate enthalten ist. Somit muss er nur diese eine Variable ändern
# 6.
# die Sterne würden bei jedem durchlauf an einer zufälligen Position wiedert auftauchen. Dadurch würde man nur ein komischen flackern von Punkten erkennen
# 7.
# man kann viele Sachen gleichzeitig animieren, indem man durch eine for Schleife eine Liste mit den verschiedenen Koordinaten der Sachen erstellt, welche dann verändert wird
# 8.
# print(stars[1][0])
# 9.
# man muss x und y nicht festlegen, da die jeweiligen Stellen schon festgelegt sind und somit direkt aus der liste genommen werden können
# 10.
# im Programm bleibt der Mittelpunkt der verwendeten Linie immer gleich und der äußere Punkt wird dadurch berechnet, das man den mit dem Radius und dem Sinus des Kreises immer den Punkt entlang des Kreises verschiebt. Außerdem geht er immer weiter herum, da der Winkel von Durchlauf zu Durchlauf vergrößert wird