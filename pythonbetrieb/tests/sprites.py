import pygame
import random
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
class Block(pygame.sprite.Sprite): # Diese Klasse repräsentiert den Ball und leitet sich von der "Sprite"-Klasse in Pygame ab.
    def __init__(self, color, width, height): # Übergibt die Farbe des Blocks und seine Größe.
        super().__init__()
        self.image = pygame.Surface([width, height]) # Erstellen Sie ein Bild des Blocks und füllen Sie es mit einer Farbe. Dies könnte auch ein Bild aus einem Ordner sein.
        self.image.fill(color)
        self.rect = self.image.get_rect() # Ruft das rechteckige Objekt ab, das die Abmessungen des Bildes hat. Aktualisiert die Position dieses Objekts, indem die Werte von rect.x und rect.y festlegt werden.
    def reset_pos(self):
        self.rect.y=random.randrange(-300,-20)
        self.rect.x = random.randrange(700-20)
    def update(self):
        self.rect.y +=1
        if self.rect.y > 410:
            self.reset_pos()
class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
block_list = pygame.sprite.Group() # Dies ist eine Liste von 'Sprites'. Jeder Block im Programm wird dieser Liste hinzugefügt. Die Liste wird von einer Klasse namens „Group“ verwaltet.
all_sprites_list = pygame.sprite.Group() # Dies ist eine Liste aller Sprites. Alle Blöcke und auch der Spielerblock.
for i in range(50): # Erstellt 50 gleiche Blöcke an verschiedenen Postionen.
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block) # Fügt den Block zur Liste der Objekte hinzu
    all_sprites_list.add(block)
player = Player(RED, 20, 15) # Erstellt den Block des Spielers
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()
score = 0
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    screen.fill(WHITE)
    all_sprites_list.update()
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False) # Prüfen, ob der Spielerblock mit irgendetwas kollidiert ist. -> Wenn der letzte Wert True ist werden die Blöcke nach dem Berühren gelöscht -> False = nicht gelöscht
    for block in blocks_hit_list: # Überprüft die Liste der Kollisionen.
        score += 1
        print(score)
        block.reset_pos()
    all_sprites_list.draw(screen) # Alle Sprites einzeichnen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()