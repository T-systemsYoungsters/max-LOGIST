# 1.
# Die x-Koordinaten funktionieren genauso wie das kartesische Koordinatensystem. Aber die y-Koordinaten sind vertauscht. -> Deckt unteren rechten Quadranten ab / negative Koordinaten -> außerhalb der Anzeige
# 2.
# import pygame & pygame.init()
# 3.
# Jedes Element von RGB ist eine Zahl zwischen 0 und 255. 0 bedeutet, dass keine Farbe vorhanden ist. 255 bedeutet, dass die volle Intensität der Farbe gefordert wird. Die Farben werden additiv kombiniert -> alle 3 Farben angegeben -> Farbe auf dem Monitor weiß.
# 4.
# Da sich die Grundfarben nicht ändern sind sie Konstanten und werden groß geschrieben. Dahingegen kann man bespielsweise aber auch Farbennamen verwenden die sich ändern können(wenn man etwas ein wenig dunkler oder heller haben möchte)
# 5.
# Diese Anweisung legt die Größe des Fensters fest.
# 6.
# Diese loop Prüft auf eingaben des Users
# 7.
# Wird verwendet, um anzugeben, wie schnell der Bildschirm aktualisiert wird
# 8.
# Zeichnet eine Linie auf dem Bildschirm, die grün ist uind von (0, 0) bis (100, 100) geht. Außerdem ist sie 5 Pixel breit.
# 9. 
# y_offset = 0 / while y_offset < 100: / pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5) / y_offset = y_offset + 10
# 10.
# Sobald man die "width" auf 0 setzt oder sie nicht angibt wird das Rechteck ausgefüllt
# 11. 
# (20,20)beschreibt den Ursprung der Ellipse -> wobei der Punkt die obere linke Ecke des Rechtecks ist, in dem die Ellipse gezeichnet wird, (250,100)beschreibt die Höhe und Breite der Ellipse
# 12.
# Es enthält Start- und Endwinkel für den zu zeichnenden Bogen und die Winkel sind im Bogenmaß angegeben.
# 13. 
# 1. Schriftart festlegen / 2. Text in Farbe eingeben / 3. den Text auf dem Bildschirm positionieren
# 14.
# Das ist notwendig, damit man die Schriftart in der gesamten Datei verwenden kann und nicht immer neu definieren muss
# 15.
# Das Polygon ist zwischen den Eckpunkten: (50,100),(0,200),(200,200),(100,50) aufgespannt
# 16.
# Updated das Fenster mit dem was man gezeichnet hat
# 17. 
# schließt das Fenster von pygame
# 18. 
# pygame.draw.circle(screen, (226, 0, 116), (100,100), 100)