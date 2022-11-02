import pygame
import math
import random
import time
pygame.init()
# fenster erstellen
screen = pygame.display.set_mode([600, 500])
# Fenstertitel setzen
pygame.display.set_caption("Flappybird")
# steuert wie oft das Fenster geupdated wird
zeit=pygame.time.Clock()
# laufen lassen bis Fenster geschlossen wird
running = True
while running:
# Test ob Fenster geschlossen wurde
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            running=False
# Hintergrund mit Farbe füllen
    screen.fill([226, 0, 116])
# updated das Fenster mit dem was man gezeichnet hat
    pygame.display.flip()
# auf 20 fps beschränkt
zeit.tick(60)
# schließen von pygame
pygame.quit()