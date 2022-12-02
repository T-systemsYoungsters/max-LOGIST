from turtle import update
import pygame
import random
import badblock_library
import goodblock_library
import os
path = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self):
        if self.rect.x <0:
            self.rect.x+=0.1
            bump.play()
        elif self.rect.x >960:
            self.rect.x-=0.1
            bump.play()
        elif self.rect.y <0:
            self.rect.y+=0.1
            bump.play()
        elif self.rect.y >728:
            self.rect.y-=0.1
            bump.play()
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
def show_score(scoreofplayer):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score: " + str(scoreofplayer), True, (0,0,0))
    screen.blit(score,(20,20))
pygame.init() 
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode([screen_width, screen_height])
good_block_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(50):
    block1 = goodblock_library.Goodblock("dollar.jpg")
    block1.rect.x = random.randrange(screen_width)
    block1.rect.y = random.randrange(screen_height)
    good_block_list.add(block1)
    all_sprites_list.add(block1)
for i in range(50):
    block = badblock_library.BadBlock("shit.jpg")
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)
player = Player("ufo.png")
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()
score = 0
bad = pygame.mixer.Sound("bad.wav")
bump = pygame.mixer.Sound("bump.wav")
good = pygame.mixer.Sound("good.wav")
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
    all_sprites_list.update()
    screen.fill((255,255,255))
    blocks_hit_list1 = pygame.sprite.spritecollide(player, good_block_list, True)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    goodblock_library.Goodblock.update(block1)
    badblock_library.BadBlock.update(block)
    for block in blocks_hit_list:
        score -= 1
        bad.play()
    for block1 in blocks_hit_list1:
        score += 1
        good.play()
    show_score(score)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()