import pygame
def mousetelekom(screen, x, y):
    pygame.draw.rect(screen, (226, 0, 116), [0+x, 0+y, 30, 10])
    pygame.draw.rect(screen, (226, 0, 116), [10+x, 10+y, 10, 30])
    pygame.draw.rect(screen, (226, 0, 116), [0+x, 20+y, 5, 5])
    pygame.draw.rect(screen, (226, 0, 116), [25+x, 20+y, 5, 5])
    pygame.draw.rect(screen, (226, 0, 116), [35+x, 20+y, 5, 5])
    pygame.draw.rect(screen, (226, 0, 116), [45+x, 20+y, 5, 5])
def keycloud(screen,x,y):
    pygame.draw.circle(screen, (226,0,116), (0+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (20+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (60+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (80+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (10+x, 10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, 20+y), 25)
    pygame.draw.circle(screen, (226,0,116), (70+x, 10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (10+x, -10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, -20+y), 25)
    pygame.draw.circle(screen, (226,0,116), (70+x, -10+y), 25)
pygame.init()
size = [1000, 1000]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
x_speed = 0
y_speed = 0
x_coord = 25
y_coord = 45
pygame.mouse.set_visible(0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    screen.fill((255,255,255))
    mousetelekom(screen, x, y)
    if x_coord<30 and x_speed<0:
        y_coord = y_coord + y_speed
        keycloud(screen, x_coord, y_coord)
    elif x_coord>890 and x_speed>0:
        y_coord = y_coord + y_speed
        keycloud(screen, x_coord, y_coord)
    elif y_coord<50 and y_speed<0:
        x_coord = x_coord + x_speed
        keycloud(screen, x_coord, y_coord)
    elif y_coord>950 and y_speed>0:
        x_coord = x_coord + x_speed
        keycloud(screen, x_coord, y_coord)
    else:
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
        keycloud(screen, x_coord, y_coord)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()