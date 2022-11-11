import random
import pygame
pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
rectx=50
recty=50
rectchangex=5
rectchangey=3
snowlist=[]
for i in range(50):
    x=random.randrange(0,500)
    y=random.randrange(0,500)
    snowlist.append([x,y])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rectx=rectx+rectchangex
    recty=recty+rectchangey
    if rectx>450 or rectx<0:
        rectchangex=rectchangex*-1
    if recty>450 or recty<0:
        rectchangey=rectchangey*-1
    screen.fill((0,0,0))
    for item in snowlist:
        item[1]=item[1]+10
        pygame.draw.circle(screen, [255,255,255], item,2)
        if item[1]>500:
            item[1]=random.randrange(-30,0)
            item[0]=random.randrange(0,500)
    pygame.draw.rect(screen, [255,255,255], [rectx,recty,50,50])
    rectx=rectx+rectchangex
    recty=recty+rectchangey
    pygame.display.flip()
    clock.tick(10)
pygame.quit()