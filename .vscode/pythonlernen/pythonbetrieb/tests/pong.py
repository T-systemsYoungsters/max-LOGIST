import pygame, math
from pygame.locals import * 
import time
pygame.init()
black = ( 0, 0, 0)
white = ( 255, 255, 255)
width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
# Variablen/Konstanten
ballpos_x = 10
ballpos_y = 30
ball_diameter = 20
movement_x = 8
movement_y = 6
player_1_x = 20
player_1_y = 20
player_1_movement = 0
player_2_x = width - (2 * 20)
player_2_y = 20
player_2_movment = 0
paddle_height = 100
score_player_1 = 0
score_player_2 = 0
# Schleife Hauptprogramm
active = True
while active:
    # Überprüfen nach Aktion
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1_movement = -10
            elif event.key == pygame.K_s:
                player_1_movement = 10 
            elif event.key == pygame.K_UP:
                player_2_movment = -10
            elif event.key == pygame.K_DOWN:
                player_2_movment = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_1_movement = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_2_movment = 0
    # Spiellogik 
    if player_1_movement != 0:
        player_1_y += player_1_movement
    if player_1_y < 5:
        player_1_y = 5
    if player_1_y > height - paddle_height -5 :
        player_1_y = height - paddle_height - 5
    if player_2_movment != 0:
        player_2_y += player_2_movment    
    if player_2_y < 5:
        player_2_y = 5
    if player_2_y > height - paddle_height -5 :
        player_2_y = height - paddle_height -5
    # Spielfeld löschen
    screen.fill(black)
    # Spielfeld/figuren zeichnen
    ball = pygame.draw.ellipse(screen, white, [ballpos_x, ballpos_y, ball_diameter, ball_diameter])
    player1 = pygame.draw.rect(screen, white, [player_1_x, player_1_y, 20, paddle_height])
    player2 = pygame.draw.rect(screen, white, [player_2_x, player_2_y, 20, paddle_height])
    # Kollidierung
    if player1.colliderect(ball):
        movement_x = movement_x - 0
        movement_y = movement_y - 0
        movement_x = movement_x * -1
        ballpos_x = 40        
    if player2.colliderect(ball):
        movement_x = movement_x + 0
        movement_y = movement_y + 0
        movement_x = movement_x * -1
        bellpos_x = 570
    # Score
    font = pygame.font.Font('freesansbold.ttf', 32)   
    text_x = width / 3
    text_y = 10
    def show_score(x,y):    
        score = font.render("Player A: " + str(score_player_1) + "     Player B: " + str(score_player_2), True, (255,255,255))
        screen.blit(score, (x,y))
    # Bewegung
    ballpos_x += movement_x
    ballpos_y += movement_y
    if ballpos_y > height - ball_diameter or ballpos_y < 0:
        movement_y = movement_y * -1             
    if ballpos_x > width - ball_diameter:
        movement_x = movement_x * -1
        score_player_1 += 1
        time.sleep(0.5)
        ballpos_x = width / 2
        ballpos_y = height / 2
    if ballpos_x <= 0:
        movement_x = movement_x * -1
        score_player_2 += 1
        time.sleep(0.5)
        ballpos_x = width / 2
        ballpos_y = height / 2    
    show_score(text_x, text_y)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()