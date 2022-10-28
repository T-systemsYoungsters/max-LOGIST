# Import und Initialisierung von pygame
import pygame
pygame.init()
# fenster erstellen
screen = pygame.display.set_mode([600, 500])
# Fenstertitel setzen
pygame.display.set_caption("Telekom an die 1")
# steuert wie oft das Fenster geupdated wird
zeit=pygame.time.Clock()
# laufen lassen bis Fenster geschlossen wird
running = True
while running:
# Test ob Fenster geschlossen wurde
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Hintergrund mit Farbe füllen
    screen.fill((255, 255, 255))
# Zeichnen von Rechtecken -> das was später gezeichnet wird überdeckt das von davor
    pygame.draw.rect(screen, (226, 0, 116), [50, 50, 300, 100])
    pygame.draw.rect(screen, (226, 0, 116), [150, 150, 100, 300])
    pygame.draw.rect(screen, (226, 0, 116), [50, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [300, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [400, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [500, 250, 50, 50])
# schreiben im Fenster
    schrift = pygame.font.SysFont('Arial', 25, True, False)
    text = schrift.render("Erleben, was verbindet.", True, (226, 0, 116))
    screen.blit(text, [300, 350])
# updated das Fenster mit dem was man gezeichnet hat
    pygame.display.flip()
# auf 20 fps beschränkt
zeit.tick(20)
# schließen von pygame
pygame.quit()