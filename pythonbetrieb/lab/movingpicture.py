import pygame
import random
pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Telekom an die #1!")
time=pygame.time.Clock()
running = True
rectx=0
recty=0
rectchangex=5
rectchangey=3
tlist=[]
for i in range(50):
    x=random.randrange(0,600)
    y=random.randrange(0,600)
    tlist.append([x,y])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rectx=rectx+rectchangex/20
    recty=recty+rectchangey/20
    if rectx>580 or rectx<0:
        rectchangex=rectchangex*-1
    if recty>575 or recty<0:
        rectchangey=rectchangey*-1
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (226, 0, 116), [50, 50, 300, 100])
    pygame.draw.rect(screen, (226, 0, 116), [150, 150, 100, 300])
    pygame.draw.rect(screen, (226, 0, 116), [50, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [300, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [400, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [500, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [20, 20, 560, 560], 5)
    pygame.draw.rect(screen, [0,255,0], [rectx,recty,20,5])
    pygame.draw.rect(screen, [0,255,0], [rectx+7,recty+5,6,20])
    for offset in range(0, 15, 5):
        pygame.draw.line(screen, (226, 0, 116), [32, 500 + offset], [568, 500 + offset], 3)
        pygame.draw.line(screen, (226, 0, 116), [55, 560 + offset], [545, 560 + offset], 3)
    font = pygame.font.SysFont('Arial', 48, True, False)
    text1 = font.render("Erleben, was verbindet.", True, (226, 0, 116))
    text2 = font.render("#DABEI sein ist alles!", True, (226, 0, 116))
    screen.blit(text1, [32, 450])
    screen.blit(text2, [55, 510])
    for item in tlist:
        item[1]=item[1]+0.5
        pygame.draw.rect(screen, [0,255,0], [tlist[i][0], tlist[i][1],20,5])
        pygame.draw.rect(screen, [0,255,0], [tlist[i][0]+7, tlist[i][1]+5,6,20])
        if item[1]>600:
            item[1]=random.randrange(-30,0)
            item[0]=random.randrange(0,600)
    pygame.display.flip()
time.tick(10)
pygame.quit()